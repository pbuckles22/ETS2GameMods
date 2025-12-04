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

1. **Extract from game**:
   - Use SCS Extractor to extract `def.scs`
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

