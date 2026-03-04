#!/usr/bin/env python3
"""Tests for generate_quarto_website.py"""

import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_quarto_website import (
    category_to_slug,
    category_display_name,
    get_all_categories,
    resolve_logo,
    write_index_page,
    write_category_page,
    COURSES_RAW_BASE,
)
from generate_project_yaml import CATEGORY_LIST


# ---------------------------------------------------------------------------
# category_to_slug
# ---------------------------------------------------------------------------


def test_category_to_slug_simple():
    assert category_to_slug("Tischler") == "tischler"
    print("✓ test_category_to_slug_simple")


def test_category_to_slug_with_underscores():
    assert category_to_slug("Arbeits-_und_Gesundheitsschutz") == "arbeits-und-gesundheitsschutz"
    print("✓ test_category_to_slug_with_underscores")


def test_category_to_slug_uppercase_acronym():
    assert category_to_slug("SHK") == "shk"
    print("✓ test_category_to_slug_uppercase_acronym")


def test_category_to_slug_all_categories():
    """All CATEGORY_LIST entries must produce a non-empty slug."""
    for cat in CATEGORY_LIST:
        slug = category_to_slug(cat)
        assert slug, f"Empty slug for category '{cat}'"
        assert slug == slug.lower(), f"Slug not lower-case for '{cat}': {slug}"
    print("✓ test_category_to_slug_all_categories")


# ---------------------------------------------------------------------------
# category_display_name
# ---------------------------------------------------------------------------


def test_category_display_name_plain():
    assert category_display_name("Tischler") == "Tischler"
    print("✓ test_category_display_name_plain")


def test_category_display_name_compound():
    assert (
        category_display_name("Arbeits-_und_Gesundheitsschutz")
        == "Arbeits- und Gesundheitsschutz"
    )
    print("✓ test_category_display_name_compound")


# ---------------------------------------------------------------------------
# get_all_categories
# ---------------------------------------------------------------------------


def test_get_all_categories_multi():
    """A course tagged with two trade categories must appear in both."""
    result = get_all_categories({"tags": ["Maler", "Raumausstatter"]})
    assert "Maler" in result
    assert "Raumausstatter" in result
    print("✓ test_get_all_categories_multi")


def test_get_all_categories_single():
    result = get_all_categories({"tags": ["Tischler", "Holzarten"]})
    assert result == ["Tischler"]
    print("✓ test_get_all_categories_single")


def test_get_all_categories_no_match():
    """Courses with no matching category tag fall into 'Sonstige'."""
    result = get_all_categories({"tags": ["UnknownTag"]})
    assert result == ["Sonstige"]
    print("✓ test_get_all_categories_no_match")


def test_get_all_categories_empty_tags():
    result = get_all_categories({"tags": []})
    assert result == ["Sonstige"]
    print("✓ test_get_all_categories_empty_tags")


def test_get_all_categories_none_tags():
    result = get_all_categories({"tags": None})
    assert result == ["Sonstige"]
    print("✓ test_get_all_categories_none_tags")


def test_get_all_categories_string_tag():
    """Tags stored as a plain string should also be handled."""
    result = get_all_categories({"tags": "Tischler"})
    assert "Tischler" in result
    print("✓ test_get_all_categories_string_tag")


# ---------------------------------------------------------------------------
# resolve_logo
# ---------------------------------------------------------------------------


def test_resolve_logo_absolute_url_unchanged():
    url = "https://example.com/img/logo.jpg"
    assert resolve_logo(url) == url
    print("✓ test_resolve_logo_absolute_url_unchanged")


def test_resolve_logo_relative_path_expanded():
    result = resolve_logo("img/farben.jpg")
    assert result == COURSES_RAW_BASE + "img/farben.jpg"
    assert result.startswith("https://")
    print("✓ test_resolve_logo_relative_path_expanded")


def test_resolve_logo_empty_string():
    assert resolve_logo("") == ""
    print("✓ test_resolve_logo_empty_string")


def test_resolve_logo_leading_slash_stripped():
    result = resolve_logo("/img/farben.jpg")
    assert result == COURSES_RAW_BASE + "img/farben.jpg"
    print("✓ test_resolve_logo_leading_slash_stripped")


# ---------------------------------------------------------------------------
# File writers (smoke tests using a temporary directory)
# ---------------------------------------------------------------------------


def _sample_categories():
    return {
        "Tischler": [
            {
                "title": "Holzarten I",
                "comment": "Quiz zu Holz",
                "logo": "https://example.com/logo.jpg",
                "tags": ["Tischler", "Holzarten"],
                "url": "https://raw.githubusercontent.com/org/repo/refs/tags/holzarten_01_v1.0/courses/Holzarten_01.md",
                "release_urls": {
                    "PDF": "https://github.com/org/repo/releases/download/holzarten_01_v1.0/Holzarten_01_v1.0_Documentation.pdf",
                    "SCORM": "https://github.com/org/repo/releases/download/holzarten_01_v1.0/Holzarten_01_v1.0_SCORM.zip",
                },
            }
        ],
        "SHK": [
            {
                "title": "Grundkurs SHK",
                "comment": "",
                "logo": "",
                "tags": ["SHK"],
                "url": "https://raw.githubusercontent.com/org/repo/refs/heads/main/courses/GIH1.md",
                "release_urls": {},
            }
        ],
    }


def test_write_index_page_contains_category_links():
    cats = _sample_categories()
    with tempfile.TemporaryDirectory() as tmpdir:
        out = Path(tmpdir)
        write_index_page(cats, out)
        content = (out / "index.qmd").read_text(encoding="utf-8")
        assert "[Tischler](tischler.qmd)" in content
        assert "[SHK](shk.qmd)" in content
        assert "1 Kurs*" in content  # singular for SHK with one course
    print("✓ test_write_index_page_contains_category_links")


def test_write_category_page_contains_course_info():
    cats = _sample_categories()
    with tempfile.TemporaryDirectory() as tmpdir:
        out = Path(tmpdir)
        write_category_page("Tischler", cats["Tischler"], out)
        content = (out / "tischler.qmd").read_text(encoding="utf-8")
        assert "Holzarten I" in content
        assert "https://liascript.github.io/course/?" in content
        assert "📄 PDF" in content
        assert "📦 SCORM" in content
        assert "`Tischler`" in content
    print("✓ test_write_category_page_contains_course_info")


def test_write_category_page_no_release_links_when_empty():
    cats = _sample_categories()
    with tempfile.TemporaryDirectory() as tmpdir:
        out = Path(tmpdir)
        write_category_page("SHK", cats["SHK"], out)
        content = (out / "shk.qmd").read_text(encoding="utf-8")
        assert "Grundkurs SHK" in content
        assert "📄 PDF" not in content
        assert "📦 SCORM" not in content
    print("✓ test_write_category_page_no_release_links_when_empty")


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


def run_all_tests():
    print("\n" + "=" * 60)
    print("Running tests for generate_quarto_website.py")
    print("=" * 60 + "\n")

    tests = [
        test_category_to_slug_simple,
        test_category_to_slug_with_underscores,
        test_category_to_slug_uppercase_acronym,
        test_category_to_slug_all_categories,
        test_category_display_name_plain,
        test_category_display_name_compound,
        test_get_all_categories_multi,
        test_get_all_categories_single,
        test_get_all_categories_no_match,
        test_get_all_categories_empty_tags,
        test_get_all_categories_none_tags,
        test_get_all_categories_string_tag,
        test_resolve_logo_absolute_url_unchanged,
        test_resolve_logo_relative_path_expanded,
        test_resolve_logo_empty_string,
        test_resolve_logo_leading_slash_stripped,
        test_write_index_page_contains_category_links,
        test_write_category_page_contains_course_info,
        test_write_category_page_no_release_links_when_empty,
    ]

    failed = []
    for test in tests:
        try:
            test()
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed.append((test.__name__, str(e)))
        except Exception as e:
            print(f"✗ {test.__name__} errored: {e}")
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
