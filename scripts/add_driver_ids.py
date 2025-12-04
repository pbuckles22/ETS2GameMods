#!/usr/bin/env python3
"""
Script to automatically add driver IDs to driver names in ETS2 driver_names.sii file.

This script modifies the driver_names.sii file by prepending the array index to each name.
The Driver ID is the array index, so name[152] is driver ID 152.

Usage:
    python scripts/add_driver_ids.py <input_file> <output_file>

Example:
    python scripts/add_driver_ids.py extracted/driver_names.sii mods/driver_id_names/universal/locale/en_us/driver_names.sii
"""

import os
import re
import sys
from pathlib import Path


def modify_driver_names_file(input_file, output_file, format_string="{index} - {name}"):
    """
    Modify driver_names.sii file to prepend index to each name.
    
    Args:
        input_file: Path to input driver_names.sii
        output_file: Path to output driver_names.sii
        format_string: Format for the name (default: "{index} - {name}")
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match: name[X]: "Driver Name"
        # We want to change it to: name[X]: "X - Driver Name"
        pattern = r'name\[(\d+)\]:\s*"([^"]+)"'
        
        def replace_name(match):
            index = match.group(1)
            current_name = match.group(2)
            
            # Check if ID is already prepended (avoid double-processing)
            if re.match(r'^\d+\s*-\s*', current_name) or re.match(r'^\[\d+\]', current_name):
                return match.group(0)  # Already has ID, don't modify
            
            # Format the new name
            new_name = format_string.format(index=index, name=current_name)
            return f'name[{index}]: "{new_name}"'
        
        modified_content = re.sub(pattern, replace_name, content)
        
        # Write to output
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        # Count how many names were modified
        matches = re.findall(pattern, content)
        modified_count = len([m for m in matches if not re.match(r'^\d+\s*-\s*', m[1])])
        
        return True, len(matches), modified_count
    except Exception as e:
        print(f"Error processing {input_file}: {e}")
        return False, 0, 0


def main():
    if len(sys.argv) < 3:
        print("ETS2 Driver ID Adder - driver_names.sii Modifier")
        print("=" * 60)
        print("\nUsage:")
        print("  python add_driver_ids.py <input_file> <output_file>")
        print("\nExample:")
        print("  python add_driver_ids.py extracted/driver_names.sii mods/driver_id_names/universal/locale/en_us/driver_names.sii")
        print("\nThis script:")
        print("  - Reads driver_names.sii from the extracted game files")
        print("  - Prepends the array index to each name (e.g., name[152]: \"152 - Felix\")")
        print("  - Writes the modified file to your mod directory")
        print("\nThe Driver ID is the array index, so this ensures unique names!")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Optional format string (default: "{index} - {name}")
    format_string = sys.argv[3] if len(sys.argv) > 3 else "{index} - {name}"
    
    print("ETS2 Driver ID Adder")
    print("=" * 60)
    print(f"Input:  {input_file}")
    print(f"Output: {output_file}")
    print(f"Format: {format_string}")
    print()
    
    if not os.path.exists(input_file):
        print(f"Error: Input file does not exist: {input_file}")
        sys.exit(1)
    
    success, total_names, modified_count = modify_driver_names_file(input_file, output_file, format_string)
    
    if success:
        print(f"\n✓ Success!")
        print(f"  Total names found: {total_names}")
        print(f"  Names modified: {modified_count}")
        print(f"  Names already had IDs: {total_names - modified_count}")
        print(f"\nOutput file: {output_file}")
        print("\nNext steps:")
        print("1. Review the modified file")
        print("2. Build the mod: .\\scripts\\build.ps1 -ModName driver_id_names")
        print("3. Test in-game - all 260 drivers should show IDs immediately!")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
