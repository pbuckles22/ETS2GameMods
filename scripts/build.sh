#!/bin/bash

# Build script for ETS2 mods
# This script packages mod directories into .scs files

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODS_DIR="$SCRIPT_DIR/../mods"
OUTPUT_DIR="$SCRIPT_DIR/../dist"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Function to build a single mod
build_mod() {
    local mod_dir="$1"
    local mod_name=$(basename "$mod_dir")
    local output_file="$OUTPUT_DIR/${mod_name}.scs"
    
    # Check if manifest.sii exists
    if [[ ! -f "$mod_dir/manifest.sii" ]]; then
        echo "Warning: Skipping $mod_name - no manifest.sii found"
        return
    fi
    
    echo "Building mod: $mod_name"
    
    # Create .scs file (which is just a zip file with .scs extension)
    cd "$mod_dir"
    zip -r "$output_file" . -x "*.gitkeep"
    
    echo "Created: $output_file"
}

# Build all mods or a specific mod
if [[ -n "$1" ]]; then
    # Build specific mod
    if [[ -d "$MODS_DIR/$1" ]]; then
        build_mod "$MODS_DIR/$1"
    else
        echo "Error: Mod '$1' not found in $MODS_DIR"
        exit 1
    fi
else
    # Build all mods
    echo "Building all mods..."
    for mod_dir in "$MODS_DIR"/*/; do
        if [[ -d "$mod_dir" ]]; then
            build_mod "$mod_dir"
        fi
    done
fi

echo ""
echo "Build complete! .scs files are in: $OUTPUT_DIR"
echo "Copy these files to: Documents/Euro Truck Simulator 2/mod/"
