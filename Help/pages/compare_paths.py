"""Compare paths: the four interface choices and the learner's recorded decision."""

import streamlit as st

from Help.content.catalog import PATHS
from Help.state.session import PATH_BY_ID, field, get_journey, go
from Help.ui.components import hero, path_cards


def render():
    hero("DECISION DESK / FOUR VALID ROUTES", "Choose the path that fits.",
          "Compare the interaction, the strengths, and the work each route asks of you.")
    path_cards()
    st.caption("Fit assessments are editorial judgments based on the official feature documentation, not performance benchmarks. “Planned” means the walkthrough here is still to be written.")
    st.table({
        "Path": [p["name"] for p in PATHS],
        "How you work": [p["interaction"] for p in PATHS],
        "Role in this video project": [p["video_fit"] for p in PATHS],
        "Our coverage": [p["status"] for p in PATHS],
    })
    for path in PATHS:
        with st.expander(path["name"] + " · strengths & tradeoffs", expanded=path["id"] == "comfyui"):
            left, right = st.columns(2)
            with left:
                st.markdown("**Reasons to choose it**")
                for item in path["strengths"]:
                    st.markdown("- " + item)
            with right:
                st.markdown("**What you take on**")
                for item in path["tradeoffs"]:
                    st.markdown("- " + item)
            st.markdown(f'[Official {path["name"]} project]({path["url"]})')
            if path["id"] != "comfyui":
                st.caption("Expansion reserved: setup → first output → video handoff → reproducible example. See Sources & roadmap.")
    with st.container(border=True):
        st.subheader("Keep the decision visible")
        field(st.selectbox, "My chosen path", "chosen_path", options=list(PATH_BY_ID),
               format_func=lambda value: PATH_BY_ID[value]["name"])
        field(st.text_area, "Why this route? What am I trading off?", "decision_reason", max_chars=10000,
               placeholder="For example: I want to see and share each step, so the node learning curve is worth it.")
        if get_journey()["chosen_path"] != "comfyui":
            st.info("Your choice is recorded. This route's walkthrough is planned; its official project link is available above. The ComfyUI walkthrough remains available for comparison.")
        else:
            st.button("Follow the ComfyUI path →", on_click=go, args=("ComfyUI guide",), type="primary")
