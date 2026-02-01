#!/usr/bin/env python3
"""
Download Material Design Icons (MDI) for computer/audio-visual use.

This script downloads a curated set of tech/AV icons from the Material Design Icons
repository and packages them for use with gflabel.
"""
from __future__ import annotations

import json
import zipfile
from pathlib import Path
from urllib.request import urlopen

# Base URL for MDI SVG files (using jsdelivr CDN for stable access)
MDI_BASE_URL = "https://raw.githubusercontent.com/Templarian/MaterialDesign/master/svg/"

# Curated list of computer/AV icons to include
ICONS = {
    # USB related
    "usb": {"name": "USB", "category": "CONNECTIVITY", "tags": ["usb", "port", "connector"]},
    "usb-port": {"name": "USB Port", "category": "CONNECTIVITY", "tags": ["usb", "port", "type-a"]},
    "usb-c-port": {"name": "USB-C Port", "category": "CONNECTIVITY", "tags": ["usb", "usb-c", "type-c", "port"]},
    "usb-flash-drive": {"name": "USB Flash Drive", "category": "CONNECTIVITY", "tags": ["usb", "flash", "drive", "storage"]},
    
    # HDMI and video
    "hdmi-port": {"name": "HDMI Port", "category": "CONNECTIVITY", "tags": ["hdmi", "port", "video"]},
    "video-input-hdmi": {"name": "HDMI Input", "category": "CONNECTIVITY", "tags": ["hdmi", "input", "video"]},
    
    # Display ports and video connectors
    "monitor": {"name": "Monitor", "category": "DISPLAY", "tags": ["monitor", "display", "screen"]},
    "television": {"name": "Television", "category": "DISPLAY", "tags": ["tv", "television", "display"]},
    "projector": {"name": "Projector", "category": "DISPLAY", "tags": ["projector", "display"]},
    "video": {"name": "Video Port", "category": "CONNECTIVITY", "tags": ["video", "port", "display", "displayport", "dvi"]},
    "video-box": {"name": "Video Box", "category": "CONNECTIVITY", "tags": ["video", "box", "display"]},
    "video-input-component": {"name": "Component Video", "category": "CONNECTIVITY", "tags": ["component", "video", "display", "rca"]},
    "video-input-svideo": {"name": "S-Video", "category": "CONNECTIVITY", "tags": ["svideo", "s-video", "video"]},
    
    # Audio connectors
    "headphones": {"name": "Headphones", "category": "AUDIO", "tags": ["headphones", "audio", "sound"]},
    "speaker": {"name": "Speaker", "category": "AUDIO", "tags": ["speaker", "audio", "sound"]},
    "microphone": {"name": "Microphone", "category": "AUDIO", "tags": ["microphone", "mic", "audio"]},
    "audio-input-rca": {"name": "RCA Audio", "category": "AUDIO", "tags": ["rca", "audio", "connector"]},
    "audio-input-xlr": {"name": "XLR Audio", "category": "AUDIO", "tags": ["xlr", "audio", "connector", "pro"]},
    "audio-input-stereo-minijack": {"name": "3.5mm Audio Jack", "category": "AUDIO", "tags": ["3.5mm", "minijack", "audio", "headphone", "jack"]},
    "audio-video": {"name": "Audio/Video", "category": "AUDIO", "tags": ["av", "audio", "video"]},
    "toslink": {"name": "TOSLink", "category": "AUDIO", "tags": ["toslink", "optical", "audio", "spdif"]},
    
    # Network
    "ethernet": {"name": "Ethernet", "category": "CONNECTIVITY", "tags": ["ethernet", "network", "lan", "rj45"]},
    "ethernet-cable": {"name": "Ethernet Cable", "category": "CONNECTIVITY", "tags": ["ethernet", "cable", "network", "lan"]},
    "lan": {"name": "LAN", "category": "CONNECTIVITY", "tags": ["lan", "network", "ethernet"]},
    "wan": {"name": "WAN", "category": "CONNECTIVITY", "tags": ["wan", "network"]},
    "wifi": {"name": "WiFi", "category": "CONNECTIVITY", "tags": ["wifi", "wireless", "network"]},
    
    # Other computer connectors
    "serial-port": {"name": "Serial Port", "category": "CONNECTIVITY", "tags": ["serial", "port", "rs232", "db9"]},
    "cable-data": {"name": "Data Cable", "category": "CONNECTIVITY", "tags": ["cable", "data", "connector"]},
    "firewire": {"name": "FireWire", "category": "CONNECTIVITY", "tags": ["firewire", "ieee1394", "port"]},
    
    # Storage
    "harddisk": {"name": "Hard Disk", "category": "STORAGE", "tags": ["hdd", "hard disk", "storage"]},
    "sd": {"name": "SD Card", "category": "STORAGE", "tags": ["sd", "card", "storage"]},
    "micro-sd": {"name": "MicroSD Card", "category": "STORAGE", "tags": ["microsd", "micro-sd", "card", "storage"]},
    "disc": {"name": "Disc", "category": "STORAGE", "tags": ["disc", "cd", "dvd", "bluray"]},
    
    # Power
    "power-plug": {"name": "Power Plug", "category": "POWER", "tags": ["power", "plug", "ac"]},
    "battery": {"name": "Battery", "category": "POWER", "tags": ["battery", "power"]},
    "lightning-bolt": {"name": "Lightning Bolt", "category": "POWER", "tags": ["power", "electricity", "thunderbolt"]},
}


def download_icon(icon_id: str) -> str:
    """Download an icon SVG from MDI repository."""
    url = f"{MDI_BASE_URL}{icon_id}.svg"
    print(f"Downloading {icon_id}...")
    try:
        with urlopen(url) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"  Warning: Could not download {icon_id}: {e}")
        return None


def main():
    """Main function to download icons and create package."""
    output_dir = Path(__file__).parent.parent / "src" / "gflabel" / "resources"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    temp_dir = Path(__file__).parent / "temp_mdi_icons"
    temp_dir.mkdir(exist_ok=True)
    svg_dir = temp_dir / "SVG"
    svg_dir.mkdir(exist_ok=True)
    
    manifest = []
    downloaded_count = 0
    
    for icon_id, metadata in ICONS.items():
        svg_content = download_icon(icon_id)
        if svg_content:
            # Save SVG file
            svg_path = svg_dir / f"{icon_id}.svg"
            svg_path.write_text(svg_content, encoding="utf-8")
            
            # Add to manifest
            manifest.append({
                "id": icon_id,
                "name": metadata["name"],
                "category": metadata["category"],
                "standard": "MDI",
                "filename": icon_id,
                "tags": metadata["tags"],
            })
            downloaded_count += 1
    
    print(f"\nDownloaded {downloaded_count} icons")
    
    # Write manifest
    manifest_path = temp_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Created manifest with {len(manifest)} icons")
    
    # Create zip file
    zip_path = output_dir / "mdi-tech-icons.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(manifest_path, "manifest.json")
        for svg_file in svg_dir.glob("*.svg"):
            zf.write(svg_file, f"SVG/{svg_file.name}")
    
    print(f"\nCreated {zip_path}")
    print(f"Package contains {len(manifest)} icons")
    
    # Cleanup temp directory
    import shutil
    shutil.rmtree(temp_dir)
    print("Cleaned up temporary files")


if __name__ == "__main__":
    main()
