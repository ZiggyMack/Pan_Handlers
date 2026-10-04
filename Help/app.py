"""Run from the repository root: python -m streamlit run Help/app.py."""

import sys
from pathlib import Path

import streamlit as st

# Keep imports independent of the launch directory and other dashboards' pages.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.console import render


def main():
    st.set_page_config(
        page_title="Pathfinder | Pan Handlers",
        page_icon="🧭",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    render(standalone=True)


if __name__ == "__main__":
    main()
