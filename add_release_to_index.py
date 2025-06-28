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
    """Construct the result dict as specified."""
    result = {}
    for item in item_list.get("itemListElement", []):
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
    
    urls = [
        f"{base_url}/{file_base}_Documentation.pdf",
        f"{base_url}/{file_base}_IMS.zip",
        f"{base_url}/{file_base}_SCORM.zip"
    ]
    return urls

def add_release_links(soup, result):
    cards = soup.find_all("div", class_="card-body")
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
        ul = soup.new_tag("ul")
        for url in urls:
            li = soup.new_tag("li")
            a = soup.new_tag("a", href=url, target="_blank")
            a.string = os.path.basename(url)
            li.append(a)
            ul.append(li)
        card.append(ul)

def save_html(soup, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

def main(input_file, output_file):
    soup = load_html(input_file)
    json_data = extract_json_ld(soup)
    result = build_result(json_data)
    add_release_links(soup, result)
    save_html(soup, output_file)

if __name__ == "__main__":
    loc = Path("docs")
    main(loc / "index.html", loc / "index.html")

