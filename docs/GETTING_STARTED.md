# Getting Started with ETS2 Modding

## Overview

This guide will help you create your first Euro Truck Simulator 2 mod, from understanding the basics to testing in-game.

## Understanding ETS2 Mod Architecture

### File Formats and Languages

ETS2 mods use several file formats:

| Format | Extension | Purpose | Language Type |
|--------|-----------|---------|---------------|
| **SII** | `.sii` | Game definitions, manifests, configs | Custom text format (similar to INI) |
| **MAT** | `.mat` | Material definitions | Custom text format |
| **SUI** | `.sui` | UI definitions | Custom text format |
| **DDS** | `.dds` | Textures | Binary (DirectDraw Surface) |
| **PMD/PMG** | `.pmd`, `.pmg` | 3D Models | Binary (SCS proprietary) |
| **OGG** | `.ogg` | Sound/Music | Binary (Ogg Vorbis audio) |

### Important: No Traditional Programming Required!

**ETS2 mods do NOT use C++, Python, JavaScript, or other traditional programming languages.**

The game uses its own custom formats:
- **SII format**: Text-based configuration (see examples below)
- **Binary assets**: Models, textures, sounds created with external tools

For advanced modding (creating the game engine itself), SCS Software uses C++, but **mod creators only use the SII text format and asset files**.

## Testing Your Mods

### Can I Use TDD (Test-Driven Development)?

**Short answer: No, traditional TDD doesn't apply to ETS2 mods.**

ETS2 mods are configuration and asset files, not executable code. Testing is done through:

1. **In-Game Testing** (Primary method)
   - Build your mod → Install → Launch game → Test
   - This is how 99% of mod testing is done

2. **Validation Checks** (Limited automated testing)
   - Syntax validation of SII files
   - File structure verification
   - Asset format validation

### Testing Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    ETS2 MOD TESTING WORKFLOW                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. EDIT FILES                                                  │
│     └── Modify .sii files, textures, sounds, etc.              │
│                                                                 │
│  2. BUILD MOD                                                   │
│     └── Run: ./scripts/build.sh my_mod                         │
│                                                                 │
│  3. INSTALL                                                     │
│     └── Copy .scs file to ETS2 mod folder                      │
│                                                                 │
│  4. TEST IN-GAME                                                │
│     ├── Launch ETS2                                             │
│     ├── Enable mod in Mod Manager                               │
│     ├── Load/Start game                                         │
│     └── Verify changes work                                     │
│                                                                 │
│  5. CHECK GAME LOG                                              │
│     └── Review game.log.txt for errors                          │
│         Windows: Documents/Euro Truck Simulator 2/game.log.txt  │
│         Linux:   ~/.local/share/Euro Truck Simulator 2/         │
│                                                                 │
│  6. ITERATE                                                     │
│     └── If issues found, return to step 1                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Debug Tips

1. **Enable Developer Console**: Add `-developer` to game launch options
2. **Check game.log.txt**: Shows loading errors and warnings
3. **Start Simple**: Test one change at a time
4. **Backup Saves**: Before testing major mods

## Minimal Mod Structures

### Do I Need All Those Folders?

**NO!** You only need folders for the content you're modifying.

#### Minimal Sound Mod (2 files + audio)
```
my_sound_mod/
├── manifest.sii      # Required
├── desc.txt          # Required
└── sound/
    └── music/
        └── mymusic.ogg
```

#### Minimal Skin Mod (2 files + texture)
```
my_skin_mod/
├── manifest.sii      # Required
├── desc.txt          # Required
└── vehicle/
    └── truck/
        └── skin.dds
```

#### Full Mod (all possible folders)
```
complete_mod/
├── manifest.sii      # Required
├── desc.txt          # Required
├── icon.jpg          # Optional (276x162 px)
├── def/              # Only if changing definitions
├── sound/            # Only if adding sounds
├── vehicle/          # Only if modifying vehicles
├── material/         # Only if custom materials
├── model/            # Only if custom 3D models
└── ui/               # Only if custom UI
```

## Next Steps

- See [STEP_BY_STEP_GUIDE.md](STEP_BY_STEP_GUIDE.md) for creating your first mod
- See [SII_FORMAT_REFERENCE.md](SII_FORMAT_REFERENCE.md) for SII syntax details
- Check example mods in the `mods/` directory
