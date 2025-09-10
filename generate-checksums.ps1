# Generate checksums for ImageResizerPro.exe
param(
    [string]$ExecutablePath = ".\dist\ImageResizerPro.exe",
    [string]$OutputFile = ".\checksums.txt"
)

if (Test-Path $ExecutablePath) {
    Write-Host "Generating checksums for: $ExecutablePath"
    
    # Get file info
    $fileInfo = Get-Item $ExecutablePath
    $fileName = $fileInfo.Name
    $fileSize = $fileInfo.Length
    
    # Generate checksums
    $md5Hash = Get-FileHash -Path $ExecutablePath -Algorithm MD5
    $sha1Hash = Get-FileHash -Path $ExecutablePath -Algorithm SHA1
    $sha256Hash = Get-FileHash -Path $ExecutablePath -Algorithm SHA256
    
    # Create checksum file
    $checksumContent = @"
# Checksums for $fileName
# File size: $fileSize bytes
# Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss UTC')

## SHA256
$($sha256Hash.Hash.ToLower())  $fileName

## SHA1
$($sha1Hash.Hash.ToLower())  $fileName

## MD5
$($md5Hash.Hash.ToLower())  $fileName

## Verification Instructions
To verify the integrity of your download:

### Windows (PowerShell):
```powershell
Get-FileHash -Path "$fileName" -Algorithm SHA256
```

### Linux/macOS:
```bash
sha256sum "$fileName"
```

The output should match the SHA256 hash above.
"@

    $checksumContent | Out-File -FilePath $OutputFile -Encoding UTF8
    Write-Host "Checksums saved to: $OutputFile" -ForegroundColor Green
    
    # Display checksums
    Write-Host "`nChecksums:"
    Write-Host "SHA256: $($sha256Hash.Hash.ToLower())" -ForegroundColor Yellow
    Write-Host "SHA1:   $($sha1Hash.Hash.ToLower())" -ForegroundColor Yellow
    Write-Host "MD5:    $($md5Hash.Hash.ToLower())" -ForegroundColor Yellow
} else {
    Write-Host "Executable not found at: $ExecutablePath" -ForegroundColor Red
}