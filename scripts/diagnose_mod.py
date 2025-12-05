#!/usr/bin/env python3
"""
Diagnostic script to check if the driver_names mod is set up correctly.
"""

import sys
import zipfile
from pathlib import Path

def check_mod_file(mod_path):
    """Check if the mod .scs file has the correct structure."""
    print("Checking mod file structure...")
    print(f"Mod file: {mod_path}")
    
    if not Path(mod_path).exists():
        print(f"❌ ERROR: Mod file not found: {mod_path}")
        return False
    
    try:
        with zipfile.ZipFile(mod_path, 'r') as zip_ref:
            entries = zip_ref.namelist()
            
            print(f"\n✅ Mod file found ({len(entries)} entries)")
            
            # Check for required files
            has_manifest = any('manifest.sii' in e for e in entries)
            has_desc = any('desc.txt' in e for e in entries)
            has_driver_names = any('driver_names.sii' in e for e in entries)
            
            print(f"  manifest.sii: {'✅' if has_manifest else '❌'}")
            print(f"  desc.txt: {'✅' if has_desc else '❌'}")
            print(f"  driver_names.sii: {'✅' if has_driver_names else '❌'}")
            
            # Check driver_names.sii location
            driver_names_paths = [e for e in entries if 'driver_names.sii' in e]
            if driver_names_paths:
                print(f"\n📁 driver_names.sii location(s):")
                for path in driver_names_paths:
                    print(f"  - {path}")
                    if 'universal/locale' in path:
                        print(f"    ✅ Correct location!")
                    else:
                        print(f"    ⚠️  WARNING: Should be in universal/locale/.../")
            
            # Check for documentation files (shouldn't be there)
            doc_files = [e for e in entries if e.endswith('.md') or 'EXAMPLE' in e]
            if doc_files:
                print(f"\n⚠️  Documentation files found (should be excluded):")
                for doc in doc_files:
                    print(f"  - {doc}")
            
            return has_manifest and has_desc and has_driver_names
            
    except Exception as e:
        print(f"❌ ERROR reading mod file: {e}")
        return False

def check_driver_names_content(mod_path):
    """Check the content of driver_names.sii in the mod."""
    print("\n" + "="*60)
    print("Checking driver_names.sii content...")
    
    try:
        with zipfile.ZipFile(mod_path, 'r') as zip_ref:
            # Find driver_names.sii
            driver_names_path = None
            for entry in zip_ref.namelist():
                if 'driver_names.sii' in entry and 'universal' in entry:
                    driver_names_path = entry
                    break
            
            if not driver_names_path:
                print("❌ driver_names.sii not found in mod!")
                return False
            
            print(f"Reading: {driver_names_path}")
            
            with zip_ref.open(driver_names_path) as f:
                content = f.read().decode('utf-8')
                lines = content.split('\n')
                
                # Check first few entries
                print("\nFirst 5 name entries:")
                name_count = 0
                for i, line in enumerate(lines[:50], 1):
                    if 'name[' in line and ':' in line:
                        name_count += 1
                        print(f"  {line.strip()}")
                        if name_count >= 5:
                            break
                
                # Check if IDs are present
                import re
                pattern = r'name\[\d+\]:\s*"(\d+\s*-\s*[^"]+)"'
                matches = re.findall(pattern, content)
                
                if matches:
                    print(f"\n✅ Found {len(matches)} entries with IDs prepended")
                    print(f"   Example: '{matches[0]}'")
                else:
                    print("\n⚠️  WARNING: No entries found with ID format 'X - Name'")
                    print("   Checking for entries without IDs...")
                    pattern2 = r'name\[\d+\]:\s*"([^"]+)"'
                    matches2 = re.findall(pattern2, content)
                    if matches2:
                        print(f"   Found {len(matches2)} entries, but IDs may be missing")
                        print(f"   Example: '{matches2[0]}'")
                
                # Check file structure
                if 'SiiNunit' in content and 'driver_names' in content:
                    print("\n✅ File structure looks correct (SiiNunit, driver_names)")
                else:
                    print("\n❌ ERROR: File structure may be incorrect")
                    return False
                
                return True
                
    except Exception as e:
        print(f"❌ ERROR reading driver_names.sii: {e}")
        return False

def main():
    mod_path = "dist/driver_id_names.scs"
    
    if len(sys.argv) > 1:
        mod_path = sys.argv[1]
    
    print("="*60)
    print("ETS2 Driver Names Mod Diagnostic Tool")
    print("="*60)
    
    # Check mod file structure
    structure_ok = check_mod_file(mod_path)
    
    # Check content
    if structure_ok:
        content_ok = check_driver_names_content(mod_path)
    else:
        content_ok = False
    
    print("\n" + "="*60)
    print("Diagnostic Summary:")
    print("="*60)
    
    if structure_ok and content_ok:
        print("✅ Mod structure and content look correct!")
        print("\nIf names still don't show IDs in-game:")
        print("1. Check your game locale (mod uses en_us)")
        print("2. Fully restart ETS2 (close completely, then reopen)")
        print("3. Check game.log.txt for errors")
        print("4. Verify mod is enabled in Mod Manager")
    else:
        print("❌ Issues found with mod structure or content")
        print("   Review the errors above and fix them")
    
    print()

if __name__ == "__main__":
    main()

