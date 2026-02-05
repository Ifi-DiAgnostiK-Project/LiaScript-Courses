# Checksum State Management

## Overview

The checksum state management system tracks changes to course files across workflow runs by storing file checksums in the repository. This approach replaces GitHub Actions artifacts, which have expiration limitations.

## Purpose

The `.checksum_state.json` file in the repository root stores SHA256 checksums of all course markdown files. This enables:

1. **Persistent change tracking**: State survives across workflow runs and doesn't expire
2. **Reliable change detection**: Accurately identifies which files changed between commits
3. **Workflow efficiency**: Only processes files that actually changed
4. **Debugging visibility**: State is visible in git history

## How It Works

### The State File

The `.checksum_state.json` file contains:
- **version**: Schema version for future compatibility
- **checksums**: Object mapping relative file paths to their SHA256 checksums

Example:
```json
{
  "version": "1.0",
  "checksums": {
    "courses/example.md": "a1b2c3d4e5f6...",
    "courses/another.md": "9f8e7d6c5b4a..."
  }
}
```

### In the GitHub Actions Workflow

The workflow (`generate-liascript-outputs.yml`) uses checksum state in the `check_changes` job:

1. **Checkout repository**: Gets latest code including `.checksum_state.json`
2. **Detect changes**: Compares current file checksums with stored checksums
3. **Process changed files**: Only generates outputs for files that changed
4. **Update state**: Commits updated `.checksum_state.json` back to repository with `[skip ci]`

### Benefits Over Artifacts

| Artifacts | Repository State |
|-----------|-----------------|
| Expire after 90 days | Never expires |
| Not available across workflow runs | Always available |
| Invisible to debugging | Visible in git history |
| Requires upload/download steps | Simple git operations |
| Can fail to download | Always present after first run |

## Using the Script

The `checksum_state.py` script provides a CLI for managing state:

### Detect Changes
```bash
python3 scripts/checksum_state.py detect
```
Compares current file checksums with stored state and lists changed files.

### Update State
```bash
python3 scripts/checksum_state.py update
```
Computes current checksums and saves them to `.checksum_state.json`.

### Show Current State
```bash
python3 scripts/checksum_state.py show
```
Displays the contents of the current state file.

### Options
```bash
python3 scripts/checksum_state.py --help
```
- `--state-file`: Path to state file (default: `.checksum_state.json`)
- `--courses-dir`: Path to courses directory (default: `courses`)

## Workflow Integration

The checksum state is integrated into the two-phase workflow:

### Phase 1: Version Increment (if needed)
1. Checkout repository with existing `.checksum_state.json`
2. Check if version needs incrementing
3. If yes, commit version changes and stop (triggers Phase 2)

### Phase 2: Generate Outputs and Update State
1. Checkout repository with existing `.checksum_state.json`
2. Detect changed markdown files using git diff
3. Process changed files (generate PDFs, SCORM packages, create releases)
4. Update `.checksum_state.json` with new checksums
5. Commit state file back to repository with `[skip ci]` tag

The `[skip ci]` tag ensures the state update doesn't trigger another workflow run.

## Troubleshooting

### State File Missing
If `.checksum_state.json` is missing:
- First workflow run will create it
- All files will be considered "new" and processed
- Normal behavior for initial setup

### State Out of Sync
If state seems incorrect:
```bash
# Manually regenerate state
python3 scripts/checksum_state.py update
git add .checksum_state.json
git commit -m "Regenerate checksum state"
git push
```

### Merge Conflicts
If multiple branches modify different courses:
- Git may show merge conflicts in `.checksum_state.json`
- Safe to accept either version or both
- Run `python3 scripts/checksum_state.py update` after merge to sync

## Security Notes

- Checksums use SHA256 for file integrity verification (detecting changes)
- SHA256 is a cryptographic hash function, but used here for content comparison, not security
- Checksums cannot be reversed to recover file contents
- State file only contains file paths (relative) and checksums
- No sensitive data stored in state file
- Original course files remain in the repository and are publicly accessible
