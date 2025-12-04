# ETS2GameMods

A repository for creating and managing Euro Truck Simulator 2 mods.

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [Getting Started](docs/GETTING_STARTED.md) | Overview, file formats, and testing philosophy |
| [Step-by-Step Guide](docs/STEP_BY_STEP_GUIDE.md) | Create your first mod with detailed instructions |
| [SII Format Reference](docs/SII_FORMAT_REFERENCE.md) | Complete SII syntax and examples |
| [Testing Guide](docs/TESTING_GUIDE.md) | How to test mods (spoiler: in-game testing required!) |
| [Advanced Modding](docs/ADVANCED_MODDING.md) | C++ DLL modding guide for advanced features |
| [Git Workflow](docs/GIT_WORKFLOW.md) | Git workflow and branch strategy for mod development |

## 🎮 Quick Facts

- **No C++ or traditional programming required!** ETS2 uses SII format (text-based config) for standard mods
- **Testing is done in-game** - TDD doesn't apply to ETS2 modding
- **You only need folders for your content type** - Simple mods need minimal structure
- **Advanced features require C++ DLL modding** - See [Advanced Modding Guide](docs/ADVANCED_MODDING.md)

## 🚛 Your Mods

See [YOUR_MODS_SUMMARY.md](YOUR_MODS_SUMMARY.md) for details on the three mods you want to create:
1. Driver ID in Names (✅ Standard modding - ready to start)
2. Ticker Logging (⚠️ Requires C++ DLL)
3. Automated Training Plans (⚠️ Requires C++ DLL)

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
│   ├── driver_id_names/     # Add driver IDs to names (standard mod)
│   ├── ticker_logger_cpp/   # Log ticker messages (C++ DLL - advanced)
│   ├── automated_training_cpp/  # Auto training plans (C++ DLL - advanced)
│   └── json_comparison_example/  # SII vs JSON comparison (educational)
├── scripts/                 # 🔧 Build scripts
│   ├── build.ps1            # PowerShell build script (Windows)
│   └── build.sh             # Bash build script (Linux/macOS)
└── dist/                    # 📦 Built .scs files (gitignored)
```

## Example Mods

| Mod | Type | Complexity | Purpose |
|-----|------|------------|---------|
| `example_mod` | Template | Full | Complete folder structure template |
| `simple_sound_mod` | Sound | Minimal | Shows bare minimum for sound mods |
| `truck_skin_mod` | Vehicle | Medium | Truck skin with definition files |
| `driver_id_names` | Driver Management | Medium | Add driver IDs to names in ticker |
| `ticker_logger_cpp` | Advanced | Hard | Log ticker messages (C++ DLL) |
| `automated_training_cpp` | Advanced | Hard | Auto training plans (C++ DLL) |
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

### Windows (PowerShell):
```powershell
# Build all mods
.\scripts\build.ps1

# Build a specific mod
.\scripts\build.ps1 -ModName my_awesome_mod
```

### Linux/macOS (Bash):
```bash
# Build all mods
./scripts/build.sh

# Build a specific mod
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
