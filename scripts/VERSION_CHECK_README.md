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

The script is integrated into the `.github/workflows/generate-liascript-outputs.yml` workflow. It runs automatically:

1. When a push is made to the `main` branch
2. When a pull request targets the `main` branch
3. Before the SCORM and PDF generation steps

The workflow will:
- Run the version check script
- Commit any version increments with message: "Auto-increment version tags for changed courses [skip ci]"
- Push the changes back to the branch

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

The workflow commits the version updates:
```bash
git commit -m "Auto-increment version tags for changed courses [skip ci]"
```

The `[skip ci]` tag prevents infinite loops in the CI/CD pipeline.

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

## Integration Details

The script is called in the `check_changes` job of the workflow:

```yaml
- name: Check and auto-increment version tags
  run: |
    cd project
    git config user.name "github-actions[bot]"
    git config user.email "github-actions[bot]@users.noreply.github.com"
    python3 scripts/check_and_increment_version.py
    if ! git diff --quiet; then
      git add courses/*.md
      git commit -m "Auto-increment version tags for changed courses [skip ci]"
      git push
    fi
```

This ensures version tags are correct before the export process begins.

## Benefits

1. **Prevents Build Failures**: Ensures every change has a version, avoiding crashes
2. **Automatic Versioning**: No need to manually remember to update versions
3. **Semantic Versioning Support**: Maintains proper Major.Minor.Patch format
4. **Flexible**: Manual version updates (e.g., major/minor bumps) are respected
5. **Transparent**: All version changes are logged and committed

## Maintenance

The script is self-contained with no external dependencies beyond Python 3 standard library. It uses:
- `subprocess` for git operations
- `re` for version parsing
- `pathlib` for file handling

No additional Python packages need to be installed.
