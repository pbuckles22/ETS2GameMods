# ETS2GameMods

A repository for creating and managing Euro Truck Simulator 2 mods.

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [Getting Started](docs/GETTING_STARTED.md) | Overview, file formats, and testing philosophy |
| [Step-by-Step Guide](docs/STEP_BY_STEP_GUIDE.md) | Create your first mod with detailed instructions |
| [SII Format Reference](docs/SII_FORMAT_REFERENCE.md) | Complete SII syntax and examples |
| [Testing Guide](docs/TESTING_GUIDE.md) | How to test mods (spoiler: in-game testing required!) |

## 🎮 Quick Facts

- **No C++ or traditional programming required!** ETS2 uses SII format (text-based config)
- **Testing is done in-game** - TDD doesn't apply to ETS2 modding
- **You only need folders for your content type** - Simple mods need minimal structure

## Repository Structure

```
ETS2GameMods/
├── docs/                    # 📚 Documentation
│   ├── GETTING_STARTED.md   # Start here!
│   ├── STEP_BY_STEP_GUIDE.md
│   ├── SII_FORMAT_REFERENCE.md
│   └── TESTING_GUIDE.md
├── mods/                    # 🎮 All mods live here
│   ├── example_mod/         # Full template with all folders
│   ├── simple_sound_mod/    # Minimal sound mod example
│   ├── truck_skin_mod/      # Truck skin example with definitions
│   └── json_comparison_example/  # SII vs JSON comparison (educational)
├── scripts/                 # 🔧 Build scripts
│   └── build.sh             # Package mods into .scs files
└── dist/                    # 📦 Built .scs files (gitignored)
```

## Example Mods

| Mod | Type | Complexity | Purpose |
|-----|------|------------|---------|
| `example_mod` | Template | Full | Complete folder structure template |
| `simple_sound_mod` | Sound | Minimal | Shows bare minimum for sound mods |
| `truck_skin_mod` | Vehicle | Medium | Truck skin with definition files |
| `json_comparison_example` | Educational | N/A | Compare SII format to JSON |

## Creating a New Mod

1. **Create a new folder** in the `mods/` directory:
   ```bash
   mkdir -p mods/my_awesome_mod
   ```

2. **Copy the template files** from `example_mod`:
   ```bash
   cp mods/example_mod/manifest.sii mods/my_awesome_mod/
   cp mods/example_mod/desc.txt mods/my_awesome_mod/
   ```

3. **Edit `manifest.sii`** with your mod details:
   - `package_version`: Your mod version (e.g., "1.0.0")
   - `display_name`: Name shown in game's Mod Manager
   - `author`: Your name
   - `category[]`: Mod category ("truck", "trailer", "sound", "other", etc.)
   - `compatible_versions[]`: Game versions your mod works with

4. **Add your mod content** to the appropriate directories

5. **Optionally add an icon** (276x162 pixels, JPEG format)

## Building Mods

The build script packages your mods into `.scs` files that can be used with ETS2.

### Build all mods:
```bash
./scripts/build.sh
```

### Build a specific mod:
```bash
./scripts/build.sh my_awesome_mod
```

Built files will be placed in the `dist/` directory.

## Installing Mods

1. Build your mod using the build script
2. Copy the `.scs` file from `dist/` to your ETS2 mod folder:
   - **Windows**: `Documents/Euro Truck Simulator 2/mod/`
   - **Linux**: `~/.local/share/Euro Truck Simulator 2/mod/`
   - **macOS**: `~/Library/Application Support/Euro Truck Simulator 2/mod/`
3. Enable the mod in the game's Mod Manager

## Mod Categories

Available categories for `manifest.sii`:
- `truck` - Truck modifications
- `trailer` - Trailer modifications
- `sound` - Sound modifications
- `interior` - Interior modifications
- `map` - Map modifications
- `other` - Other modifications

## Resources

- [SCS Modding Wiki](https://modding.scssoft.com/wiki/Main_Page) - Official modding documentation
- [ETS2 Steam Workshop](https://steamcommunity.com/app/227300/workshop/) - Community mods
- [SCS Forum](https://forum.scssoft.com/) - Community support

## File Formats

- **Music files**: Ogg Vorbis format (.ogg)
- **Textures**: DDS format (.dds)
- **Models**: PMD/PMG format (.pmd, .pmg)
- **Definitions**: SII format (.sii)
- **Materials**: MAT format (.mat)

## Mods in This Repository

| Mod Name | Description | Version |
|----------|-------------|---------|
| example_mod | Full template with all folder types | 1.0.0 |
| simple_sound_mod | Minimal sound mod template | 1.0.0 |
| truck_skin_mod | Truck skin with paint job definition | 1.0.0 |
| json_comparison_example | Educational: SII vs JSON comparison | 1.0.0 |

*Add your mods to this table as you create them!*

## License

See individual mod folders for licensing information.
