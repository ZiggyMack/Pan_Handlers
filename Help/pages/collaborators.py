"""Teach collaborator handoffs; production files and operations stay in CFA."""

import streamlit as st

from Help.content.collaborators import (
    REVIEWED, PROVIDERS, COMMON_LESSONS, EVIDENCE_STATES, DISCOVERY, PRESERVATION,
)
from Help.state.session import go
from Help.ui.components import hero


_LESSONS = {
    "reference": "Reference roles and image-to-image comparisons",
    "comparison": "One change at a time · controlled comparison",
    "prompts": "Prompt composition · inspect the exact words",
    "files": "Save, open and inspect a workflow",
    "audio": "Video, soundtrack and timing handoffs",
}


def _remember(field, key):
    st.session_state["help_collaborators_choices"][field] = st.session_state[key]


def _choice(kind, label, field, options, **kwargs):
    choices = st.session_state.setdefault("help_collaborators_choices", {})
    key = "help_collaborators_" + field
    if key not in st.session_state:
        st.session_state[key] = choices.get(field, next(iter(options)))
    return kind(label, options=list(options), key=key, on_change=_remember,
                args=(field, key), **kwargs)


def _evidence(label, path):
    st.caption(label + " · local CFA source record")
    st.code("D:/Documents/CFA/" + path.removeprefix("../../CFA/"), language="text")


def guide_markdown(provider_id):
    """Portable teaching notes and provenance, with no private media or state."""
    provider = PROVIDERS[provider_id]
    lines = ["# Collaborators / " + provider["name"], "", "Snapshot: " + REVIEWED, "",
             "Teaching notes only. This download contains no media, model, Comfy execution graph or production review state.", "",
             provider["purpose"], "", "## Prepare the handoff", ""]
    lines.extend(f"{i}. {step}" for i, step in enumerate(provider["how"], 1))
    lines.extend(["", provider["boundaries"], "", "## Preserve an existing design", ""])
    lines.extend("- " + item for item in PRESERVATION)
    lines.extend(["", "## Explore a new design", ""])
    lines.extend("- " + item for item in DISCOVERY)
    lines.extend(["", "## Know what the evidence establishes", ""])
    for state in EVIDENCE_STATES:
        lines.extend(["- **" + state["Stage"] + ":** " + state["Meaning"]])
    for lesson in COMMON_LESSONS:
        lines.extend(["", "## " + lesson["title"], "", lesson["meaning"], "", lesson["example"], "",
                      "[CFA evidence](" + lesson["evidence"] + ")"])
    lines.extend(["", "## Sources", ""])
    lines.extend(f"- [{label}]({url})" for label, url in provider["sources"])
    lines.extend(f"- [{label}]({path})" for label, path in provider["evidence"])
    lines.extend(["", "Local evidence links are relative to Help in adjacent Pan_Handlers/CFA checkouts. The hosted guide does not read those files. CFA owns the current masters, actual uploads, graphs and acceptance decisions.", ""])
    return "\n".join(lines)


def _practice():
    lesson = _choice(st.selectbox, "Learn the part needed for this handoff", "lesson", _LESSONS,
                     format_func=_LESSONS.get)
    if lesson == "reference":
        from Help.guides.image_edit_lab import render
        render()
    elif lesson == "comparison":
        from Help.guides.sampling_lab import render
        render()
    elif lesson == "prompts":
        from Help.guides.prompt_wiring import render_composition
        render_composition("help_collaborators_prompt")
    elif lesson == "files":
        from Help.guides.workflow_files import render
        render("help_collaborators_files")
    else:
        from Help.guides.video_handoff import render
        render("help_collaborators_audio")
    st.caption("These are the existing ComfyUI exercises. Their method transfers between collaborators; model settings and node instructions belong to the named Comfy recipe. Reading or planning does not submit a provider task.")


def render():
    hero("COLLABORATORS / HOW AND WHY", "Choose the role. Keep the thread.",
         "Give each collaborator a clear brief, references with specific jobs, and a result you can review. Carry the lesson back into the next experiment.")
    st.caption("Saved CFA records reviewed " + REVIEWED + ". This page does not inspect live accounts or synchronize project reviews.")
    provider_id = _choice(st.radio, "Which collaborator are you working with?", "provider", PROVIDERS,
                          format_func=lambda key: PROVIDERS[key]["name"], horizontal=True)
    provider = PROVIDERS[provider_id]
    role, approach, practice = st.tabs(["01 / Role & handoff", "02 / Preserve or explore", "03 / Continue a lesson"])
    with role:
        st.subheader(provider["name"] + " · the job in this project")
        st.write(provider["purpose"])
        for number, step in enumerate(provider["how"], 1):
            st.markdown(f"**{number}.** {step}")
        st.info(provider["boundaries"])
        st.markdown("**What has actually happened?**")
        st.table(EVIDENCE_STATES)
        with st.expander("Source records and current project handoffs"):
            st.caption("Pathfinder explains the method. CFA Creative Studio owns the operational library, review choices and handoffs. One asset keeps one master record even when shown under both project and collaborator.")
            st.link_button("Open CFA Creative Studio", "https://algaib.streamlit.app/")
            for label, url in provider["sources"]:
                st.markdown(f"[{label}]({url})")
            for label, path in provider["evidence"]:
                _evidence(label, path)
            st.caption("Local paths require the CFA checkout; they are provenance references, not media loaded by the hosted app.")
    with approach:
        lane = _choice(st.radio, "What kind of brief is this?", "lane",
                       ("Preserve an existing design", "Explore a new design"), horizontal=True)
        for instruction in PRESERVATION if lane.startswith("Preserve") else DISCOVERY:
            st.markdown("- " + instruction)
        st.write("Keep Hon Dolo / Strictly Business and Lisan Al Gaib / Meta Mirror in separate project briefs. A useful costume, tattoo or pose reference does not automatically replace the identity master.")
        for lesson in COMMON_LESSONS:
            with st.expander(lesson["title"]):
                st.write(lesson["meaning"])
                st.markdown("**From CFA's recorded work:** " + lesson["example"])
                _evidence("Case provenance", lesson["evidence"])
    with practice:
        _practice()
        left, right = st.columns(2)
        left.button("Review a moving take in Video workshop", on_click=go, args=("Video workshop",),
                    key="help_collaborators_to_video")
        right.button("Keep observations in Field journal", on_click=go, args=("Field journal",),
                     key="help_collaborators_to_journal")
    st.download_button("Download these collaborator teaching notes", guide_markdown(provider_id),
                       "pathfinder-collaborator-" + provider_id + ".md", "text/markdown",
                       key="help_collaborators_download")
    st.caption("This download contains explanations and source references only. It is not a media ZIP, a selection list or an export of CFA's review state. Save/export that state in CFA; use Field journal for your Pathfinder observations.")
