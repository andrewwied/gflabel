# Tech Icons Quick Reference

Complete list of all 36 available tech/AV icons with their IDs, names, and searchable tags.

## Connectivity Icons (17)

### USB
| ID | Name | Tags |
|---|---|---|
| `usb` | USB | usb, port, connector |
| `usb-port` | USB Port | usb, port, type-a |
| `usb-c-port` | USB-C Port | usb, usb-c, type-c, port |
| `usb-flash-drive` | USB Flash Drive | usb, flash, drive, storage |

**Usage:** `{icon(usb-c-port)}`, `{icon(usb port)}`, `{icon(type-c)}`

### HDMI
| ID | Name | Tags |
|---|---|---|
| `hdmi-port` | HDMI Port | hdmi, port, video |
| `video-input-hdmi` | HDMI Input | hdmi, input, video |

**Usage:** `{icon(hdmi-port)}`, `{icon(hdmi)}`

### Video Connectors
| ID | Name | Tags |
|---|---|---|
| `video` | Video Port | video, port, display, displayport, dvi |
| `video-box` | Video Box | video, box, display |
| `video-input-component` | Component Video | component, video, display, rca |
| `video-input-svideo` | S-Video | svideo, s-video, video |

**Usage:** `{icon(video)}` for DisplayPort/DVI, `{icon(displayport)}`, `{icon(component)}`

### Network
| ID | Name | Tags |
|---|---|---|
| `ethernet` | Ethernet | ethernet, network, lan, rj45 |
| `ethernet-cable` | Ethernet Cable | ethernet, cable, network, lan |
| `lan` | LAN | lan, network, ethernet |
| `wan` | WAN | wan, network |
| `wifi` | WiFi | wifi, wireless, network |

**Usage:** `{icon(ethernet)}`, `{icon(rj45)}`, `{icon(wifi)}`

### Other Connectors
| ID | Name | Tags |
|---|---|---|
| `serial-port` | Serial Port | serial, port, rs232, db9 |
| `cable-data` | Data Cable | cable, data, connector |
| `firewire` | FireWire | firewire, ieee1394, port |

**Usage:** `{icon(firewire)}`, `{icon(serial-port)}`, `{icon(db9)}`

## Audio Icons (7)

| ID | Name | Tags |
|---|---|---|
| `headphones` | Headphones | headphones, audio, sound |
| `speaker` | Speaker | speaker, audio, sound |
| `microphone` | Microphone | microphone, mic, audio |
| `audio-input-rca` | RCA Audio | rca, audio, connector |
| `audio-input-xlr` | XLR Audio | xlr, audio, connector, pro |
| `audio-input-stereo-minijack` | 3.5mm Audio Jack | 3.5mm, minijack, audio, headphone, jack |
| `toslink` | TOSLink | toslink, optical, audio, spdif |
| `audio-video` | Audio/Video | av, audio, video |

**Usage:** `{icon(toslink)}`, `{icon(xlr)}`, `{icon(3.5mm)}`, `{icon(optical)}`

## Display Icons (3)

| ID | Name | Tags |
|---|---|---|
| `monitor` | Monitor | monitor, display, screen |
| `television` | Television | tv, television, display |
| `projector` | Projector | projector, display |

**Usage:** `{icon(monitor)}`, `{icon(tv)}`, `{icon(projector)}`

## Storage Icons (4)

| ID | Name | Tags |
|---|---|---|
| `harddisk` | Hard Disk | hdd, hard disk, storage |
| `sd` | SD Card | sd, card, storage |
| `micro-sd` | MicroSD Card | microsd, micro-sd, card, storage |
| `disc` | Disc | disc, cd, dvd, bluray |

**Usage:** `{icon(micro-sd)}`, `{icon(microsd)}`, `{icon(sd)}`

## Power Icons (3)

| ID | Name | Tags |
|---|---|---|
| `power-plug` | Power Plug | power, plug, ac |
| `battery` | Battery | battery, power |
| `lightning-bolt` | Lightning Bolt | power, electricity, thunderbolt |

**Usage:** `{icon(power-plug)}`, `{icon(battery)}`, `{icon(thunderbolt)}`

## Usage Tips

### Exact Match (Recommended)
Use the exact ID from the table:
```bash
{icon(usb-c-port)}
{icon(hdmi-port)}
{icon(toslink)}
```

### Fuzzy Match with Tags
Any of the tags will match the icon:
```bash
{icon(optical)}      # Matches toslink
{icon(type-c)}       # Matches usb-c-port
{icon(displayport)}  # Matches video
{icon(rj45)}         # Matches ethernet
{icon(ieee1394)}     # Matches firewire
{icon(3.5mm)}        # Matches audio-input-stereo-minijack
```

### Multiple Matches
If your search matches multiple icons, you'll see a table of options:
```bash
{icon(usb)}  # Could match usb, usb-port, or usb-c-port
```

Output will show:
```
Could not decide on tech icon from specification "usb". Possible options:
    ID         Name       Category
    usb        USB        CONNECTIVITY
    usb-port   USB Port   CONNECTIVITY
    usb-c-port USB-C Port CONNECTIVITY
```

Refine by being more specific:
```bash
{icon(usb-c)}     # Now matches only usb-c-port
{icon(usb type-a)} # Now matches only usb-port
```

## Notes

- **DisplayPort/DVI**: Use `{icon(video)}` - MDI doesn't have separate icons for these
- **USB Micro/Mini/B**: MDI doesn't have specific variants; use `{icon(usb-port)}` for Type-A
- **Thunderbolt**: Use `{icon(lightning-bolt)}` as a generic symbol
- Some complex SVG icons may have rendering issues (noted in output as "invalid nesting")
