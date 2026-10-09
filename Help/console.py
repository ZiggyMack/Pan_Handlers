"""Pathfinder navigation shell, shared by the standalone app and dashboard.

Each sidebar destination is implemented in its matching Help/pages module.
"""

import streamlit as st

from Help.content.catalog import STEPS
from Help.pages import (
    comfyui_guide, collaborators, compare_paths, field_journal, rewrite_scene, sources_roadmap,
    start_here, video_workshop,
)
from Help.state.session import get_journey, go
from Help.ui.components import downloads, html
from Help.ui.theme import apply_theme


SECTIONS = ("Start here", "Video workshop", "Collaborators", "Rewrite a scene", "Compare paths", "ComfyUI guide", "Field journal", "Sources & roadmap")


def _sidebar():
    with st.sidebar:
        st.markdown("### 🧭 Pathfinder")
        st.caption("PAN HANDLERS / THE FIELD GUIDE")
        st.markdown("**A task. Several paths. A trail to follow.**")
        st.divider()
        for group, sections in (
            ("ORIENT", ("Start here", "Compare paths")),
            ("ACTIVE MISSION", ("Video workshop", "Collaborators")),
            ("OTHER SCENE TOOLS", ("Rewrite a scene",)),
            ("MAKE", ("ComfyUI guide", "Field journal")),
            ("KEEP EXPLORING", ("Sources & roadmap",)),
        ):
            st.caption(group)
            for section in sections:
                st.button(section, key="help_nav_" + section, use_container_width=True,
                          type="primary" if st.session_state["help_section"] == section else "secondary",
                          on_click=go, args=(section,))
        st.divider()
        st.toggle("Matrix mode", key="help_matrix")
        count = len(get_journey()["completed_steps"])
        st.caption(f"COMFYUI FOUNDATIONS · {count} / {len(STEPS)} CHECKPOINTS")
        st.progress(count / len(STEPS))
        with st.expander("Take your journey with you"):
            st.caption("Notes stay in this session. Download JSON before closing; restore it in Field journal next time.")
            downloads("sidebar")
        st.caption("Active task: lifelike video · preserve the performance")


def render(standalone=False):
    get_journey()
    st.session_state.setdefault("help_section", SECTIONS[0])
    st.session_state.setdefault("help_matrix", False)
    if standalone:
        _sidebar()
        matrix = st.session_state["help_matrix"]
    else:
        matrix = st.session_state.get("matrix_mode", False)
    apply_theme(matrix_mode=matrix)
    if st.session_state.get("help_save_error"):
        st.error(st.session_state["help_save_error"])
    if not standalone:
        st.radio("Pathfinder / turn the page", SECTIONS, key="help_section", horizontal=True)
    renderers = {
        "Start here": start_here.render,
        "Video workshop": video_workshop.render,
        "Collaborators": collaborators.render,
        "Rewrite a scene": rewrite_scene.render,
        "Compare paths": compare_paths.render,
        "ComfyUI guide": comfyui_guide.render,
        "Field journal": field_journal.render,
        "Sources & roadmap": sources_roadmap.render,
    }
    renderers[st.session_state["help_section"]]()
    html('<div class="help-footer">PAN HANDLERS / PATHFINDER · Compare honestly. Record the experiment. Pass it on.</div>')
