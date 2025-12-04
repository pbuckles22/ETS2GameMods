# Advanced ETS2 Modding Guide

## Standard Modding vs Advanced Modding

ETS2 supports two types of mods:

### 1. Standard Mods (SII/Asset Files)
- **What they can do**: Modify game data, textures, sounds, UI layouts, driver names, etc.
- **Limitations**: Cannot intercept events, log data, or run automated logic
- **Tools needed**: Text editor, asset conversion tools
- **Difficulty**: Easy to Medium

### 2. Advanced Mods (C++ DLL)
- **What they can do**: Hook into game functions, intercept events, log data, automate actions
- **Limitations**: Complex, requires reverse engineering, breaks with game updates
- **Tools needed**: C++ compiler, reverse engineering tools, game SDK knowledge
- **Difficulty**: Hard to Very Hard

## Your Three Mods: Feasibility Analysis

### Mod 1: Driver ID in Names ✅ **STANDARD MODDING (Possible)**

**Approach**: Modify driver name files in `def/company/driver/`

**How it works**:
- ETS2 stores driver names in `.sii` files
- You can modify these files to append driver IDs
- Works for existing and new drivers

**Complexity**: Medium (requires understanding driver file structure)

**Status**: ✅ Can be done with standard SII modding

---

### Mod 2: Log Ticker Messages ⚠️ **REQUIRES C++ DLL**

**Approach**: Hook into game's notification/ticker system

**Why C++ is needed**:
- Ticker messages are generated at runtime
- No SII file contains ticker message history
- Must intercept game's internal notification functions
- Requires DLL injection and function hooking

**Complexity**: Hard (reverse engineering required)

**Status**: ⚠️ Requires C++ DLL modding

**Alternative**: If ticker messages appear in `game.log.txt`, you could parse that file externally (not a mod, but a workaround)

---

### Mod 3: Automated Training Plans ⚠️ **REQUIRES C++ DLL**

**Approach**: Monitor driver levels and automatically change training

**Why C++ is needed**:
- Training changes require runtime logic
- Must detect when drivers level up
- Must programmatically change training settings
- No SII file can execute conditional logic

**Complexity**: Hard (requires game state monitoring and automation)

**Status**: ⚠️ Requires C++ DLL modding

**Alternative**: Manual training plan templates (SII files) that you can quickly apply, but not automated

---

## C++ DLL Modding Overview

### What You'll Need

1. **Development Environment**:
   - Visual Studio 2019/2022 (Windows)
   - C++ compiler
   - Windows SDK

2. **Reverse Engineering Tools**:
   - Cheat Engine (for finding function addresses)
   - x64dbg or IDA Pro (for disassembly)
   - Process Monitor (for understanding file access)

3. **Knowledge Required**:
   - C++ programming
   - Windows DLL injection
   - Function hooking (detours, minhook, etc.)
   - Reverse engineering basics

### C++ DLL Mod Structure

```
advanced_mod/
├── src/
│   ├── main.cpp          # DLL entry point
│   ├── hooks.cpp         # Function hooks
│   ├── logging.cpp       # Logging functionality
│   └── training.cpp      # Training automation
├── include/
│   └── game_structs.h    # Game structure definitions
├── CMakeLists.txt        # Build configuration
└── README.md
```

### Risks and Limitations

1. **Game Updates**: DLL mods break when game updates
2. **Anti-Cheat**: Some multiplayer features may detect DLL injection
3. **Stability**: Can cause crashes if hooks are incorrect
4. **Complexity**: Requires deep game knowledge

### Legal Considerations

- DLL injection is generally allowed for single-player mods
- Don't use for cheating in multiplayer/World of Trucks
- Respect SCS Software's terms of service

---

## Recommended Approach

### Start with Mod 1 (Driver IDs)
- Learn standard modding first
- Understand SII file structure
- Get comfortable with mod building/testing

### Then Consider Mods 2 & 3
- Evaluate if C++ DLL modding is worth the complexity
- Consider external tools as alternatives
- Join ETS2 modding communities for support

---

## Resources for C++ DLL Modding

- [SCS Modding Wiki](https://modding.scssoft.com/wiki/Main_Page)
- [ETS2 Modding Forums](https://forum.scssoft.com/)
- [MinHook Library](https://github.com/TsudaKageyu/minhook) - Function hooking
- [Detours Library](https://github.com/microsoft/Detours) - Microsoft's hooking library

---

## Alternative Solutions

### For Ticker Logging:
- **External Tool**: Create a program that monitors `game.log.txt` for relevant messages
- **Screenshot**: Use a tool that captures ticker area and OCRs text
- **Manual Logging**: Use a hotkey tool to save current ticker text

### For Training Plans:
- **Template System**: Create SII templates for different garage types
- **External Manager**: Build a tool that reads save file and suggests training changes
- **Manual Process**: Create a checklist/system for managing training

These alternatives don't require C++ DLL modding but may be less integrated.

