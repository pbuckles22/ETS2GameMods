# Step-by-Step Walkthrough: Driver ID Mod

This guide walks you through every step, explaining what each file does and why.

## Overview of the Process

1. **Extract** the game's `driver_names.sii` file
2. **Examine** the file structure to understand it
3. **Modify** it using our Python script
4. **Build** the mod into a `.scs` file
5. **Install** and test in-game

---

## Step 1: Understanding What We're Modifying

### What is `driver_names.sii`?

This is a **single file** that contains an array of all possible driver names in ETS2. Think of it like a phone book:

```
Index 0  → "Felix"
Index 1  → "John D."
Index 2  → "Jane S."
Index 152 → "Another Name"
...
```

### Why This File?

- The game uses **array indices as Driver IDs**
- When you hire driver #152, the game looks up `name[152]` in this file
- Your save file stores the ID (152), not the name string
- By modifying this file, we change what name displays for each ID

### File Location in Game

The file is inside `def.scs` (a compressed archive):
```
def.scs
└── locale/
    └── en_us/              # Your language
        └── driver_names.sii
```

---

## Step 2: Extracting .scs Files

### What are .scs Files?

ETS2's `.scs` files are **just ZIP files with a different extension**. You can extract them with:
- Any ZIP tool (7-Zip, WinRAR, Windows built-in)
- Python's built-in `zipfile` module
- Official SCS tools (if available)

### Method 1: Using 7-Zip (Recommended - Easiest)

**7-Zip** is free, reliable, and works perfectly for this:

1. **Download 7-Zip** (if you don't have it):
   - Official site: https://www.7-zip.org/
   - Free and open source
   - Works on Windows, Linux, macOS

2. **Extract def.scs**:
   - Right-click `def.scs` in your ETS2 folder
   - Select "7-Zip" → "Extract to def\"
   - Or drag and drop to a folder
   - Location: `Steam/steamapps/common/Euro Truck Simulator 2/def.scs`

3. **Find the file**:
   - Navigate to: `def/locale/en_us/driver_names.sii`

### Method 2: Using Windows Built-in (Windows 10/11)

1. **Rename the file**:
   - Copy `def.scs` to a working folder
   - Rename `def.scs` to `def.zip`

2. **Extract**:
   - Right-click → "Extract All..."
   - Choose output folder

3. **Find the file**:
   - Navigate to: `def/locale/en_us/driver_names.sii`

### Method 3: Using Python (If you prefer command line)

```python
import zipfile
import shutil

# Extract def.scs (it's just a ZIP file)
with zipfile.ZipFile('def.scs', 'r') as zip_ref:
    zip_ref.extractall('extracted/')
```

### Method 4: Official SCS Tools (If Available)

SCS Software may provide official tools:
- Check: https://eurotrucksimulator2.com/mod_tools.php
- Look for "Game Archive Extractor" or similar
- **Note**: Official tools may not always be available or up-to-date

### Which Method Should You Use?

✅ **Recommended**: **7-Zip** (Method 1)
- Free, reliable, widely used
- No need to rename files
- Works on all platforms
- Most modders use this

⚠️ **Alternative**: Windows built-in (Method 2)
- Works if you don't want to install anything
- Requires renaming .scs to .zip

### Important Notes

- **.scs files ARE ZIP files** - you can use any ZIP tool
- **No special tool required** - despite what some guides say
- **7-Zip is the most common** tool used by modders
- **Multiple tools exist** but they all do the same thing (extract ZIP files)

### What You'll Get

After extraction, you'll have a folder structure like:
```
ETS2_Extracted/
├── def/
├── locale/
│   └── en_us/
│       └── driver_names.sii    ← This is what we need!
└── ... (many other folders)
```

### Finding the File

Navigate to:
```
ETS2_Extracted/locale/en_us/driver_names.sii
```

**Note**: If you play in a different language, look in:
- `locale/en_us/` (US English)
- `locale/de_de/` (German)
- `locale/fr_fr/` (French)
- etc.

---

## Step 3: Examining driver_names.sii

### Open the File

Open `driver_names.sii` in a text editor (Notepad++, VS Code, or even Notepad).

### What You'll See

```sii
SiiNunit
{
    driver_names : .driver.names
    {
        name[0]: "Felix"
        name[1]: "John D."
        name[2]: "Jane S."
        name[3]: "Mike T."
        name[4]: "Sarah L."
        # ... hundreds more entries
        name[500]: "Last Name"
    }
}
```

### Understanding the Structure

1. **`SiiNunit`**: Every SII file starts with this
2. **`driver_names : .driver.names`**: Object type and name
3. **`name[0]: "Felix"`**: 
   - `name[0]` = array index 0 (Driver ID 0)
   - `"Felix"` = the name that displays for Driver ID 0
4. **Each line** = one driver name in the pool

### Count the Entries

You can count how many names there are by searching for `name[` in your editor. There are typically 500-1000+ names in the pool.

---

## Step 4: Understanding the Python Script

### What the Script Does

The script (`scripts/add_driver_ids.py`) does the following:

1. **Reads** the `driver_names.sii` file
2. **Finds** each `name[X]: "Some Name"` line
3. **Extracts** the index number (X) and the name
4. **Modifies** it to `name[X]: "X - Some Name"`
5. **Writes** the modified file to your mod directory

### Script Breakdown

Let's look at the key parts:

```python
# Pattern to match: name[X]: "Driver Name"
pattern = r'name\[(\d+)\]:\s*"([^"]+)"'

# This regex finds:
# - name[152]: "Felix"
# - Captures: index=152, name="Felix"
```

```python
def replace_name(match):
    index = match.group(1)      # Gets "152"
    current_name = match.group(2) # Gets "Felix"
    
    # Check if already modified (avoid double-processing)
    if re.match(r'^\d+\s*-\s*', current_name):
        return match.group(0)  # Already has ID, skip
    
    # Create new name: "152 - Felix"
    new_name = f"{index} - {current_name}"
    return f'name[{index}]: "{new_name}"'
```

### What Gets Changed

**Before:**
```sii
name[0]: "Felix"
name[152]: "John D."
```

**After:**
```sii
name[0]: "0 - Felix"
name[152]: "152 - John D."
```

### Running the Script

```powershell
python scripts/add_driver_ids.py <input> <output>
```

**Example:**
```powershell
python scripts/add_driver_ids.py C:\ETS2_Extracted\locale\en_us\driver_names.sii mods\driver_id_names\universal\locale\en_us\driver_names.sii
```

**What happens:**
1. Script reads the extracted file
2. Modifies each name entry
3. Creates the directory structure if needed
4. Writes the modified file to your mod

---

## Step 5: Understanding the Mod Structure

### Why This Structure?

```
driver_id_names/
├── universal/
│   └── locale/
│       └── en_us/
│           └── driver_names.sii
├── manifest.sii
└── desc.txt
```

### The `universal/` Folder

- `universal/` means "applies to all game versions"
- This is the standard location for locale files in ETS2 mods
- The game will load this file and use it instead of the base game file

### The `locale/en_us/` Path

- Matches the game's internal structure
- `en_us` = English (US)
- If you play in German, you'd use `locale/de_de/`

### manifest.sii

This tells ETS2:
- Mod name
- Version
- Author
- Compatible game versions

### desc.txt

Description shown in the Mod Manager.

---

## Step 6: Building the Mod

### What is Building?

Building packages your mod files into a `.scs` file (which is just a ZIP with a different extension).

### The Build Script

`scripts/build.ps1` does:
1. Takes all files in `mods/driver_id_names/`
2. Zips them into `dist/driver_id_names.scs`
3. This `.scs` file is what ETS2 can load

### Running the Build

```powershell
.\scripts\build.ps1 -ModName driver_id_names
```

**What happens:**
- Script looks in `mods/driver_id_names/`
- Finds `manifest.sii` (required)
- Zips everything into `dist/driver_id_names.scs`
- You'll see: "Created: dist/driver_id_names.scs"

---

## Step 7: Installing and Testing

### Installation

1. **Copy** `dist/driver_id_names.scs` to:
   ```
   Documents/Euro Truck Simulator 2/mod/
   ```

2. **Launch** ETS2

3. **Go to** Mod Manager (from main menu)

4. **Enable** "Driver ID in Names" mod

5. **Load** your save game

### What Should Happen

✅ **Immediately**: All 260 of your existing drivers should show IDs:
- "152 - Felix" instead of "Felix"
- "153 - John D." instead of "John D."

✅ **Ticker**: When a driver levels up, you'll see:
- "152 - Felix leveled up!" (you know exactly which driver)

✅ **New Hires**: When you hire a new driver:
- They automatically get an ID (e.g., 200)
- They show as "200 - Some Name" automatically

### Troubleshooting

**Names not changing?**
- Check `game.log.txt` for errors
- Verify mod is enabled in Mod Manager
- Make sure file is in `universal/locale/en_us/` (not just `locale/`)

**Game crashes?**
- Check SII syntax (matching braces, proper quotes)
- Verify the file structure is correct

**Wrong language?**
- Make sure you modified the correct locale file
- Check what language your game is set to

---

## Summary: The Complete Flow

```
1. Extract def.scs
   └──> Get driver_names.sii

2. Examine driver_names.sii
   └──> Understand: name[152]: "Felix"

3. Run Python script
   └──> Modify to: name[152]: "152 - Felix"

4. Build mod
   └──> Create driver_id_names.scs

5. Install mod
   └──> Copy to ETS2 mod folder

6. Enable in game
   └──> All drivers show IDs immediately!
```

---

## Next Steps

Once you've downloaded SCS Extractor and extracted the files, we can:
1. Look at your actual `driver_names.sii` file together
2. Run the script step-by-step
3. Verify the output
4. Build and test

Ready when you are! 🚛

