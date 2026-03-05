# Scripts Directory

This directory contains utility scripts for the LiaScript-Courses repository.

## Link Conversion Tools

### Convert Relative Links

**File:** `convert_relative_links.py`

Converts relative image and stylesheet paths in course YAML headers and markdown
bodies to absolute `raw.githubusercontent.com` URLs pointing to `refs/heads/main`.
Also warns when a YAML field contains a tag-based URL (`refs/tags/…`) from this
repository.

**Fields processed:**
- `logo:` – course logo image
- `icon:` – course icon image
- `link:` – external stylesheet (e.g. `style.css`)
- Markdown images: `![alt](path)`
- HTML images: `<img src="path">`

**Usage:**
```bash
# Convert all courses
python3 scripts/convert_relative_links.py

# Convert a single file
python3 scripts/convert_relative_links.py courses/my_course.md

# Dry-run (show what would change without writing)
python3 scripts/convert_relative_links.py --dry-run
```

**What it does:**
- Converts `link: style.css` → `link: https://raw.githubusercontent.com/.../refs/heads/main/courses/style.css`
- Leaves already-absolute `refs/heads/main` URLs unchanged
- Reports `⚠️` warnings for `refs/tags/…` URLs (must be fixed manually)
- Reports `❌` errors for referenced paths that don't exist on disk

**Test suite:** `test_convert_relative_links.py`

---

## YAML Validation Tools

### Pre-Commit Hook

**File:** `pre-commit`

Pre-commit hook that runs automatically before each commit on staged course files.
It performs two steps in order:

1. **Link conversion** – converts relative `logo:`, `icon:`, and `link:` values and
   relative Markdown/HTML image paths to absolute `refs/heads/main` URLs; re-stages
   modified files automatically.  Warns (non-blocking) if any field contains a
   `refs/tags/…` URL from this repository.
2. **YAML validation** – validates YAML syntax in the course header.

**Install:**
```bash
python3 scripts/install-pre-commit-hook.py
```

**Features:**
- Runs automatically before each commit
- Validates only staged course files
- Auto-converts relative image/stylesheet paths to absolute URLs
- Warns when `link:`, `logo:`, or `icon:` uses a fragile `refs/tags/` URL
- Rejects commits with missing referenced files or YAML errors
- Provides clear error messages

### Hook Installer

**File:** `install-pre-commit-hook.py`

Installs the pre-commit hook into your local repository.

**Usage:**
```bash
python3 scripts/install-pre-commit-hook.py
```

**What it does:**
- Creates symlink from `.git/hooks/pre-commit` to `scripts/pre-commit`
- Makes the hook executable
- Verifies installation

### Validation Script

**File:** `validate_course_yaml.py`

Validates YAML syntax in all course markdown files.

**Usage:**
```bash
# Validate all courses
python3 scripts/validate_course_yaml.py

# Show all files (including valid ones)
python3 scripts/validate_course_yaml.py --verbose

# Strict mode (treat warnings as errors)
python3 scripts/validate_course_yaml.py --strict
```

**When to use:**
- Manual validation before committing (if no hook)
- Check all courses in repository
- Debugging YAML issues
- CI/CD pipelines

### Test Suites

**Files:** `test_validate_course_yaml.py`, `test_convert_relative_links.py`

**Usage:**
```bash
# Run YAML validation tests
python3 scripts/test_validate_course_yaml.py

# Run link conversion tests
python3 scripts/test_convert_relative_links.py
```

**YAML validation tests:**
- Valid YAML is accepted
- Invalid YAML (unquoted brackets) is rejected
- Valid quoted YAML is accepted
- Missing YAML block is detected
- Missing version field generates warning
- Empty YAML is rejected

**Link conversion tests:**
- Relative `logo:`, `icon:`, `link:` values are converted to absolute URLs
- Already-absolute `refs/heads/main` URLs are left unchanged
- `refs/tags/…` URLs produce warnings (not auto-converted)
- Relative Markdown and HTML image paths are converted
- Missing referenced files are reported as errors

## Version Management

### Check and Increment Version

**File:** `check_and_increment_version.py`

Automatically increments version numbers in course files based on content changes.

**Documentation:** See `VERSION_CHECK_README.md`

### Checksum State Management

**File:** `checksum_state.py`

Manages checksum state for tracking file changes across workflow runs.

**Documentation:** See `CHECKSUM_STATE_README.md`

## Cleanup

### Cleanup Old Releases

**File:** `cleanup_old_releases.py`

Removes old release tags and artifacts to keep the repository clean.

**Test:** `test_cleanup_old_releases.py`

## Documentation

For detailed information about YAML validation and link conversion, see:
- **User Guide:** `docs/YAML_VALIDATION_GUIDE.md`
- **Workflow Guide:** `docs/WORKFLOW_RACE_CONDITION_FIX.md`

## Best Practices

1. **Always install the pre-commit hook:**
   ```bash
   python3 scripts/install-pre-commit-hook.py
   ```

2. **Use `refs/heads/main` for `link:`, `logo:`, and `icon:` URLs** – never use
   `refs/tags/…` URLs in YAML header fields.  The hook will warn you if you do.

3. **Run validation before pushing:**
   ```bash
   python3 scripts/validate_course_yaml.py
   ```

4. **Test after modifying validation or conversion logic:**
   ```bash
   python3 scripts/test_validate_course_yaml.py
   python3 scripts/test_convert_relative_links.py
   ```

5. **Quote special characters in YAML:**
   ```yaml
   attribute: "[[Value with brackets](https://example.com)]"
   ```
