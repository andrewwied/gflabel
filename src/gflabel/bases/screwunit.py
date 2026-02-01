from __future__ import annotations

import argparse
import logging
import sys

from build123d import Axis, BuildPart, BuildSketch, RectangleRounded, Vector, extrude, fillet

from ..util import unit_registry
from . import LabelBase

logger = logging.getLogger(__name__)


class ScrewUnitBase(LabelBase):
    """
    Generate a label for K2_Kevin ScrewUnit bins.
    
    The ScrewUnit system has two standard sizes:
    - small: 23mm x 13mm
    - wide: 53mm x 13mm
    
    Origin is positioned at the center of the label, with the label
    surface at z=0.
    
    Based on the ScrewUnit Label Creator by K2_Kevin.
    """

    # Default to small size width
    DEFAULT_WIDTH = unit_registry.Quantity(23, unit_registry.mm)
    DEFAULT_WIDTH_UNIT = unit_registry.mm
    DEFAULT_MARGIN = unit_registry.Quantity(1.5, "mm")
    
    # ScrewUnit standard dimensions (in mm)
    SIZES = {
        "small": {"width": 23, "height": 13},
        "wide": {"width": 53, "height": 13},
    }
    
    # Default depth and fillet from OpenSCAD code
    DEFAULT_DEPTH = 0.6
    DEFAULT_FILLET = 1.0

    def __init__(self, args: argparse.Namespace):
        # Get the requested size
        size = self.SIZES.get(args.screwunit_size, self.SIZES["small"])
        width_mm = size["width"]
        height_mm = size["height"]
        
        logger.info(f"Using ScrewUnit size: {args.screwunit_size} ({width_mm}x{height_mm}mm)")
        depth_mm = args.label_depth.to("mm").magnitude if args.label_depth else self.DEFAULT_DEPTH / 2
        
        with BuildPart() as part:
            with BuildSketch() as _sketch:
                RectangleRounded(width_mm, height_mm, self.DEFAULT_FILLET)
            
            # Extrude the base down (negative direction)
            extrude(amount=-depth_mm)
            
            # Optional: Add small fillet to edges for better print quality
            # Get top edges and fillet them slightly
            try:
                top_edges = part.edges().group_by(Axis.Z)[-1]
                fillet(top_edges, radius=0.1)
            except Exception:
                # If filleting fails, continue without it
                pass

        self.part = part.part
        self.area = Vector(width_mm, height_mm)
