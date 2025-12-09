# Build script for driver_id_names mod
# Uses locale/en_us/ path (confirmed working)

param()

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir
$ModDir = Join-Path $RootDir "mods\driver_id_names"
$DistDir = Join-Path $RootDir "dist"

# Create dist folder if it doesn't exist
New-Item -ItemType Directory -Path $DistDir -Force | Out-Null

$ManifestPath = Join-Path $ModDir "manifest.sii"
$DescPath = Join-Path $ModDir "desc.txt"
$IconPath = Join-Path $ModDir "mod_icon.jpg"
$DriverNamesPath = Join-Path $ModDir "locale\en_us\driver_names.sii"

# Load .NET compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

Write-Host "Building driver_id_names mod..."

$zipPath = Join-Path $DistDir "driver_id_names.scs"
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }

$zip = [System.IO.Compression.ZipFile]::Open($zipPath, [System.IO.Compression.ZipArchiveMode]::Create)
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $ManifestPath, "manifest.sii") | Out-Null
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $DescPath, "desc.txt") | Out-Null
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $IconPath, "mod_icon.jpg") | Out-Null
[System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $DriverNamesPath, "locale/en_us/driver_names.sii") | Out-Null
$zip.Dispose()

Write-Host "Created: $zipPath"
Write-Host ""
Write-Host "Structure inside .scs:"
Write-Host "  - manifest.sii"
Write-Host "  - desc.txt"
Write-Host "  - mod_icon.jpg"
Write-Host "  - locale/en_us/driver_names.sii"
Write-Host ""
Write-Host "Copy to: Documents\Euro Truck Simulator 2\mod\"

