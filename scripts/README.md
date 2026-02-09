# Scripts Directory

This directory contains utility scripts for the LiaScript-Courses repository.

## YAML Validation Tools

### Pre-Commit Hook

**File:** `pre-commit`

Pre-commit hook that validates YAML syntax in course files before allowing commits.

**Install:**
```bash
python3 scripts/install-pre-commit-hook.py
```

**Features:**
- Runs automatically before each commit
- Validates only staged course files
- Rejects commits with YAML errors
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

### Test Suite

**File:** `test_validate_course_yaml.py`

Test suite for the YAML validation functionality.

**Usage:**
```bash
python3 scripts/test_validate_course_yaml.py
```

**Tests:**
- Valid YAML is accepted
- Invalid YAML (unquoted brackets) is rejected
- Valid quoted YAML is accepted
- Missing YAML block is detected
- Missing version field generates warning
- Empty YAML is rejected

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

For detailed information about YAML validation, see:
- **User Guide:** `docs/YAML_VALIDATION_GUIDE.md`
- **Workflow Guide:** `docs/WORKFLOW_RACE_CONDITION_FIX.md`

## Best Practices

1. **Always install the pre-commit hook:**
   ```bash
   python3 scripts/install-pre-commit-hook.py
   ```

2. **Run validation before pushing:**
   ```bash
   python3 scripts/validate_course_yaml.py
   ```

3. **Test after modifying validation logic:**
   ```bash
   python3 scripts/test_validate_course_yaml.py
   ```

4. **Quote special characters in YAML:**
   ```yaml
   attribute: "[[Value with brackets](https://example.com)]"
   ```
