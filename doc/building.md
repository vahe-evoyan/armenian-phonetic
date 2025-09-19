## Build and packaging guide

### Prerequisites

- macOS with Xcode Command Line Tools (for `iconutil`)
- Python 3.12+ (managed by `pyenv` via `.python-version`)
- Poetry (to install Python deps and run tools)

---

### 1) Install dependencies

```sh
poetry install
```

This installs `dmgbuild` (Python) and any other Python dependencies declared in `pyproject.toml`.

---

### 2) Build the DMG with dmgbuild (recommended)

`settings.py` defines the configurations for the DMG (volume name, background, icon positions, etc.).

```sh
poetry run dmgbuild -s settings.py 'Armenian Phonetic' ArmenianPhonetic.dmg
```

This produces `ArmenianPhonetic.dmg` in the project root.

---

### 3) Generate ICNS files from an .iconset (Apple toolchain)

If you need to (re)generate the ICNS assets inside the bundle, make sure there are correctly sized PNGs inside the iconset folder (must end with `.iconset`). The canonical names and pixel sizes are:

- `icon_16x16.png` (16x16)
- `icon_16x16@2x.png` (32x32)
- `icon_32x32.png` (32x32)
- `icon_32x32@2x.png` (64x64)
- `icon_128x128.png` (128x128)
- `icon_128x128@2x.png` (256x256)
- `icon_256x256.png` (256x256)
- `icon_256x256@2x.png` (512x512)
- `icon_512x512.png` (512x512)
- `icon_512x512@2x.png` (1024x1024)

Quick size checks (optional):

```sh
sips -g pixelWidth -g pixelHeight './resources/Armenian Phonetic.iconset/icon_128x128.png'
```

Build each target ICNS into the bundle resources (note the quoted paths with spaces):

```sh
iconutil -c icns './resources/Armenian Phonetic.iconset' -o 'ArmenianPhonetic.bundle/Contents/Resources/Armenian Phonetic.icns'
iconutil -c icns './resources/Armenian Phonetic.iconset' -o 'ArmenianPhonetic.bundle/Contents/Resources/Armenian Phonetic With English.icns'
iconutil -c icns './resources/Armenian Phonetic.iconset' -o 'ArmenianPhonetic.bundle/Contents/Resources/Armenian Phonetic (KDWin).icns'
iconutil -c icns './resources/Armenian Phonetic.iconset' -o 'ArmenianPhonetic.bundle/Contents/Resources/Armenian Phonetic (KDWin) With English.icns'
```

Notes:
- PNGs may be any shape (transparency supported), but the canvas must be square and exactly the sizes listed above.
- Use standard 8‑bit RGBA, sRGB. Avoid CMYK/16‑bit images.


### Troubleshooting

- `iconutil: Failed to generate ICNS.`
  - Ensure filenames and pixel sizes match Apple’s expectations (see list above).
  - Verify sizes with `sips -g pixelWidth -g pixelHeight file.png`.
  - Make sure the folder name ends with `.iconset`.
  - Quote paths that contain spaces.

- DMG icons or layout not matching
  - Re-check coordinates in `settings.py` under `icon_locations` and `window_rect`.
  - Ensure `background` and `icon` files referenced in `settings.py` exist.

- Non-rectangular icons
  - Transparent PNGs are fine; only square canvas and exact pixel sizes matter.

---

### Outputs

- DMG: `ArmenianPhonetic.dmg`
- ICNS (inside bundle):
  - `ArmenianPhonetic.bundle/Contents/Resources/Armenian Phonetic.icns`
  - `ArmenianPhonetic.bundle/Contents/Resources/Armenian Phonetic With English.icns`
  - `ArmenianPhonetic.bundle/Contents/Resources/Armenian Phonetic (KDWin).icns`
  - `ArmenianPhonetic.bundle/Contents/Resources/Armenian Phonetic (KDWin) With English.icns`
