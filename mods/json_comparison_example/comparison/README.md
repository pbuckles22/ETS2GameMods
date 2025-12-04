# SII vs JSON Format Comparison

This folder contains side-by-side examples showing the difference between
ETS2's SII format and JSON format.

## Files

| File | Format | Can ETS2 Use It? |
|------|--------|------------------|
| `example.sii` | SII | ✅ YES |
| `example_comparison.json` | JSON | ❌ NO (educational only) |

## Key Differences

| Feature | SII Format | JSON Format |
|---------|------------|-------------|
| File extension | `.sii` | `.json` |
| Comments | `# comment` or `// comment` | Not supported |
| Object declaration | `type : name { }` | `{ "type": "...", "name": "..." }` |
| Property syntax | `key: value` | `"key": "value"` |
| Arrays | `key[]: val1` (repeated) | `"key": ["val1", "val2"]` |
| Vectors | `(1.0, 2.0, 3.0)` | `{"x": 1.0, "y": 2.0, "z": 3.0}` |
| Separators | Newlines | Commas required |
| String quotes | Required for strings | Required for keys and strings |

## Why This Matters

If you're familiar with JSON from web development, understanding these
differences will help you write correct SII files:

1. **No commas between properties** - SII uses newlines
2. **Array syntax is different** - Repeat the property name with `[]`
3. **Comments are allowed** - Great for documentation
4. **Object header syntax** - `type : name` before the braces

## Common Mistake

```
# WRONG - JSON style (doesn't work)
{
    "display_name": "My Mod",
    "category": ["truck", "sound"]
}

# CORRECT - SII style
SiiNunit
{
    mod_package : .my_mod
    {
        display_name: "My Mod"
        category[]: "truck"
        category[]: "sound"
    }
}
```
