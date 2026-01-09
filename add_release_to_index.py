#!/usr/bin/env python3

import json
import hashlib
from pathlib import Path
from unittest import result

from bs4 import BeautifulSoup
from bs4.element import Tag
import os
import requests
from urllib.parse import urlparse
import posixpath
from generate_project_yaml import get_url

def load_html(filepath):
    """Load and parse HTML file."""
    with open(filepath, encoding="utf-8") as f:
        return BeautifulSoup(f, "html.parser")

def extract_json_ld(soup):
    """Extract JSON-LD content from <script> tag."""
    script_tag = soup.find("script", type="application/ld+json")
    if not script_tag:
        raise ValueError("No JSON-LD script tag found.")
    return json.loads(script_tag.string)

def hash_id(id_str):
    """Return a SHA256 hash of the ID URL."""
    return hashlib.sha256(id_str.encode("utf-8")).hexdigest()

def separate_filename(id_url):
    """Separate file name and URL from the ID URL."""
    if not id_url:
        return ""
    else:
        parsed = urlparse(id_url)
        file_name = posixpath.basename(parsed.path)
        return file_name

def build_result(item_list):
    """Construct the result dict from nested itemListElements."""
    result = {}
    outer_list = item_list.get("itemListElement", [])

    for outer in outer_list:
        inner_list = outer.get("itemListElement", [])
        for item in inner_list:
            id_url = item.get("@id", "")
            version = item.get("version", "")
            file_name = separate_filename(id_url)
            id_hash = hash_id(id_url)
            result[id_hash] = {
                "version": version,
                "file_name": file_name,
                "id_url": id_url,
                "release_urls": generate_release_urls(file_name, id_url, version),
                "tag_course": get_url(Path(file_name), version, tagged=True)
            }
    return result

def build_release_asset_baseurl(id_url: str) -> str:
    """
    Convert a GitHub raw/blob URL (or a repo subfolder URL) to a releases/download URL.
    Examples handled:
      - https://raw.githubusercontent.com/{owner}/{repo}/{ref}/path/to/file.ext
      - https://github.com/{owner}/{repo}/blob/{ref}/path/to/file.ext
      - https://github.com/{owner}/{repo}/tree/{ref}/path/to/folder
      - https://raw.githubusercontent.com/{owner}/{repo}/refs/heads/main/courses
    Returns:
      https://github.com/{owner}/{repo}/releases/download
    """
    if not id_url:
        raise ValueError("id_url is empty")

    p = urlparse(id_url)
    host = p.netloc.lower()
    # split and drop empty segments (leading slash)
    parts = [seg for seg in p.path.split('/') if seg]

    if host not in ("raw.githubusercontent.com", "github.com"):
        raise ValueError(f"Not a GitHub URL: {id_url}")

    # Extract owner/repo
    if len(parts) < 2:
        raise ValueError(f"Cannot extract owner/repo from: {id_url}")
    owner, repo = parts[0], parts[1]

    return f"https://github.com/{owner}/{repo}/releases/download"

def generate_release_urls(file_name, id_url, version):
    """
    Generate GitHub release URLs for PDF, IMS, and SCORM versions.
    """
    base_name = os.path.splitext(file_name)[0]

    #base_url = f"https://github.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/releases/download/{version_tag}"
    base_url = build_release_asset_baseurl(id_url)

    release_urlbase = f"{base_url}/{base_name.lower()}_v{version.lower()}/{base_name}_v{version}"

    return {
        "Documentation": f"{release_urlbase}_Documentation.pdf",
        "SCORM": f"{release_urlbase}_SCORM.zip"
    }

def release_exists(doc_url):
    """check if the url exists"""
    try:
        response = requests.head(doc_url, timeout=10)
        print(f"Release URL: {doc_url} - Status: {response.status_code}")
        return response.status_code in (200, 302)
    except Exception:
        return False

def get_result_key(href, result):
    """Extract the hash key from the href query param."""
    if "?" in href:
        id_url = href.split("?")[1]
    else:
        raise ValueError(f"Invalid href: {href}")
    id_hash = hash_id(id_url)
    if id_hash not in result:
        raise ValueError(f"Hash key not found for href: {href}")
    return id_hash

def add_release_links(soup, result):
    cards = get_cards_to_inject(soup)
    for card in cards:
        link = card.find("a", href=True)
        if not link:
            continue
        try:
            id_hash = get_result_key(link["href"], result)
        except ValueError as e:
            print(f"Error processing card: {e}")
            continue

        # change href to the taged version
        link["href"] = link["href"].replace(
            result[id_hash]["id_url"], result[id_hash]["tag_course"]
        )

        # insert download cards
        urls = result[id_hash]["release_urls"]
        # test if releases exist, with external urls a non-existent release can happen
        if release_exists(urls.get("SCORM")):
            element = build_individual_release_links(soup, urls)
        else:
            print(f"Release not found for {result[id_hash]['file_name']}")
            element = build_no_release_found_span(soup)

        card.parent.insert(card.parent.contents.index(card) + 1, element)


def build_no_release_found_span(soup):
    span = soup.new_tag("span", **{"class": "release-not-found"})
    span.string = "Links not available."
    return span


def build_individual_release_links(soup, urls):
    # Create new div.card-links
    card_links_div = soup.new_tag("div", **{"class": "card-links"})
    ul = soup.new_tag("ul", **{"class": "list-inline"})
    icon_map = {
        "Documentation": "📄",
        "SCORM": "📦"
    }
    for label, url in urls.items():
        # we drop the link if the release does not exist
        if not release_exists(url):
            print(f"Release {label} not found for {url}")
            continue
        li = soup.new_tag("li", **{"class": "list-inline-item"})
        a = soup.new_tag("a", href=url, target="_blank")
        a.string = f"{icon_map.get(label, '')} {label}"
        li.append(a)
        ul.append(li)
    card_links_div.append(ul)
    return card_links_div


def get_cards_to_inject(soup):
    cards = soup.select("div.card-body div.row div.card-body")
    return cards


def add_css_link(soup):
    head = soup.find("head")
    if not head:
        raise ValueError("No <head> found")
    link_tag = soup.new_tag("link", rel="stylesheet", href="linklayout.css")
    head.append(link_tag)

def save_html(soup, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

def inject_course_title_icons(soup, src='icon.ico', alt='liascript-icon'):
    """
    Ensure each card's anchor has an <img class="course-title-icon"> immediately before
    its h6.card-title.

    - Finds all div.card .card-body elements.
    - Verifies the first element child is an <a>.
    - Locates h6.card-title inside the anchor.
    - If an <img.course-title-icon> already exists, it will be moved so it's directly before the h6.
    - If none exists, a new <img> is created and inserted before the h6.
    - Returns the number of newly inserted <img> elements (moves are not counted).

    Parameters:
    - soup: BeautifulSoup object for the HTML document.
    - src: image src (default 'icon.ico').
    - alt: alt text for the image (default 'liascript-icon').
    """
    inserted = 0

    for card_body in soup.select('div.card .card-body'):
        # pick first element child (skip whitespace/text)
        first_elem = None
        for child in card_body.children:
            if isinstance(child, Tag):
                first_elem = child
                break
        if first_elem is None or first_elem.name != 'a':
            continue

        anchor = first_elem
        h6 = anchor.find('h6', class_='card-title')
        if not h6:
            continue

        existing_img = anchor.find('img', class_='course-title-icon')
        if existing_img:
            # Check whether the existing image is the previous element sibling (ignoring text)
            prev_tag = None
            for sib in h6.previous_siblings:
                if isinstance(sib, Tag):
                    prev_tag = sib
                    break
            if prev_tag is existing_img:
                # already in the right place
                continue
            # move the existing image to right before the h6
            existing_img.extract()
            h6.insert_before(existing_img)
            continue

        # create and insert a new image before the h6
        img = soup.new_tag('img', src=src, alt=alt)
        img['class'] = 'course-title-icon'
        h6.insert_before(img)
        inserted += 1

    return inserted

def main(input_file, output_file):
    soup = load_html(input_file)
    json_data = extract_json_ld(soup)
    result = build_result(json_data)
    add_release_links(soup, result)
    # add icons for titles
    inject_course_title_icons(soup)
    add_css_link(soup)
    save_html(soup, output_file)

if __name__ == "__main__":
    loc = Path("docs")
    main(loc / "index.html", loc / "index.html")

