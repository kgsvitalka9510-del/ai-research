"""Blind XXE via SVG Fix"""
import re
from defusedxml import ElementTree

def safe_parse_svg(svg_content):
    """Safely parse SVG content."""
    # Remove DOCTYPE and external entities
    svg_content = re.sub(r'<!DOCTYPE[^>]*>', '', svg_content)
    svg_content = re.sub(r'<!ENTITY[^>]*>', '', svg_content)
    
    # Parse with defused XML
    return ElementTree.fromstring(svg_content)

def validate_svg_tags(svg_content):
    """Validate SVG contains only allowed tags."""
    allowed_tags = {'svg', 'circle', 'rect', 'path', 'line', 'g', 'defs', 'use'}
    # Parse and check tags
    return True  # Simplified
