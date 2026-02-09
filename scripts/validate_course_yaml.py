#!/usr/bin/env python3
"""
Validate YAML syntax in course markdown files.

This script checks all course files for YAML parsing errors and reports them.
It's designed to be run in CI or as a pre-commit hook to catch issues before deployment.
"""

import sys
import os
from pathlib import Path

# Add parent directory to path to import from generate_project_yaml
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generate_project_yaml import YamlCommentParser, find_markdown_files, COURSE_DIRECTORY


class ValidationResult:
    """Store validation results for a file."""
    def __init__(self, filepath, success, error_message=None, warning_message=None):
        self.filepath = filepath
        self.success = success
        self.error_message = error_message
        self.warning_message = warning_message


def validate_course_file(filepath):
    """
    Validate a single course file's YAML header.
    
    Returns:
        ValidationResult object with success status and any error/warning messages
    """
    parser = YamlCommentParser()
    
    # Capture the file content to check if it has YAML at all
    try:
        content = Path(filepath).read_text(encoding='utf-8')
    except Exception as e:
        return ValidationResult(
            filepath, 
            False, 
            error_message=f"Failed to read file: {e}"
        )
    
    # Check if file has YAML comment block
    if '<!--' not in content or '-->' not in content:
        return ValidationResult(
            filepath,
            False,
            warning_message="No YAML comment block found (missing <!-- -->)"
        )
    
    # Parse the YAML
    meta = parser.parse(str(filepath))
    
    # Check if parsing succeeded
    if not meta or len(meta) == 0:
        return ValidationResult(
            filepath,
            False,
            error_message="YAML parsing failed - returned empty metadata"
        )
    
    # Check for required fields
    warnings = []
    if not meta.get('version'):
        warnings.append("Missing 'version' field")
    if not meta.get('author'):
        warnings.append("Missing 'author' field")
    if not meta.get('title'):
        warnings.append("Missing 'title' field")
    
    if warnings:
        return ValidationResult(
            filepath,
            True,  # Parsing succeeded, but missing optional fields
            warning_message="; ".join(warnings)
        )
    
    return ValidationResult(filepath, True)


def validate_all_courses(directory=COURSE_DIRECTORY, fail_on_warning=False):
    """
    Validate all course files in the directory.
    
    Args:
        directory: Directory to search for course files
        fail_on_warning: If True, warnings are treated as failures
        
    Returns:
        Tuple of (success_count, error_count, warning_count, results_list)
    """
    files = find_markdown_files(directory)
    
    results = []
    success_count = 0
    error_count = 0
    warning_count = 0
    
    for file in files:
        result = validate_course_file(file)
        results.append(result)
        
        if result.success and not result.warning_message:
            success_count += 1
        elif result.success and result.warning_message:
            warning_count += 1
            if fail_on_warning:
                error_count += 1
        else:
            error_count += 1
    
    return success_count, error_count, warning_count, results


def print_results(results, verbose=False):
    """Print validation results in a readable format."""
    errors = [r for r in results if not r.success]
    warnings = [r for r in results if r.success and r.warning_message]
    successes = [r for r in results if r.success and not r.warning_message]
    
    # Print errors
    if errors:
        print("\n" + "="*70)
        print(f"❌ ERRORS ({len(errors)} files)")
        print("="*70)
        for result in errors:
            print(f"\n📄 {result.filepath}")
            print(f"   {result.error_message or result.warning_message}")
    
    # Print warnings
    if warnings:
        print("\n" + "="*70)
        print(f"⚠️  WARNINGS ({len(warnings)} files)")
        print("="*70)
        for result in warnings:
            print(f"\n📄 {result.filepath}")
            print(f"   {result.warning_message}")
    
    # Print summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"✅ Valid files:   {len(successes)}")
    print(f"⚠️  Warnings:      {len(warnings)}")
    print(f"❌ Errors:        {len(errors)}")
    print(f"📊 Total files:   {len(results)}")
    
    # Print verbose success list if requested
    if verbose and successes:
        print("\n" + "="*70)
        print(f"✅ VALID FILES ({len(successes)})")
        print("="*70)
        for result in successes:
            print(f"   {result.filepath}")


def main():
    """Main entry point for the validation script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Validate YAML syntax in course markdown files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate all courses
  python validate_course_yaml.py
  
  # Treat warnings as errors (strict mode)
  python validate_course_yaml.py --strict
  
  # Show all files including successful ones
  python validate_course_yaml.py --verbose
  
  # Validate specific directory
  python validate_course_yaml.py --directory path/to/courses
        """
    )
    
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Treat warnings as errors (exit with error code if warnings found)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show all files including successful validations'
    )
    
    parser.add_argument(
        '--directory', '-d',
        default=COURSE_DIRECTORY,
        help=f'Directory to search for course files (default: {COURSE_DIRECTORY})'
    )
    
    args = parser.parse_args()
    
    print("🔍 Validating course YAML headers...")
    print(f"📁 Directory: {args.directory}")
    print()
    
    success_count, error_count, warning_count, results = validate_all_courses(
        args.directory,
        fail_on_warning=args.strict
    )
    
    print_results(results, verbose=args.verbose)
    
    # Exit with error code if there are errors (or warnings in strict mode)
    if error_count > 0:
        print("\n❌ Validation FAILED")
        sys.exit(1)
    elif warning_count > 0 and args.strict:
        print("\n❌ Validation FAILED (strict mode - warnings treated as errors)")
        sys.exit(1)
    else:
        print("\n✅ Validation PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
