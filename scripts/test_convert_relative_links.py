#!/usr/bin/env python3
"""
Tests for convert_relative_links.py

This test suite validates the relative-to-absolute link conversion logic.
"""

import sys
import os
import shutil
import tempfile
from pathlib import Path

# Make sure the scripts directory is on the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from convert_relative_links import (
    is_absolute_url,
    make_absolute_url,
    convert_yaml_header,
    convert_body,
    convert_file,
    ConversionResult,
    RAW_BASE_URL,
    REPO_ROOT,
)


# ── Helpers ────────────────────────────────────────────────────────────────


def make_course_file(content: str) -> tuple[Path, Path]:
    """
    Write *content* to a temporary file inside a temporary 'courses/' directory.

    Returns (filepath, repo_root) so callers can pass both to convert_file().
    """
    tmp_repo = Path(tempfile.mkdtemp())
    courses_dir = tmp_repo / "courses"
    courses_dir.mkdir()
    md_file = courses_dir / "test_course.md"
    md_file.write_text(content, encoding="utf-8")
    return md_file, tmp_repo


def cleanup(tmp_repo: Path):
    shutil.rmtree(tmp_repo, ignore_errors=True)


# ── Unit tests ─────────────────────────────────────────────────────────────


def test_is_absolute_url():
    """is_absolute_url correctly identifies http/https URLs."""
    assert is_absolute_url("https://example.com/foo.png")
    assert is_absolute_url("http://example.com/foo.png")
    assert not is_absolute_url("img/foo.png")
    assert not is_absolute_url("./img/foo.png")
    assert not is_absolute_url("../img/foo.png")
    assert not is_absolute_url("")
    print("✓ test_is_absolute_url passed")


def test_make_absolute_url_simple():
    """make_absolute_url converts a simple relative path correctly."""
    url = make_absolute_url("img/foo.jpg", "courses")
    assert url == f"{RAW_BASE_URL}/courses/img/foo.jpg", f"Unexpected: {url}"
    print("✓ test_make_absolute_url_simple passed")


def test_make_absolute_url_dot_prefix():
    """make_absolute_url strips a leading './' from the relative path."""
    url = make_absolute_url("./img/foo.jpg", "courses")
    assert url == f"{RAW_BASE_URL}/courses/img/foo.jpg", f"Unexpected: {url}"
    print("✓ test_make_absolute_url_dot_prefix passed")


def test_make_absolute_url_parent_traversal():
    """make_absolute_url resolves '../' correctly."""
    url = make_absolute_url("../img/foo.jpg", "courses/subdir")
    assert url == f"{RAW_BASE_URL}/courses/img/foo.jpg", f"Unexpected: {url}"
    print("✓ test_make_absolute_url_parent_traversal passed")


def test_convert_yaml_header_logo():
    """convert_yaml_header converts a relative logo: value."""
    yaml_block = "\nauthor: Test\nlogo: img/cover.jpg\n"
    result = convert_yaml_header(yaml_block, "courses")
    expected = f"logo: {RAW_BASE_URL}/courses/img/cover.jpg"
    assert expected in result, f"Expected '{expected}' in:\n{result}"
    print("✓ test_convert_yaml_header_logo passed")


def test_convert_yaml_header_icon():
    """convert_yaml_header converts a relative icon: value."""
    yaml_block = "\nauthor: Test\nicon: img/icon.png\n"
    result = convert_yaml_header(yaml_block, "courses")
    assert f"{RAW_BASE_URL}/courses/img/icon.png" in result, f"Unexpected: {result}"
    print("✓ test_convert_yaml_header_icon passed")


def test_convert_yaml_header_already_absolute():
    """convert_yaml_header leaves already-absolute logo: values unchanged."""
    abs_url = "https://example.com/logo.png"
    yaml_block = f"\nauthor: Test\nlogo: {abs_url}\n"
    result = convert_yaml_header(yaml_block, "courses")
    assert abs_url in result
    assert result == yaml_block, "Absolute URL should not be modified"
    print("✓ test_convert_yaml_header_already_absolute passed")


def test_convert_body_markdown_image():
    """convert_body converts a relative Markdown image link."""
    body = "\n![Alt text](img/photo.jpg)\n"
    result = convert_body(body, "courses")
    assert f"{RAW_BASE_URL}/courses/img/photo.jpg" in result, f"Unexpected: {result}"
    print("✓ test_convert_body_markdown_image passed")


def test_convert_body_markdown_image_with_title():
    """convert_body converts a Markdown image with a title/caption."""
    body = '![Alt](img/photo.jpg "_Caption_")\n'
    result = convert_body(body, "courses")
    assert f"{RAW_BASE_URL}/courses/img/photo.jpg" in result, f"Unexpected: {result}"
    assert '"_Caption_"' in result, "Caption should be preserved"
    print("✓ test_convert_body_markdown_image_with_title passed")


def test_convert_body_markdown_image_already_absolute():
    """convert_body leaves absolute Markdown image links unchanged."""
    abs_url = "https://example.com/photo.jpg"
    body = f"![Alt]({abs_url})\n"
    result = convert_body(body, "courses")
    assert result == body, "Absolute Markdown image link should not be modified"
    print("✓ test_convert_body_markdown_image_already_absolute passed")


def test_convert_body_html_img_double_quotes():
    """convert_body converts a relative HTML <img src="..."> with double quotes."""
    body = '<img src="img/photo.jpg" alt="test">\n'
    result = convert_body(body, "courses")
    assert f'src="{RAW_BASE_URL}/courses/img/photo.jpg"' in result, f"Unexpected: {result}"
    print("✓ test_convert_body_html_img_double_quotes passed")


def test_convert_body_html_img_single_quotes():
    """convert_body converts a relative HTML <img src='...'> with single quotes."""
    body = "<img src='img/photo.jpg' alt='test'>\n"
    result = convert_body(body, "courses")
    assert f"src='{RAW_BASE_URL}/courses/img/photo.jpg'" in result, f"Unexpected: {result}"
    print("✓ test_convert_body_html_img_single_quotes passed")


def test_convert_body_html_img_already_absolute():
    """convert_body leaves absolute HTML img src attributes unchanged."""
    abs_url = "https://example.com/photo.jpg"
    body = f'<img src="{abs_url}" alt="test">\n'
    result = convert_body(body, "courses")
    assert result == body, "Absolute HTML img src should not be modified"
    print("✓ test_convert_body_html_img_already_absolute passed")


def test_convert_file_modifies_relative_links():
    """convert_file rewrites relative links and returns True."""
    content = """\
<!--

author: Test Author
version: 0.1.0
logo: img/logo.png
icon: img/icon.png

-->

# Test Course

![Photo](img/photo.jpg)

<img src="img/banner.png" alt="banner">
"""
    filepath, repo_root = make_course_file(content)
    try:
        changed = convert_file(filepath, repo_root)
        assert changed, "File with relative links should be marked as modified"

        result = filepath.read_text(encoding="utf-8")
        base = f"{RAW_BASE_URL}/courses"
        assert f"logo: {base}/img/logo.png" in result, f"logo not converted:\n{result}"
        assert f"icon: {base}/img/icon.png" in result, f"icon not converted:\n{result}"
        assert f"![Photo]({base}/img/photo.jpg)" in result, f"md image not converted:\n{result}"
        assert f'src="{base}/img/banner.png"' in result, f"html img not converted:\n{result}"
        print("✓ test_convert_file_modifies_relative_links passed")
    finally:
        cleanup(repo_root)


def test_convert_file_no_changes_when_already_absolute():
    """convert_file returns False when all links are already absolute."""
    base = f"{RAW_BASE_URL}/courses"
    content = f"""\
<!--

author: Test Author
version: 0.1.0
logo: {base}/img/logo.png
icon: {base}/img/icon.png

-->

# Test Course

![Photo]({base}/img/photo.jpg)

<img src="{base}/img/banner.png" alt="banner">
"""
    filepath, repo_root = make_course_file(content)
    try:
        changed = convert_file(filepath, repo_root)
        assert not changed, "File with only absolute links should not be modified"
        print("✓ test_convert_file_no_changes_when_already_absolute passed")
    finally:
        cleanup(repo_root)


def test_convert_file_no_yaml_header():
    """convert_file returns False when there is no YAML header."""
    content = "# Course without YAML header\n\n![Photo](img/photo.jpg)\n"
    filepath, repo_root = make_course_file(content)
    try:
        changed = convert_file(filepath, repo_root)
        assert not changed, "File without YAML header should not be modified"
        print("✓ test_convert_file_no_yaml_header passed")
    finally:
        cleanup(repo_root)


def test_convert_file_mixed_links():
    """convert_file converts only relative links, leaving absolute ones intact."""
    abs_url = "https://upload.wikimedia.org/example.jpg"
    base = f"{RAW_BASE_URL}/courses"
    content = f"""\
<!--

author: Test Author
version: 0.1.0
logo: img/logo.png

-->

# Test Course

![Absolute]({abs_url})
![Relative](img/local.jpg)
"""
    filepath, repo_root = make_course_file(content)
    try:
        changed = convert_file(filepath, repo_root)
        assert changed

        result = filepath.read_text(encoding="utf-8")
        assert f"logo: {base}/img/logo.png" in result
        assert f"![Absolute]({abs_url})" in result, "Absolute image should be unchanged"
        assert f"![Relative]({base}/img/local.jpg)" in result
        print("✓ test_convert_file_mixed_links passed")
    finally:
        cleanup(repo_root)


def make_course_file_with_images(content: str, image_rel_paths: list[str]) -> tuple[Path, Path]:
    """
    Write *content* to a temporary file and also create stub image files for
    each relative path listed in *image_rel_paths* (relative to the course
    file's directory, i.e. ``<tmp_repo>/courses/``).

    Returns (filepath, repo_root).
    """
    filepath, repo_root = make_course_file(content)
    for rel_path in image_rel_paths:
        img_file = filepath.parent / rel_path
        img_file.parent.mkdir(parents=True, exist_ok=True)
        img_file.write_bytes(b"stub")  # minimal non-empty stub
    return filepath, repo_root


# ── Existence-checking tests ───────────────────────────────────────────────


def test_convert_file_returns_conversion_result():
    """convert_file returns a ConversionResult, not a plain bool."""
    content = """\
<!--
author: Test Author
version: 0.1.0
-->
# Course
"""
    filepath, repo_root = make_course_file(content)
    try:
        result = convert_file(filepath, repo_root)
        assert isinstance(result, ConversionResult), \
            f"Expected ConversionResult, got {type(result)}"
        print("✓ test_convert_file_returns_conversion_result passed")
    finally:
        cleanup(repo_root)


def test_convert_file_no_missing_when_images_exist():
    """convert_file reports no missing paths when the referenced images exist on disk."""
    content = """\
<!--
author: Test Author
version: 0.1.0
logo: img/logo.png
-->
# Course
![Photo](img/photo.jpg)
"""
    filepath, repo_root = make_course_file_with_images(
        content, ["img/logo.png", "img/photo.jpg"]
    )
    try:
        result = convert_file(filepath, repo_root)
        assert result.modified, "Should have converted relative links"
        assert result.missing_paths == [], \
            f"No missing paths expected, got: {result.missing_paths}"
        print("✓ test_convert_file_no_missing_when_images_exist passed")
    finally:
        cleanup(repo_root)


def test_convert_file_detects_missing_markdown_image():
    """convert_file reports a missing path for a Markdown image that doesn't exist."""
    content = """\
<!--
author: Test Author
version: 0.1.0
-->
# Course
![Photo](img/typo_photo.jpg)
"""
    filepath, repo_root = make_course_file(content)  # no image files created
    try:
        result = convert_file(filepath, repo_root)
        assert "img/typo_photo.jpg" in result.missing_paths, \
            f"Expected missing path, got: {result.missing_paths}"
        print("✓ test_convert_file_detects_missing_markdown_image passed")
    finally:
        cleanup(repo_root)


def test_convert_file_detects_missing_yaml_logo():
    """convert_file reports a missing path for a logo: field that doesn't exist."""
    content = """\
<!--
author: Test Author
version: 0.1.0
logo: img/missing_logo.png
-->
# Course
"""
    filepath, repo_root = make_course_file(content)
    try:
        result = convert_file(filepath, repo_root)
        assert "img/missing_logo.png" in result.missing_paths, \
            f"Expected missing path, got: {result.missing_paths}"
        print("✓ test_convert_file_detects_missing_yaml_logo passed")
    finally:
        cleanup(repo_root)


def test_convert_file_detects_missing_html_img():
    """convert_file reports a missing path for an HTML <img src> that doesn't exist."""
    content = """\
<!--
author: Test Author
version: 0.1.0
-->
# Course
<img src="img/missing.png" alt="test">
"""
    filepath, repo_root = make_course_file(content)
    try:
        result = convert_file(filepath, repo_root)
        assert "img/missing.png" in result.missing_paths, \
            f"Expected missing path, got: {result.missing_paths}"
        print("✓ test_convert_file_detects_missing_html_img passed")
    finally:
        cleanup(repo_root)


def test_convert_file_absolute_urls_not_existence_checked():
    """convert_file does not existence-check already-absolute URLs."""
    abs_url = "https://example.com/remote_image.jpg"
    content = f"""\
<!--
author: Test Author
version: 0.1.0
-->
# Course
![Remote]({abs_url})
"""
    filepath, repo_root = make_course_file(content)
    try:
        result = convert_file(filepath, repo_root)
        assert result.missing_paths == [], \
            f"Absolute URLs should not be existence-checked, got: {result.missing_paths}"
        print("✓ test_convert_file_absolute_urls_not_existence_checked passed")
    finally:
        cleanup(repo_root)


def test_convert_file_mixed_existing_and_missing():
    """convert_file distinguishes between existing and missing relative paths."""
    content = """\
<!--
author: Test Author
version: 0.1.0
logo: img/exists.png
-->
# Course
![Exists](img/exists.png)
![Missing](img/typo.png)
"""
    filepath, repo_root = make_course_file_with_images(content, ["img/exists.png"])
    try:
        result = convert_file(filepath, repo_root)
        assert "img/typo.png" in result.missing_paths, \
            f"Should report missing 'img/typo.png', got: {result.missing_paths}"
        assert "img/exists.png" not in result.missing_paths, \
            f"Should NOT report existing 'img/exists.png', got: {result.missing_paths}"
        print("✓ test_convert_file_mixed_existing_and_missing passed")
    finally:
        cleanup(repo_root)


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("Running tests for convert_relative_links.py")
    print("=" * 60 + "\n")

    tests = [
        test_is_absolute_url,
        test_make_absolute_url_simple,
        test_make_absolute_url_dot_prefix,
        test_make_absolute_url_parent_traversal,
        test_convert_yaml_header_logo,
        test_convert_yaml_header_icon,
        test_convert_yaml_header_already_absolute,
        test_convert_body_markdown_image,
        test_convert_body_markdown_image_with_title,
        test_convert_body_markdown_image_already_absolute,
        test_convert_body_html_img_double_quotes,
        test_convert_body_html_img_single_quotes,
        test_convert_body_html_img_already_absolute,
        test_convert_file_modifies_relative_links,
        test_convert_file_no_changes_when_already_absolute,
        test_convert_file_no_yaml_header,
        test_convert_file_mixed_links,
        # existence-checking tests
        test_convert_file_returns_conversion_result,
        test_convert_file_no_missing_when_images_exist,
        test_convert_file_detects_missing_markdown_image,
        test_convert_file_detects_missing_yaml_logo,
        test_convert_file_detects_missing_html_img,
        test_convert_file_absolute_urls_not_existence_checked,
        test_convert_file_mixed_existing_and_missing,
    ]

    failed = []
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed.append((test.__name__, str(e)))
        except Exception as e:
            import traceback
            print(f"✗ {test.__name__} errored: {e}")
            traceback.print_exc()
            failed.append((test.__name__, str(e)))

    print("\n" + "=" * 60)
    if failed:
        print(f"FAILED: {len(failed)} test(s) failed")
        for name, error in failed:
            print(f"  - {name}: {error}")
        sys.exit(1)
    else:
        print(f"SUCCESS: All {len(tests)} tests passed")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_all_tests()
