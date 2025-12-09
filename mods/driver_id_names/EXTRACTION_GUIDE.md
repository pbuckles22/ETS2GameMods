# How to Extract .scs Files - Complete Guide

## The Truth About .scs Files

**Important**: Most `.scs` files (like `def.scs`, `base.scs`) are **ZIP files with a different extension**. However, some files like `locale.scs` use SCS's proprietary hashfs format and require specialized tools.

**Good News**: `driver_names.sii` is a **generic file** - it's the same for all players! If extraction is difficult, you can use a file from another player or the modding community.

## Why the Confusion?

Many guides mention "SCS Extractor" as if it's a special tool, but:
- There are multiple tools with similar names
- Some are outdated or abandoned
- You don't actually need a special tool
- Any ZIP extractor works perfectly

## Recommended Method: 7-Zip (Easiest & Most Reliable)

### Why 7-Zip?

✅ **Free and open source**  
✅ **Widely used by modders**  
✅ **Works on Windows, Linux, macOS**  
✅ **No need to rename files**  
✅ **Handles .scs files natively**  

### Step-by-Step with 7-Zip

1. **Download 7-Zip** (if needed):
   - Official site: https://www.7-zip.org/
   - Download the installer for your system
   - Install it (takes 1 minute)

2. **Locate the .scs files**:
   - Usually: `Steam/steamapps/common/Euro Truck Simulator 2/`
   - Or: `C:\Program Files (x86)\Steam\steamapps\common\Euro Truck Simulator 2\`
   - You may need to extract **both** `def.scs` and `locale.scs`

3. **Extract**:
   - **Option A**: Right-click `def.scs` → "7-Zip" → "Extract to def\"
   - **Option B**: Right-click `locale.scs` → "7-Zip" → "Extract to locale\"
   - **Option C**: Open 7-Zip, navigate to the `.scs` file, click "Extract"
   - **Option D**: Drag `.scs` file into 7-Zip window, then extract

4. **Find driver_names.sii**:
   - Check **first**: `locale/en_us/driver_names.sii` (if you extracted `locale.scs`)
   - Check **also**: `def/locale/en_us/driver_names.sii` (if you extracted `def.scs`)
   - (Or `locale/de_de/` for German, etc.)

### Verification

After extraction, you should have one of these structures:

**If extracted from locale.scs:**
```
extracted/
└── locale/
    └── en_us/
        └── driver_names.sii  ← This is what we need!
```

**If extracted from def.scs:**
```
extracted/
└── def/
    └── locale/
        └── en_us/
            └── driver_names.sii  ← This is what we need!
```

**Note**: In newer ETS2 versions, `driver_names.sii` is often in `locale.scs` rather than `def.scs`.

---

## Alternative Methods

### Method 2: Windows Built-in (No Installation)

**Works on**: Windows 10/11

1. **Copy** `def.scs` to a working folder
2. **Rename** `def.scs` to `def.zip`
3. **Right-click** → "Extract All..."
4. **Choose** output folder
5. **Find** `def/locale/en_us/driver_names.sii`

**Note**: Some Windows versions may not recognize .scs as ZIP. If that happens, use 7-Zip instead.

---

### Method 3: WinRAR

If you have WinRAR installed:

1. Right-click `def.scs`
2. Select "Extract to def\"
3. Done!

---

### Method 4: Python Script (For Programmers)

If you prefer command line (works for ZIP-based .scs files only):

```python
import zipfile
import os

# Extract def.scs
scs_file = r'C:\Steam\steamapps\common\Euro Truck Simulator 2\def.scs'
output_dir = r'C:\ETS2_Extracted'

with zipfile.ZipFile(scs_file, 'r') as zip_ref:
    zip_ref.extractall(output_dir)

print(f"Extracted to: {output_dir}")
```

Save as `extract_scs.py` and run:
```powershell
python extract_scs.py
```

**Note**: This only works for ZIP-based .scs files. For `locale.scs` (hashfs format), use SXC Extractor (see Method 5).

---

### Method 5: SXC Extractor (For locale.scs and hashfs files)

**When to use**: When `locale.scs` cannot be extracted with standard tools.

1. **Download SXC Extractor**:
   - Search for "SXC Extractor ETS2" on modding sites
   - Example: https://ets2mods.lt/euro-truck-simulator-2-mods/ets2-others/sxc-extractor-mod-file-extraction-tool-v1-23-2-14/

2. **Extract locale.scs**:
   ```powershell
   sxc_extractor.exe "C:\Path\To\locale.scs" -d "C:\Path\To\Output\Folder"
   ```

3. **Find driver_names.sii**:
   - Look in: `locale/en_us/driver_names.sii`

**Why needed**: `locale.scs` uses SCS's hashfs format, which standard ZIP tools cannot handle.

---

### Method 6: Use a Generic File from Another Player (Easiest Alternative!)

**When to use**: When extraction is difficult or you can't extract `locale.scs`.

✅ **Good news**: `driver_names.sii` is a **generic master list** - it's the same for all players!

**The file is NOT player-specific**:
- It's the game's master list of possible driver names
- Everyone with the same game version and locale has the same file
- Your save file stores Driver IDs (indices), not the names themselves
- The game looks up names dynamically from this file

**Steps**:
1. Get `driver_names.sii` from:
   - Another player who has extracted it
   - ETS2 modding communities/forums
   - Modding Discord servers
   - Or ask in modding forums

2. **Important**: Make sure it matches your locale:
   - `en_us` for US English
   - `de_de` for German
   - `fr_fr` for French
   - etc.

3. Place it in a temporary location (e.g., `extracted/driver_names.sii`)

4. Run the modification script:
   ```powershell
   python scripts/add_driver_ids.py extracted/driver_names.sii mods/driver_id_names/universal/locale/en_us/driver_names.sii
   ```

**Why this works**: The file is identical for all players (same version/locale), so you don't need YOUR specific file - any player's file will work perfectly!

---

## What About "SCS Extractor" Tools?

### The Reality

There are several tools with names like:
- "SCS Extractor"
- "scs_extractor"
- "SCS Archive Extractor"
- etc.

**The truth**: They all just extract ZIP files. Some are:
- GUI tools that wrap ZIP extraction
- Python scripts that use zipfile
- Abandoned projects
- Outdated versions

### Should You Use Them?

**You don't need to!** Here's why:

✅ **7-Zip works perfectly** - no need for special tools  
✅ **More reliable** - widely used, well-maintained  
✅ **Simpler** - one tool for everything  
✅ **No confusion** - clear what it does  

### If You Really Want One

If you find a tool specifically for ETS2:
- Check when it was last updated
- Verify it's from a trusted source
- Remember: it's probably just extracting ZIP files anyway
- **7-Zip is still easier and more reliable**

---

## Official SCS Tools

SCS Software may provide official tools:
- **Website**: https://eurotrucksimulator2.com/mod_tools.php
- **Look for**: "Game Archive Extractor" or similar
- **Status**: May not always be available or up-to-date

**Recommendation**: Use 7-Zip instead - it's more reliable and always available.

---

## Troubleshooting

### "Can't open .scs file"

**Solution**: Use 7-Zip or rename to .zip

### "File is corrupted"

**Solution**: 
- Make sure you're extracting, not trying to open it
- Try a different ZIP tool
- Verify the file isn't actually corrupted (check file size)

### "Can't find driver_names.sii"

**Solution**:
- **The file might be in `locale.scs`, not `def.scs`!** Try extracting `locale.scs` as well
- Make sure you extracted the entire `def.scs` file
- Check the locale folder matches your game language
- Look in: `def/locale/en_us/` or `locale/en_us/` (or your locale)
- If using `scs_extractor` and it fails on `locale.scs`, use 7-Zip instead (see below)

### "Root directory not found" error when extracting locale.scs

**This error means**: `locale.scs` uses SCS's hashfs format, not a standard ZIP. Neither `scs_extractor` nor 7-Zip can extract it directly.

**Solution**: Use **SXC Extractor** (specialized tool for ETS2/ATS files):

1. **Download SXC Extractor**:
   - Available from ETS2 modding sites (search for "SXC Extractor ETS2")
   - Example: https://ets2mods.lt/euro-truck-simulator-2-mods/ets2-others/sxc-extractor-mod-file-extraction-tool-v1-23-2-14/
   - This tool is specifically designed for ETS2/ATS hashfs archives

2. **Extract locale.scs**:
   ```powershell
   sxc_extractor.exe "C:\Path\To\locale.scs" -d "C:\Path\To\Output\Folder"
   ```

3. **Find driver_names.sii**:
   - Look in: `locale/en_us/driver_names.sii` (or your locale)

**Why this happens**: `locale.scs` uses SCS's proprietary hashfs format, which requires specialized tools. Standard ZIP extractors (7-Zip, WinRAR) and some `scs_extractor` versions cannot handle this format.

### "Multiple extractors, which one?"

**Solution**: Use **7-Zip** - it's the standard tool used by most modders.

---

## Summary

| Tool | Pros | Cons | Recommendation |
|------|------|------|----------------|
| **7-Zip** | Free, reliable, works for ZIP-based .scs | Doesn't work for hashfs files | ✅ **Use for def.scs, base.scs** |
| **SXC Extractor** | Handles hashfs format (locale.scs) | Requires download | ✅ **Use for locale.scs** |
| Windows Built-in | No installation | Requires renaming, doesn't work for hashfs | ✅ Good alternative for ZIP-based files |
| WinRAR | Works well | Paid (free trial), doesn't work for hashfs | ✅ If you have it |
| Python script | Programmatic | Requires Python, doesn't work for hashfs | ✅ If you're comfortable |
| "scs_extractor" | ETS2-specific | May not support all formats | ⚠️ May fail on locale.scs |

---

## Final Recommendation

**Just use 7-Zip.** It's:
- Free
- Reliable
- What most modders use
- Works perfectly for this task
- No confusion about versions or authors

Download: https://www.7-zip.org/

---

## Quick Reference

```powershell
# Using 7-Zip (recommended):
1. Install 7-Zip from https://www.7-zip.org/
2. Right-click def.scs → "7-Zip" → "Extract to def\"
3. Find: def/locale/en_us/driver_names.sii

# Using Windows (alternative):
1. Copy def.scs to working folder
2. Rename def.scs to def.zip
3. Right-click → "Extract All..."
4. Find: def/locale/en_us/driver_names.sii
```

That's it! No need to search for "SCS Extractor" - just use 7-Zip! 🎯

