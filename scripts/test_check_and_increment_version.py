#!/usr/bin/env python3
"""
Tests for check_and_increment_version.py

This test suite validates the version checking and incrementing functionality.
"""

import tempfile
import os
import sys
from pathlib import Path

# Import the functions we want to test
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_and_increment_version import extract_version_from_content, increment_patch_version


def test_extract_version_basic():
    """Test basic version extraction"""
    content = """<!--
version: 1.2.3
-->
"""
    result = extract_version_from_content(content)
    assert result is not None, "Should find version"
    full_match, major, minor, patch = result
    assert major == 1
    assert minor == 2
    assert patch == 3
    print("✓ test_extract_version_basic passed")


def test_extract_version_with_spaces():
    """Test version extraction with various whitespace"""
    test_cases = [
        ("version:   1.2.3", (1, 2, 3)),
        ("version:1.2.3", (1, 2, 3)),
        ("version: 0.0.5", (0, 0, 5)),
        ("version:  10.20.30  ", (10, 20, 30)),
    ]
    
    for line, expected in test_cases:
        content = f"<!--\n{line}\n-->"
        result = extract_version_from_content(content)
        assert result is not None, f"Should find version in: {line}"
        _, major, minor, patch = result
        exp_major, exp_minor, exp_patch = expected
        assert major == exp_major and minor == exp_minor and patch == exp_patch, \
            f"Expected {expected}, got ({major}, {minor}, {patch})"
    
    print("✓ test_extract_version_with_spaces passed")


def test_extract_version_not_found():
    """Test when version is not present"""
    content = """<!--
author: Test
title: My Course
-->
"""
    result = extract_version_from_content(content)
    assert result is None, "Should not find version"
    print("✓ test_extract_version_not_found passed")


def test_increment_patch_version_functionality():
    """Test the version increment functionality"""
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write("""<!--
author: Test Author
version: 1.2.3
title: Test Course
-->

# Test Content
""")
        temp_path = f.name
    
    try:
        # Run the increment function
        success = increment_patch_version(temp_path)
        assert success, "Should successfully increment version"
        
        # Read the result
        with open(temp_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check the version was incremented
        result = extract_version_from_content(content)
        assert result is not None, "Should still have a version"
        _, major, minor, patch = result
        assert major == 1 and minor == 2 and patch == 4, \
            f"Expected version 1.2.4, got {major}.{minor}.{patch}"
        
        print("✓ test_increment_patch_version_functionality passed")
        
    finally:
        # Clean up
        os.unlink(temp_path)


def test_increment_preserves_formatting():
    """Test that increment preserves the original formatting"""
    test_cases = [
        ("version: 0.0.5", "version: 0.0.6"),
        ("version:  1.2.3", "version:  1.2.4"),
        ("version:10.20.30", "version:10.20.31"),
    ]
    
    for original, expected in test_cases:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
            f.write(f"<!--\n{original}\n-->\n# Content")
            temp_path = f.name
        
        try:
            success = increment_patch_version(temp_path)
            assert success, f"Should successfully increment version for: {original}"
            
            with open(temp_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            assert expected in content, f"Expected to find '{expected}' in content"
            print(f"  ✓ Correctly handled: {original} → {expected}")
            
        finally:
            os.unlink(temp_path)
    
    print("✓ test_increment_preserves_formatting passed")


def test_increment_with_missing_version():
    """Test increment when version tag is missing"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write("""<!--
author: Test Author
title: Test Course
-->
# Content
""")
        temp_path = f.name
    
    try:
        # Should return False when version is missing
        success = increment_patch_version(temp_path)
        assert not success, "Should fail when version tag is missing"
        print("✓ test_increment_with_missing_version passed")
        
    finally:
        os.unlink(temp_path)


def run_all_tests():
    """Run all tests"""
    print("Running tests for check_and_increment_version.py...\n")
    
    tests = [
        test_extract_version_basic,
        test_extract_version_with_spaces,
        test_extract_version_not_found,
        test_increment_patch_version_functionality,
        test_increment_preserves_formatting,
        test_increment_with_missing_version,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Results: {passed} passed, {failed} failed")
    print(f"{'='*60}")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
