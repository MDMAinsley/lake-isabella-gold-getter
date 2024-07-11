# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['completer.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

a.datas += [('sounds\\finished.mp3','C:\\Users\\MDMAinsley\\OneDrive\\git-projects\\python-projects\\LakeIsabella\\sounds\\finished.mp3', "DATA")]
a.datas += [('sounds\\finished1.mp3','C:\\Users\\MDMAinsley\\OneDrive\\git-projects\\python-projects\\LakeIsabella\\sounds\\finished1.mp3', "DATA")]
a.datas += [('sounds\\finished2.mp3','C:\\Users\\MDMAinsley\\OneDrive\\git-projects\\python-projects\\LakeIsabella\\sounds\\finished2.mp3', "DATA")]
a.datas += [('sounds\\finished3.mp3','C:\\Users\\MDMAinsley\\OneDrive\\git-projects\\python-projects\\LakeIsabella\\sounds\\finished3.mp3', "DATA")]
a.datas += [('sounds\\finished4.mp3','C:\\Users\\MDMAinsley\\OneDrive\\git-projects\\python-projects\\LakeIsabella\\sounds\\finished4.mp3', "DATA")]

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Lake Isabella Gold Getter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['logo.ico'],
)
