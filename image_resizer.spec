# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['image_resizer.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Add any additional files here if needed
        # ('icon.ico', '.'),  # Uncomment if you have an icon file
    ],
    hiddenimports=[
        'PIL._tkinter_finder',
        'PIL._imaging',
        'PIL.Image',
        'PIL.ImageTk',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ImageResizerPro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',  # Make sure you have this file, or remove this line
    version_info={
        'version': (1, 0, 0, 0),
        'file_version': (1, 0, 0, 0),
        'product_version': (1, 0, 0, 0),
        'file_description': 'Image Resizer Pro - Easy image resizing tool',
        'product_name': 'Image Resizer Pro',
        'company_name': 'Your Name',
        'legal_copyright': '© 2025 Your Name',
    }
)