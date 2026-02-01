# Using Tech Icons in GFLabel

GFLabel now supports computer and audio-visual technology icons through Material Design Icons!

## Available Icons

You can list all available tech icons with:

```bash
gflabel --list-tech-icons
```

This includes icons for:
- **USB** (USB, USB Port, USB-C Port, USB Flash Drive)
- **HDMI** (HDMI Port, HDMI Input)
- **Video** (Video Port/DisplayPort, Component Video, S-Video)
- **Display** (Monitor, Television, Projector)
- **Audio** (Headphones, Speaker, Microphone, RCA Audio, XLR Audio, 3.5mm Jack, TOSLink Optical)
- **Network** (Ethernet, Ethernet Cable, LAN, WAN, WiFi)
- **Other Ports** (Serial Port, FireWire, Data Cable)
- **Storage** (Hard Disk, SD Card, MicroSD Card, Disc)
- **Power** (Power Plug, Battery, Lightning Bolt)

## Usage

Tech icons are added using the `{icon(...)}`, `{tech(...)}`, or `{techicon(...)}` fragment:

### Basic Examples

**USB-C Label:**
```bash
gflabel pred "{icon(usb-c-port)} USB-C" -o usb-c.stl
```

**HDMI Label:**
```bash
gflabel pred "{icon(hdmi-port)} HDMI" -o hdmi.stl
```

**Multiple Icons:**
```bash
gflabel pred "{icon(usb-c-port)} USB-C" "{icon(hdmi-port)} HDMI" -o ports.stl
```

### Matching Icons

You can specify icons in three ways:

1. **Exact ID** (recommended): Use the exact ID from `--list-tech-icons`
   ```bash
   {icon(usb-c-port)}
   {icon(hdmi-port)}
   {icon(ethernet)}
   ```

2. **Exact Name**: Use the full name
   ```bash
   {icon(USB-C Port)}
   {icon(HDMI Port)}
   ```

3. **Fuzzy Matching**: Use keywords (may match multiple icons)
   ```bash
   {icon(usb port)}      # Matches USB Port and USB-C Port
   {icon(wifi)}          # Matches WiFi
   {icon(audio)}         # May match multiple audio icons
   ```

If fuzzy matching finds multiple icons, you'll see a table of options to help you refine your choice.

### Complex Examples

**Cable Organization:**
```bash
gflabel pred "{icon(usb-port)}{...}USB" "{icon(hdmi-port)}{...}HDMI" "{icon(ethernet)}{...}ETH" -o cables.stl
```

**Audio Equipment:**
```bash
gflabel pred "{icon(headphones)} Headphones" "{icon(microphone)} Mic" "{icon(speaker)} Speaker" -o audio.stl
```

**Storage Labels:**
```bash
gflabel predbox -w=5 "{icon(harddisk)} HDD\\nBackups" -o storage.stl
```

**Network Ports:**
```bash
gflabel pred "{icon(ethernet)} LAN 1" "{icon(ethernet)} LAN 2" "{icon(wifi)} WiFi" -o network.stl
```

**Optical Audio:**
```bash
gflabel pred "{icon(toslink)} Optical" "{icon(audio-input-xlr)} XLR" -o audio-pro.stl
```

**Legacy/Pro Connectors:**
```bash
gflabel pred "{icon(firewire)} FireWire" "{icon(serial-port)} Serial" -o legacy.stl
```

**Video Ports (DisplayPort/DVI):**
```bash
gflabel pred "{icon(video)} DP/DVI" "{icon(video-input-component)} Component" -o video.stl
```

## Combining with Other Fragments

Tech icons work with all other gflabel features:

**With Columns:**
```bash
gflabel predbox -w=5 "{icon(usb-c-port)}{|}USB-C\\nType C{|}{icon(hdmi-port)}{|}HDMI\\nVideo" -o multi.stl
```

**With Alignment:**
```bash
gflabel pred "{<}{icon(usb-port)} USB" -o left-aligned.stl
```

**With Spacing:**
```bash
gflabel pred "{icon(ethernet)}{2}Network" -o spaced.stl
```

## Icon Attribution

Tech icons are from **Material Design Icons** (https://github.com/Templarian/MaterialDesign)
Licensed under Apache License 2.0
Copyright © 2014-2024 Austin Andrews & Google & Pictogrammers contributors
