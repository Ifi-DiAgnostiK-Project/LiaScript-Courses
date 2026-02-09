#!/usr/bin/env python3
"""
Tests for generate_project_yaml.py

This test suite validates the tag existence checking and URL generation functionality.
"""

import tempfile
import os
import sys
from pathlib import Path
import subprocess

# Import the functions we want to test
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_project_yaml import tag_exists, get_url, to_github_tag, get_git_tags


def test_tag_exists_with_existing_tag():
    """Test that tag_exists returns True for existing tags"""
    # Get actual tags from the repository
    tags = get_git_tags()
    
    if not tags:
        print("⚠ No tags found in repository, skipping test")
        return
    
    # Pick a tag we know exists
    sample_tag = next(iter(tags))
    assert tag_exists(sample_tag), f"Should find existing tag: {sample_tag}"
    print(f"✓ test_tag_exists_with_existing_tag passed (tested with {sample_tag})")


def test_tag_exists_with_non_existing_tag():
    """Test that tag_exists returns False for non-existing tags"""
    fake_tag = "this_tag_definitely_does_not_exist_v999.999.999"
    assert not tag_exists(fake_tag), f"Should not find non-existing tag: {fake_tag}"
    print("✓ test_tag_exists_with_non_existing_tag passed")


def test_get_url_with_existing_tag():
    """Test that get_url generates tag-based URL when tag exists"""
    # Create a mock file path
    test_file = Path("courses/test_course.md")
    test_version = "0.0.1"
    
    # Get actual tags to find one that exists
    tags = get_git_tags()
    if not tags:
        print("⚠ No tags found in repository, skipping test")
        return
    
    # Find a tag that matches our pattern (if any)
    matching_tags = [t for t in tags if t.endswith(f"_v{test_version}")]
    if not matching_tags:
        print("⚠ No matching tags found, skipping test")
        return
    
    # Use a real course file that has a tag
    sample_tag = matching_tags[0]
    course_name = sample_tag.rsplit("_v", 1)[0]
    test_file = Path(f"courses/{course_name}.md")
    
    url = get_url(test_file, test_version, tagged=True)
    assert "refs/tags/" in url, f"Should use tag-based URL: {url}"
    assert f"_v{test_version}" in url, f"Should include version in URL: {url}"
    print(f"✓ test_get_url_with_existing_tag passed (URL: {url})")


def test_get_url_with_non_existing_tag():
    """Test that get_url falls back to HEAD when tag doesn't exist"""
    test_file = Path("courses/nonexistent_course.md")
    test_version = "999.999.999"
    
    url = get_url(test_file, test_version, tagged=True)
    assert "refs/heads/main" in url, f"Should fall back to HEAD URL: {url}"
    assert "refs/tags/" not in url, f"Should not use tag-based URL: {url}"
    print(f"✓ test_get_url_with_non_existing_tag passed (URL: {url})")


def test_get_url_external_url():
    """Test that get_url returns external URLs as-is"""
    external_url = "https://example.com/course.md"
    result = get_url(external_url, "1.0.0", tagged=True)
    assert result == external_url, f"Should return external URL unchanged: {result}"
    print("✓ test_get_url_external_url passed")


def test_get_url_not_tagged():
    """Test that get_url uses HEAD URL when tagged=False"""
    test_file = Path("courses/test_course.md")
    test_version = "1.0.0"
    
    url = get_url(test_file, test_version, tagged=False)
    assert "refs/heads/main" in url, f"Should use HEAD URL when tagged=False: {url}"
    assert "refs/tags/" not in url, f"Should not use tag-based URL: {url}"
    print("✓ test_get_url_not_tagged passed")


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("Running tests for generate_project_yaml.py")
    print("="*60 + "\n")
    
    tests = [
        test_tag_exists_with_existing_tag,
        test_tag_exists_with_non_existing_tag,
        test_get_url_with_existing_tag,
        test_get_url_with_non_existing_tag,
        test_get_url_external_url,
        test_get_url_not_tagged,
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
    
    print("\n" + "="*60)
    if failed:
        print(f"FAILED: {len(failed)} test(s) failed")
        for name, error in failed:
            print(f"  - {name}: {error}")
        sys.exit(1)
    else:
        print(f"SUCCESS: All {len(tests)} tests passed")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_all_tests()
