# Course YAML Validation Guide

## Overview

All course markdown files in the `courses/` directory must have a valid YAML header enclosed in HTML comments (`<!-- -->`). This guide explains common YAML syntax errors and how to fix them.

## Running Validation

### Manually

```bash
# Validate all courses
python3 scripts/validate_course_yaml.py

# Show all files (including valid ones)
python3 scripts/validate_course_yaml.py --verbose

# Strict mode (treat warnings as errors)
python3 scripts/validate_course_yaml.py --strict
```

### Automatically

The validation runs automatically on:
- **Pull Requests** - When course files are modified
- **Pushes to main** - Before deployment

If validation fails, the workflow will show exactly which files have errors.

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

### Current Behavior (After Fix)

1. **Detection**: The system detects the YAML parsing error
2. **Logging**: Clear error messages are logged with the file path and error details
3. **Fallback**: The course URL falls back to `refs/heads/main` instead of failing
4. **Warning**: Build logs show which file has the error and how to fix it

### Example Error Message

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

### 3. Validate Before Committing

Run the validation script locally before pushing:
```bash
python3 scripts/validate_course_yaml.py
```

### 4. Test Your YAML

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
- `logo` - URL to course logo image
- `icon` - URL to course icon
- `link` - External stylesheets
- `import` - Import other LiaScript modules
- `attribute` - Attribution for images/content
- `date` - Course creation/update date
- `edit` - Whether course is editable

## FAQ

**Q: Will YAML errors be automatically fixed?**

A: No. Automatic fixing could introduce unintended changes. The system:
- Detects errors with clear messages
- Handles them gracefully (uses fallback URLs)
- Requires manual fixing to ensure correctness

**Q: Can I still deploy a course with YAML errors?**

A: The validation workflow will fail on PRs with YAML errors, but if somehow deployed:
- The course will still be accessible (uses main branch URL)
- It won't have a versioned release tag
- Error messages will guide you to fix it

**Q: How do I fix a YAML error in an existing course?**

1. Look at the error message for the line number
2. Check for unquoted special characters
3. Add quotes around the problematic value
4. Run validation: `python3 scripts/validate_course_yaml.py`
5. Commit and push the fix

## Getting Help

If you encounter YAML errors you can't resolve:

1. Check this guide for common issues
2. Run validation with verbose output: `python3 scripts/validate_course_yaml.py --verbose`
3. Check the GitHub Actions logs for detailed error messages
4. Test your YAML at https://www.yamllint.com/
5. Ask for help in the repository issues

## Related Files

- **Validation Script**: `scripts/validate_course_yaml.py`
- **Generation Script**: `generate_project_yaml.py`
- **Workflow**: `.github/workflows/validate-yaml.yml`
