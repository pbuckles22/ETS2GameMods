# Quick Start Guide - Driver ID in Names

## The Problem

You have 260 AI drivers, and some have the same name (e.g., "John D."). When the ticker says "John D. leveled up!", you can't tell which John D. it is.

## The Solution

Modify `driver_names.sii` to prepend the Driver ID (array index) to each name:
- `name[152]: "Felix"` → `name[152]: "152 - Felix"`
- Driver ID 152 will now show as "152 - Felix" everywhere

## Why This Works

✅ **Driver ID = Array Index**: The game uses the array index as the driver ID
✅ **Unique by Design**: Each index is unique, so no duplicates possible
✅ **Automatic**: New hires automatically get the correct name from their ID
✅ **Instant Update**: Your 260 existing drivers update immediately when you enable the mod

## 5-Minute Setup

### Step 1: Extract driver_names.sii
```powershell
# Use 7-Zip (or any ZIP tool) to extract def.scs
# .scs files are just ZIP files with a different extension!
# Right-click def.scs → "7-Zip" → "Extract to def\"
# Navigate to: def/locale/en_us/driver_names.sii
# Copy it to: extracted/driver_names.sii
```

### Step 2: Run the Script
```powershell
python scripts/add_driver_ids.py extracted/driver_names.sii mods/driver_id_names/universal/locale/en_us/driver_names.sii
```

### Step 3: Build the Mod
```powershell
.\scripts\build.ps1 -ModName driver_id_names
```

### Step 4: Install and Test
1. Copy `dist/driver_id_names.scs` to `Documents/Euro Truck Simulator 2/mod/`
2. Enable in Mod Manager
3. Load your save - all 260 drivers should show IDs immediately!

## Result

- ✅ Every driver has a unique name (e.g., "152 - Felix", "153 - John D.")
- ✅ Ticker shows: "152 - Felix leveled up!" (you know exactly which driver)
- ✅ No duplicates possible (each ID is unique)
- ✅ New hires automatically get IDs (no extra work needed)

## Troubleshooting

**Q: Names not changing?**
- Check that file is in `universal/locale/en_us/` (or your locale)
- Verify the mod is enabled in Mod Manager
- Check `game.log.txt` for errors

**Q: Wrong locale?**
- If you play in German, use `locale/de_de/` instead of `en_us/`
- Run the script for each locale you want to support

**Q: Want different format?**
- Edit the script's format string (default: `"{index} - {name}"`)
- Options: `"{name} [ID: {index}]"`, `"[{index}] {name}"`, etc.

