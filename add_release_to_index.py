#!/usr/bin/env python3

import json
import hashlib
from pathlib import Path
from bs4 import BeautifulSoup
import os

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

def build_result(item_list):
    """Construct the result dict from nested itemListElements."""
    result = {}
    outer_list = item_list.get("itemListElement", [])

    for outer in outer_list:
        inner_list = outer.get("itemListElement", [])
        for item in inner_list:
            id_url = item.get("@id", "")
            version = item.get("version", "")
            file_name = id_url.split("/")[-1] if id_url else ""
            id_hash = hash_id(id_url)
            result[id_hash] = {
                "version": version,
                "file_name": file_name,
                "id_url": id_url,
                "release_urls": generate_release_urls(file_name, version)
            }
    return result

def generate_release_urls(file_name, version):
    """
    Generate GitHub release URLs for PDF, IMS, and SCORM versions.
    """
    base_name = os.path.splitext(file_name)[0]
    version_tag = f"{base_name.lower()}_v{version.lower()}"
    file_base = f"{base_name}_v{version}"

    base_url = f"https://github.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/releases/download/{version_tag}"

    return {
        "Documentation": f"{base_url}/{file_base}_Documentation.pdf",
        "IMS": f"{base_url}/{file_base}_IMS.zip",
        "SCORM": f"{base_url}/{file_base}_SCORM.zip"
    }

def add_release_links(soup, result):
    cards = get_cards_to_inject(soup)
    for card in cards:
        link = card.find("a", href=True)
        if not link:
            continue
        href = link["href"]
        # Extract ID URL from href query param
        if "?" in href:
            id_url = href.split("?")[1]
        else:
            continue

        id_hash = hash_id(id_url)
        if id_hash not in result:
            continue

        urls = result[id_hash]["release_urls"]
        # Create new div.card-links
        card_links_div = soup.new_tag("div", **{"class": "card-links"})
        ul = soup.new_tag("ul", **{"class": "list-inline"})

        icon_map = {
            "Documentation": "📄",
            "IMS": "📦",
            "SCORM": "📦"
        }

        for label, url in urls.items():
            li = soup.new_tag("li", **{"class": "list-inline-item"})
            a = soup.new_tag("a", href=url, target="_blank")
            a.string = f"{icon_map.get(label, '')} {label}"
            li.append(a)
            ul.append(li)

        card_links_div.append(ul)
        card.parent.insert(card.parent.contents.index(card) + 1, card_links_div)


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

def main(input_file, output_file):
    soup = load_html(input_file)
    json_data = extract_json_ld(soup)
    result = build_result(json_data)
    add_release_links(soup, result)
    add_css_link(soup)
    save_html(soup, output_file)

if __name__ == "__main__":
    loc = Path("docs")
    main(loc / "index.html", loc / "index.html")

