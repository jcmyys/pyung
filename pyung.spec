# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:/_Projects/pyung/pyung.py'],
    pathex=[],
    binaries=[],
    datas=[('D:/_Python/Python/tcl/tcl8.6', '_tcl_data'), ('D:/_Python/Python/tcl/tk8.6', '_tk_data')],
    hiddenimports=[],
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
    name='pyung',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\_Projects\\pyung\\pyung.ico'],
)
