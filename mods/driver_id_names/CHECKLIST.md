# Driver ID Mod - Step-by-Step Checklist

Use this checklist to track your progress. Check off each step as you complete it.

## Preparation

- [ ] **Download 7-Zip** (Recommended - easiest method)
  - Official site: https://www.7-zip.org/
  - Free and open source
  - Works perfectly for extracting .scs files (which are just ZIP files)
  
  **Alternative**: Use Windows built-in extractor (rename .scs to .zip)
  
  **Note**: You don't need a special "SCS Extractor" - any ZIP tool works!

- [ ] **Locate your ETS2 installation**
  - Usually: `Steam/steamapps/common/Euro Truck Simulator 2/`
  - Find `def.scs` file

- [ ] **Create a working folder**
  - Example: `C:\ETS2_Modding\`
  - This is where you'll extract files

## Step 1: Extract Game Files

- [ ] **Extract def.scs using 7-Zip** (or Windows built-in)
  - **Method 1 (7-Zip)**: Right-click `def.scs` → "7-Zip" → "Extract to def\"
  - **Method 2 (Windows)**: Rename `def.scs` to `def.zip`, then right-click → "Extract All..."
  - Choose output folder (e.g., `C:\ETS2_Modding\extracted\`)
  - Wait for extraction (may take a few minutes)
  
  **Note**: .scs files are just ZIP files - any ZIP extractor works!

- [ ] **Verify extraction**
  - Navigate to: `extracted/locale/en_us/` (or your locale)
  - Confirm `driver_names.sii` exists
  - File size should be several KB

## Step 2: Examine the File

- [ ] **Open driver_names.sii in a text editor**
  - Use Notepad++, VS Code, or similar
  - Don't modify it yet - just look!

- [ ] **Understand the structure**
  - See lines like: `name[0]: "Felix"`
  - See lines like: `name[152]: "John D."`
  - Count how many entries (search for `name[`)

- [ ] **Note any duplicates**
  - Look for the same name appearing multiple times
  - Example: "John D." at index 1 and index 153
  - This is why we need IDs!

## Step 3: Prepare the Script

- [ ] **Verify Python is installed**
  - Open PowerShell
  - Run: `python --version`
  - Should show Python 3.x

- [ ] **Navigate to project directory**
  ```powershell
  cd C:\Users\pbuck\Desktop\Development\ETS2GameMods\ETS2GameMods
  ```

- [ ] **Test script help**
  ```powershell
  python scripts/add_driver_ids.py
  ```
  - Should show usage instructions

## Step 4: Run the Script

- [ ] **Prepare the command**
  - Input: Path to extracted `driver_names.sii`
  - Output: Path to mod directory
  
  Example:
  ```powershell
  python scripts/add_driver_ids.py "C:\ETS2_Modding\extracted\locale\en_us\driver_names.sii" "mods\driver_id_names\universal\locale\en_us\driver_names.sii"
  ```

- [ ] **Run the script**
  - Copy your command
  - Paste in PowerShell
  - Press Enter

- [ ] **Verify output**
  - Script should show:
    - Total names found: XXX
    - Names modified: XXX
    - Output file path
  - Check that the output file was created

- [ ] **Review the modified file**
  - Open: `mods/driver_id_names/universal/locale/en_us/driver_names.sii`
  - Verify names now have IDs: `name[152]: "152 - Felix"`
  - Check a few entries to make sure it worked

## Step 5: Build the Mod

- [ ] **Run build script**
  ```powershell
  .\scripts\build.ps1 -ModName driver_id_names
  ```

- [ ] **Verify build output**
  - Check: `dist/driver_id_names.scs` exists
  - File should be several KB in size
  - Should see: "Created: dist/driver_id_names.scs"

## Step 6: Install the Mod

- [ ] **Locate ETS2 mod folder**
  - Windows: `Documents/Euro Truck Simulator 2/mod/`

- [ ] **Copy the mod file**
  - Copy: `dist/driver_id_names.scs`
  - Paste to: `Documents/Euro Truck Simulator 2/mod/`

- [ ] **Verify file is in place**
  - Check that `driver_id_names.scs` is in the mod folder

## Step 7: Test in Game

- [ ] **Launch ETS2**

- [ ] **Go to Mod Manager**
  - From main menu
  - Find "Driver ID in Names" mod

- [ ] **Enable the mod**
  - Check the box next to the mod
  - Move it to "Active Mods" if needed

- [ ] **Load your save game**
  - Load your existing save with 260 drivers

- [ ] **Verify drivers show IDs**
  - Go to Company Management
  - Check driver list
  - All drivers should show: "152 - Felix", "153 - John D.", etc.

- [ ] **Test ticker notification**
  - Wait for a driver to level up or earn money
  - Check ticker - should show: "152 - Felix leveled up!"
  - You should be able to identify which driver it is

## Step 8: Verify Everything Works

- [ ] **Check existing drivers**
  - All 260 drivers should have IDs in their names
  - No duplicates (each ID is unique)

- [ ] **Test new hire** (optional)
  - Hire a new driver
  - They should automatically get an ID in their name
  - No extra work needed

- [ ] **Check game.log.txt** (if issues)
  - Location: `Documents/Euro Truck Simulator 2/game.log.txt`
  - Look for errors related to the mod
  - Should see mod loading successfully

## Troubleshooting

If something doesn't work:

- [ ] **Mod not showing in Mod Manager?**
  - Check `manifest.sii` syntax
  - Verify file structure is correct

- [ ] **Names not changing?**
  - Verify mod is enabled
  - Check file is in `universal/locale/en_us/`
  - Check `game.log.txt` for errors

- [ ] **Script errors?**
  - Verify Python is installed
  - Check file paths are correct
  - Make sure input file exists

- [ ] **Game crashes?**
  - Check SII file syntax
  - Verify all braces match
  - Check quotes are correct

## Success Criteria

✅ All 260 existing drivers show IDs in their names  
✅ Ticker notifications include driver IDs  
✅ No duplicate names (each ID is unique)  
✅ New hires automatically get IDs  
✅ Game runs without errors  

---

**Once all steps are complete, you're done!** 🎉

Your drivers will now be uniquely identifiable, making it easy to track who leveled up or earned money.

