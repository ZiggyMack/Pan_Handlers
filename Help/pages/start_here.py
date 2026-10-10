"""Start here: choose source material and keep the larger creative goal visible."""

import streamlit as st

from Help.content.catalog import REQUIREMENTS_BOOKMARK, TUTORIAL_URL
from Help.pages.video_workshop import render_entry
from Help.state.journey import OUTPUT_KINDS
from Help.state.session import field, get_journey, go
from Help.ui.components import hero, html, path_cards


def render():
    path_cards()
    hero("VIDEO FIRST / THE NEXT EXPERIMENT", "Keep the performance. Change the world.",
          "Start with your source material, borrow the right workflow, and work toward one convincing shot before finishing it in HD and 4K.")
    st.caption("PROJECT MEMORY / October 8 CFA records: video-control tests executed but failed strict preservation; local soundtrack swap preserved the picture. Lip-sync and an accepted finished video remain ahead.")
    render_entry(go)
    st.divider()
    left, right = st.columns([1.5, 1], gap="large")
    with left:
        st.subheader("Keep the larger goal in view")
        field(st.text_input, "Your shot or task", "goal", max_chars=4000,
               placeholder="Transform an existing clip while preserving its motion and performance")
        field(st.radio, "What should the result contain?", "output_kind", options=OUTPUT_KINDS)
        kind = get_journey()["output_kind"]
        if kind == "AI video":
            st.info("Generate a clip or edit an existing scene. Scene dialogue replacement starts with footage and speech; editable 3D geometry is a separate deliverable.")
        elif kind == "Editable 3D + AI":
            st.info("Plan for meshes, materials, cameras and an animation scene. Use ComfyUI for concepts or assets, then assemble and render in Blender.")
        else:
            st.info("Choose the kind of experiment: rewrite an existing scene, generate a new clip, or build an editable 3D scene. Each has a different first step.")
        buttons = st.columns(2)
        buttons[0].button("Compare all four paths →", on_click=go, args=("Compare paths",),
                          use_container_width=True)
        buttons[1].button("What does ComfyUI unlock? →", on_click=go, args=("ComfyUI guide",),
                          type="primary", use_container_width=True)
    with right:
        html('<div class="help-callout"><div class="help-kicker">THE METHOD</div>'
              '<h3>Learn it. Try it. Leave a recipe.</h3>'
              '<p>01 / Compare the options and record your decision.</p>'
              '<p>02 / Make one small, repeatable experiment.</p>'
              '<p>03 / Keep the settings, result and lesson together.</p></div>')
        st.markdown("**Your first milestone**")
        st.write("One short source shot, one controlled visual change and a saved comparison. Accept the performance before making an HD master and reviewing a 4K derivative.")
        st.caption("This console is a guide and notebook. Rendering happens in the tool you choose.")
    with st.expander("Other creative branches"):
        st.caption("All four tools remain valid options. ComfyUI is the first deep guide. Editable 3D and game development remain future branches.")
        st.button("Explore the dialogue-rewrite branch →", on_click=go, args=("Rewrite a scene",), key="help_scene_home")
    st.divider()
    with st.expander("Where the idea started · pixaroma's ComfyUI series"):
        st.markdown(f"[Ep01 · Introduction and Installation]({TUTORIAL_URL})")
        st.markdown(f'**Captured learning point:** [{REQUIREMENTS_BOOKMARK["timestamp"]} · {REQUIREMENTS_BOOKMARK["title"]}]({REQUIREMENTS_BOOKMARK["url"]})')
        st.caption("The slide and its current setup considerations are saved in ComfyUI guide → Setup routes. This bookmark records where the learning conversation reached; it does not mark your setup complete.")
        st.caption("Published July 9, 2024. Use the series for concepts and the linked current docs for installation. The chapter references come from the public video description.")
        if st.checkbox("Load the YouTube player", key="help_video_player"):
            st.video(TUTORIAL_URL)
        st.write("00:00 Introduction · 02:40 Windows installation · 06:22 Models · 09:52 First image · 14:32 Save/load workflows · 18:47 Manager")
