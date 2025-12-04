# Automated Training Plans Mod (C++ DLL)

## Overview

This is an **advanced C++ DLL mod** that automatically manages driver training plans based on garage type and driver level.

## ⚠️ Important: This Requires C++ DLL Development

This mod cannot be created with standard SII modding. It requires:
- C++ programming knowledge
- DLL injection and function hooking
- Reverse engineering game functions
- Understanding of ETS2's driver management system

## What This Mod Does

- Monitors driver levels in real-time
- Automatically switches training plans when drivers reach certain levels
- Supports different training plans per garage type
- Configurable training plan rules

## Example Training Plan

**Garage Type A** (Long Distance Focus):
- Level 1-4: Long Distance
- Level 5-8: High Value Cargo
- Level 9+: Balanced

**Garage Type B** (High Value Focus):
- Level 1-3: High Value Cargo
- Level 4-6: Fragile Cargo
- Level 7+: Balanced

## Project Structure

```
automated_training_cpp/
├── src/
│   ├── main.cpp          # DLL entry point
│   ├── hooks.cpp         # Function hooks
│   ├── training.cpp      # Training plan logic
│   └── config.cpp        # Configuration loading
├── include/
│   ├── game_structs.h    # Game structure definitions
│   └── training_config.h # Training plan configuration
├── config/
│   └── training_plans.json  # Training plan definitions
└── README.md
```

## Development Requirements

1. **Visual Studio 2019/2022** with C++ development tools
2. **Windows SDK**
3. **Hooking Library**: MinHook or Microsoft Detours
4. **JSON Library**: For configuration (e.g., nlohmann/json)
5. **Reverse Engineering Tools**: Cheat Engine, x64dbg

## How It Works (Conceptual)

1. **DLL Injection**: The DLL is injected into the ETS2 process
2. **Driver Monitoring**: Hooks into functions that handle driver level changes
3. **Level Detection**: Detects when a driver reaches a threshold level
4. **Training Update**: Programmatically changes the driver's training plan
5. **Configuration**: Reads training plans from a JSON config file

## Getting Started

### Step 1: Understand Driver System

You'll need to reverse engineer:
- How driver data is stored in memory
- Functions that handle training plan changes
- How to identify garage types
- How to programmatically change training

### Step 2: Set Up Project

1. Create a new DLL project in Visual Studio
2. Add MinHook/Detours library
3. Add JSON library for configuration
4. Set up hooking infrastructure

### Step 3: Implement Training Logic

See `src/training.cpp` for example structure.

### Step 4: Create Configuration

Define your training plans in `config/training_plans.json`.

### Step 5: Build and Test

1. Build the DLL
2. Use a DLL injector to inject into ETS2 process
3. Test that training plans change automatically

## Configuration Format

```json
{
  "garage_types": {
    "long_distance_focus": {
      "plans": [
        { "level_min": 1, "level_max": 4, "training": "long_distance" },
        { "level_min": 5, "level_max": 8, "training": "high_value" },
        { "level_min": 9, "level_max": 99, "training": "balanced" }
      ]
    },
    "high_value_focus": {
      "plans": [
        { "level_min": 1, "level_max": 3, "training": "high_value" },
        { "level_min": 4, "level_max": 6, "training": "fragile" },
        { "level_min": 7, "level_max": 99, "training": "balanced" }
      ]
    }
  }
}
```

## Alternative: External Tool

Instead of a DLL mod, consider creating an **external tool** that:
- Reads your save file periodically
- Analyzes driver levels
- Suggests training changes
- Optionally modifies the save file directly

This is simpler but requires save file format knowledge and manual application of changes.

## Legal and Safety

- ✅ Allowed for single-player use
- ⚠️ Modifying save files can corrupt them - always backup
- ⚠️ May conflict with World of Trucks features
- ⚠️ Can cause crashes if hooks are incorrect
- ⚠️ Will break when game updates

## Resources

- [MinHook Library](https://github.com/TsudaKageyu/minhook)
- [Microsoft Detours](https://github.com/microsoft/Detours)
- [ETS2 Modding Forums](https://forum.scssoft.com/)
- [SCS Modding Wiki](https://modding.scssoft.com/wiki/Main_Page)

## Status

⚠️ **This is a template/structure only**. You'll need to:
1. Reverse engineer the game to find function addresses
2. Understand driver data structures
3. Implement the actual hooks and training logic
4. Test thoroughly

This is a very complex project that requires significant C++ and reverse engineering knowledge.

