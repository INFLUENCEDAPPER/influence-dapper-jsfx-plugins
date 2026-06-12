# INFLUENCE DAPPER JSFX PLUGINS

**Professional JSFX Effects for REAPER**

A collection of MIDI-controlled synth plugins for REAPER featuring precision limiter design with peaks set at -0.3dB to avoid plugin clipping and deliver instant mix punch.

---

## 🎛️ Plugins Included

### 1. Bible Thumper
**"Kick, Snare & More (Limiter)"**

MIDI CONTROLLED SYNTH with MORE (Peaks set at -0.3dB to avoid PLUGIN Clipping and instant Mix Punch).

- **SNARE**: Toggle snare synthesis on/off
- **KICK**: Toggle kick synthesis on/off  
- **MORE**: Blend limiter intensity (0-100%)

**MIDI Control**: 
- Black keys trigger kick drum
- White keys trigger snare

---

### 2. Deep Bible Thumper
**"Thump, Rump & More (Limiter)"**

MIDI CONTROLLED SYNTH with MORE (Peaks set at -0.3dB to avoid PLUGIN Clipping and instant Mix Punch).

- **THUMP**: Toggle thump synthesis on/off (basketball-on-wood character)
- **RUMP**: Toggle rump synthesis on/off (palm-on-pork slap character)
- **MORE**: Blend limiter intensity (0-100%)

**MIDI Control**: 
- Black keys trigger rump
- White keys trigger thump
- Built-in band-limiting: 90 Hz HP (12 dB/oct) and 10 kHz LP (12 dB/oct)

---

## 🚀 Installation

### Option 1: Automatic Installation (Recommended)

**Requirements:** Python 3.6+

1. Download the installer script for your plugin:
   - `Bible_Thumper_Install.py`
   - `Deep_Bible_Thumper_Install.py`

2. Place the installer script **in the same folder** as the corresponding `.jsfx` file.

3. Run the installer:
   ```bash
   python Bible_Thumper_Install.py
   ```
   or
   ```bash
   python Deep_Bible_Thumper_Install.py
   ```

4. The script will:
   - Locate your REAPER Effects folder automatically
   - Copy the `.jsfx` file to `Effects/InfluenceDapper/`
   - Write metadata and tags for easy discovery

5. **In REAPER**: Open the FX browser → `JS` → `InfluenceDapper` → select your plugin

---

### Option 2: Manual Installation

**Windows:**
```
C:\Users\<YourUsername>\AppData\Roaming\REAPER\Effects\InfluenceDapper\
```

**macOS:**
```
~/Library/Application Support/REAPER/Effects/InfluenceDapper/
```

**Linux:**
```
~/.config/REAPER/Effects/InfluenceDapper/
```

1. Create the `InfluenceDapper` folder in your REAPER Effects directory (if it doesn't exist)
2. Copy the `.jsfx` files into this folder
3. Copy any `.metadata.json` files into the same folder
4. Restart REAPER or rescan the FX browser
5. Navigate to: `JS` → `InfluenceDapper` → select your plugin

---

## 📋 File Structure

```
influence-dapper-jsfx-plugins/
├── BibleThumper.jsfx
├── Bible_Thumper_Install.py
├── DeepBibleThumper.jsfx
├── Deep_Bible_Thumper_Install.py
├── README.md
├── LICENSE.md
└── media/
    ├── bible_thumper_preview.png
    └── deep_bible_thumper_preview.png
```

---

## 🎛️ Usage Tips

- **MIDI Input Required**: Both plugins respond to MIDI note input. Configure MIDI routing in REAPER's FX chain.
- **Limiter Performance**: The "MORE" slider controls how much the built-in limiter blends with your signal. Higher values = more limiting safety.
- **Peak Safety**: All peaks are hard-limited to -0.3dB to prevent digital clipping and maintain mix translation.
- **Instant Mix Punch**: The limiter design provides immediate transient control for tight, punchy mixes.

---

## ⚖️ License

Copyright © Influence Dapper, 2023–2026.

All plugins are licensed under **Creative Commons Attribution-NonCommercial 4.0 International (CC-NC-4.0 INTL)**.

**You are free to:**
- Use the plugins for personal and non-commercial projects
- Modify the source code for your own use
- Share and redistribute (with attribution)

**You may not:**
- Use these plugins for commercial purposes
- Sell or profit from these plugins
- Remove attribution or license notices

For full license terms, see `LICENSE.md`.

---

## 🔗 Links

- **Website**: https://influencedapper.com
- **Author**: INFLUENCEDAPPER.COM
- **License**: CC-NC-4.0 International

---

## 🛠️ Support & Issues

If you encounter issues:

1. Ensure REAPER has been opened at least once so the Effects folder exists
2. Verify the plugin files are in the correct REAPER Effects directory
3. Restart REAPER and rescan the FX browser
4. Check that your REAPER installation is up to date

---

**Enjoy your plugins!** 🎵
