#!/usr/bin/env python3
"""
Script to check the range of driver names in driver_names.sii file.

This helps determine:
- How many names are defined
- What's the highest index
- If you might run out of names for your drivers
"""

import re
import sys
from pathlib import Path


def check_driver_names_range(input_file):
    """
    Check the range of driver names in the file.
    
    Args:
        input_file: Path to driver_names.sii file
    
    Returns:
        Dictionary with statistics
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all name[X]: entries
        pattern = r'name\[(\d+)\]:\s*"([^"]+)"'
        matches = re.findall(pattern, content)
        
        if not matches:
            return None
        
        # Extract indices
        indices = [int(match[0]) for match in matches]
        names = {int(match[0]): match[1] for match in matches}
        
        min_index = min(indices)
        max_index = max(indices)
        total_entries = len(matches)
        
        # Check for gaps
        expected_indices = set(range(min_index, max_index + 1))
        actual_indices = set(indices)
        gaps = sorted(expected_indices - actual_indices)
        
        # Check for duplicate names (same name at different indices)
        name_to_indices = {}
        for idx, name in names.items():
            if name not in name_to_indices:
                name_to_indices[name] = []
            name_to_indices[name].append(idx)
        
        duplicates = {name: indices for name, indices in name_to_indices.items() if len(indices) > 1}
        
        return {
            'min_index': min_index,
            'max_index': max_index,
            'total_entries': total_entries,
            'gaps': gaps,
            'duplicates': duplicates,
            'names': names
        }
    except Exception as e:
        print(f"Error processing {input_file}: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print("Driver Names Range Checker")
        print("=" * 60)
        print("\nUsage:")
        print("  python check_driver_names_range.py <driver_names.sii>")
        print("\nExample:")
        print("  python check_driver_names_range.py extracted/driver_names.sii")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not Path(input_file).exists():
        print(f"Error: File does not exist: {input_file}")
        sys.exit(1)
    
    print("Driver Names Range Checker")
    print("=" * 60)
    print(f"\nAnalyzing: {input_file}\n")
    
    stats = check_driver_names_range(input_file)
    
    if not stats:
        print("❌ No driver names found in file!")
        sys.exit(1)
    
    print(f"📊 Statistics:")
    print(f"  Minimum index: {stats['min_index']}")
    print(f"  Maximum index: {stats['max_index']}")
    print(f"  Total entries: {stats['total_entries']}")
    print(f"  Index range: {stats['max_index'] - stats['min_index'] + 1}")
    
    if stats['gaps']:
        print(f"\n⚠️  Gaps found: {len(stats['gaps'])} missing indices")
        if len(stats['gaps']) <= 20:
            print(f"   Missing indices: {stats['gaps']}")
        else:
            print(f"   Missing indices: {stats['gaps'][:20]}... (and {len(stats['gaps']) - 20} more)")
    else:
        print(f"\n✅ No gaps - indices are continuous from {stats['min_index']} to {stats['max_index']}")
    
    if stats['duplicates']:
        print(f"\n⚠️  Duplicate names found: {len(stats['duplicates'])} names appear at multiple indices")
        print("   (This is normal - the same name can appear at different indices)")
        if len(stats['duplicates']) <= 10:
            for name, indices in list(stats['duplicates'].items())[:10]:
                print(f"   '{name}' appears at indices: {indices}")
        else:
            print("   (Too many to list - this is normal)")
    else:
        print(f"\n✅ No duplicate names found")
    
    print(f"\n💡 What this means:")
    print(f"  - You can have up to {stats['max_index'] + 1} drivers before names wrap around")
    print(f"  - Driver IDs go from {stats['min_index']} to {stats['max_index']}")
    print(f"  - If you hire driver #{stats['max_index'] + 1}, the game will likely wrap around")
    print(f"  - But with IDs added, each driver will still be unique!")
    
    print(f"\n✅ Recommendation:")
    if stats['max_index'] >= 500:
        print(f"  You have plenty of names ({stats['max_index'] + 1} entries) - unlikely to run out!")
    elif stats['max_index'] >= 300:
        print(f"  You have {stats['max_index'] + 1} names - should be enough for most players")
    else:
        print(f"  You have {stats['max_index'] + 1} names - if you hire more drivers, names may wrap around")
        print(f"  But IDs will still make each driver unique!")


if __name__ == "__main__":
    main()

