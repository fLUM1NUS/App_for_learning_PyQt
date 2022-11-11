# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/darte/PycharmProjects/App_for_learning_PyQt/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/darte/PycharmProjects/App_for_learning_PyQt/res', 'res/'), ('C:/Users/darte/PycharmProjects/App_for_learning_PyQt/lessons', 'lessons/'), ('C:/Users/darte/PycharmProjects/App_for_learning_PyQt/pdf_js', 'pdf_js/'), ('C:/Users/darte/PycharmProjects/App_for_learning_PyQt/UI', 'UI/'), ('C:/Users/darte/PycharmProjects/App_for_learning_PyQt/sc.txt', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PyQt Learner',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\darte\\PycharmProjects\\App_for_learning_PyQt\\res\\App_logo-256.png'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PyQt Learner',
)
