# Distribution Guide for ImageResizerPro

## Overview
This guide covers how to safely build, sign, and distribute the ImageResizerPro executable.

## Current Build Information
- **Executable:** `dist/ImageResizerPro.exe`
- **Size:** ~27.5 MB
- **Built with:** PyInstaller
- **Target:** Windows 64-bit

## Quick Distribution Checklist

### For Each Release:
1. ✅ Build the executable: `pyinstaller ImageResizerPro.spec`
2. ⚠️ **Sign the executable** (see Code Signing section)
3. ✅ Generate checksums: `powershell -File generate-checksums.ps1`
4. ⚠️ Test on clean Windows system
5. ⚠️ Create GitHub release or upload to distribution platform

## Code Signing (Recommended)

### Why Sign?
- Prevents Windows security warnings
- Establishes trust and authenticity
- Required for Microsoft Store distribution

### How to Sign:
1. **Get a Code Signing Certificate:**
   - Purchase from: DigiCert, Sectigo, or other trusted CA
   - Cost: ~$200-400/year
   - Alternatives: Self-signed certificates (less trusted)

2. **Sign the executable:**
   ```powershell
   .\sign-exe.ps1 -CertificatePath "path\to\certificate.pfx" -CertificatePassword "your_password"
   ```

### Self-Signed Certificate (Development Only):
```powershell
# Create self-signed certificate (for testing only)
New-SelfSignedCertificate -Subject "CN=YourCompany" -Type CodeSigning -CertStoreLocation Cert:\CurrentUser\My
```

## Distribution Methods

### 1. GitHub Releases (Recommended)
- **Setup:** Push a version tag to trigger automatic release
- **Benefits:** Free, automatic checksums, version history
- **Usage:** `git tag v1.0.0 && git push origin v1.0.0`

### 2. Direct Download
- Host on your website with HTTPS
- Always provide checksums alongside download
- Include clear installation instructions

### 3. Package Managers
- **Chocolatey:** For Windows package management
- **Winget:** Microsoft's package manager
- **Scoop:** Alternative Windows package manager

## Security Best Practices

### Before Distribution:
1. **Scan for malware:** Use Windows Defender or VirusTotal
2. **Test on clean systems:** Ensure no missing dependencies
3. **Verify checksums:** Always match generated checksums
4. **Document requirements:** List Windows version compatibility

### File Integrity:
- Always generate and publish checksums
- Use SHA256 as primary hash (most secure)
- Include file size in release notes
- Provide verification instructions

## Release Process

### Automated (GitHub Actions):
1. Create version tag: `git tag v1.0.0`
2. Push tag: `git push origin v1.0.0`
3. GitHub Actions automatically builds and creates release

### Manual Process:
1. Build executable: `pyinstaller ImageResizerPro.spec`
2. Sign executable (if certificate available)
3. Generate checksums: `powershell -File generate-checksums.ps1`
4. Create release on GitHub with files:
   - `ImageResizerPro.exe`
   - `checksums.txt`
   - Release notes

## Troubleshooting Common Issues

### "Windows protected your PC" Warning:
- **Cause:** Unsigned executable
- **Solution:** Code signing certificate
- **Workaround:** Users can click "More info" → "Run anyway"

### Antivirus False Positives:
- **Common with:** PyInstaller executables
- **Submit to:** VirusTotal, vendor whitelisting
- **Prevention:** Code signing reduces false positives

### Large File Size:
- **Current size:** ~27.5 MB
- **Optimization:** Consider excluding unused modules in .spec file
- **Alternative:** Create installer instead of single executable

## Distribution Platforms

### Free Options:
- GitHub Releases
- SourceForge
- Your own website

### Commercial Options:
- Microsoft Store ($19 one-time fee)
- Software distribution networks
- Download portals (often require fees)

## Legal Considerations
- Include proper licensing information
- Consider privacy policy for data collection
- Comply with export regulations if applicable
- Include disclaimer about Windows security warnings for unsigned software

---

## Quick Commands Reference

```powershell
# Build executable
pyinstaller ImageResizerPro.spec

# Generate checksums
.\generate-checksums.ps1

# Sign executable (with certificate)
.\sign-exe.ps1 -CertificatePath "cert.pfx" -CertificatePassword "password"

# Create GitHub release tag
git tag v1.0.0
git push origin v1.0.0
```