# Driver Names File Location

## Purpose

This directory contains the modified `driver_names.sii` file with driver IDs prepended to names.

## File Location

The file should be placed at:
```
universal/locale/en_us/driver_names.sii
```

## Locale Support

If you play in a different language, create the appropriate directory:
- English (US): `universal/locale/en_us/driver_names.sii`
- English (UK): `universal/locale/en_gb/driver_names.sii`
- German: `universal/locale/de_de/driver_names.sii`
- French: `universal/locale/fr_fr/driver_names.sii`
- etc.

## How to Get the File

**Important**: `driver_names.sii` is a **generic master list** - it's the same for all players (same game version and locale). You don't need YOUR specific file - any player's file will work!

### Option 1: Use a File from Someone Else (Easiest!)

✅ **You can use a generic `driver_names.sii` file from another player!**

- The file is **not player-specific** - it's the game's master list
- As long as it's from the same locale (en_us, de_de, etc.), it will work
- Game version differences are usually fine (newer versions may have more entries, but it's backward compatible)

**Steps**:
1. Get `driver_names.sii` from another player or modding community
2. Place it in a temporary location (e.g., `extracted/driver_names.sii`)
3. Run the modification script:
   ```powershell
   python scripts/add_driver_ids.py extracted/driver_names.sii mods/driver_id_names/universal/locale/en_us/driver_names.sii
   ```

### Option 2: Extract from Your Game

1. **Extract from game**:
   - Use SCS Extractor or 7-Zip to extract `def.scs` or `locale.scs`
   - Navigate to `locale/en_us/` (or your locale)
   - Find `driver_names.sii`

2. **Modify using script**:
   ```powershell
   python scripts/add_driver_ids.py extracted/driver_names.sii mods/driver_id_names/universal/locale/en_us/driver_names.sii
   ```

## File Format

The file should look like:

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

## Important Notes

- **Driver ID = Array Index**: `name[152]` is driver ID 152
- **Uniqueness guaranteed**: Each index is unique, so no duplicate names possible
- **Automatic for new hires**: New drivers automatically get the correct name from their ID
- **Works retroactively**: Existing drivers update immediately when mod is enabled

