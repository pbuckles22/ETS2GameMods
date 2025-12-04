# Build script for ETS2 mods (PowerShell version for Windows)
# This script packages mod directories into .scs files

param(
    [string]$ModName = ""
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ModsDir = Join-Path $ScriptDir "..\mods"
$OutputDir = Join-Path $ScriptDir "..\dist"

# Create output directory if it doesn't exist
if (-not (Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir | Out-Null
}

# Function to build a single mod
function Build-Mod {
    param(
        [string]$ModDir
    )
    
    $modName = Split-Path -Leaf $ModDir
    $manifestPath = Join-Path $ModDir "manifest.sii"
    
    # Check if manifest.sii exists
    if (-not (Test-Path $manifestPath)) {
        Write-Warning "Skipping $modName - no manifest.sii found"
        return
    }
    
    Write-Host "Building mod: $modName"
    
    $outputFile = Join-Path $OutputDir "$modName.scs"
    
    # Remove existing .scs file if it exists
    if (Test-Path $outputFile) {
        Remove-Item $outputFile -Force
    }
    
    # Create .scs file (which is just a zip file with .scs extension)
    # Compress-Archive doesn't support custom extensions, so we'll rename after
    $tempZip = Join-Path $env:TEMP "$modName.zip"
    if (Test-Path $tempZip) {
        Remove-Item $tempZip -Force
    }
    
    # Get all files in mod directory, excluding .gitkeep files
    $files = Get-ChildItem -Path $ModDir -Recurse -File | Where-Object { $_.Name -ne ".gitkeep" }
    
    if ($files.Count -eq 0) {
        Write-Warning "No files found in $modName"
        return
    }
    
    # Create zip file
    Compress-Archive -Path $files.FullName -DestinationPath $tempZip -CompressionLevel Optimal
    
    # Rename to .scs
    Move-Item -Path $tempZip -Destination $outputFile -Force
    
    Write-Host "Created: $outputFile"
}

# Build all mods or a specific mod
if ($ModName) {
    # Build specific mod
    $modPath = Join-Path $ModsDir $ModName
    if (Test-Path $modPath) {
        Build-Mod -ModDir $modPath
    } else {
        Write-Error "Mod '$ModName' not found in $ModsDir"
        exit 1
    }
} else {
    # Build all mods
    Write-Host "Building all mods..."
    $modDirs = Get-ChildItem -Path $ModsDir -Directory
    foreach ($modDir in $modDirs) {
        Build-Mod -ModDir $modDir.FullName
    }
}

Write-Host ""
Write-Host "Build complete! .scs files are in: $OutputDir"
Write-Host "Copy these files to: Documents\Euro Truck Simulator 2\mod\"

