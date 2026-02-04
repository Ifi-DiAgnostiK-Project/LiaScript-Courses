# Tag Cleanup Script

## Overview

This script helps manage course releases by keeping only the most recent versions and removing old tags and releases to keep the repository clean.

## Purpose

Each time a course is changed, a new SCORM course is built with a corresponding version tag in the format `course_name_vMajor.Minor.Patch` (e.g., `zahntechniker_grundkurs_v0.0.3`). Over time, this can result in many tags and releases. This script automatically cleans up old versions, keeping only the latest specified number of versions per course.

## Requirements

- Python 3.7 or higher
- Git
- GitHub CLI (`gh`) - for deleting releases (optional if using `--tags-only`)

### Installing GitHub CLI

If you need to delete releases (not just tags), install the GitHub CLI:

**Ubuntu/Debian:**
```bash
sudo apt install gh
```

**macOS:**
```bash
brew install gh
```

**Windows:**
```bash
winget install GitHub.cli
```

After installation, authenticate with:
```bash
gh auth login
```

## Usage

### Dry Run (Recommended First Step)

Always start with a dry run to see what would be deleted:

```bash
python3 cleanup_old_releases.py
```

This will show you:
- Which courses have tags
- How many versions each course has
- Which versions would be kept
- Which versions would be deleted

### Execute Cleanup

After reviewing the dry run output, execute the actual cleanup:

```bash
python3 cleanup_old_releases.py --execute
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `--execute` | Actually delete tags and releases (without this, it's a dry run) | Dry run |
| `--keep N` | Number of highest versions to keep per course | 2 |
| `--tags-only` | Only delete tags, not releases (useful if you don't have `gh` CLI) | False |

### Examples

**Keep only the last 2 versions (default):**
```bash
python3 cleanup_old_releases.py --execute
```

**Keep only the last 3 versions:**
```bash
python3 cleanup_old_releases.py --execute --keep 3
```

**Delete only tags, not releases:**
```bash
python3 cleanup_old_releases.py --execute --tags-only
```

**Dry run with keeping 5 versions:**
```bash
python3 cleanup_old_releases.py --keep 5
```

## How It Works

1. **Fetch Tags**: The script retrieves all tags from the repository
2. **Parse Tags**: Tags are parsed to extract the course name and version number
3. **Group by Course**: Tags are grouped by their course name
4. **Sort Versions**: Within each course, versions are sorted using semantic versioning
5. **Select for Deletion**: All but the N highest versions are marked for deletion
6. **Delete**: 
   - First, the corresponding GitHub release is deleted (if exists and not using `--tags-only`)
   - Then, the tag is deleted both locally and from the remote repository

## Tag Format

The script expects tags in the format:
```
course_name_vMajor.Minor.Patch
```

Examples:
- `zahntechniker_grundkurs_v0.0.3`
- `tischler_kreissaege_v1.2.0`
- `shk_heizung_v2.0.1`

Tags that don't match this format will be skipped and reported.

## Safety Features

- **Dry Run by Default**: The script won't delete anything unless you explicitly use `--execute`
- **Clear Output**: Shows exactly what will be kept and what will be deleted
- **Skipped Tags Report**: Reports any tags that don't match the expected format
- **Per-Course Analysis**: Processes each course independently

## Output Example

```
======================================================================
Course Tag/Release Cleanup Script
======================================================================

⚠️  DRY RUN MODE - No changes will be made
   Add --execute flag to actually delete tags and releases

Configuration:
  - Keeping 2 highest version(s) per course
  - Tags only mode: False

======================================================================
Fetching tags...
======================================================================
Found 15 tag(s)

======================================================================
Analyzing tags...
======================================================================
Found 3 course(s)

======================================================================
Determining which tags to delete...
======================================================================

Course 'zahntechniker_grundkurs': 6 version(s)
  Keeping 2:
    - zahntechniker_grundkurs_v0.0.6 (v0.0.6)
    - zahntechniker_grundkurs_v0.0.5 (v0.0.5)
  Deleting 4:
    - zahntechniker_grundkurs_v0.0.4 (v0.0.4)
    - zahntechniker_grundkurs_v0.0.3 (v0.0.3)
    - zahntechniker_grundkurs_v0.0.2 (v0.0.2)
    - zahntechniker_grundkurs_v0.0.1 (v0.0.1)

Course 'tischler_kreissaege': 2 version(s) - keeping all

Course 'shk_heizung': 7 version(s)
  Keeping 2:
    - shk_heizung_v1.0.0 (v1.0.0)
    - shk_heizung_v0.9.9 (v0.9.9)
  Deleting 5:
    - shk_heizung_v0.9.8 (v0.9.8)
    ...

======================================================================
Summary
======================================================================
Total tags to delete: 9

⚠️  This was a DRY RUN - no changes were made
   Run with --execute to actually delete tags and releases
```

## Troubleshooting

### "Warning: Could not fetch releases with 'gh' CLI"

This means the GitHub CLI is not installed or not authenticated. You have two options:
1. Install and authenticate `gh` CLI (see Requirements section)
2. Use the `--tags-only` flag to only delete tags: `python3 cleanup_old_releases.py --execute --tags-only`

### "Warning: Could not delete release"

This can happen if:
- The release doesn't exist (tag exists but no release was created)
- You don't have permission to delete releases
- GitHub API is temporarily unavailable

The script will continue to delete the tag even if the release deletion fails.

### Tags Don't Match Expected Format

If you see tags being skipped, ensure they follow the format `course_name_vMajor.Minor.Patch`. The version number must have exactly three parts (major, minor, patch) separated by dots.

## Integration with CI/CD

You can run this script periodically in a GitHub Action:

```yaml
name: Cleanup Old Releases
on:
  schedule:
    - cron: '0 0 * * 0'  # Run weekly on Sunday at midnight
  workflow_dispatch:  # Allow manual trigger

jobs:
  cleanup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Fetch all tags
      
      - name: Setup GitHub CLI
        run: |
          gh auth setup-git
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Run cleanup script
        run: |
          python3 cleanup_old_releases.py --execute --keep 2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## Notes

- The script processes each course independently, so different courses can have different numbers of versions
- Semantic versioning is used for comparison (v1.0.0 > v0.9.9)
- Deleted tags and releases cannot be easily recovered - always do a dry run first!
- The script only deletes tags/releases; it does not delete any course files or commits
