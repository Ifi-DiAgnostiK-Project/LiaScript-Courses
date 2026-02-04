#!/usr/bin/env python3
"""
Script to check and auto-increment version tags in LiaScript course files.

This script:
1. Detects changed markdown files in the courses directory
2. For each changed file, checks if the version tag also changed
3. If the version hasn't changed, increments the patch version
"""

import re
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple, Optional


# Version pattern for LiaScript course files
VERSION_PATTERN = r'version:\s*(\d+)\.(\d+)\.(\d+)\s*$'


def get_changed_course_files(base_ref: str = "HEAD^", head_ref: str = "HEAD") -> List[str]:
    """
    Get list of changed markdown files in the courses directory.
    
    Args:
        base_ref: Base git reference (default: HEAD^)
        head_ref: Head git reference (default: HEAD)
    
    Returns:
        List of changed course file paths
    """
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", base_ref, head_ref],
            capture_output=True,
            text=True,
            check=True
        )
        
        files = result.stdout.strip().split("\n")
        # Filter for markdown files in courses directory
        course_files = [f for f in files if f.startswith("courses/") and f.endswith(".md")]
        return course_files
    except subprocess.CalledProcessError as e:
        print(f"Error getting changed files: {e}", file=sys.stderr)
        return []


def extract_version_from_content(content: str) -> Optional[Tuple[str, int, int, int]]:
    """
    Extract version tag from file content.
    
    Args:
        content: File content to search
    
    Returns:
        Tuple of (full_match, major, minor, patch) or None if not found
    """
    for line in content.split('\n'):
        match = re.match(VERSION_PATTERN, line)
        if match:
            major = int(match.group(1))
            minor = int(match.group(2))
            patch = int(match.group(3))
            return (match.group(0), major, minor, patch)
    
    return None


def has_version_changed(filepath: str, base_ref: str = "HEAD^", head_ref: str = "HEAD") -> bool:
    """
    Check if the version tag has changed in the specified file.
    
    Args:
        filepath: Path to the file to check
        base_ref: Base git reference
        head_ref: Head git reference
    
    Returns:
        True if version changed, False otherwise
    """
    try:
        # Get old version from base ref
        old_content = subprocess.run(
            ["git", "show", f"{base_ref}:{filepath}"],
            capture_output=True,
            text=True,
            check=True
        ).stdout
        
        # Get new version from head ref
        new_content = subprocess.run(
            ["git", "show", f"{head_ref}:{filepath}"],
            capture_output=True,
            text=True,
            check=True
        ).stdout
        
        old_version = extract_version_from_content(old_content)
        new_version = extract_version_from_content(new_content)
        
        # If either version is missing, consider it changed
        if old_version is None or new_version is None:
            return True
        
        # Compare version tuples (excluding the full match string)
        return old_version[1:] != new_version[1:]
        
    except subprocess.CalledProcessError:
        # File might be new, consider version as changed
        return True


def increment_patch_version(filepath: str) -> bool:
    """
    Increment the patch version in the specified file.
    
    Args:
        filepath: Path to the file to modify
    
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        version_info = extract_version_from_content(content)
        if version_info is None:
            print(f"Warning: No version tag found in {filepath}", file=sys.stderr)
            return False
        
        full_match, major, minor, patch = version_info
        new_patch = patch + 1
        
        # Create the replacement using the same pattern as VERSION_PATTERN
        # Capture groups: (1) version: and spaces, (2) version number, (3) trailing spaces
        def replacer(match):
            return f"{match.group(1)}{major}.{minor}.{new_patch}{match.group(3)}"
        
        # Use a pattern consistent with VERSION_PATTERN for replacement
        replace_pattern = r'(version:\s*)(\d+\.\d+\.\d+)(\s*)$'
        new_content = re.sub(replace_pattern, replacer, content, count=1, flags=re.MULTILINE)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Incremented version in {filepath}: {major}.{minor}.{patch} → {major}.{minor}.{new_patch}")
            return True
        else:
            print(f"Warning: Could not replace version in {filepath}", file=sys.stderr)
            return False
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}", file=sys.stderr)
        return False


def main():
    """Main function to process all changed course files."""
    # Get changed files
    changed_files = get_changed_course_files()
    
    if not changed_files:
        print("No changed course files detected.")
        return 0
    
    print(f"Found {len(changed_files)} changed course file(s):")
    for f in changed_files:
        print(f"  - {f}")
    print()
    
    files_modified = []
    
    # Process each changed file
    for filepath in changed_files:
        print(f"Checking {filepath}...")
        
        # Check if file exists (it might have been deleted)
        if not Path(filepath).exists():
            print(f"  → File deleted, skipping")
            continue
        
        # Check if version changed
        if has_version_changed(filepath):
            print(f"  → Version already changed, skipping")
        else:
            print(f"  → Version unchanged, incrementing patch version...")
            if increment_patch_version(filepath):
                files_modified.append(filepath)
    
    print()
    if files_modified:
        print(f"Modified {len(files_modified)} file(s) with auto-incremented versions:")
        for f in files_modified:
            print(f"  - {f}")
        print("\nPlease review and commit these changes.")
        return 0
    else:
        print("No files needed version updates.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
