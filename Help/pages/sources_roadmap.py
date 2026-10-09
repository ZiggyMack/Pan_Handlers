"""Sources and roadmap: research references, coverage and room for other paths."""

import streamlit as st

from Help.content.catalog import FUTURE_CHECKLIST, PATHS, SOURCES
from Help.content.cfa_learning import SUMMARY as CFA_SUMMARY
from Help.content.scene_content import SCENE_SOURCES
from Help.content.video_routes import SOURCES as VIDEO_SOURCES
from Help.guides.model_library import MODEL_SOURCES
from Help.ui.components import hero, route_strip


def render():
    hero("SOURCEBOOK / ROOM TO GROW", "Keep the alternatives alive.",
          "ComfyUI gets the first walkthrough. Every other path keeps its place, its tradeoffs and a clear expansion plan.")
    route_strip()
    tabs = st.tabs(["Expansion roadmap", "Sources", "About this console"])
    with tabs[0]:
        for path in PATHS:
            with st.expander(path["name"] + " · " + path["status"], expanded=path["id"] != "comfyui"):
                if path["id"] == "comfyui":
                    st.write("Available: environment choices, first still, workflow anatomy, video experiment, optional 3D branch, checkpoint notes and an exportable journal.")
                    st.write("Active mission: transform a source video's look, setting or characters while preserving motion and performance. Video workshop routes to researched templates, captures review evidence and leads from an accepted take to HD and reviewed 4K. The dialogue guide remains a related branch.")
                    st.write(CFA_SUMMARY)
                    st.write("Next video evidence: a reviewed output and its exact execution recipe. Game development remains a future branch.")
                else:
                    for item in FUTURE_CHECKLIST:
                        st.markdown("- " + item)
                st.markdown(f'[Official project]({path["url"]})')
    with tabs[1]:
        st.caption("Video workshop sources checked October 2, 2026. Earlier foundations and dialogue research retain their September 12 context. Public documentation does not verify an account's installed nodes or model access.")
        source_tabs = st.tabs(["Video workshop", "Toolkit & foundations", "Scene rewrite", "Models & files"])
        with source_tabs[0]:
            for title, url in VIDEO_SOURCES:
                st.markdown(f'[{title}]({url})')
        for source_tab, source_group in zip(source_tabs[1:], (SOURCES, SCENE_SOURCES, MODEL_SOURCES)):
            with source_tab:
                for source in source_group:
                    st.markdown(f'**[{source["title"]}]({source["url"]})**')
                    st.write(source["note"])
    with tabs[2]:
        st.write("Pathfinder is the reusable guide in Pan Handlers; CFA keeps the production experiments. The active task is high-resolution, lifelike video: change an existing shot while preserving motion and performance. Dialogue rewriting and editable 3D remain available branches; game development is parked for a later return.")
        st.write("The guide is shared; each visitor's journal belongs to their session. Download and restore JSON to carry your progress between visits, or share the Markdown field guide.")
        st.write("Visual roots: the Nyquist Ledger's teal palette, dark sidebar, serif headings and layered menus, with Pan Handlers' optional Matrix mode.")
