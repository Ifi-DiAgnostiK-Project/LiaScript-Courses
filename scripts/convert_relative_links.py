#!/usr/bin/env python3
"""
Convert relative image/stylesheet links in course markdown files to absolute URLs.

Relative paths in LiaScript courses are problematic when courses are served via
tag-based URLs: LiaScript resolves relative paths against the tag URL, which
includes the tag name and makes copying/reusing links fragile.

This script converts all relative paths to absolute raw.githubusercontent.com
URLs that always point to the main branch (refs/heads/main), so assets load
correctly regardless of which URL the course is accessed through.

It also warns when a YAML header field contains an absolute URL that still
points to a ``refs/tags/…`` snapshot of this repository, which is equally
fragile.

Converted link types:
  - YAML header fields:  logo:, icon:, link:
  - Markdown images:     ![alt](relative/path)
  - HTML img tags:       <img src="relative/path">

Usage (standalone):
    python3 scripts/convert_relative_links.py courses/my_course.md
    python3 scripts/convert_relative_links.py  # converts all courses

Installation as pre-commit hook:
    python3 scripts/install-pre-commit-hook.py
"""

import re
import sys
import os
import posixpath
import shutil
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

# Repository constants (must match generate_project_yaml.py)
REPO_OWNER = "Ifi-DiAgnostiK-Project"
REPO_NAME = "LiaScript-Courses"
BRANCH = "main"
RAW_BASE_URL = (
    f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}"
    f"/refs/heads/{BRANCH}"
)

# YAML fields that contain image or stylesheet paths (images: logo, icon;
# stylesheet: link) – converted from relative to absolute refs/heads/main
# URLs and checked for tag-based URL warnings.
YAML_IMAGE_FIELDS = ("logo", "icon", "link")

# Prefix used to detect tag-based URLs pointing to this repository.
# Any YAML field value starting with this prefix uses a tag-based URL that
# should be updated to point to refs/heads/main instead.
_OUR_RAW_TAGS_PREFIX = (
    f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/refs/tags/"
)

# Compiled regex patterns shared between conversion and existence checking
# ── Markdown: ![alt](URL optional-title/whitespace)
_MD_IMAGE_PATTERN = re.compile(r"!\[([^\]]*)\]\((\S+?)((?:\s[^)]*)?\))")
# ── HTML <img src="..."> double quotes
_HTML_SRC_DQ_PATTERN = re.compile(r'(<img\b[^>]*?\bsrc=)"([^"]*)"')
# ── HTML <img src='...'> single quotes
_HTML_SRC_SQ_PATTERN = re.compile(r"(<img\b[^>]*?\bsrc=)'([^']*)'")

# Determine repo root relative to this script file
SCRIPT_PATH = Path(__file__).resolve()
if SCRIPT_PATH.parent.name == "hooks":
    # Running as .git/hooks/pre-commit (symlinked)
    REPO_ROOT = SCRIPT_PATH.parent.parent.parent
else:
    # Running from scripts/
    REPO_ROOT = SCRIPT_PATH.parent.parent


def is_absolute_url(path: str) -> bool:
    """Return True if the path is already an absolute URL."""
    return path.startswith("http://") or path.startswith("https://")


def _resolve_relative_path(relative_path: str, course_dir: str) -> str:
    """
    Resolve a relative image path to a repo-relative POSIX path.

    Args:
        relative_path: Relative path as it appears in the course file
        course_dir: Directory of the course file relative to the repo root

    Returns:
        Normalised POSIX path relative to the repository root
        (e.g. 'courses/img/foo.jpg')
    """
    if relative_path.startswith("./"):
        relative_path = relative_path[2:]
    return posixpath.normpath(posixpath.join(course_dir, relative_path))


def make_absolute_url(relative_path: str, course_dir: str) -> str:
    """
    Convert a relative path to an absolute GitHub raw content URL.

    Args:
        relative_path: Relative path as it appears in the course file
                       (e.g. 'img/foo.jpg' or './img/foo.jpg' or '../img/foo.jpg')
        course_dir: Directory of the course file relative to the repo root
                    (e.g. 'courses' for a file at courses/foo.md)

    Returns:
        Absolute raw.githubusercontent.com URL pointing to refs/heads/main
    """
    resolved = _resolve_relative_path(relative_path, course_dir)
    return f"{RAW_BASE_URL}/{resolved}"


@dataclass
class ConversionResult:
    """
    Result returned by :func:`convert_file`.

    Attributes:
        modified: True if the file was modified on disk.
        missing_paths: Relative paths that were referenced in the file but do
                       not exist in the repository.  Empty list = all OK.
        tag_url_warnings: Absolute URLs in YAML fields that point to a
                          ``refs/tags/…`` snapshot of this repository.  These
                          should be updated to point to ``refs/heads/main``
                          instead.  Empty list = all OK.
    """

    modified: bool
    missing_paths: list[str] = field(default_factory=list)
    tag_url_warnings: list[str] = field(default_factory=list)

    def __bool__(self) -> bool:
        """Allow ``if convert_file(...)`` to test for modification."""
        return self.modified


def _replace_yaml_image_field(match: re.Match, course_dir: str) -> str:
    """Replacement function for a single YAML image-field match."""
    prefix = match.group(1)   # e.g. 'logo:   '
    value = match.group(2)    # current value (possibly relative)
    suffix = match.group(3)   # trailing whitespace / empty string

    if is_absolute_url(value):
        return match.group(0)

    abs_url = make_absolute_url(value, course_dir)
    return f"{prefix}{abs_url}{suffix}"


def convert_yaml_header(yaml_block: str, course_dir: str) -> str:
    """
    Convert relative logo:/icon: values inside the YAML header block to
    absolute URLs.

    Args:
        yaml_block: The full ``<!-- ... -->`` YAML comment block as a string
        course_dir: Course directory relative to repo root

    Returns:
        Updated YAML block string
    """
    field_pattern = re.compile(
        r"^(\s*(?:" + "|".join(YAML_IMAGE_FIELDS) + r"):\s+)"  # field name + spaces
        r"(\S+)"                                                  # value
        r"(\s*)$",                                               # trailing whitespace
        re.MULTILINE,
    )

    return field_pattern.sub(
        lambda m: _replace_yaml_image_field(m, course_dir),
        yaml_block,
    )


def convert_body(body: str, course_dir: str) -> str:
    """
    Convert relative image paths in the markdown/HTML body to absolute URLs.

    Handles:
    - Markdown images:  ![alt](path) or ![alt](path "title")
    - HTML img tags:    <img src="path"> (double or single quotes)

    Args:
        body: The body text (everything after the closing ``-->`` of the header)
        course_dir: Course directory relative to repo root

    Returns:
        Updated body string
    """

    # ── Markdown images ────────────────────────────────────────────────────
    # Match: ![alt](URL optional-rest)
    #   group 1 = alt text
    #   group 2 = URL (no spaces)
    #   group 3 = everything after the URL up to and including ')'
    def _replace_md_image(m: re.Match) -> str:
        alt = m.group(1)
        path = m.group(2)
        rest = m.group(3)  # trailing title / whitespace + closing ')'
        if is_absolute_url(path):
            return m.group(0)
        abs_url = make_absolute_url(path, course_dir)
        return f"![{alt}]({abs_url}{rest}"

    body = _MD_IMAGE_PATTERN.sub(_replace_md_image, body)

    # ── HTML <img src="..."> with double quotes ────────────────────────────
    def _replace_html_src_dq(m: re.Match) -> str:
        before = m.group(1)
        path = m.group(2)
        if is_absolute_url(path):
            return m.group(0)
        abs_url = make_absolute_url(path, course_dir)
        return f'{before}"{abs_url}"'

    body = _HTML_SRC_DQ_PATTERN.sub(_replace_html_src_dq, body)

    # ── HTML <img src='...'> with single quotes ────────────────────────────
    def _replace_html_src_sq(m: re.Match) -> str:
        before = m.group(1)
        path = m.group(2)
        if is_absolute_url(path):
            return m.group(0)
        abs_url = make_absolute_url(path, course_dir)
        return f"{before}'{abs_url}'"

    body = _HTML_SRC_SQ_PATTERN.sub(_replace_html_src_sq, body)

    return body


def _find_relative_paths_in_yaml(
    yaml_block: str, course_dir: str
) -> list[tuple[str, str]]:
    """
    Return all relative image paths found in the YAML header block.

    Returns:
        List of ``(original_relative_path, resolved_repo_relative_path)`` tuples.
    """
    field_pattern = re.compile(
        r"^\s*(?:" + "|".join(YAML_IMAGE_FIELDS) + r"):\s+(\S+)\s*$",
        re.MULTILINE,
    )
    results = []
    for m in field_pattern.finditer(yaml_block):
        path = m.group(1)
        if not is_absolute_url(path):
            results.append((path, _resolve_relative_path(path, course_dir)))
    return results


def _find_tag_url_warnings_in_yaml(yaml_block: str) -> list[str]:
    """
    Return absolute URLs in YAML image/link fields that point to a
    ``refs/tags/…`` snapshot of this repository.

    Such URLs should be updated to point to ``refs/heads/main`` instead so
    that the asset is always served from the latest version of the main branch.

    Returns:
        List of tag-based URL strings found in the header.
    """
    field_pattern = re.compile(
        r"^\s*(?:" + "|".join(YAML_IMAGE_FIELDS) + r"):\s+(\S+)\s*$",
        re.MULTILINE,
    )
    warnings = []
    for m in field_pattern.finditer(yaml_block):
        value = m.group(1)
        if value.startswith(_OUR_RAW_TAGS_PREFIX):
            warnings.append(value)
    return warnings


def _find_relative_paths_in_body(
    body: str, course_dir: str
) -> list[tuple[str, str]]:
    """
    Return all relative image paths found in the markdown/HTML body.

    Returns:
        List of ``(original_relative_path, resolved_repo_relative_path)`` tuples.
    """
    results = []

    # Markdown images
    for m in _MD_IMAGE_PATTERN.finditer(body):
        path = m.group(2)  # group 1 = alt, group 2 = URL
        if not is_absolute_url(path):
            results.append((path, _resolve_relative_path(path, course_dir)))

    # HTML img – double quotes
    for m in _HTML_SRC_DQ_PATTERN.finditer(body):
        path = m.group(2)
        if path and not is_absolute_url(path):
            results.append((path, _resolve_relative_path(path, course_dir)))

    # HTML img – single quotes
    for m in _HTML_SRC_SQ_PATTERN.finditer(body):
        path = m.group(2)
        if path and not is_absolute_url(path):
            results.append((path, _resolve_relative_path(path, course_dir)))

    return results


def convert_file(filepath: Path, repo_root: Path = REPO_ROOT) -> "ConversionResult":
    """
    Convert all relative image links in a course file to absolute URLs in-place
    and check that every referenced relative path actually exists on disk.

    Args:
        filepath: Absolute path to the course markdown file
        repo_root: Absolute path to the repository root

    Returns:
        :class:`ConversionResult` whose ``modified`` flag is ``True`` when the
        file was rewritten and whose ``missing_paths`` list contains the
        repo-relative paths of every referenced image that could not be found.
    """
    try:
        content = filepath.read_text(encoding="utf-8")
    except OSError as e:
        print(f"  ❌ Cannot read {filepath}: {e}", file=sys.stderr)
        return ConversionResult(modified=False)

    # Determine the course directory relative to the repo root (POSIX style)
    try:
        course_dir = filepath.parent.relative_to(repo_root).as_posix()
    except ValueError:
        # filepath is not under repo_root – use its parent directly
        course_dir = filepath.parent.as_posix()

    # ── Split content into YAML header and body ────────────────────────────
    # The LiaScript YAML header is the first <!-- ... --> block in the file.
    header_match = re.search(r"(<!--\s*)(.*?)(\s*-->)", content, re.DOTALL)
    if not header_match:
        # No YAML header found; nothing to do
        return ConversionResult(modified=False)

    before_header = content[: header_match.start()]
    open_tag = header_match.group(1)
    yaml_block = header_match.group(2)
    close_tag = header_match.group(3)
    after_header = content[header_match.end() :]

    # ── Check existence of relative paths ─────────────────────────────────
    missing_paths: list[str] = []
    all_relative = (
        _find_relative_paths_in_yaml(yaml_block, course_dir)
        + _find_relative_paths_in_body(after_header, course_dir)
    )
    for orig_path, resolved in all_relative:
        if not (repo_root / resolved).exists():
            missing_paths.append(orig_path)

    # ── Check for tag-based URLs that should point to refs/heads/main ──────
    tag_url_warnings = _find_tag_url_warnings_in_yaml(yaml_block)

    # ── Convert YAML header ────────────────────────────────────────────────
    new_yaml_block = convert_yaml_header(yaml_block, course_dir)

    # ── Convert body ───────────────────────────────────────────────────────
    new_body = convert_body(after_header, course_dir)

    new_content = before_header + open_tag + new_yaml_block + close_tag + new_body

    modified = new_content != content
    if modified:
        filepath.write_text(new_content, encoding="utf-8")

    return ConversionResult(
        modified=modified,
        missing_paths=missing_paths,
        tag_url_warnings=tag_url_warnings,
    )


def convert_all_courses(courses_dir: Path = None) -> list[Path]:
    """
    Convert relative image links in all course markdown files.

    Args:
        courses_dir: Directory containing course files (defaults to <repo_root>/courses)

    Returns:
        List of files that were modified
    """
    if courses_dir is None:
        courses_dir = REPO_ROOT / "courses"

    modified = []
    for md_file in sorted(courses_dir.rglob("*.md")):
        if convert_file(md_file):
            modified.append(md_file)

    return modified


def main():
    """
    CLI entry point.

    Usage:
        python3 convert_relative_links.py [file1.md file2.md ...]

    If no files are specified, all course files are processed.
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert relative image links in course files to absolute URLs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "files",
        nargs="*",
        metavar="FILE",
        help="Course markdown file(s) to convert. If omitted, all courses are processed.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which files would be modified without actually changing them",
    )
    args = parser.parse_args()

    if args.files:
        targets = [Path(f) for f in args.files]
    else:
        targets = sorted((REPO_ROOT / "courses").rglob("*.md"))

    modified_count = 0
    missing_count = 0
    tag_warning_count = 0
    for filepath in targets:
        if not filepath.exists():
            print(f"⚠️  File not found: {filepath}")
            continue

        if args.dry_run:
            # Check without writing - use a temporary copy
            content = filepath.read_text(encoding="utf-8")

            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".md", delete=False, encoding="utf-8"
            ) as tmp:
                tmp.write(content)
                tmp_path = Path(tmp.name)
            try:
                result = convert_file(tmp_path, REPO_ROOT)
            finally:
                tmp_path.unlink(missing_ok=True)

            if result.modified:
                print(f"  📝 Would convert: {filepath}")
                modified_count += 1
            for mp in result.missing_paths:
                print(f"  ❌ Missing image '{mp}' referenced in {filepath}")
                missing_count += 1
            for tw in result.tag_url_warnings:
                print(f"  ⚠️  Tag-based URL in {filepath}:")
                print(f"      {tw}")
                print(f"      Replace 'refs/tags/…' with 'refs/heads/main'")
                tag_warning_count += 1
        else:
            result = convert_file(filepath)
            if result.modified:
                print(f"  ✅ Converted: {filepath}")
                modified_count += 1
            for mp in result.missing_paths:
                print(f"  ❌ Missing image '{mp}' referenced in {filepath}")
                missing_count += 1
            for tw in result.tag_url_warnings:
                print(f"  ⚠️  Tag-based URL in {filepath}:")
                print(f"      {tw}")
                print(f"      Replace 'refs/tags/…' with 'refs/heads/main'")
                tag_warning_count += 1

    if modified_count == 0 and missing_count == 0 and tag_warning_count == 0:
        print("✅ No relative image links found – all links are already absolute.")
    else:
        if modified_count:
            action = "would be" if args.dry_run else "were"
            print(f"\n✅ {modified_count} file(s) {action} updated.")
        if tag_warning_count:
            print(f"\n⚠️  {tag_warning_count} tag-based URL(s) found.")
            print("   Update them to point to refs/heads/main.")
        if missing_count:
            print(f"\n❌ {missing_count} missing image path(s) found.")
            print("   Fix the typos above before committing.")
            sys.exit(1)


if __name__ == "__main__":
    main()
