# Version Check and Auto-Increment Script

## Overview

The `check_and_increment_version.py` script automatically manages version tags in LiaScript course files. It ensures that every change to a course file has a corresponding version update, preventing crashes in the SCORM package generation workflow.

## Purpose

When a course file in the `courses/` directory is modified without updating its version tag, the SCORM package generation can fail. This script:

1. Detects which course markdown files have changed in the current commit
2. Checks if the version tag in the file's preamble was also updated
3. If the version wasn't changed, automatically increments the patch version
4. Commits the version changes back to the repository

## Version Format

The script expects version tags in the following format within the file's front matter:

```markdown
<!--
version: Major.Minor.Patch
-->
```

Examples:
- `version: 1.0.0`
- `version:  0.0.5`
- `version:1.2.3`

The whitespace around the version number is flexible, but the version must be on a single line.

## Usage

### Manual Usage

You can run the script manually from the repository root:

```bash
python3 scripts/check_and_increment_version.py
```

The script will:
- Compare HEAD with HEAD^ (the previous commit)
- Check all changed markdown files in `courses/`
- Auto-increment patch versions where needed
- Report which files were modified

### Automatic Usage in GitHub Actions

The script is integrated into the `.github/workflows/generate-liascript-outputs.yml` workflow. It runs in a **two-phase approach** to ensure version increments and tag creation are properly synchronized:

#### Phase 1: Version Increment (First Workflow Run)

When a user pushes changes to a course file:

1. The workflow detects this is NOT a version-increment commit
2. Runs the version check script
3. If version needs incrementing, commits the change WITHOUT `[skip ci]`
4. Pushes the version-increment commit
5. **Stops processing** (doesn't create releases yet)
6. The push triggers a second workflow run

#### Phase 2: Tag Creation (Second Workflow Run)

When the version-increment commit is pushed:

1. The workflow detects this IS a version-increment commit (by checking commit message)
2. **Skips the version increment step**
3. Continues to create tags and releases with the updated version
4. Updates the documentation index

This two-phase approach ensures:
- Version increments and tag creation are always synchronized
- If the workflow crashes after version increment, it can be re-run
- No infinite loops (version-increment commits don't trigger another version increment)
- Better error recovery and debugging capabilities

#### Why Not Use `[skip ci]`?

Previous versions used `[skip ci]` to prevent infinite loops. However, this caused a critical issue:
- If the workflow crashed after version increment but before tag creation
- The `[skip ci]` prevented automatic retry
- Version in the repository was out of sync with tags
- Manual intervention was required to fix the state

The new approach solves this by using **commit message detection** instead of `[skip ci]` to prevent infinite loops.

The workflow will:
- Run when changes are pushed to course files
- Create a version-increment commit (if needed) WITHOUT `[skip ci]`
- Trigger a second workflow run that creates the tags
- The second run detects it's a version-increment commit and skips version checking

## How It Works

### 1. Detect Changed Files

```python
git diff --name-only HEAD^ HEAD
```

Filters for files matching `courses/*.md`

### 2. Check Version Changes

For each changed file, the script:
- Extracts the version from HEAD^ (old version)
- Extracts the version from HEAD (new version)
- Compares the version numbers

### 3. Increment Patch Version

If versions match (file changed but version didn't):
- Parse the version: `Major.Minor.Patch`
- Increment patch: `Major.Minor.(Patch+1)`
- Update the file preserving whitespace
- Report the change

### 4. Commit Changes

The workflow commits the version updates in Phase 1:
```bash
git commit -m "Auto-increment version tags for changed courses"
```

Note: No `[skip ci]` is used. The workflow prevents infinite loops by checking the commit message instead.

## Examples

### Example 1: File Changed Without Version Update

**Before:**
```markdown
<!--
version: 0.0.5
-->
# My Course
Some content was modified...
```

**After running script:**
```markdown
<!--
version: 0.0.6
-->
# My Course
Some content was modified...
```

### Example 2: File Changed With Manual Version Update

**Before (in previous commit):**
```markdown
version: 0.0.5
```

**After (in current commit):**
```markdown
version: 1.0.0
```

**Result:** Script detects the version was manually updated and skips auto-increment.

## Error Handling

The script handles several edge cases:

- **Missing version tag**: Warns but doesn't fail
- **New files**: Skips version check (considers version as "changed")
- **Deleted files**: Skips processing
- **Invalid version format**: Warns and skips the file

### Workflow Crash Recovery

The new two-phase approach provides better error recovery:

1. **If workflow crashes during version increment**:
   - Version changes are not committed
   - Next commit or manual workflow run will retry
   - No state inconsistency

2. **If workflow crashes after version increment but before tag creation**:
   - Version increment commit is already pushed
   - Can manually trigger workflow again (or push another commit)
   - The second run will detect it's a version-increment commit
   - Skips version increment and proceeds to create tags
   - **No manual fixing required** - the workflow is self-healing

3. **If workflow crashes during tag creation**:
   - Version increment is complete
   - Tags partially created or not created
   - Manual workflow trigger or another commit will retry tag creation
   - GitHub handles duplicate release creation gracefully

This design ensures that the repository state can always be recovered automatically, eliminating the need for manual intervention to fix version/tag mismatches.

## Integration Details

The script is called in the `check_changes` job of the workflow. The job includes logic to detect whether this is a version-increment commit:

```yaml
- name: Check if this is a version-increment commit
  id: check_commit
  run: |
    cd project
    COMMIT_MSG=$(git log -1 --pretty=%B)
    if echo "$COMMIT_MSG" | grep -q "Auto-increment version tags"; then
      echo "is_version_commit=true" >> $GITHUB_OUTPUT
    else
      echo "is_version_commit=false" >> $GITHUB_OUTPUT
    fi

- name: Check and auto-increment version tags
  id: version_check
  if: steps.check_commit.outputs.is_version_commit != 'true'
  run: |
    cd project
    git config user.name "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"
    python3 scripts/check_and_increment_version.py
    if ! git diff --quiet; then
      git add -u courses/
      git commit -m "Auto-increment version tags for changed courses"
      git push
      echo "version_incremented=true" >> $GITHUB_OUTPUT
    fi
```

The subsequent steps only run if version wasn't just incremented OR if this is already a version-increment commit:

```yaml
- name: Detect Changed Markdown Files
  id: changes
  if: |
    (steps.version_check.outputs.version_incremented != 'true' || steps.check_commit.outputs.is_version_commit == 'true')
  run: |
    # ... detect changed files
```

This ensures version tags are correct before the export process begins, and that releases are created in a separate workflow run with the updated versions.

## Benefits

1. **Prevents Build Failures**: Ensures every change has a version, avoiding crashes
2. **Automatic Versioning**: No need to manually remember to update versions
3. **Semantic Versioning Support**: Maintains proper Major.Minor.Patch format
4. **Flexible**: Manual version updates (e.g., major/minor bumps) are respected
5. **Transparent**: All version changes are logged and committed
6. **Synchronized State**: Version increments and tag creation are always in sync
7. **Self-Healing**: Workflow can recover from crashes without manual intervention
8. **No Infinite Loops**: Uses commit message detection instead of `[skip ci]` to prevent loops
9. **Better Error Recovery**: Can retry tag creation if workflow fails after version increment

## Maintenance

The script is self-contained with no external dependencies beyond Python 3 standard library. It uses:
- `subprocess` for git operations
- `re` for version parsing
- `pathlib` for file handling

No additional Python packages need to be installed.
