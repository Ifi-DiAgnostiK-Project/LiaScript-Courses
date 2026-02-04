# Checksum-based State Persistence

This document describes the checksum-based state persistence mechanism for tracking changes in course files and generating deploy artifacts.

## Overview

Previously, the GitHub Actions workflow only checked for changes in the last commit (`HEAD^ HEAD`). This approach had limitations:
- Only detected changes in the most recent commit
- Could not track changes across multiple commits
- Required `fetch-depth: 2` which didn't work well with some workflow scenarios

The new checksum-based mechanism:
- Persists the state of all course files as checksums in a JSON file
- Stores the state as a GitHub Actions artifact between workflow runs
- Detects any changes since the last workflow run, regardless of how many commits
- Falls back to git-based detection when the state file is not available

## Components

### 1. Checksum State Module (`scripts/checksum_state.py`)

A Python module that provides utilities for:
- Computing SHA256 checksums for course files
- Loading and saving state to `.checksum_state.json`
- Detecting changed files by comparing old and new checksums
- CLI interface for manual state management

#### Usage

```bash
# Detect changed files since last state
python3 scripts/checksum_state.py detect

# Update state with current checksums
python3 scripts/checksum_state.py update

# Show current state
python3 scripts/checksum_state.py show
```

### 2. Updated Version Check Script (`scripts/check_and_increment_version.py`)

The version increment script now:
1. Attempts to use checksum-based change detection first
2. Falls back to git-based detection (`HEAD^`) if:
   - No state file exists
   - Checksum module is not available
   - Checksum detection fails

This maintains backward compatibility while providing enhanced functionality.

### 3. Workflow Integration (`.github/workflows/generate-liascript-outputs.yml`)

The workflow has been updated to:
1. Download the previous checksum state from artifacts (if available)
2. Run version checks and artifact generation
3. Update the checksum state after processing
4. Upload the new state as an artifact (retained for 90 days)

## State File Format

The `.checksum_state.json` file has the following structure:

```json
{
  "version": "1.0",
  "checksums": {
    "courses/file1.md": "abc123...",
    "courses/file2.md": "def456...",
    ...
  }
}
```

**Note:** The state file is not committed to the repository. It only exists as a GitHub Actions artifact.

## Benefits

1. **Accurate Change Detection**: Detects all changes since the last workflow run, not just the last commit
2. **Efficient Processing**: Only processes files that have actually changed
3. **Persistent State**: State persists across workflow runs via artifacts
4. **Backward Compatible**: Falls back to git-based detection when needed
5. **Incremental Versioning**: Works seamlessly with the auto-increment version system

## Workflow Behavior

### First Run (No State)
- No previous state artifact exists
- Falls back to git-based detection (`HEAD^ HEAD`)
- Creates initial state file
- Uploads state as artifact

### Subsequent Runs (With State)
- Downloads previous state from artifact
- Compares current checksums with previous state
- Detects all changed files since last run
- Updates and uploads new state

### Manual Workflow Dispatch
- Behaves the same as push/PR triggers
- Uses existing state if available
- Creates new state if not

## Maintenance

### State Artifact Retention
The checksum state artifact is retained for **90 days** by default. This can be adjusted in the workflow file:

```yaml
retention-days: 90
```

### Manual State Reset
If needed, the state can be reset by:
1. Letting the artifact expire (after 90 days)
2. Manually deleting the artifact from the GitHub Actions UI
3. The next workflow run will create a new state

## Troubleshooting

### "No checksum state file found"
This is normal for the first run or after state expiration. The system falls back to git-based detection.

### State Not Detecting Changes
1. Verify the state file was uploaded in the previous run
2. Check that the artifact hasn't expired
3. Ensure the workflow has proper permissions to upload/download artifacts

### Too Many Changes Detected
If the state is missing or expired, the system may detect all files as changed. This is expected behavior and the system will create a new baseline state.
