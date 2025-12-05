#!/usr/bin/env python3
"""
Script to find driver_names.sii in extracted ETS2 .scs files.

This script searches recursively through extracted folders to locate
the driver_names.sii file, which might be in different locations
depending on how the extraction was done.

Usage:
    python scripts/find_driver_names.py [search_directory]

Example:
    python scripts/find_driver_names.py extracted/
    python scripts/find_driver_names.py .  # Search current directory
"""

import os
import sys
from pathlib import Path


def find_driver_names_file(search_dir="."):
    """
    Recursively search for driver_names.sii file.
    
    Args:
        search_dir: Directory to search in (default: current directory)
    
    Returns:
        List of found file paths
    """
    search_path = Path(search_dir).resolve()
    
    if not search_path.exists():
        print(f"Error: Directory does not exist: {search_path}")
        return []
    
    print(f"Searching for driver_names.sii in: {search_path}")
    print("=" * 60)
    
    found_files = []
    
    # Search recursively
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file == "driver_names.sii":
                full_path = Path(root) / file
                found_files.append(full_path)
                print(f"\n✓ Found: {full_path}")
                
                # Show relative path from search directory
                try:
                    rel_path = full_path.relative_to(search_path)
                    print(f"  Relative path: {rel_path}")
                except ValueError:
                    pass
    
    return found_files


def main():
    search_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    print("ETS2 driver_names.sii Finder")
    print("=" * 60)
    print()
    
    found_files = find_driver_names_file(search_dir)
    
    print()
    print("=" * 60)
    
    if not found_files:
        print("\n❌ No driver_names.sii files found!")
        print("\nPossible reasons:")
        print("1. Extraction didn't complete - try extracting again")
        print("2. File is in a different .scs file (try extracting all .scs files)")
        print("3. File might be in a different location than expected")
        print("\nTry searching in:")
        print("  - The root of your extracted folder")
        print("  - Any 'locale' folders")
        print("  - Check if there are other .scs files to extract")
        print("\nCommon .scs files in ETS2:")
        print("  - def.scs (definitions)")
        print("  - base.scs (base game files)")
        print("  - dlc_*.scs (DLC files)")
    else:
        print(f"\n✓ Found {len(found_files)} driver_names.sii file(s)")
        print("\nNext steps:")
        print("1. Copy one of these files to a working directory")
        print("2. Run the modification script:")
        print("   python scripts/add_driver_ids.py <found_file> mods/driver_id_names/universal/locale/en_us/driver_names.sii")
        
        if len(found_files) == 1:
            print(f"\nQuick command:")
            print(f'  python scripts/add_driver_ids.py "{found_files[0]}" mods/driver_id_names/universal/locale/en_us/driver_names.sii')


if __name__ == "__main__":
    main()

