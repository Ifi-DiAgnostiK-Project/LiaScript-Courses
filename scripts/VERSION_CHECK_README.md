# Version Check and Auto-Increment Script

## Quick Reference

**Two Ways to Update Course Versions:**

| You Do | Script Does | Use For |
|--------|-------------|---------|
| Edit course only (don't touch version) | Auto-increments patch (1.2.3 → 1.2.4) | Typos, small fixes, minor content updates |
| Edit course + manually change version | Nothing (respects your version) | Major updates (2.0.0), minor updates (1.3.0) |

**Key Point**: Manual version changes are **always respected**. The script only helps when you forget!

## Overview

The `check_and_increment_version.py` script automatically manages version tags in LiaScript course files. It ensures that every change to a course file has a corresponding version update, preventing crashes in the SCORM package generation workflow.

## Purpose

When a course file in the `courses/` directory is modified without updating its version tag, the SCORM package generation can fail. This script:

1. Detects which course markdown files have changed in the current commit
2. Checks if the version tag in the file's preamble was also updated
3. If the version wasn't changed, automatically increments the patch version
4. Commits the version changes back to the repository

## Two Working Modes

The script intelligently supports **two working modes** for course development:

### Mode 1: Automatic Patch Increment (Default)
When you modify a course file **without** changing the version:
- ✅ Script detects content changed
- ✅ Script detects version unchanged
- ✅ Script automatically increments patch version (e.g., 1.2.3 → 1.2.4)
- ✅ Commits the version change automatically

**Use this mode for**: Small fixes, typos, content updates

### Mode 2: Manual Version Control
When you modify a course file **and manually change the version**:
- ✅ Script detects content changed
- ✅ Script detects version **already changed** by you
- ✅ Script **skips auto-increment** (respects your manual change)
- ✅ Continues to create releases with your version

**Use this mode for**: Major updates (1.x.x → 2.0.0), minor updates (1.2.x → 1.3.0), or any semantic version bump

### Example: Manual Major Version Update

**Scenario**: You've made significant changes and want to bump to version 2.0.0

```markdown
<!-- Before (in courses/my_course.md) -->
version: 1.5.3

<!-- After your manual edit -->
version: 2.0.0
```

**What happens**:
1. You commit both the content changes and version update
2. Workflow runs and detects both changes
3. Script sees version changed from 1.5.3 to 2.0.0
4. Script prints: "✓ Version already changed, skipping auto-increment"
5. Workflow continues to create tags/releases with version 2.0.0
6. **No additional commits** are made by the workflow

✅ **Your manual version is respected!**

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

### Example 1: Automatic Patch Increment (Mode 1)

**Scenario**: You fix a typo in your course but forget to update the version.

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

**Result**: Script automatically increments patch version from 0.0.5 to 0.0.6.

### Example 2: Manual Major Version Update (Mode 2)

**Scenario**: You've completely rewritten a course section and want to bump to version 2.0.0.

**Before (in previous commit):**
```markdown
<!--
version: 1.3.5
-->
# My Course
Old content...
```

**After your manual edit (in current commit):**
```markdown
<!--
version: 2.0.0
-->
# My Course
Completely rewritten content!
```

**Result**: Script detects the version was manually updated from 1.3.5 to 2.0.0 and **skips auto-increment**. Your version 2.0.0 is used for creating releases.

### Example 3: Manual Minor Version Update (Mode 2)

**Scenario**: You add a new chapter and want to increment the minor version.

**Before (in previous commit):**
```markdown
version: 1.2.8
```

**After your manual edit (in current commit):**
```markdown
version: 1.3.0
```

**Result**: Script detects manual version change and skips auto-increment. Version 1.3.0 is used.

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

## Frequently Asked Questions (FAQ)

### Q1: What happens if I manually change the version?

**A**: The script respects your manual version change! 

When you edit a course file and manually update the version (e.g., 1.2.3 → 2.0.0), the script:
1. Detects that the version has changed between commits
2. Prints: "✓ Version already changed, skipping auto-increment"
3. Does NOT modify the file
4. Workflow continues to create releases using YOUR version

This allows you to control major and minor version bumps while still getting automatic patch increments for routine changes.

### Q2: Can I bump to a major or minor version manually?

**A**: Yes! Absolutely.

Simply edit your course file and change the version line:
```markdown
<!-- From this: -->
version: 1.5.9

<!-- To this: -->
version: 2.0.0  <!-- or 1.6.0 for minor -->
```

Commit your changes. The script will detect your manual version update and skip auto-increment.

### Q3: When should I manually change the version?

**A**: Use manual version changes for semantic versioning:

- **Major (x.0.0)**: Breaking changes, complete rewrites, major new features
  - Example: 1.9.5 → 2.0.0
- **Minor (1.x.0)**: New chapters, significant additions, new features
  - Example: 1.5.3 → 1.6.0
- **Patch (1.2.x)**: Small fixes, typos, minor updates (automatic)
  - Example: 1.2.3 → 1.2.4 (handled by script)

### Q4: What if I forget to update the version?

**A**: No problem! The script automatically increments the patch version for you.

This is the default mode - just edit your course and commit. The workflow will:
1. Detect the content changed
2. Detect the version didn't change
3. Automatically increment the patch version (1.2.3 → 1.2.4)
4. Commit the version change
5. Create releases with the new version

### Q5: Will the script override my manual version changes?

**A**: No, never! Your manual version changes are always respected.

The script only increments versions when you DON'T change them. If you manually update the version, the script detects this and skips any automatic changes.

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
  # Run in two cases:
  # 1. This IS a version-increment commit (Phase 2: create releases)
  # 2. No version was just incremented (normal flow or manual version change)
  # Skip if version was just incremented (Phase 1: wait for Phase 2)
  if: |
    steps.check_commit.outputs.is_version_commit == 'true' || steps.version_check.outputs.version_incremented != 'true'
  run: |
    # ... detect changed files
```

**Plain language explanation**: This step runs when either:
- We're in Phase 2 (this is already a version-increment commit), OR
- We're in normal flow (no version was just incremented, either because it wasn't needed or was manually updated)

The step is skipped only in Phase 1 when a version was just auto-incremented and committed.

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
