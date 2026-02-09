#!/usr/bin/env python3
"""
Tests for validate_course_yaml.py

This test suite validates the YAML validation functionality.
"""

import tempfile
import os
import sys
from pathlib import Path

# Import the validation functions
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from validate_course_yaml import validate_course_file, ValidationResult


def test_valid_yaml():
    """Test that valid YAML is accepted"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write("""<!--
author: Test Author
email: test@example.com
version: 1.0.0
language: de
narrator: Deutsch Male
title: Test Course
tags:
  - Test
-->

# Test Course
Content here
""")
        f.flush()
        
        try:
            result = validate_course_file(f.name)
            assert result.success, f"Valid YAML should pass: {result.error_message}"
            assert result.error_message is None, "Valid YAML should have no error message"
            assert result.warning_message is None, "Valid YAML should have no warning message"
            print("✓ test_valid_yaml passed")
        finally:
            os.unlink(f.name)


def test_yaml_with_unquoted_brackets():
    """Test that YAML with unquoted brackets fails"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write("""<!--
author: Test Author
version: 1.0.0
attribute: [[This has unquoted brackets](https://example.com)]
tags:
  - Test
-->

# Test Course
""")
        f.flush()
        
        try:
            result = validate_course_file(f.name)
            assert not result.success, "Invalid YAML should fail"
            assert result.error_message is not None, "Invalid YAML should have error message"
            print("✓ test_yaml_with_unquoted_brackets passed")
        finally:
            os.unlink(f.name)


def test_yaml_with_quoted_brackets():
    """Test that YAML with properly quoted brackets succeeds"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write("""<!--
author: Test Author
email: test@example.com
version: 1.0.0
language: de
narrator: Deutsch Male
title: Test Course
attribute: "[[This has quoted brackets](https://example.com)]"
tags:
  - Test
-->

# Test Course
""")
        f.flush()
        
        try:
            result = validate_course_file(f.name)
            assert result.success, f"Valid quoted YAML should pass: {result.error_message}"
            print("✓ test_yaml_with_quoted_brackets passed")
        finally:
            os.unlink(f.name)


def test_missing_yaml_comment_block():
    """Test that files without YAML comment block are detected"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write("""# Test Course
Content here with no YAML header
""")
        f.flush()
        
        try:
            result = validate_course_file(f.name)
            assert not result.success, "Missing YAML should fail"
            assert "No YAML comment block" in result.warning_message, "Should mention missing YAML"
            print("✓ test_missing_yaml_comment_block passed")
        finally:
            os.unlink(f.name)


def test_missing_version_field():
    """Test that missing version field generates warning"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write("""<!--
author: Test Author
email: test@example.com
title: Test Course
tags:
  - Test
-->

# Test Course
""")
        f.flush()
        
        try:
            result = validate_course_file(f.name)
            assert result.success, "Missing version should still parse successfully"
            assert result.warning_message is not None, "Missing version should generate warning"
            assert "version" in result.warning_message.lower(), "Warning should mention version"
            print("✓ test_missing_version_field passed")
        finally:
            os.unlink(f.name)


def test_empty_yaml():
    """Test that empty YAML block fails"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
        f.write("""<!--
-->

# Test Course
""")
        f.flush()
        
        try:
            result = validate_course_file(f.name)
            assert not result.success, "Empty YAML should fail"
            print("✓ test_empty_yaml passed")
        finally:
            os.unlink(f.name)


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("Running tests for validate_course_yaml.py")
    print("="*60 + "\n")
    
    tests = [
        test_valid_yaml,
        test_yaml_with_unquoted_brackets,
        test_yaml_with_quoted_brackets,
        test_missing_yaml_comment_block,
        test_missing_version_field,
        test_empty_yaml,
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
