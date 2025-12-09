# Build 3 variants of driver_id_names mod to test different paths
param()

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir
$ModDir = Join-Path $RootDir "mods\driver_id_names"
$DistDir = Join-Path $RootDir "dist"

# Create dist folder if it doesn't exist
New-Item -ItemType Directory -Path $DistDir -Force | Out-Null

$ManifestPath = Join-Path $ModDir "manifest.sii"
$DescPath = Join-Path $ModDir "desc.txt"

# Load .NET compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

Write-Host "Building 3 variants of driver_id_names mod..."
Write-Host ""

# === BUILD 1: universal/locale/en_us/ ===
Write-Host "Building: driver_id_names_universal.scs"
$zipPath = Join-Path $DistDir "driver_id_names_universal.scs"
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
$zip = [System.IO.Compression.ZipFile]::Open($zipPath, [System.IO.Compression.ZipArchiveMode]::Create)
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $ManifestPath, "manifest.sii") | Out-Null
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $DescPath, "desc.txt") | Out-Null
$driverFile = Join-Path $ModDir "universal\locale\en_us\driver_names.sii"
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $driverFile, "universal/locale/en_us/driver_names.sii") | Out-Null
$zip.Dispose()
Write-Host "  Created: $zipPath"

# === BUILD 2: def/locale/en_us/ ===
Write-Host "Building: driver_id_names_def.scs"
$zipPath = Join-Path $DistDir "driver_id_names_def.scs"
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
$zip = [System.IO.Compression.ZipFile]::Open($zipPath, [System.IO.Compression.ZipArchiveMode]::Create)
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $ManifestPath, "manifest.sii") | Out-Null
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $DescPath, "desc.txt") | Out-Null
$driverFile = Join-Path $ModDir "def\locale\en_us\driver_names.sii"
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $driverFile, "def/locale/en_us/driver_names.sii") | Out-Null
$zip.Dispose()
Write-Host "  Created: $zipPath"

# === BUILD 3: locale/en_us/ ===
Write-Host "Building: driver_id_names_locale.scs"
$zipPath = Join-Path $DistDir "driver_id_names_locale.scs"
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
$zip = [System.IO.Compression.ZipFile]::Open($zipPath, [System.IO.Compression.ZipArchiveMode]::Create)
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $ManifestPath, "manifest.sii") | Out-Null
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $DescPath, "desc.txt") | Out-Null
$driverFile = Join-Path $ModDir "locale\en_us\driver_names.sii"
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $driverFile, "locale/en_us/driver_names.sii") | Out-Null
$zip.Dispose()
Write-Host "  Created: $zipPath"

Write-Host ""
Write-Host "Done! Built 3 variants:"
Write-Host "  1. driver_id_names_universal.scs - uses universal/locale/en_us/"
Write-Host "  2. driver_id_names_def.scs       - uses def/locale/en_us/"
Write-Host "  3. driver_id_names_locale.scs    - uses locale/en_us/"
Write-Host ""
Write-Host "Test each one separately (only enable ONE at a time in Mod Manager)"
Write-Host "Copy to: Documents\Euro Truck Simulator 2\mod\"

