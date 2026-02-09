#!/usr/bin/env python3
import pathlib
import re
import yaml
import logging
import urllib.request  # newly added import for URL support
from collections import defaultdict
from pathlib import Path
import unicodedata
import os.path
import subprocess


# Konfiguration
BASE_URL = "https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/"
TAG_URL = "tags/"
HEAD_URL = "heads/main/"
CATEGORY_LIST = [
    "Tischler", "SHK", "Zahntechniker", "Maler", "Raumausstatter",  "Belehrung", "Arbeits-_und_Gesundheitsschutz", "Umfragen", "Wissensspeicher", "Experimente", "Sonstige"
]
OUTPUT_FILE = "project.yml"
HEADER_FILE = "project-part.yaml"
ADDITIONALS = "additional_courses.yaml"
COURSE_DIRECTORY = "courses"

# Logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Cache for git tags to avoid repeated subprocess calls
_GIT_TAGS_CACHE = None


def get_git_tags():
    """Get all git tags from the repository. Returns a set of tag names."""
    global _GIT_TAGS_CACHE
    if _GIT_TAGS_CACHE is None:
        try:
            result = subprocess.run(
                ['git', 'tag'],
                capture_output=True,
                text=True,
                check=True
            )
            _GIT_TAGS_CACHE = set(result.stdout.strip().split('\n')) if result.stdout.strip() else set()
            logging.info(f"Loaded {len(_GIT_TAGS_CACHE)} git tags from repository")
        except subprocess.CalledProcessError as e:
            logging.warning(f"Failed to get git tags: {e}")
            _GIT_TAGS_CACHE = set()
    return _GIT_TAGS_CACHE


def tag_exists(tag_name):
    """Check if a specific git tag exists."""
    return tag_name in get_git_tags()


def is_url(filepath):
    try:
        return filepath.startswith("http://") or filepath.startswith("https://")
    except AttributeError:
        # if it is posixPath then string ops won't work
        return False


class YamlCommentParser:
    def __init__(self, strip_macros=True):
        self.strip_macros = strip_macros

    def parse(self, filepath):
        try:
            # If filepath is a URL, download its content; otherwise, read from the local file system.
            if is_url(filepath):
                with urllib.request.urlopen(filepath) as response:
                    content = response.read().decode('utf-8')
            else:
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

def load_additional_courses(yaml_path):
    """Load additional course URLs from a YAML file."""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data.get('courses', [])

def find_markdown_files(base_dir=COURSE_DIRECTORY):
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

def build_structure(files: list, external_dict: dict):
    categories = defaultdict(list)
    parser = YamlCommentParser()

    for file in files:
        meta = parser.parse(str(file))
        title = meta.get("title")
        category, tags = categorize_file(meta)
        version = meta.get("version")

        # add title and tags if they exist
        entry = {
            key: value
            for key, value in {
                "title": title,
                "tags": tags
            }.items()
            if value
        }
        # add the right url, baseurl + file or the whole url string
        entry["url"] = get_url(file, version, tagged = external_dict.get(file, False))

        categories[category].append(entry)
        logging.info(f"Added {file} to category '{category}'")
    return categories


def get_url(file, version, tagged = False):
    if is_url(file):
        url = file
    elif tagged and version:
        # Check if the tag exists before using it
        tag_name = f"{to_github_tag(file)}_v{version}"
        if tag_exists(tag_name):
            # https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/tags/augschutz_shk_v0.0.13/courses/AuGSchutz_SHK.md
            folder = "" if file.parent.match("courses") else "courses/"
            url = f"{BASE_URL}{TAG_URL}{tag_name}/{folder}{file.as_posix()}"
            logging.debug(f"Using tag-based URL for {file}: {tag_name}")
        else:
            # Tag doesn't exist yet, fall back to main branch
            url = f"{BASE_URL}{HEAD_URL}{file.as_posix()}"
            logging.info(f"Tag {tag_name} not found for {file}, using HEAD URL instead")
    else:
        url = f"{BASE_URL}{HEAD_URL}{file.as_posix()}"
    return url


def write_yaml_header(out):
    if Path(HEADER_FILE).exists():
        with open(HEADER_FILE, "r", encoding="utf-8") as header:
            out.write(header.read())
            out.write("\n")

def write_output_yaml(categories):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        # Optionaler YAML-Header
        write_yaml_header(out)

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

def to_github_tag(s: pathlib.Path, max_length: int = 100, allow_underscore: bool = True) -> str:
    """
    Convert an arbitrary string into a GitHub-style tag:
    - If the input appears to be a filename (has an extension), the extension is stripped.
    - Normalize unicode to ASCII,
    - lower-case,
    - replace any sequence of characters that are not [a-z0-9-] (or underscore if allowed)
      with a single hyphen,
    - collapse repeated hyphens,
    - strip leading/trailing hyphens,
    - optionally trim to max_length and remove any trailing hyphen after trim.

    Returns an empty string for empty/None input after normalization.
    """
    # Detect and strip final extension from the basename if present
    base = s.name
    stem = s.stem

    # Normalize unicode (e.g., convert accented characters to ASCII equivalents)
    stem = unicodedata.normalize("NFKD", stem)
    stem = stem.encode("ascii", "ignore").decode("ascii")

    stem = stem.lower().strip()

    # Build regex for allowed characters
    if allow_underscore:
        allowed_re = r"[^a-z0-9_-]+"
    else:
        allowed_re = r"[^a-z0-9-]+"

    # Replace disallowed runs with a single hyphen
    stem = re.sub(allowed_re, "-", stem)

    # Collapse multiple hyphens and strip edges
    stem = re.sub(r"-{2,}", "-", stem).strip("-")

    # Trim to max_length if requested and strip trailing hyphen
    if max_length and max_length > 0:
        stem = stem[:max_length].rstrip("-")

    return stem


def create_external_dict(files: list, externals: list):
    external_dict = {key: False if key in externals else True for key in files}
    return external_dict


def main():
    logging.info("Searching for markdown files...")
    files = find_markdown_files()
    logging.info(f"Found {len(files)} markdown files.")
    adds = load_additional_courses(ADDITIONALS)
    logging.info(f"Loaded {len(adds)} additional courses.")
    files.extend(adds)
    external_dict = create_external_dict(files, adds)
    categories = build_structure(files, external_dict)
    write_output_yaml(categories)
    logging.info(f"Written output to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

