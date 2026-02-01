# Tech Icons Implementation Summary

## What Was Added

I've successfully added computer and audio-visual technology icon support to GFLabel using Material Design Icons (MDI).

## Files Created/Modified

### New Files Created:
1. **`util/download_mdi_icons.py`** - Script to download and package MDI icons
2. **`src/gflabel/resources/mdi-tech-icons.zip`** - Package containing 24 curated tech icons
3. **`src/gflabel/resources/LICENSE_mdi_icons`** - License file for Material Design Icons
4. **`TECH_ICONS_USAGE.md`** - Documentation on how to use tech icons

### Files Modified:
1. **`src/gflabel/fragments.py`** - Added tech icon fragment support:
   - `tech_icons_manifest()` - Loads the MDI icon manifest
   - `_match_tech_icon_with_selectors()` - Fuzzy matching for tech icons
   - `_tech_icon_fragment` - Fragment class registered as `{icon(...)}`, `{tech(...)}`, `{techicon(...)}`

2. **`src/gflabel/cli.py`** - Added CLI support:
   - `ListTechIconsAction` - Action class to list available tech icons
   - `--list-tech-icons` argument - CLI flag to display all tech icons

## Available Icons (36 total)

### Connectivity (17 icons)
- **USB**: usb, usb-port, usb-c-port, usb-flash-drive
- **HDMI**: hdmi-port, video-input-hdmi
- **Video**: video (DisplayPort/DVI), video-box, video-input-component, video-input-svideo
- **Network**: ethernet, ethernet-cable, lan, wan, wifi
- **Other**: serial-port, cable-data, firewire

### Display (3 icons)
- monitor, television, projector

### Audio (7 icons)
- headphones, speaker, microphone
- audio-input-rca, audio-input-xlr, audio-input-stereo-minijack
- toslink, audio-video

### Storage (4 icons)
- harddisk, sd, micro-sd, disc

### Power (3 icons)
- power-plug, battery, lightning-bolt

## Usage Examples

### List Available Icons
```bash
gflabel --list-tech-icons
```

### Create Labels with Icons

**USB-C and HDMI:**
```bash
gflabel pred "{icon(usb-c-port)} USB-C" "{icon(hdmi-port)} HDMI" -o ports.stl
```

**Network Setup:**
```bash
gflabel pred "{icon(ethernet)} LAN" "{icon(wifi)} WiFi" -o network.stl
```

**Audio Equipment:**
```bash
gflabel pred "{icon(headphones)} Headphones" "{icon(microphone)} Mic" -o audio.stl
```

**Optical/Pro Audio:**
```bash
gflabel pred "{icon(toslink)} Optical" "{icon(audio-input-xlr)} XLR" -o audio-pro.stl
```

**Legacy/Pro Connectors:**
```bash
gflabel pred "{icon(firewire)} FireWire" "{icon(serial-port)} Serial" -o legacy.stl
```

**DisplayPort/Video:**
```bash
gflabel pred "{icon(video)} DisplayPort" "{icon(video-input-component)} Component" -o video.stl
```

## Library Information

**Icon Library:** Material Design Icons (MDI)
- Source: https://github.com/Templarian/MaterialDesign
- License: Apache License 2.0
- Copyright: © 2014-2024 Austin Andrews & Google & Pictogrammers contributors

## How It Works

1. The icon downloader script (`download_mdi_icons.py`) fetches SVG files from the MDI repository
2. Icons are packaged into a ZIP file with a manifest (similar to the existing electronic symbols)
3. The fragment system uses the same pattern-matching approach as electronic symbols
4. Icons support exact ID matching, exact name matching, and fuzzy matching with tags
5. Icons are rendered as SVG and scaled to match the label height

## Testing

Generated test files:
- `usb-hdmi-test.stl` - USB-C and HDMI labels
- `tech-icons-demo.stl` - Multiple tech icon labels  
- `toslink-firewire.stl` - TOSLink and FireWire labels
- `displayport-microsd.stl` - DisplayPort and MicroSD labels

## Installation Notes

To use this functionality:
1. The changes need to be in the gflabel package
2. Run the download script if you need to regenerate icons: `python util/download_mdi_icons.py`
3. Install/reinstall gflabel: `pip install -e .` from the repo root
