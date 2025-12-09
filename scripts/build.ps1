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
    
    # Get all files in mod directory, excluding documentation and example files
    # Only include: manifest.sii, desc.txt, and files in universal/ directory
    $files = Get-ChildItem -Path $ModDir -Recurse -File | Where-Object {
        # Exclude .gitkeep files
        if ($_.Name -eq ".gitkeep") { return $false }
        
        # Exclude all .md files (documentation)
        if ($_.Extension -eq ".md") { return $false }
        
        # Exclude EXAMPLE_*.sii files (example/documentation files)
        if ($_.Name -like "EXAMPLE_*") { return $false }
        
        # Exclude incorrect paths (def/ and locale/ at root - these are wrong for mods)
        $relativePath = [System.IO.Path]::GetRelativePath($ModDir, $_.FullName)
        # Normalize path separators for comparison (handle both \ and /)
        $normalizedPath = $relativePath.Replace('\', '/')
        if ($normalizedPath -like "def/*" -or $normalizedPath -like "locale/*") {
            return $false
        }
        
        # Include everything else (manifest.sii, desc.txt, universal/ files, etc.)
        return $true
    }
    
    if ($files.Count -eq 0) {
        Write-Warning "No files found in $modName"
        return
    }
    
    Write-Host "Found $($files.Count) file(s) to include"
    
    # Create zip file preserving directory structure
    # We need to use .NET ZipFile class to preserve paths relative to mod directory
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $zip = [System.IO.Compression.ZipFile]::Open($tempZip, [System.IO.Compression.ZipArchiveMode]::Create)
    
    foreach ($file in $files) {
        # Get relative path from mod directory using PowerShell's built-in method
        $relativePath = [System.IO.Path]::GetRelativePath($ModDir, $file.FullName)
        # Normalize path separators for ZIP (use forward slashes)
        $relativePath = $relativePath.Replace('\', '/')
        [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $file.FullName, $relativePath)
    }
    
    $zip.Dispose()
    
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

