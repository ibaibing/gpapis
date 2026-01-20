#!/usr/bin/env python3
"""
Command-line interface for gpapis.
Provides commands to manage GlobalPlatform API specifications.
"""

import sys
import argparse
from pathlib import Path
from .api import get_api_root, set_api_root, list_api_versions, get_all_resources

def main() -> int:
    """
    Main entry point for CLI commands.
    
    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """
    parser = argparse.ArgumentParser(
        description="gpapis - GlobalPlatform API Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="This tool helps manage GlobalPlatform API specifications."
    )
    
    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Validate command
    validate_parser = subparsers.add_parser("validate", help="Validate API configuration")
    
    # Info command
    info_parser = subparsers.add_parser("info", help="Show API information")
    
    # Wizard command
    wizard_parser = subparsers.add_parser("wizard", help="Interactive API configuration wizard")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Execute command
    if args.command == "validate":
        return cmd_validate()
    elif args.command == "info":
        return cmd_info()
    elif args.command == "wizard":
        return cmd_wizard()
    else:
        parser.print_help()
        return 1

def cmd_validate() -> int:
    """
    Validate API configuration.
    
    Returns:
        int: Exit code
    """
    api_root = get_api_root()
    
    print("=== API Configuration Validation ===")
    
    if not api_root:
        print("Status: ERROR")
        print("\nIssues found:")
        print("  - GLOBALPLATFORM_API_ROOT environment variable is not set")
        return 1
    
    api_root_path = Path(api_root)
    if not api_root_path.exists() or not api_root_path.is_dir():
        print("Status: ERROR")
        print("\nIssues found:")
        print(f"  - API root directory does not exist: {api_root}")
        return 1
    
    # Check if any API directories exist
    all_resources = get_all_resources()
    if not all_resources:
        print("Status: WARNING")
        print(f"\nAPI root is set to: {api_root}")
        print("No API specifications found.")
        return 0
    
    print("Status: SUCCESS")
    print(f"\nAPI root is set to: {api_root}")
    print(f"Found {len(all_resources)} API types with specifications.")
    
    return 0

def cmd_info() -> int:
    """
    Show API information.
    
    Returns:
        int: Exit code
    """
    api_root = get_api_root()
    all_resources = get_all_resources()
    
    print("=== API Information ===")
    print(f"GLOBALPLATFORM_API_ROOT: {api_root or 'Not set'}")
    
    if all_resources:
        print(f"\nDetected API Types ({len(all_resources)}):")
        for api_type, versions in all_resources.items():
            print(f"  {api_type}:")
            for version in versions:
                print(f"    - {version}")
    else:
        print("\nNo API specifications detected.")
    
    return 0

def cmd_wizard() -> int:
    """
    Interactive API configuration wizard.
    
    Returns:
        int: Exit code
    """
    print("=== GlobalPlatform API Configuration Wizard ===")
    print("This wizard will help you configure your GlobalPlatform API specifications.")
    print()
    
    # Step 1: Check if APIs are already configured
    api_root = get_api_root()
    if api_root:
        print(f"✓ GLOBALPLATFORM_API_ROOT is already set to: {api_root}")
        confirm = input("Would you like to change it? (y/N): ").strip().lower()
        if confirm != "y":
            print("✓ Keeping current configuration.")
            return 0
    
    # Step 2: Get API root path
    while True:
        api_path = input("Enter path to your GlobalPlatform APIs directory: ").strip()
        if not api_path:
            print("Path cannot be empty.")
            continue
        
        path = Path(api_path)
        if not path.exists() or not path.is_dir():
            print(f"Error: Directory does not exist or is not accessible: {api_path}")
            continue
        
        # Try to set the path
        if set_api_root(api_path):
            print(f"✓ GLOBALPLATFORM_API_ROOT set to: {api_path}")
            break
        else:
            print(f"Error: Failed to set API root path.")
    
    print()
    
    # Step 3: Show detected APIs
    print("Detecting API specifications...")
    all_resources = get_all_resources()
    
    if all_resources:
        print(f"✓ Found {len(all_resources)} API types with specifications.")
        print("Detected API Types:")
        for api_type, versions in all_resources.items():
            print(f"  - {api_type}: {len(versions)} versions")
    else:
        print("! No API specifications found in the specified directory.")
        print("Please ensure the directory contains API specifications in the expected structure.")
    
    print()
    print("=== Wizard Complete ===")
    print("You can now use the 'validate' and 'info' commands to check your configuration.")
    return 0

if __name__ == "__main__":
    sys.exit(main())