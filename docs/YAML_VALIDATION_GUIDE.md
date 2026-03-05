# Course YAML Validation Guide

## Overview

All course markdown files in the `courses/` directory must have a valid YAML header enclosed in HTML comments (`<!-- -->`). This guide explains common YAML syntax errors and how to fix them.

## Running Validation

### Pre-Commit Hook (Recommended)

Install the pre-commit hook to automatically validate YAML before each commit:

```bash
# Install the hook
python3 scripts/install-pre-commit-hook.py

# The hook will now run automatically before every commit
# If validation fails, the commit will be rejected
```

**Benefits:**
- ✅ Converts relative `logo:`, `icon:`, `link:` paths to absolute URLs automatically
- ✅ Warns when stylesheet/image fields use fragile `refs/tags/` URLs
- ✅ Catches YAML errors before they're committed
- ✅ No CI overhead or race conditions
- ✅ Faster feedback (instant)
- ✅ Works offline

**To bypass the hook (not recommended):**
```bash
git commit --no-verify
```

### Manual Validation

```bash
# Validate all courses
python3 scripts/validate_course_yaml.py

# Show all files (including valid ones)
python3 scripts/validate_course_yaml.py --verbose

# Strict mode (treat warnings as errors)
python3 scripts/validate_course_yaml.py --strict
```

## Automatic Link Conversion

The pre-commit hook (and `scripts/convert_relative_links.py`) automatically fixes
common link issues in the YAML header and course body **before** YAML validation runs.

### Relative paths → absolute URLs

Relative paths in `logo:`, `icon:`, and `link:` fields are automatically converted
to absolute `raw.githubusercontent.com` URLs pointing to `refs/heads/main`.

**Example (automatic fix at commit time):**
```yaml
<!-- Before commit: -->
logo: img/cover.jpg
icon: img/icon.png
link: style.css

<!-- After hook runs (automatically re-staged): -->
logo: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/cover.jpg
icon: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/img/icon.png
link: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/style.css
```

The same conversion applies to Markdown images (`![alt](path)`) and HTML `<img src="path">` tags in the course body.

### Tag-based URLs → warning

If a `logo:`, `icon:`, or `link:` field contains an absolute URL that still points
to a `refs/tags/…` snapshot of **this repository**, the hook emits a **non-blocking
warning**. The commit is allowed, but you should update the URL before pushing.

**❌ WRONG – uses a tag snapshot (fragile, will not update):**
```yaml
link: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/tags/raumausstatter_polstergestelle_v0.1.2/courses/style.css
```

**✅ CORRECT – points to the main branch (always up-to-date):**
```yaml
link: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/style.css
```

**Why:** A tag URL is frozen at the version that was tagged.  If the stylesheet
is updated in a later commit, courses using the old tag URL will not pick up the
change.  Using `refs/heads/main` ensures the latest version is always used.

**Hook output example:**
```
🔗 Converting relative image links in 1 staged course file(s)...
   ⚠️  Tag-based URL in courses/Raumausstatter_polstergestelle.md:
       https://raw.githubusercontent.com/.../refs/tags/raumausstatter_polstergestelle_v0.1.2/courses/style.css
       Replace 'refs/tags/…' with 'refs/heads/main'

======================================================================
⚠️  WARNING – tag-based stylesheet URL(s) found in YAML header(s)
======================================================================

The link: (or logo:/icon:) field(s) above point to a refs/tags/ snapshot.
This means the asset will not update when the course is republished.
Replace 'refs/tags/<tag>' with 'refs/heads/main' in the URL(s).

Example fix:
  Before: link: https://raw.githubusercontent.com/.../refs/tags/<tag>/courses/style.css
  After:  link: https://raw.githubusercontent.com/.../refs/heads/main/courses/style.css

Commit allowed, but please fix these warnings.
```

### Manual conversion

You can also run the conversion script manually at any time:
```bash
# Convert all courses
python3 scripts/convert_relative_links.py

# Dry-run – show what would change without writing files
python3 scripts/convert_relative_links.py --dry-run

# Convert a specific file
python3 scripts/convert_relative_links.py courses/my_course.md
```

---

## Common YAML Errors and Fixes

### 1. Unquoted Special Characters

**❌ WRONG:**
```yaml
<!--
attribute: [[_Source: Example_](https://example.com)]
-->
```

**✅ CORRECT:**
```yaml
<!--
attribute: "[[_Source: Example_](https://example.com)]"
-->
```

**Why:** Square brackets `[ ]` are special YAML syntax for arrays. When they appear in your text, quote the entire value.

### 2. Unquoted Colons in Values

**❌ WRONG:**
```yaml
<!--
title: Module 1: Introduction
-->
```

**✅ CORRECT:**
```yaml
<!--
title: "Module 1: Introduction"
-->
```

**Why:** Colons `:` indicate key-value pairs in YAML. Quote values containing colons.

### 3. Missing Required Fields

**⚠️ WARNING (still valid but incomplete):**
```yaml
<!--
author: John Doe
-->
```

**✅ RECOMMENDED:**
```yaml
<!--
author: John Doe
version: 0.0.1
title: Course Title
email: john@example.com
language: de
narrator: Deutsch Male
tags:
  - Category
-->
```

**Why:** While the file will parse, missing `version`, `title`, or `author` may cause issues with URL generation or categorization.

### 4. Incorrect Indentation

**❌ WRONG:**
```yaml
<!--
tags:
- Tag1
  - Tag2
-->
```

**✅ CORRECT:**
```yaml
<!--
tags:
  - Tag1
  - Tag2
-->
```

**Why:** YAML is indent-sensitive. All list items must have the same indentation.

### 5. Missing HTML Comment Markers

**❌ WRONG:**
```yaml
author: John Doe
version: 1.0.0
```

**✅ CORRECT:**
```yaml
<!--
author: John Doe
version: 1.0.0
-->
```

**Why:** The YAML header must be wrapped in HTML comment tags.

## What Happens When YAML is Invalid?

### With Pre-Commit Hook (Recommended)

1. **Step 1 – Link conversion**: Hook converts relative `logo:`/`icon:`/`link:` paths and image links to absolute URLs, then re-stages modified files.  Warns (non-blocking) for `refs/tags/` URLs.
2. **Step 2 – YAML validation**: Checks all staged course files.
3. **Rejection**: Commit is rejected if YAML errors found (or if referenced image files are missing).
4. **Clear Messages**: Shows exactly which file and what's wrong.
5. **Quick Fix**: Fix the error and commit again.

**Example (YAML error):**
```
🔗 Converting relative image links in 1 staged course file(s)...
   (no relative links found)

🔍 Validating 1 staged course file(s)...

❌ courses/example_course.md
   YAML parsing failed - returned empty metadata

======================================================================
❌ COMMIT REJECTED - YAML validation failed
======================================================================

Fix the errors above and try again.
Or run: python3 scripts/validate_course_yaml.py --verbose
```

### Runtime Behavior (If Hook Bypassed)

If YAML errors slip through (e.g., via `--no-verify`):

1. **Detection**: The system detects the YAML parsing error
2. **Logging**: Clear error messages are logged with the file path and error details
3. **Fallback**: The course URL falls back to `refs/heads/main` instead of failing
4. **Warning**: Build logs show which file has the error and how to fix it

### Example Runtime Error Message

```
[ERROR] ❌ YAML parsing error in courses/example_course.md
[ERROR]    Error: while parsing a flow sequence
           in "<unicode string>", line 3, column 12:
             attribute: [[_Source: Example_](https://... 
                        ^
[ERROR]    Please check the YAML header syntax (especially attribute fields with special characters like [[ ]])
[ERROR]    Tip: Quote values that contain special YAML characters
[WARNING] ⚠️  Course courses/example_course.md has no version field or failed to parse
[WARNING]    This may indicate a YAML parsing error. Please check the YAML header in this file.
```

## Best Practices

### 1. Always Quote Complex Values

When in doubt, quote it:
```yaml
<!--
attribute: "Any value with special characters: [], {}, :, -, *, &, !, |, >"
-->
```

### 2. Use Multi-line Strings for Long Values

```yaml
<!--
comment: >
  This is a long comment
  that spans multiple lines
  and is easier to read.
-->
```

### 3. Install Pre-Commit Hook

Install the pre-commit hook to catch errors automatically:
```bash
python3 scripts/install-pre-commit-hook.py
```

### 4. Validate Before Committing (If No Hook)

If you don't use the pre-commit hook, run validation manually:
```bash
python3 scripts/validate_course_yaml.py
```

### 5. Test Your YAML

If you're unsure about YAML syntax, test it at [YAML Lint](https://www.yamllint.com/)

## Required Fields

These fields should be present in every course:

- `author` - Course author name
- `email` - Author's email
- `version` - Semantic version (e.g., 0.0.1, 1.2.3)
- `language` - Language code (e.g., de, en)
- `narrator` - Narrator voice (e.g., "Deutsch Male")
- `title` - Course title
- `tags` - List of tags for categorization

## Optional Fields

- `comment` - Course description
- `logo` - URL to course logo image *(relative paths auto-converted; use `refs/heads/main` for absolute URLs)*
- `icon` - URL to course icon *(relative paths auto-converted; use `refs/heads/main` for absolute URLs)*
- `link` - External stylesheet URL *(relative paths auto-converted; use `refs/heads/main` for absolute URLs)*
- `import` - Import other LiaScript modules
- `attribute` - Attribution for images/content
- `date` - Course creation/update date
- `edit` - Whether course is editable

## FAQ

**Q: Will YAML errors be automatically fixed?**

A: No. Automatic fixing could introduce unintended changes. The system:
- Detects errors with clear messages (pre-commit hook or runtime)
- Prevents commits with errors (if hook installed)
- Handles them gracefully at runtime (uses fallback URLs)
- Requires manual fixing to ensure correctness

**Q: What if I don't install the pre-commit hook?**

A: You can still commit, but:
- YAML errors won't be caught until runtime
- The course will use main branch URL (not versioned tag)
- You'll need to fix errors and commit again
- It's recommended to install the hook: `python3 scripts/install-pre-commit-hook.py`

**Q: Can I bypass the pre-commit hook?**

A: Yes, but not recommended:
```bash
git commit --no-verify
```
This skips validation, so errors may reach production.

**Q: How do I fix a YAML error in an existing course?**

1. Look at the error message for the line number
2. Check for unquoted special characters
3. Add quotes around the problematic value
4. Run validation: `python3 scripts/validate_course_yaml.py`
5. Commit (hook will validate automatically)

**Q: I see a ⚠️ warning about a tag-based URL in my `link:` / `logo:` / `icon:` field.  What do I do?**

A: The warning means the URL contains `refs/tags/<tag>` instead of `refs/heads/main`.  The commit is allowed but please fix it:

1. Open the course file
2. Find the `link:`, `logo:`, or `icon:` field in the YAML header
3. Replace `refs/tags/<tag-name>` with `refs/heads/main`

**Before:**
```yaml
link: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/tags/raumausstatter_polstergestelle_v0.1.2/courses/style.css
```

**After:**
```yaml
link: https://raw.githubusercontent.com/Ifi-DiAgnostiK-Project/LiaScript-Courses/refs/heads/main/courses/style.css
```

**Q: Why are my `link:` / `logo:` / `icon:` paths automatically changed when I commit?**

A: The pre-commit hook converts relative paths (e.g. `link: style.css`) to absolute
`raw.githubusercontent.com` URLs so the assets load correctly regardless of which
URL the course is accessed through (tag-based or head-based).  This change is
applied automatically and the file is re-staged — you don't need to do anything.

## Getting Help

If you encounter YAML errors you can't resolve:

1. Check this guide for common issues
2. Run validation with verbose output: `python3 scripts/validate_course_yaml.py --verbose`
3. Test your YAML at https://www.yamllint.com/
4. Ask for help in the repository issues

## Related Files

- **Pre-Commit Hook**: `scripts/pre-commit`
- **Hook Installer**: `scripts/install-pre-commit-hook.py`
- **Link Conversion Script**: `scripts/convert_relative_links.py`
- **Link Conversion Tests**: `scripts/test_convert_relative_links.py`
- **Validation Script**: `scripts/validate_course_yaml.py`
- **Generation Script**: `generate_project_yaml.py`
- **Test Suite**: `scripts/test_validate_course_yaml.py`
