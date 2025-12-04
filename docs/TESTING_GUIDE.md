# Testing Guide for ETS2 Mods

## Testing Philosophy

Unlike traditional software development where Test-Driven Development (TDD) is common, **ETS2 modding requires in-game testing**. This is because:

1. Mods are configuration/asset files, not executable code
2. The game engine interprets your files at runtime
3. There's no ETS2 simulator or emulator for automated testing

## Testing Workflow

### 1. Development Cycle

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   DEVELOP   │───▶│    BUILD    │───▶│   INSTALL   │
│  Edit files │    │ ./build.sh  │    │  Copy .scs  │
└─────────────┘    └─────────────┘    └─────────────┘
       ▲                                     │
       │                                     ▼
       │           ┌─────────────┐    ┌─────────────┐
       │           │   ANALYZE   │◀───│    TEST     │
       └───────────│ Check logs  │    │ Play game   │
                   └─────────────┘    └─────────────┘
```

### 2. Quick Iteration Script

Create a test script for faster iteration:

```bash
#!/bin/bash
# scripts/test.sh - Build and install mod for testing

MOD_NAME=$1
ETS2_MOD_DIR="$HOME/Documents/Euro Truck Simulator 2/mod"

# Build the mod
./scripts/build.sh "$MOD_NAME"

# Install to game
cp "dist/${MOD_NAME}.scs" "$ETS2_MOD_DIR/"

echo "Mod installed! Launch ETS2 to test."
```

## Pre-Flight Checks (Before In-Game Testing)

### 1. File Structure Validation
```bash
# Check required files exist
ls mods/your_mod/manifest.sii
ls mods/your_mod/desc.txt
```

### 2. SII Syntax Check
Look for common errors:
- Matching braces `{ }`
- No trailing commas
- Proper quoting on strings
- Valid property names

### 3. Asset Verification
- Images are DDS format (not PNG/JPG for textures)
- Audio is OGG format (not MP3/WAV)
- Correct dimensions for icons (276x162)

## In-Game Testing Checklist

### Basic Functionality
- [ ] Mod appears in Mod Manager
- [ ] Mod can be enabled without errors
- [ ] Game loads with mod enabled
- [ ] No crash on game start

### Content Verification
- [ ] Added content appears in-game
- [ ] Textures display correctly
- [ ] Sounds play properly
- [ ] No visual glitches

### Compatibility
- [ ] Works with current game version
- [ ] No conflicts with common mods
- [ ] Saves work correctly with mod

## Reading Game Logs

### Log Location
| OS | Path |
|----|------|
| Windows | `Documents/Euro Truck Simulator 2/game.log.txt` |
| Linux | `~/.local/share/Euro Truck Simulator 2/game.log.txt` |
| macOS | `~/Library/Application Support/Euro Truck Simulator 2/game.log.txt` |

### Common Log Messages

#### Success Indicators
```
[mod_package] Loading package 'your_mod' ...
[mod_package] Package 'your_mod' loaded successfully
```

#### Warning (may still work)
```
[warning] Unknown property 'some_property' in unit
```

#### Error (needs fixing)
```
[error] Cannot open file '/def/something.sii'
[error] Failed to load texture '/material/texture.dds'
```

### Debugging Steps

1. **Read the full error message** - It usually tells you exactly what's wrong
2. **Check file paths** - Most errors are path-related
3. **Verify file formats** - Wrong format won't load
4. **Simplify your mod** - Remove content until it works, then add back

## Testing Best Practices

### 1. Start Minimal
Begin with just `manifest.sii` and `desc.txt`, verify it loads, then add content incrementally.

### 2. One Change at a Time
When debugging, change only one thing between tests.

### 3. Keep Backups
Save working versions before making changes.

### 4. Use Developer Mode
Add `-developer` to game launch options for:
- Console access
- More detailed logging
- Faster testing

### 5. Test on Fresh Profile
Create a test profile to avoid corrupting your main save.

## Automated Validation (Limited)

While full automated testing isn't possible, you can validate some things:

### Bash Script for Basic Checks
```bash
#!/bin/bash
# scripts/validate.sh

MOD_DIR=$1

echo "Validating mod: $MOD_DIR"

# Check required files
if [[ ! -f "$MOD_DIR/manifest.sii" ]]; then
    echo "ERROR: Missing manifest.sii"
    exit 1
fi

if [[ ! -f "$MOD_DIR/desc.txt" ]]; then
    echo "ERROR: Missing desc.txt"
    exit 1
fi

# Check SII syntax (basic brace matching)
OPEN=$(grep -c "{" "$MOD_DIR/manifest.sii")
CLOSE=$(grep -c "}" "$MOD_DIR/manifest.sii")
if [[ $OPEN -ne $CLOSE ]]; then
    echo "ERROR: Unmatched braces in manifest.sii"
    exit 1
fi

echo "Basic validation passed!"
```

## Summary

| What You Can Test Automatically | What Requires In-Game Testing |
|--------------------------------|-------------------------------|
| File existence | Visual appearance |
| Basic syntax | Gameplay functionality |
| File formats | Performance impact |
| Required fields | Compatibility |
| Path validity | User experience |

**Bottom Line**: Plan for in-game testing as your primary validation method. The build → install → test cycle is how ETS2 modding works.
