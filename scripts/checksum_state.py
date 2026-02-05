#!/usr/bin/env python3
"""
Checksum-based state management for tracking file changes.

This module provides utilities to compute and persist checksums of course files,
enabling change detection across multiple commits and workflow runs.
"""

import hashlib
import json
import sys
from pathlib import Path
from typing import Dict, Set, Optional


DEFAULT_STATE_FILE = ".checksum_state.json"


def compute_file_checksum(filepath: Path) -> Optional[str]:
    """
    Compute SHA256 checksum of a file.
    
    Args:
        filepath: Path to the file
    
    Returns:
        Hex digest of the file checksum, or None if file doesn't exist or on error
    """
    try:
        if not filepath.exists():
            return None
        
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            # Read in chunks to handle large files
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error computing checksum for {filepath}: {e}", file=sys.stderr)
        return None


def compute_checksums_for_courses(courses_dir: Path = Path("courses")) -> Dict[str, str]:
    """
    Compute checksums for all markdown files in the courses directory.
    
    Args:
        courses_dir: Path to the courses directory
    
    Returns:
        Dictionary mapping relative file paths to their checksums
    """
    checksums = {}
    
    if not courses_dir.exists():
        print(f"Warning: Courses directory {courses_dir} does not exist", file=sys.stderr)
        return checksums
    
    for md_file in courses_dir.rglob("*.md"):
        # Get relative path from current working directory
        try:
            relative_path = str(md_file.relative_to(Path.cwd()))
        except ValueError:
            # If file is not relative to cwd, use absolute path
            relative_path = str(md_file)
        
        checksum = compute_file_checksum(md_file)
        
        if checksum is not None:
            checksums[relative_path] = checksum
    
    return checksums


def load_state(state_file: Path = Path(DEFAULT_STATE_FILE)) -> Dict[str, str]:
    """
    Load the previous checksum state from file.
    
    Args:
        state_file: Path to the state file
    
    Returns:
        Dictionary mapping file paths to checksums, empty dict if file doesn't exist
    """
    if not state_file.exists():
        return {}
    
    try:
        with open(state_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("checksums", {})
    except Exception as e:
        print(f"Warning: Could not load state file {state_file}: {e}", file=sys.stderr)
        return {}


def save_state(checksums: Dict[str, str], state_file: Path = Path(DEFAULT_STATE_FILE)) -> bool:
    """
    Save checksum state to file.
    
    Args:
        checksums: Dictionary mapping file paths to checksums
        state_file: Path to the state file
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Sort checksums alphabetically for consistent diffs across runs
        sorted_checksums = dict(sorted(checksums.items()))
        state_data = {
            "version": "1.0",
            "checksums": sorted_checksums
        }
        
        # Don't use sort_keys=True to preserve top-level key order (version, then checksums)
        # Checksums are already sorted above for consistent diffs
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(state_data, f, indent=2)
        
        return True
    except Exception as e:
        print(f"Error saving state file {state_file}: {e}", file=sys.stderr)
        return False


def detect_changed_files(
    old_checksums: Dict[str, str],
    new_checksums: Dict[str, str]
) -> Set[str]:
    """
    Detect which files have changed by comparing checksums.
    
    Args:
        old_checksums: Previous checksums dictionary
        new_checksums: Current checksums dictionary
    
    Returns:
        Set of file paths that have changed, been added, or been deleted
    """
    changed_files = set()
    
    # Check for new or modified files
    for filepath, new_checksum in new_checksums.items():
        old_checksum = old_checksums.get(filepath)
        if old_checksum is None or old_checksum != new_checksum:
            changed_files.add(filepath)
    
    # Check for deleted files
    for filepath in old_checksums:
        if filepath not in new_checksums:
            # File was deleted, but we don't add it to changed_files
            # since we can't process a deleted file
            pass
    
    return changed_files


def get_changed_course_files(
    state_file: Path = Path(DEFAULT_STATE_FILE),
    courses_dir: Path = Path("courses")
) -> Set[str]:
    """
    Get list of changed course files since last state.
    
    This is the main entry point for detecting changes using checksums.
    
    Args:
        state_file: Path to the state file
        courses_dir: Path to the courses directory
    
    Returns:
        Set of changed file paths
    """
    old_checksums = load_state(state_file)
    new_checksums = compute_checksums_for_courses(courses_dir)
    changed_files = detect_changed_files(old_checksums, new_checksums)
    
    return changed_files


def update_state(
    state_file: Path = Path(DEFAULT_STATE_FILE),
    courses_dir: Path = Path("courses")
) -> bool:
    """
    Update the state file with current checksums.
    
    Args:
        state_file: Path to the state file
        courses_dir: Path to the courses directory
    
    Returns:
        True if successful, False otherwise
    """
    new_checksums = compute_checksums_for_courses(courses_dir)
    return save_state(new_checksums, state_file)


def main():
    """Main function for testing and CLI usage."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Manage checksum state for course files"
    )
    parser.add_argument(
        "action",
        choices=["detect", "update", "show"],
        help="Action to perform: detect changes, update state, or show current state"
    )
    parser.add_argument(
        "--state-file",
        default=DEFAULT_STATE_FILE,
        help="Path to state file"
    )
    parser.add_argument(
        "--courses-dir",
        default="courses",
        help="Path to courses directory"
    )
    
    args = parser.parse_args()
    
    state_file = Path(args.state_file)
    courses_dir = Path(args.courses_dir)
    
    if args.action == "detect":
        changed = get_changed_course_files(state_file, courses_dir)
        if changed:
            print(f"Changed files ({len(changed)}):")
            for f in sorted(changed):
                print(f"  {f}")
        else:
            print("No changes detected.")
        return 0
    
    elif args.action == "update":
        if update_state(state_file, courses_dir):
            print(f"✓ State updated in {state_file}")
            return 0
        else:
            print("✗ Failed to update state", file=sys.stderr)
            return 1
    
    elif args.action == "show":
        checksums = load_state(state_file)
        if checksums:
            print(f"Current state ({len(checksums)} files):")
            for filepath in sorted(checksums):
                print(f"  {filepath}: {checksums[filepath][:12]}...")
        else:
            print("No state file found or state is empty.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
