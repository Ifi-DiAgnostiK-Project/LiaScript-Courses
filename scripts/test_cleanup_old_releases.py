#!/usr/bin/env python3
"""
Unit tests for cleanup_old_releases.py script.
"""

import unittest
from cleanup_old_releases import Version, parse_tag, group_tags_by_course, find_tags_to_delete


class TestVersion(unittest.TestCase):
    """Test the Version class."""
    
    def test_version_comparison(self):
        """Test version comparison operators."""
        v1 = Version(1, 0, 0)
        v2 = Version(2, 0, 0)
        v3 = Version(1, 5, 0)
        v4 = Version(1, 0, 5)
        
        self.assertTrue(v1 < v2)
        self.assertTrue(v1 < v3)
        self.assertTrue(v1 < v4)
        self.assertTrue(v4 < v3)
        self.assertTrue(v3 < v2)
    
    def test_version_equality(self):
        """Test version equality."""
        v1 = Version(1, 2, 3)
        v2 = Version(1, 2, 3)
        v3 = Version(1, 2, 4)
        
        self.assertEqual(v1, v2)
        self.assertNotEqual(v1, v3)
    
    def test_version_repr(self):
        """Test version string representation."""
        v = Version(1, 2, 3)
        self.assertEqual(repr(v), "v1.2.3")


class TestParseTag(unittest.TestCase):
    """Test the parse_tag function."""
    
    def test_valid_tag(self):
        """Test parsing valid tags."""
        course, version = parse_tag("zahntechniker_grundkurs_v0.0.3")
        self.assertEqual(course, "zahntechniker_grundkurs")
        self.assertEqual(version, Version(0, 0, 3))
    
    def test_valid_tag_with_numbers(self):
        """Test parsing tags with numbers in course name."""
        course, version = parse_tag("course123_test_v1.2.3")
        self.assertEqual(course, "course123_test")
        self.assertEqual(version, Version(1, 2, 3))
    
    def test_valid_tag_with_underscores(self):
        """Test parsing tags with multiple underscores."""
        course, version = parse_tag("long_course_name_here_v10.20.30")
        self.assertEqual(course, "long_course_name_here")
        self.assertEqual(version, Version(10, 20, 30))
    
    def test_invalid_tag_no_version(self):
        """Test parsing tag without version."""
        with self.assertRaises(ValueError):
            parse_tag("zahntechniker_grundkurs")
    
    def test_invalid_tag_wrong_version_format(self):
        """Test parsing tag with wrong version format."""
        with self.assertRaises(ValueError):
            parse_tag("zahntechniker_grundkurs_v0.0")
        
        with self.assertRaises(ValueError):
            parse_tag("zahntechniker_grundkurs_v0.0.0.0")
    
    def test_invalid_tag_no_underscore_before_version(self):
        """Test parsing tag without underscore before version."""
        with self.assertRaises(ValueError):
            parse_tag("zahntechniker_grundkursv0.0.3")


class TestGroupTagsByCourse(unittest.TestCase):
    """Test the group_tags_by_course function."""
    
    def test_single_course(self):
        """Test grouping tags for a single course."""
        tags = [
            "course1_v0.0.1",
            "course1_v0.0.2",
            "course1_v0.0.3"
        ]
        grouped = group_tags_by_course(tags)
        
        self.assertEqual(len(grouped), 1)
        self.assertIn("course1", grouped)
        self.assertEqual(len(grouped["course1"]), 3)
    
    def test_multiple_courses(self):
        """Test grouping tags for multiple courses."""
        tags = [
            "course1_v0.0.1",
            "course1_v0.0.2",
            "course2_v1.0.0",
            "course2_v1.0.1",
            "course3_v2.0.0"
        ]
        grouped = group_tags_by_course(tags)
        
        self.assertEqual(len(grouped), 3)
        self.assertEqual(len(grouped["course1"]), 2)
        self.assertEqual(len(grouped["course2"]), 2)
        self.assertEqual(len(grouped["course3"]), 1)
    
    def test_mixed_valid_invalid_tags(self):
        """Test grouping with some invalid tags."""
        tags = [
            "course1_v0.0.1",
            "invalid_tag",
            "course1_v0.0.2",
            "another_invalid"
        ]
        grouped = group_tags_by_course(tags)
        
        self.assertEqual(len(grouped), 1)
        self.assertEqual(len(grouped["course1"]), 2)


class TestFindTagsToDelete(unittest.TestCase):
    """Test the find_tags_to_delete function."""
    
    def test_keep_two_versions(self):
        """Test keeping two highest versions."""
        grouped = {
            "course1": [
                ("course1_v0.0.1", Version(0, 0, 1)),
                ("course1_v0.0.2", Version(0, 0, 2)),
                ("course1_v0.0.3", Version(0, 0, 3)),
                ("course1_v0.0.4", Version(0, 0, 4)),
            ]
        }
        to_delete = find_tags_to_delete(grouped, keep_count=2)
        
        self.assertEqual(len(to_delete), 2)
        self.assertIn("course1_v0.0.1", to_delete)
        self.assertIn("course1_v0.0.2", to_delete)
        self.assertNotIn("course1_v0.0.3", to_delete)
        self.assertNotIn("course1_v0.0.4", to_delete)
    
    def test_keep_all_when_not_enough(self):
        """Test that all versions are kept when there are fewer than keep_count."""
        grouped = {
            "course1": [
                ("course1_v0.0.1", Version(0, 0, 1)),
            ]
        }
        to_delete = find_tags_to_delete(grouped, keep_count=2)
        
        self.assertEqual(len(to_delete), 0)
    
    def test_keep_three_versions(self):
        """Test keeping three highest versions."""
        grouped = {
            "course1": [
                ("course1_v0.0.1", Version(0, 0, 1)),
                ("course1_v0.0.2", Version(0, 0, 2)),
                ("course1_v0.0.3", Version(0, 0, 3)),
                ("course1_v0.0.4", Version(0, 0, 4)),
                ("course1_v0.0.5", Version(0, 0, 5)),
            ]
        }
        to_delete = find_tags_to_delete(grouped, keep_count=3)
        
        self.assertEqual(len(to_delete), 2)
        self.assertIn("course1_v0.0.1", to_delete)
        self.assertIn("course1_v0.0.2", to_delete)
    
    def test_multiple_courses(self):
        """Test with multiple courses."""
        grouped = {
            "course1": [
                ("course1_v0.0.1", Version(0, 0, 1)),
                ("course1_v0.0.2", Version(0, 0, 2)),
                ("course1_v0.0.3", Version(0, 0, 3)),
            ],
            "course2": [
                ("course2_v1.0.0", Version(1, 0, 0)),
                ("course2_v1.0.1", Version(1, 0, 1)),
                ("course2_v1.0.2", Version(1, 0, 2)),
                ("course2_v1.0.3", Version(1, 0, 3)),
            ]
        }
        to_delete = find_tags_to_delete(grouped, keep_count=2)
        
        self.assertEqual(len(to_delete), 3)  # 1 from course1, 2 from course2
        self.assertIn("course1_v0.0.1", to_delete)
        self.assertIn("course2_v1.0.0", to_delete)
        self.assertIn("course2_v1.0.1", to_delete)
    
    def test_semantic_versioning_order(self):
        """Test that semantic versioning is correctly applied."""
        grouped = {
            "course1": [
                ("course1_v0.0.9", Version(0, 0, 9)),
                ("course1_v0.1.0", Version(0, 1, 0)),
                ("course1_v1.0.0", Version(1, 0, 0)),
                ("course1_v0.0.10", Version(0, 0, 10)),
            ]
        }
        to_delete = find_tags_to_delete(grouped, keep_count=2)
        
        # Should keep v1.0.0 and v0.1.0
        self.assertEqual(len(to_delete), 2)
        self.assertIn("course1_v0.0.9", to_delete)
        self.assertIn("course1_v0.0.10", to_delete)
        self.assertNotIn("course1_v1.0.0", to_delete)
        self.assertNotIn("course1_v0.1.0", to_delete)


if __name__ == '__main__':
    unittest.main()
