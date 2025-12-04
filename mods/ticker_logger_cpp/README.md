# Ticker Logger Mod (C++ DLL)

## Overview

This is an **advanced C++ DLL mod** that logs ticker messages (driver level ups, earnings, etc.) to a file so you can review them later.

## ⚠️ Important: This Requires C++ DLL Development

This mod cannot be created with standard SII modding. It requires:
- C++ programming knowledge
- DLL injection and function hooking
- Reverse engineering game functions
- Visual Studio or similar C++ compiler

## What This Mod Does

- Intercepts ticker/notification messages from the game
- Logs them to `Documents/Euro Truck Simulator 2/ticker_log.txt`
- Optionally displays a UI button to view log history
- Timestamps each entry

## Project Structure

```
ticker_logger_cpp/
├── src/
│   ├── main.cpp          # DLL entry point
│   ├── hooks.cpp         # Function hooks for ticker messages
│   ├── logging.cpp       # Logging functionality
│   └── ui.cpp            # Optional UI for viewing logs
├── include/
│   └── game_structs.h    # Game structure definitions
├── CMakeLists.txt        # Build configuration (if using CMake)
├── ticker_logger.vcxproj # Visual Studio project file
└── README.md
```

## Development Requirements

1. **Visual Studio 2019/2022** with C++ development tools
2. **Windows SDK**
3. **Hooking Library**: MinHook or Microsoft Detours
4. **Reverse Engineering Tools**: Cheat Engine, x64dbg

## How It Works (Conceptual)

1. **DLL Injection**: The DLL is injected into the ETS2 process
2. **Function Hooking**: Hooks into the game's notification/ticker display function
3. **Message Capture**: Intercepts ticker messages before they're displayed
4. **Logging**: Writes messages to a log file with timestamps

## Getting Started

### Step 1: Find the Ticker Function

You'll need to reverse engineer ETS2 to find:
- The function that displays ticker messages
- The structure of ticker message data
- How to hook into it

**Tools needed**:
- Cheat Engine (to find memory addresses)
- x64dbg (to disassemble and understand the function)
- Process Monitor (to understand file/registry access)

### Step 2: Set Up Project

1. Create a new DLL project in Visual Studio
2. Add MinHook or Detours library
3. Set up the hooking infrastructure

### Step 3: Implement Hooks

See `src/hooks.cpp` for example structure (you'll need to fill in actual function addresses).

### Step 4: Build and Test

1. Build the DLL
2. Use a DLL injector to inject into ETS2 process
3. Test that messages are being logged

## Alternative: External Tool

Instead of a DLL mod, consider creating an **external tool** that:
- Monitors `game.log.txt` for relevant messages
- Parses and logs ticker-related information
- Provides a UI to view the log

This is simpler and doesn't require reverse engineering, but may miss some messages.

## Legal and Safety

- ✅ Allowed for single-player use
- ⚠️ May conflict with World of Trucks features
- ⚠️ Can cause crashes if hooks are incorrect
- ⚠️ Will break when game updates

## Resources

- [MinHook Library](https://github.com/TsudaKageyu/minhook)
- [Microsoft Detours](https://github.com/microsoft/Detours)
- [ETS2 Modding Forums](https://forum.scssoft.com/)

## Status

⚠️ **This is a template/structure only**. You'll need to:
1. Reverse engineer the game to find function addresses
2. Implement the actual hooks
3. Test thoroughly

This is a complex project that requires significant C++ and reverse engineering knowledge.

