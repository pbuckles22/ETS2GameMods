# SII Format Reference

The SII format is ETS2's custom configuration language. This document explains its syntax and common patterns.

## Basic Syntax

### File Structure
Every SII file starts with `SiiNunit` and contains objects in curly braces:

```
SiiNunit
{
    object_type : object_name
    {
        property: value
    }
}
```

### Data Types

| Type | Example | Description |
|------|---------|-------------|
| String | `"Hello World"` | Text in quotes |
| Integer | `42` | Whole numbers |
| Float | `3.14` | Decimal numbers |
| Boolean | `true` / `false` | True/false values |
| Token | `my_token` | Unquoted identifier |
| Vector2 | `(1.0, 2.0)` | 2D coordinates |
| Vector3 | `(1.0, 2.0, 3.0)` | 3D coordinates/RGB color |
| Vector4 | `(1.0, 2.0, 3.0, 4.0)` | RGBA color |
| Array | `property[]: value` | Multiple values |

### Comments
```
# This is a comment
// This also works
```

## Common Object Types

### manifest.sii (Required for every mod)
```
SiiNunit
{
    mod_package : .my_mod_name
    {
        # Version in format "major.minor.patch"
        package_version: "1.0.0"
        
        # Name shown in Mod Manager
        display_name: "My Mod Name"
        
        # Your name or team name
        author: "Author Name"
        
        # Categories: truck, trailer, sound, interior, map, other
        category[]: "sound"
        category[]: "other"    # Can have multiple
        
        # Path to description file
        description_file: "desc.txt"
        
        # Path to icon (276x162 JPEG)
        icon: "icon.jpg"
        
        # Game versions this mod works with
        compatible_versions[]: "1.50.*"
        compatible_versions[]: "1.51.*"
        compatible_versions[]: "1.52.*"
    }
}
```

### Paint Job Definition
```
SiiNunit
{
    accessory_paint_job_data : my_paintjob.truck_name.paint_job
    {
        name: "Custom Paint"
        price: 5000
        unlock: 0
        
        # RGB colors (0.0 to 1.0)
        base_color: (1.0, 0.0, 0.0)    # Red
        flip_color: (0.0, 0.0, 1.0)    # Blue
        
        suitable_for[]: "volvo.fh16"
        suitable_for[]: "scania.s"
    }
}
```

### Sound Definition
```
SiiNunit
{
    sound_data : my_sound.horn
    {
        name: "Custom Horn"
        
        sound: "/sound/truck/horn/custom.ogg"
        
        volume: 1.0
        pitch: 1.0
        
        is_2d: false
        looped: false
    }
}
```

### Material Definition (.mat format)
```
material : "ui.my_material"
{
    texture: "my_texture.dds"
    texture_name: "texture"
}
```

## Naming Conventions

### Object Names
- Use lowercase with underscores: `my_mod_name`
- Start with your unique prefix: `mymod.object_name`
- Avoid special characters

### File Paths
- Use forward slashes: `/sound/music/file.ogg`
- Relative to mod root
- Case-sensitive on Linux

## Common Patterns

### Array Properties (multiple values)
```
compatible_versions[]: "1.50.*"
compatible_versions[]: "1.51.*"
compatible_versions[]: "1.52.*"
```

### Referencing Other Objects
```
SiiNunit
{
    accessory_addon_data : my_addon
    {
        # Reference another object
        data_path: "/def/vehicle/accessory.sii"
    }
}
```

### Include Files
```
@include "common_definitions.sui"
```

## Validation Tips

1. **No trailing commas** - Unlike JSON, SII doesn't use commas
2. **Matching braces** - Every `{` needs a `}`
3. **Proper quoting** - Strings need quotes, tokens don't
4. **Case sensitivity** - Object types are case-sensitive

## Comparison: SII vs JSON

| Feature | SII Format | JSON Equivalent |
|---------|------------|-----------------|
| Object | `type : name { }` | `{ "type": "name", ... }` |
| Property | `key: value` | `"key": "value"` |
| Array | `key[]: val1` `key[]: val2` | `"key": ["val1", "val2"]` |
| Comment | `# comment` | Not supported |
| Numbers | `42` or `3.14` | `42` or `3.14` |
| Booleans | `true` / `false` | `true` / `false` |

### SII Example
```
SiiNunit
{
    mod_package : .example
    {
        package_version: "1.0.0"
        display_name: "Example"
        category[]: "other"
    }
}
```

### Conceptual JSON Equivalent (NOT valid for ETS2)
```json
{
    "type": "mod_package",
    "name": ".example",
    "package_version": "1.0.0",
    "display_name": "Example",
    "category": ["other"]
}
```

**Note**: ETS2 does NOT accept JSON files. This comparison is only to help understand the SII format if you're familiar with JSON.
