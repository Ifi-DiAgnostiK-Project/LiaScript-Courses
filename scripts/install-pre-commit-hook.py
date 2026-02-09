#!/usr/bin/env python3
"""
Install pre-commit hook for YAML validation.

This script installs the pre-commit hook that validates YAML syntax
in course markdown files before allowing commits.

Usage:
    python3 scripts/install-pre-commit-hook.py
"""

import sys
import os
from pathlib import Path
import shutil


def main():
    """Install the pre-commit hook."""
    
    repo_root = Path(__file__).parent.parent.absolute()
    hooks_dir = repo_root / '.git' / 'hooks'
    hook_source = repo_root / 'scripts' / 'pre-commit'
    hook_dest = hooks_dir / 'pre-commit'
    
    # Check if .git directory exists
    if not hooks_dir.parent.exists():
        print("❌ Error: .git directory not found")
        print("   This script must be run from a Git repository")
        sys.exit(1)
    
    # Create hooks directory if it doesn't exist
    hooks_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if hook already exists
    if hook_dest.exists():
        print("⚠️  Pre-commit hook already exists")
        response = input("   Overwrite? (y/N): ").strip().lower()
        if response != 'y':
            print("   Installation cancelled")
            sys.exit(0)
        hook_dest.unlink()
    
    # Create symbolic link to hook script
    try:
        # Use relative path for the symlink
        relative_source = Path('..') / '..' / 'scripts' / 'pre-commit'
        hook_dest.symlink_to(relative_source)
        print(f"✅ Pre-commit hook installed successfully")
        print(f"   Location: {hook_dest}")
        print(f"   Source: {hook_source}")
    except Exception as e:
        # If symlink fails, copy the file instead
        print(f"⚠️  Symlink failed: {e}")
        print("   Copying file instead...")
        shutil.copy2(hook_source, hook_dest)
        print(f"✅ Pre-commit hook copied successfully")
    
    # Make sure the hook is executable
    hook_dest.chmod(0o755)
    
    # Verify installation
    if hook_dest.exists():
        print("\n📋 Hook installed and will run on every commit")
        print("   To bypass: git commit --no-verify")
        print("   To uninstall: rm .git/hooks/pre-commit")
        print("\nTest the hook:")
        print("   1. Stage a course file: git add courses/example.md")
        print("   2. Try to commit: git commit -m 'test'")
        print("   3. Hook will validate YAML before allowing commit")
    else:
        print("❌ Installation failed")
        sys.exit(1)


if __name__ == '__main__':
    main()
