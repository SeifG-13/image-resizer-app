# ImageResizerPro

A modern, user-friendly Windows application for resizing images with a sleek dark UI. Built with Python and Tkinter, packaged as a portable executable.

## 🚀 Features

- **Modern Dark UI** - Sleek, professional interface with Microsoft-inspired design
- **Batch Processing** - Resize multiple images at once
- **Multiple Formats** - Support for PNG, JPG, JPEG, GIF, BMP, TIFF
- **Aspect Ratio Options** - Keep original proportions or set custom dimensions  
- **Quality Control** - Adjustable JPEG quality settings
- **Portable** - No installation required, runs directly from .exe file
- **Progress Tracking** - Visual progress bar for batch operations

## 📥 Download

**[📁 Download ImageResizerPro.exe](https://github.com/SeifG-13/image-resizer-app/releases/latest)**

- **No installation needed** - Just download and double-click to run
- **Size**: ~27 MB
- **Platform**: Windows 10/11 (64-bit)

## 🖥️ Screenshots

*Professional dark theme with intuitive controls*

## ⚡ Quick Start

1. **Download** `ImageResizerPro.exe` from the releases page
2. **Run** the executable (Windows may show a security warning - click "More info" → "Run anyway")
3. **Select** your input images or folder
4. **Choose** output location and settings
5. **Resize** and enjoy your optimized images!

## 🎯 How to Use

### Single Image Mode
1. Click **"Browse Input"** to select an image
2. Set desired **width** and **height**
3. Choose **output folder**
4. Click **"Resize Images"**

### Batch Mode
1. Click **"Browse Input"** and select a folder with images
2. Configure resize settings
3. Set output destination
4. Process all images with one click

### Settings
- **Maintain Aspect Ratio**: Keep original proportions
- **JPEG Quality**: Adjust compression (1-100)
- **Output Format**: Choose between different image formats

## 🔧 System Requirements

- **OS**: Windows 10 or later
- **RAM**: 2GB+ recommended
- **Storage**: 50MB free space
- **No additional software required**

## 🛡️ Security

- **Portable Application**: No system modifications or registry changes
- **Local Processing**: All image processing happens on your computer
- **No Internet Required**: Works completely offline
- **Open Source**: Source code available for review

## 🐛 Troubleshooting

### "Windows protected your PC" warning
This appears because the executable isn't code-signed. It's safe to run:
1. Click **"More info"**
2. Click **"Run anyway"**

### Large file processing
For very large images or batches:
- Close other applications to free up RAM
- Process smaller batches if needed
- Ensure sufficient disk space in output folder

## 🔄 Version History

See [Releases] (https://github.com/SeifG-13/image-resizer-app/releases) for changelog and download links.

## 👨‍💻 Development

Built with:
- **Python 3.11**
- **Tkinter** (GUI framework)
- **Pillow** (PIL - image processing)
- **PyInstaller** (executable packaging)

### Building from Source
```bash
# Clone repository
git clone https://github.com/SeifG-13/image-resizer-app.git
cd image-resizer-app

# Install dependencies
pip install pillow pyinstaller

# Build executable
pyinstaller ImageResizerPro.spec
```

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🤝 Contributing

Issues and feature requests are welcome! Feel free to open an issue or submit a pull request.

## 📞 Support

Having problems? 
- Check the [Issues](https://github.com/SeifG-13/image-resizer-app/issues) page
- Create a new issue with your problem description

---

**Made with ❤️ for the community**
