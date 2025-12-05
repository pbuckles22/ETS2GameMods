# Driver ID in Names Mod

## Overview

This mod adds unique driver IDs to driver names in the ticker notifications, making it easier to track which of your 260 AI drivers leveled up or earned money.

## How It Works

ETS2 uses a **single file** (`driver_names.sii`) that contains an array of all driver names. The **Driver ID is the array index**.

**Key Concept**: 
- Driver ID 0 = `name[0]`
- Driver ID 152 = `name[152]`
- The game saves the **ID (index)**, not the name string
- When displaying a name, the game looks up the index in `driver_names.sii`

**Result**: By modifying `name[152]: "Felix"` to `name[152]: "152 - Felix"`, every driver with ID 152 will automatically show "152 - Felix" everywhere in the game.

## Why This Prevents Duplicates

✅ **Each array index is unique** - There can only be one `name[0]`, one `name[152]`, etc.

✅ **IDs make names unique** - Even if "John D." appears at both `name[1]` and `name[153]`, they become "1 - John D." and "153 - John D." - completely unique!

✅ **Automatic for new hires** - When you hire a new driver, they get assigned an ID (e.g., 152), and the game automatically looks up `name[152]` from your modded file

✅ **Works retroactively** - Your existing 260 drivers will instantly update because the game reads the name from the array index, not from saved data

### What Happens If You Have More Drivers Than Names?

If your `driver_names.sii` has 354 names (indices 0-353) and you hire driver #354:

- **The game will wrap around** - Driver 354 will likely use `name[0]` again (or use modulo: `name[354 % 354] = name[0]`)
- **But the ID still makes it unique!** - Driver 0 shows "0 - Felix", Driver 354 shows "0 - Felix" (same name, but different IDs)
- **With IDs added**: Driver 0 = "0 - Felix", Driver 354 = "0 - Felix" - wait, that's still a problem!

**Solution**: The file typically has entries beyond what you see. Check if your file has entries like `name[500]` or higher. If not, you may need to extend the file or the game will reuse names, but the **Driver ID will still be unique** (Driver 0 vs Driver 354 are different drivers, even if they show the same name).

**Important**: The Driver ID (0, 354, etc.) is what matters - that's what's saved in your save file. The name is just for display. So even if two drivers show the same name, they have different IDs and are tracked separately by the game.

## File Structure

```
driver_id_names/
├── universal/
│   └── locale/
│       └── en_us/              # Or your locale (en_us, de_de, etc.)
│           └── driver_names.sii
├── manifest.sii
├── desc.txt
└── README.md
```

## Setup Instructions

### Step 1: Extract Base Game Files

1. Download **SCS Extractor** (search for it on ETS2 modding forums)
2. Extract `def.scs` from your ETS2 installation
3. Navigate to `locale/en_us/` (or your locale)
4. Find `driver_names.sii`
5. Copy it to a working directory (e.g., `extracted/driver_names.sii`)

### Step 2: Modify driver_names.sii

The file format looks like this:

**Before:**
```sii
SiiNunit
{
    driver_names : .driver.names
    {
        name[0]: "Felix"
        name[1]: "John D."
        name[2]: "Jane S."
        name[152]: "Another Name"
        # ... etc
    }
}
```

**After:**
```sii
SiiNunit
{
    driver_names : .driver.names
    {
        name[0]: "0 - Felix"
        name[1]: "1 - John D."
        name[2]: "2 - Jane S."
        name[152]: "152 - Another Name"
        # ... etc
    }
}
```

### Step 3: Use the Automation Script

Since you have hundreds of names, use the Python script:

```powershell
python scripts/add_driver_ids.py extracted/driver_names.sii mods/driver_id_names/universal/locale/en_us/driver_names.sii
```

The script will:
- Parse the `driver_names.sii` file
- Extract the index number from each `name[X]` line
- Prepend the index to the name: `name[X]: "X - Original Name"`
- Write the modified file to your mod directory

### Step 4: Build and Test

```powershell
.\scripts\build.ps1 -ModName driver_id_names
```

## How New Drivers Work

**You don't need to do anything!** Here's why:

1. When you hire a new driver, the game assigns them an ID (e.g., 153)
2. The game saves only the ID (153) to your save file
3. When displaying the name, the game looks up `name[153]` in your modded `driver_names.sii`
4. Since you've already modified `name[153]: "153 - Some Name"`, that's what appears automatically

**No programming needed for new hires** - the connection is automatic via the array index!

## How Existing Drivers Work

**They update instantly!** Here's why:

1. Your save file stores driver IDs (indices), not name strings
2. When you load the game, it reads `driver_names.sii` to get the display name
3. Since you've modified `name[152]: "152 - Felix"`, driver ID 152 will show "152 - Felix"
4. All 260 of your existing drivers will update immediately when you enable the mod

**No save file editing needed** - the game reads names dynamically from the mod!

## Locale Support

If you play in a different language, you'll need to modify the appropriate locale file:
- English (US): `locale/en_us/driver_names.sii`
- English (US): `locale/en_us/driver_names.sii`
- German: `locale/de_de/driver_names.sii`
- etc.

The script works the same way for any locale.

## Testing

1. Build the mod
2. Install to ETS2 mod folder
3. Enable in Mod Manager
4. Load your save game
5. **All 260 drivers should immediately show IDs in their names**
6. Wait for a driver to level up or earn money
7. Check the ticker - driver name should include ID (e.g., "152 - Felix leveled up!")

## Troubleshooting

- **Mod not loading**: Check `game.log.txt` for errors
- **Names not changing**: 
  - Verify the file is in `universal/locale/en_us/` (or your locale)
  - Check that the SII syntax is correct (matching braces, proper quotes)
- **Game crashes**: Check SII file syntax - make sure all `name[X]:` entries are valid
- **Wrong locale**: Make sure you're modifying the locale file that matches your game language

## Format Options

You can customize the format. The script uses `"X - Name"` but you could use:
- `"X - Name"` (default)
- `"Name [ID: X]"` 
- `"[X] Name"`
- `"Name #X"`

Just modify the script's format string if you want a different style.
