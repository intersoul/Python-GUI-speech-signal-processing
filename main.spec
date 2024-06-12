# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=['bianfu.py', 'biansu.py', 'end_detection.py', 'enframe.py', 'gongzhenfengguji.py', 'gongzhenfenggujihanhu.py', 'jiyinpinlv.py', 'lpc.py', 'pinyutexing.py', 'pitch_detection.py', 'shiyutexing.py', 'soundBase.py', 'timefeature.py', 'windows.py', 'yuputu.py'],
    binaries=[],
    datas=[],
    hiddenimports=['tkinter', 'librosa', 'sounddevice', 'threading', 'PIL', 'os', 'numpy', 'matplotlib', 'soundfile'],
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
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
