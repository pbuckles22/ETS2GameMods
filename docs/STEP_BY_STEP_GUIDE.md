# Step-by-Step Mod Creation Guide

This guide walks you through creating mods from scratch.

## Quick Start: Simple Sound Mod (5 minutes)

### Step 1: Create Mod Folder
```bash
mkdir -p mods/my_sound_mod/sound/music
```

### Step 2: Create manifest.sii
Create `mods/my_sound_mod/manifest.sii`:
```
SiiNunit
{
    mod_package : .my_sound_mod
    {
        package_version: "1.0.0"
        display_name: "My Custom Music"
        author: "Your Name"
        category[]: "sound"
        description_file: "desc.txt"
        compatible_versions[]: "1.50.*"
        compatible_versions[]: "1.51.*"
        compatible_versions[]: "1.52.*"
    }
}
```

### Step 3: Create desc.txt
Create `mods/my_sound_mod/desc.txt`:
```
My Custom Music Mod
===================

Adds custom music to the game radio.

Installation:
1. Copy to Documents/Euro Truck Simulator 2/mod/
2. Enable in Mod Manager

Credits: Your Name
```

### Step 4: Add Your Music
- Convert your audio to `.ogg` format (use Audacity or FFmpeg)
- Place in `mods/my_sound_mod/sound/music/`
- File must be named exactly as the game expects (e.g., `cutscene.ogg`)

### Step 5: Build and Test
```bash
./scripts/build.sh my_sound_mod
# Copy dist/my_sound_mod.scs to ETS2 mod folder
# Launch game and enable mod
```

---

## Intermediate: Truck Skin Mod (15 minutes)

### Step 1: Create Mod Structure
```bash
mkdir -p mods/my_truck_skin/vehicle/truck/upgrade/paintjob/accessible
```

### Step 2: Create Manifest
Create `mods/my_truck_skin/manifest.sii`:
```
SiiNunit
{
    mod_package : .my_truck_skin
    {
        package_version: "1.0.0"
        display_name: "Custom Truck Skin"
        author: "Your Name"
        category[]: "truck"
        description_file: "desc.txt"
        compatible_versions[]: "1.50.*"
        compatible_versions[]: "1.51.*"
        compatible_versions[]: "1.52.*"
    }
}
```

### Step 3: Create Skin Definition
Create `mods/my_truck_skin/def/vehicle/truck/your_truck.sii`:
```
SiiNunit
{
    accessory_paint_job_data : my_custom_paint.your_truck.paint_job
    {
        name: "My Custom Paint"
        price: 5000
        unlock: 0
        icon: "my_icon"
        base_color: (1.0, 0.0, 0.0)  # RGB red
        flip_color: (0.0, 0.0, 1.0)  # RGB blue
        alternate_uvset: false
    }
}
```

### Step 4: Add Texture Files
- Create textures in DDS format using GIMP or Photoshop with DDS plugin
- Use templates from SCS Modding Wiki
- Place in appropriate vehicle folder

### Step 5: Build and Test
```bash
./scripts/build.sh my_truck_skin
```

---

## Advanced: Multiple File Types

For complex mods with definitions, textures, and sounds:

### Folder Structure
```
my_complex_mod/
├── manifest.sii
├── desc.txt
├── icon.jpg
├── def/
│   ├── vehicle/
│   │   └── truck/
│   │       └── my_truck_def.sii
│   └── world/
│       └── my_world_def.sii
├── vehicle/
│   └── truck/
│       └── textures/
│           └── my_texture.dds
├── material/
│   └── ui/
│       └── my_material.mat
└── sound/
    └── truck/
        └── my_sound.ogg
```

### Key Points
1. **def/ folder**: Contains .sii definition files that tell the game what your mod adds
2. **Other folders**: Contain the actual assets (textures, sounds, models)
3. **Paths matter**: The game looks for files in specific locations

---

## Common Tasks Cheat Sheet

| Task | Key Files | Folder |
|------|-----------|--------|
| Add music | .ogg audio | sound/music/ |
| Truck skin | .dds texture + .sii def | vehicle/truck/, def/ |
| Replace sound | .ogg audio | sound/ |
| UI change | .dds + .mat | ui/, material/ |
| Map addon | .sii + .pmd | def/, model/ |

---

## Troubleshooting

### Mod doesn't show in game
- Check manifest.sii syntax (no trailing commas)
- Verify .scs file is in correct mod folder
- Check game.log.txt for errors

### Textures not loading
- Verify DDS format is correct (DXT1, DXT5, or BC7)
- Check file paths match exactly
- Verify material file references correct texture

### Sounds not playing
- Ensure OGG format (not MP3)
- Check sample rate (44100 Hz recommended)
- Verify sound definition references correct file

### Game crashes
- Remove mod and check if game runs
- Simplify mod to find problematic file
- Check for conflicting mods
