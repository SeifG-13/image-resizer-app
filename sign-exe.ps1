# Code signing script for ImageResizerPro.exe
# You'll need a code signing certificate (.pfx file)

param(
    [Parameter(Mandatory=$true)]
    [string]$CertificatePath,
    
    [Parameter(Mandatory=$true)]
    [string]$CertificatePassword,
    
    [string]$ExecutablePath = ".\dist\ImageResizerPro.exe"
)

Write-Host "Signing executable: $ExecutablePath"

# Sign the executable
signtool sign /f "$CertificatePath" /p "$CertificatePassword" /t http://timestamp.sectigo.com /v "$ExecutablePath"

if ($LASTEXITCODE -eq 0) {
    Write-Host "Successfully signed executable!" -ForegroundColor Green
    
    # Verify the signature
    Write-Host "Verifying signature..."
    signtool verify /pa "$ExecutablePath"
} else {
    Write-Host "Failed to sign executable. Error code: $LASTEXITCODE" -ForegroundColor Red
}