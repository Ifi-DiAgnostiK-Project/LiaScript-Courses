#!/usr/bin/env python3
"""
Cleanup script for old course releases and tags.

This script keeps only the last 2 highest version numbers for each course,
removing all other tags and their accompanying releases.

Tag format: course_name_vMajor.Minor.Patch
Example: zahntechniker_grundkurs_v0.0.3
"""

import argparse
import re
import subprocess
import sys
from collections import defaultdict
from typing import Dict, List, Tuple


class Version:
    """Represents a semantic version for comparison."""
    
    def __init__(self, major: int, minor: int, patch: int):
        self.major = major
        self.minor = minor
        self.patch = patch
    
    def __lt__(self, other):
        return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)
    
    def __le__(self, other):
        return (self.major, self.minor, self.patch) <= (other.major, other.minor, other.patch)
    
    def __eq__(self, other):
        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)
    
    def __ne__(self, other):
        return (self.major, self.minor, self.patch) != (other.major, other.minor, other.patch)
    
    def __gt__(self, other):
        return (self.major, self.minor, self.patch) > (other.major, other.minor, other.patch)
    
    def __ge__(self, other):
        return (self.major, self.minor, self.patch) >= (other.major, other.minor, other.patch)
    
    def __repr__(self):
        return f"v{self.major}.{self.minor}.{self.patch}"


def parse_tag(tag: str) -> Tuple[str, Version]:
    """
    Parse a tag into course name and version.
    
    Args:
        tag: Tag string in format 'course_name_vMajor.Minor.Patch'
    
    Returns:
        Tuple of (course_name, Version object)
    
    Raises:
        ValueError: If tag doesn't match expected format
    """
    # Match pattern: anything followed by _v and version number
    match = re.match(r'^(.+)_v(\d+)\.(\d+)\.(\d+)$', tag)
    if not match:
        raise ValueError(f"Tag '{tag}' doesn't match expected format 'course_name_vMajor.Minor.Patch'")
    
    course_name = match.group(1)
    major = int(match.group(2))
    minor = int(match.group(3))
    patch = int(match.group(4))
    
    return course_name, Version(major, minor, patch)


def get_all_tags() -> List[str]:
    """Get all tags from the repository."""
    try:
        result = subprocess.run(
            ['git', 'tag', '-l'],
            capture_output=True,
            text=True,
            check=True
        )
        return [tag.strip() for tag in result.stdout.strip().split('\n') if tag.strip()]
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to get tags from git. Make sure git is installed and you're in a git repository.")
        print(f"Git error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: git command not found. Please install git.")
        sys.exit(1)



def get_all_releases() -> List[str]:
    """Get all release tags using GitHub CLI."""
    try:
        result = subprocess.run(
            ['gh', 'release', 'list', '--limit', '1000'],
            capture_output=True,
            text=True,
            check=True
        )
        # Parse output: each line is "TAG    TITLE    ..."
        releases = []
        for line in result.stdout.strip().split('\n'):
            if line.strip():
                parts = line.split('\t')
                if parts:
                    releases.append(parts[0].strip())
        return releases
    except subprocess.CalledProcessError:
        print("Warning: Could not fetch releases with 'gh' CLI. Make sure GitHub CLI is installed.")
        return []


def group_tags_by_course(tags: List[str]) -> Dict[str, List[Tuple[str, Version]]]:
    """
    Group tags by course name.
    
    Args:
        tags: List of tag strings
    
    Returns:
        Dictionary mapping course names to lists of (tag, version) tuples
    """
    grouped = defaultdict(list)
    skipped = []
    
    for tag in tags:
        try:
            course_name, version = parse_tag(tag)
            grouped[course_name].append((tag, version))
        except ValueError as e:
            skipped.append((tag, str(e)))
    
    if skipped:
        print(f"\nSkipped {len(skipped)} tag(s) that don't match the expected format:")
        for tag, reason in skipped:
            print(f"  - {tag}: {reason}")
    
    return grouped


def find_tags_to_delete(grouped_tags: Dict[str, List[Tuple[str, Version]]], keep_count: int = 2) -> List[str]:
    """
    Find tags to delete, keeping only the specified number of highest versions per course.
    
    Args:
        grouped_tags: Dictionary mapping course names to lists of (tag, version) tuples
        keep_count: Number of highest versions to keep per course (default: 2)
    
    Returns:
        List of tag names to delete
    """
    tags_to_delete = []
    
    for course_name, tag_version_list in grouped_tags.items():
        if len(tag_version_list) <= keep_count:
            print(f"\nCourse '{course_name}': {len(tag_version_list)} version(s) - keeping all")
            continue
        
        # Sort by version (highest first)
        sorted_tags = sorted(tag_version_list, key=lambda x: x[1], reverse=True)
        
        # Keep the top N versions
        keep = sorted_tags[:keep_count]
        delete = sorted_tags[keep_count:]
        
        print(f"\nCourse '{course_name}': {len(tag_version_list)} version(s)")
        print(f"  Keeping {keep_count}:")
        for tag, version in keep:
            print(f"    - {tag} ({version})")
        
        print(f"  Deleting {len(delete)}:")
        for tag, version in delete:
            print(f"    - {tag} ({version})")
            tags_to_delete.append(tag)
    
    return tags_to_delete


def delete_tag(tag: str, dry_run: bool = True):
    """
    Delete a tag locally and from remote.
    
    Args:
        tag: Tag name to delete
        dry_run: If True, only print what would be done
    """
    if dry_run:
        print(f"  [DRY RUN] Would delete tag: {tag}")
    else:
        try:
            # Delete local tag
            result = subprocess.run(
                ['git', 'tag', '-d', tag],
                check=True,
                capture_output=True,
                text=True
            )
        except subprocess.CalledProcessError as e:
            print(f"  Warning: Failed to delete local tag '{tag}'")
            if e.stderr:
                print(f"    Error: {e.stderr.strip()}")
            return
        
        try:
            # Delete remote tag
            result = subprocess.run(
                ['git', 'push', 'origin', f':refs/tags/{tag}'],
                check=True,
                capture_output=True,
                text=True
            )
            print(f"  Deleted tag: {tag}")
        except subprocess.CalledProcessError as e:
            print(f"  Warning: Failed to delete remote tag '{tag}'")
            if e.stderr:
                print(f"    Error: {e.stderr.strip()}")
            # Tag was deleted locally, so note that
            print(f"    (Note: Local tag was deleted successfully)")



def delete_release(tag: str, dry_run: bool = True):
    """
    Delete a GitHub release.
    
    Args:
        tag: Release tag name to delete
        dry_run: If True, only print what would be done
    """
    if dry_run:
        print(f"  [DRY RUN] Would delete release: {tag}")
    else:
        try:
            subprocess.run(
                ['gh', 'release', 'delete', tag, '--yes'],
                check=True,
                capture_output=True
            )
            print(f"  Deleted release: {tag}")
        except subprocess.CalledProcessError as e:
            print(f"  Warning: Could not delete release '{tag}': {e}")


def positive_int(value):
    """Validate that the argument is a positive integer."""
    try:
        ivalue = int(value)
        if ivalue < 1:
            raise argparse.ArgumentTypeError(f"{value} is not a positive integer (must be >= 1)")
        return ivalue
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid integer")


def main():
    parser = argparse.ArgumentParser(
        description='Cleanup old course releases and tags, keeping only the last N versions per course.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry run (default) - see what would be deleted
  python cleanup_old_releases.py
  
  # Keep only last 2 versions (default)
  python cleanup_old_releases.py --execute
  
  # Keep only last 3 versions
  python cleanup_old_releases.py --execute --keep 3
  
  # Delete only tags, not releases
  python cleanup_old_releases.py --execute --tags-only
        """
    )
    parser.add_argument(
        '--execute',
        action='store_true',
        help='Actually delete tags and releases (default is dry-run)'
    )
    parser.add_argument(
        '--keep',
        type=positive_int,
        default=2,
        help='Number of highest versions to keep per course (default: 2)'
    )
    parser.add_argument(
        '--tags-only',
        action='store_true',
        help='Only delete tags, not releases'
    )
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("Course Tag/Release Cleanup Script")
    print("=" * 70)
    
    if not args.execute:
        print("\n⚠️  DRY RUN MODE - No changes will be made")
        print("   Add --execute flag to actually delete tags and releases")
    else:
        print("\n⚠️  EXECUTE MODE - Tags and releases WILL be deleted!")
    
    print(f"\nConfiguration:")
    print(f"  - Keeping {args.keep} highest version(s) per course")
    print(f"  - Tags only mode: {args.tags_only}")
    
    # Get all tags
    print("\n" + "=" * 70)
    print("Fetching tags...")
    print("=" * 70)
    tags = get_all_tags()
    
    if not tags:
        print("No tags found in repository.")
        return
    
    print(f"Found {len(tags)} tag(s)")
    
    # Group tags by course
    print("\n" + "=" * 70)
    print("Analyzing tags...")
    print("=" * 70)
    grouped_tags = group_tags_by_course(tags)
    
    print(f"\nFound {len(grouped_tags)} course(s)")
    
    # Find tags to delete
    print("\n" + "=" * 70)
    print("Determining which tags to delete...")
    print("=" * 70)
    tags_to_delete = find_tags_to_delete(grouped_tags, keep_count=args.keep)
    
    if not tags_to_delete:
        print(f"\n✅ No tags need to be deleted. All courses have at most {args.keep} version(s).")
        return
    
    # Get releases if needed
    releases = []
    if not args.tags_only:
        print("\n" + "=" * 70)
        print("Fetching releases...")
        print("=" * 70)
        releases = get_all_releases()
        print(f"Found {len(releases)} release(s)")
    
    # Delete tags and releases
    print("\n" + "=" * 70)
    print("Deleting tags and releases...")
    print("=" * 70)
    
    for tag in tags_to_delete:
        # Delete release first if it exists
        if not args.tags_only and tag in releases:
            delete_release(tag, dry_run=not args.execute)
        
        # Then delete tag
        delete_tag(tag, dry_run=not args.execute)
    
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total tags to delete: {len(tags_to_delete)}")
    
    if not args.execute:
        print("\n⚠️  This was a DRY RUN - no changes were made")
        print("   Run with --execute to actually delete tags and releases")
    else:
        print("\n✅ Cleanup completed!")


if __name__ == '__main__':
    main()
