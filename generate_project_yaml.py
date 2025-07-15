#!/usr/bin/env python3

import os
import re
import yaml
import logging
from collections import defaultdict
from pathlib import Path

# Konfiguration
BASE_URL = "https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/"
CATEGORY_LIST = [
    "Tischler", "SHK", "Zahntechniker", "Maler",
    "Raumausstatter", "Experimente", "Wissensspeicher", "Sonstige"
]
OUTPUT_FILE = "project.yml"
HEADER_FILE = "project-part.yaml"

# Logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

class YamlCommentParser:
    def __init__(self, strip_macros=True):
        self.strip_macros = strip_macros

    def parse(self, filepath):
        try:
            content = Path(filepath).read_text(encoding='utf-8')
        except Exception as e:
            logging.error(f"Error reading {filepath}: {e}")
            return {}

        raw_block = self._extract_html_comment(content)
        if not raw_block:
            logging.warning(f"No YAML section found in: {filepath}")
            return {}

        cleaned_yaml = self._clean_yaml_block(raw_block)
        return self._safe_load_yaml(cleaned_yaml, filepath)

    def _extract_html_comment(self, text):
        match = re.search(r'<!--\s*(.*?)\s*-->', text, re.DOTALL)
        return match.group(1) if match else None

    def _clean_yaml_block(self, block):
        lines = block.splitlines()
        cleaned_lines = []
        in_macro_block = False

        for line in lines:
            stripped = line.strip()

            # Multiline macros like @style ... @end
            if not in_macro_block and stripped.startswith("@") and stripped.lower() != "@end":
                in_macro_block = True
                continue
            if in_macro_block:
                if stripped.lower() == "@end":
                    in_macro_block = False
                continue

            # Single-line @directives
            if stripped.startswith("@"):
                continue

            # Remove keys with @ as value
            if re.match(r"^\s*\w+:\s*@\S+", line):
                continue

            cleaned_lines.append(line)

        return '\n'.join(cleaned_lines)

    def _safe_load_yaml(self, cleaned_yaml, filepath):
        try:
            parsed = yaml.safe_load(cleaned_yaml)
            if isinstance(parsed, dict):
                return parsed
            else:
                logging.warning(f"YAML section is not a dict in {filepath}, got: {type(parsed)}")
                return {}
        except yaml.YAMLError as e:
            logging.error(f"YAML parsing error in {filepath}: {e}")
            return {}


def find_markdown_files(base_dir="courses"):
    return sorted(Path(base_dir).rglob("*.md"))

def categorize_file(metadata):
    tags = metadata.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    elif tags is None:
        tags = []

    tags_lower = [tag.lower() for tag in tags]
    for category in CATEGORY_LIST[:-1]:  # exclude 'Sonstige'
        if category.lower() in tags_lower:
            return category, tags
    return "Sonstige", tags

def build_structure(files):
    categories = defaultdict(list)
    parser = YamlCommentParser()

    for file in files:
        meta = parser.parse(file)
        title = meta.get("title")
        category, tags = categorize_file(meta)

        entry = {
            "url": f"{BASE_URL}{file.as_posix()}",
        }

        if title:
            entry["title"] = title
        if tags:
            entry["tags"] = tags

        categories[category].append(entry)
        logging.info(f"Added {file} to category '{category}'")

    return categories

def write_yaml_header(out):
    if Path(HEADER_FILE).exists():
        with open(HEADER_FILE, "r", encoding="utf-8") as header:
            out.write(header.read())
            out.write("\n")

def write_output_yaml(categories):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        # Optionaler YAML-Header
        write_yaml_header(out)

        if Path(HEADER_FILE).exists():
            with open(HEADER_FILE, "r", encoding="utf-8") as header:
                out.write(header.read())
                out.write("\n")

        for category in CATEGORY_LIST:
            items = categories.get(category, [])
            if not items:
                continue

            write_yaml_body(category, items, out)


def write_yaml_body(category, items, out):
    out.write(f"""  - title: {category}
    comment: ""
    grid: true
    collection:
""")
    for item in items:
        out.write(f"      - url: {item['url']}\n")
        if "title" in item:
            out.write(f"        title: {item['title']}\n")
        if "tags" in item:
            out.write("        tags:\n")
            for tag in item["tags"]:
                out.write(f"          - {tag}\n")


def main():
    logging.info("Searching for markdown files...")
    files = find_markdown_files()
    logging.info(f"Found {len(files)} markdown files.")
    categories = build_structure(files)
    write_output_yaml(categories)
    logging.info(f"Written output to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()