"""Embed the same Pathfinder console used by Help/app.py."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.console import render as render_console


def render():
    render_console(standalone=False)
