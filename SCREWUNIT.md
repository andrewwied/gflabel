# ScrewUnit Base Labels

This feature adds support for generating labels compatible with K2_Kevin's ScrewUnit bin system.

## Overview

The ScrewUnit system is a parametric storage bin system with two standard label sizes:
- **Small**: 23mm × 13mm
- **Wide**: 53mm × 13mm

These labels are designed to fit into the K2_Kevin ScrewUnit bins, based on the original OpenSCAD label creator.

## Usage

To generate a ScrewUnit label, use the `screwunit` base:

```bash
# Small label (default)
gflabel screwunit "M3x10" -o label.stl

# Explicitly specify small size
gflabel screwunit --screwunit-size small "M3x10" -o label.stl

# Wide label
gflabel screwunit --screwunit-size wide "USB-C" -o label.stl

# Two-line label
gflabel screwunit "M3\nScrews" -o label.stl
```

## Options

- `--screwunit-size {small,wide}`: Select the label size (default: small)
  - `small`: 23mm × 13mm
  - `wide`: 53mm × 13mm

All standard gflabel options are also available (font, depth, style, etc.).

## Technical Details

- Default label depth: 0.3mm (half of the OpenSCAD default)
- Fillet radius: 1.0mm (matching OpenSCAD)
- Default margin: 1.5mm
- Label style: Embossed (raised text)

## Examples

```bash
# Simple screw size label
gflabel screwunit "M3x10" -o m3x10.stl

# Wide label for connector types
gflabel screwunit --screwunit-size wide "HDMI\nCables" -o hdmi.stl

# With custom depth
gflabel screwunit --depth 0.5 "M5" -o m5.stl

# Multiple labels at once
gflabel screwunit "M3" "M4" "M5" -o screws.stl
```

## Credits

Based on the ScrewUnit Label Creator by K2_Kevin.
Original OpenSCAD code licensed under Standard Digital File License.
