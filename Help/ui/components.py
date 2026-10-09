"""Reusable Pathfinder presentation pieces, shared across sidebar pages."""

from html import escape

import streamlit as st

from Help.content.catalog import PATHS
from Help.state.journey import dumps_journey, journey_markdown
from Help.state.session import get_journey, go


def html(content):
    st.markdown(content, unsafe_allow_html=True)


def hero(eyebrow, title, description):
    html(f'<div class="help-hero"><div class="help-eyebrow">{escape(eyebrow)}</div>'
          f'<h1>{escape(title)}</h1><p>{escape(description)}</p></div>')


def route_strip():
    labels = "".join(
        f'<span>{escape(path["name"])} · {"guide available" if path["id"] == "comfyui" else "guide planned"}</span>'
        for path in PATHS
    )
    html(f'<div class="help-route-strip">{labels}</div>')


def path_cards():
    """The Armada pattern: parallel path headers and compact tagged rows."""
    capabilities = {
        "automatic1111": [("Interface", "Forms & tabs", "strength"), ("Images", "Generate & refine", "strength"),
                          ("Extend", "Extension ecosystem", "strength"), ("Tradeoff", "Check compatibility", "tradeoff"),
                          ("Video", "Choose an extension / handoff", "tradeoff")],
        "forge": [("Interface", "Familiar WebUI", "strength"), ("Compute", "Resource management focus", "strength"),
                  ("Models", "Supported Flux workflows", "strength"), ("Tradeoff", "Benchmark on your hardware", "tradeoff"),
                  ("Video", "Choose a compatible workflow", "tradeoff")],
        "invoke": [("Interface", "Canvas & node workflows", "strength"), ("Control", "Brushes & inpainting", "strength"),
                   ("Refine", "Art direction & paintovers", "strength"), ("Tradeoff", "Image-centered workspace", "tradeoff"),
                   ("Video", "Plan an animation handoff", "tradeoff")],
        "comfyui": [("Interface", "Visible node graph", "strength"), ("Repeat", "Save & share workflows", "strength"),
                    ("Outputs", "Image, video & 3D examples", "strength"), ("Tradeoff", "Nodes & dependencies to learn", "tradeoff"),
                    ("Video", "Guided first-clip experiment", "strength")],
    }
    with st.expander("Pipeline capabilities · 4 paths / ComfyUI unpacked first", expanded=True):
        columns = []
        for path in PATHS:
            rows = []
            for badge, label, kind in capabilities[path["id"]]:
                rows.append(
                    f'<div class="help-capability-row" data-kind="{kind}">'
                    '<span class="help-status-dot" aria-hidden="true"></span>'
                    f'<span class="help-capability-tag">{escape(badge)}</span>'
                    f'<span class="help-capability-text">{escape(label)}</span></div>'
                )
            active = path["id"] == "comfyui"
            rows.append('<div class="help-capability-row" data-kind="next">'
                        f'<span class="help-status-dot{ "" if active else " planned"}" aria-hidden="true"></span>'
                        '<span class="help-capability-tag">Guide</span>'
                        f'<span class="help-capability-text">{"7 checkpoints available" if active else "Walkthrough planned"}</span></div>')
            columns.append(
                f'<article class="help-pipeline-column" data-path="{path["id"]}">'
                f'<div class="help-pipeline-head"><h3>{escape(path["name"])}</h3>'
                f'<p>{"First to unpack" if active else "Alternative path"}</p></div>'
                + "".join(rows) + f'<p class="help-column-note">{escape(path["tagline"])}</p></article>'
            )
        html('<div class="help-armada-grid">' + "".join(columns) + '</div>')
        st.caption("Badges describe capabilities and tradeoffs. Guide status describes our coverage, not whether the tool is available.")
        st.button("Unpack ComfyUI →", on_click=go, args=("ComfyUI guide",), type="primary", key="help_unpack_comfy")


def downloads(location):
    journey = get_journey()
    st.download_button(
        "Download journey · JSON", dumps_journey(journey),
        file_name="pathfinder-journey.json", mime="application/json",
        key="help_download_json_" + location, use_container_width=True,
    )
    st.download_button(
        "Download field guide · Markdown", journey_markdown(journey),
        file_name="pathfinder-field-guide.md", mime="text/markdown",
        key="help_download_md_" + location, use_container_width=True,
    )
