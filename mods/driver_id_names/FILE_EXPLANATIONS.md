# File-by-File Explanation

This document explains what each file in the mod does and why it's needed.

## Mod Directory Structure

```
driver_id_names/
├── universal/
│   └── locale/
│       └── en_us/
│           └── driver_names.sii    ← The actual mod content
├── manifest.sii                     ← Mod metadata (REQUIRED)
├── desc.txt                        ← Description for Mod Manager
├── README.md                       ← Full documentation
├── WALKTHROUGH.md                  ← Step-by-step guide
├── CHECKLIST.md                    ← Progress checklist
├── QUICK_START.md                  ← Quick reference
├── FILE_EXPLANATIONS.md            ← This file
└── EXAMPLE_driver_names.sii        ← Example file (reference only)
```

---

## Required Files (Mod Won't Work Without These)

### 1. `manifest.sii` - Mod Metadata

**What it is**: Tells ETS2 about your mod

**What it contains**:
```sii
SiiNunit
{
    mod_package : .driver_id_names
    {
        package_version: "1.0.0"              # Your mod version
        display_name: "Driver ID in Names"     # Name in Mod Manager
        author: "Your Name"                    # Your name
        category[]: "other"                    # Mod category
        description_file: "desc.txt"          # Points to description
        compatible_versions[]: "1.50.*"        # Game versions that work
        compatible_versions[]: "1.51.*"
        compatible_versions[]: "1.52.*"
    }
}
```

**Why it's needed**: ETS2 won't recognize your mod without this file. It's like a "package.json" or "manifest" for the mod.

**What you might change**:
- `display_name`: Change to whatever you want shown in Mod Manager
- `author`: Put your name here
- `compatible_versions[]`: Add newer game versions as they come out

---

### 2. `universal/locale/en_us/driver_names.sii` - The Actual Mod

**What it is**: The modified driver names file with IDs prepended

**What it contains**:
```sii
SiiNunit
{
    driver_names : .driver.names
    {
        name[0]: "0 - Felix"
        name[1]: "1 - John D."
        name[152]: "152 - Mike T."
        # ... hundreds more
    }
}
```

**Why it's needed**: This is the actual content that changes driver names in-game.

**The path structure**:
- `universal/` = applies to all game versions
- `locale/en_us/` = English (US) locale
- If you play in German, you'd use `locale/de_de/`

**How it works**:
1. Game loads this file instead of the base game's `driver_names.sii`
2. When displaying Driver ID 152, game looks up `name[152]`
3. Finds: `name[152]: "152 - Mike T."`
4. Displays: "152 - Mike T." everywhere

**What you might change**:
- The format (e.g., `"152 - Felix"` vs `"Felix [ID: 152]"`)
- Only if you want a different display style

---

### 3. `desc.txt` - Mod Description

**What it is**: Description shown in the Mod Manager

**What it contains**:
```
Driver ID in Names Mod
=======================

Adds unique driver IDs to driver names...
[Full description]
```

**Why it's needed**: Helps users understand what the mod does when they see it in Mod Manager.

**What you might change**:
- Update version history
- Add installation notes
- Add credits/thanks

---

## Documentation Files (Helpful but Not Required)

### 4. `README.md` - Full Documentation

**What it is**: Complete guide explaining the mod

**Contains**:
- Overview
- How it works
- Setup instructions
- Limitations
- Troubleshooting

**Why it's useful**: Reference for you (or others) to understand the mod later.

---

### 5. `WALKTHROUGH.md` - Step-by-Step Guide

**What it is**: Detailed walkthrough of the entire process

**Contains**:
- Explanation of each step
- What each tool does
- What to expect at each stage

**Why it's useful**: Follow along step-by-step without guessing.

---

### 6. `CHECKLIST.md` - Progress Tracker

**What it is**: Checklist to track your progress

**Contains**:
- Checkboxes for each step
- Verification steps
- Troubleshooting section

**Why it's useful**: Keep track of where you are in the process.

---

### 7. `QUICK_START.md` - Quick Reference

**What it is**: Condensed version for quick reference

**Contains**:
- The problem
- The solution
- 5-minute setup guide

**Why it's useful**: Quick reminder of the process without reading everything.

---

### 8. `EXAMPLE_driver_names.sii` - Example File

**What it is**: Shows what the file looks like before/after

**Contains**:
- Example of original format
- Example of modified format
- Explanation of how it works

**Why it's useful**: Visual reference to understand the file structure.

**Note**: This is NOT used by the game - it's just for reference!

---

## Script Files (In `scripts/` directory)

### `scripts/add_driver_ids.py` - Automation Script

**What it is**: Python script that modifies `driver_names.sii`

**What it does**:
1. Reads the original `driver_names.sii`
2. Finds each `name[X]: "Name"` line
3. Changes it to `name[X]: "X - Name"`
4. Writes the modified file to your mod directory

**Why it's needed**: Manually editing hundreds of names would take forever!

**How to use it**:
```powershell
python scripts/add_driver_ids.py <input_file> <output_file>
```

**What you might change**:
- The format string (default: `"{index} - {name}"`)
- If you want a different style like `"{name} [ID: {index}]"`

---

### `scripts/build.ps1` - Build Script

**What it is**: PowerShell script that packages the mod

**What it does**:
1. Takes all files in `mods/driver_id_names/`
2. Zips them into `dist/driver_id_names.scs`
3. This `.scs` file is what ETS2 can load

**Why it's needed**: ETS2 needs mods in `.scs` format (which is just a ZIP file).

**How to use it**:
```powershell
.\scripts\build.ps1 -ModName driver_id_names
```

**What you might change**:
- Nothing usually - it just packages everything

---

## What Gets Built

When you run the build script, it creates:

### `dist/driver_id_names.scs`

**What it is**: The final mod file that ETS2 can load

**What it contains**:
- All files from `mods/driver_id_names/` zipped up
- Same structure inside the ZIP

**Why it's needed**: This is what you copy to your ETS2 mod folder.

**File structure inside**:
```
driver_id_names.scs (ZIP file)
├── universal/
│   └── locale/
│       └── en_us/
│           └── driver_names.sii
├── manifest.sii
└── desc.txt
```

---

## Summary: What Each File Does

| File | Purpose | Required? |
|------|---------|-----------|
| `manifest.sii` | Tells ETS2 about the mod | ✅ Yes |
| `driver_names.sii` | The actual mod content | ✅ Yes |
| `desc.txt` | Description for Mod Manager | ✅ Yes |
| `README.md` | Full documentation | ❌ No |
| `WALKTHROUGH.md` | Step-by-step guide | ❌ No |
| `CHECKLIST.md` | Progress tracker | ❌ No |
| `add_driver_ids.py` | Automation script | ❌ No (but very helpful!) |
| `build.ps1` | Build script | ❌ No (but very helpful!) |

---

## File Flow Diagram

```
1. Extract driver_names.sii from game
   └──> Original file (no IDs)

2. Run add_driver_ids.py
   └──> Modified file (with IDs)
   └──> Saved to: mods/driver_id_names/universal/locale/en_us/

3. Run build.ps1
   └──> Packages everything into .scs file
   └──> Creates: dist/driver_id_names.scs

4. Copy to ETS2 mod folder
   └──> Documents/Euro Truck Simulator 2/mod/driver_id_names.scs

5. Enable in game
   └──> Game loads your modified driver_names.sii
   └──> All drivers show IDs!
```

---

## Questions?

If you're unsure about any file:
1. Check `WALKTHROUGH.md` for detailed explanations
2. Check `README.md` for full documentation
3. Look at `EXAMPLE_driver_names.sii` for visual reference

Ready to proceed? Start with the `CHECKLIST.md`! ✅

