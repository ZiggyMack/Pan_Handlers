"""Field journal: record experiments and restore or export portable progress."""

from datetime import date

import streamlit as st

from Help.content.catalog import STEPS
from Help.state.journey import loads_journey, validate_journey
from Help.state.session import PATH_BY_ID, STATE_KEY, get_journey
from Help.ui.components import downloads, hero


def render():
    hero("FIELD JOURNAL / YOUR FOOTSTEPS", "Keep the useful details.",
          "A result becomes a guide when the next person can see your decisions, settings, mistakes and next steps.")
    journey = get_journey()
    st.info("Your journal lives in this browser session. Download JSON before closing or refreshing the app; restore that file below next time. Markdown gives you a readable copy to share.")
    with st.expander("Restore a saved journey"):
        uploaded = st.file_uploader("Journey JSON (up to 1 MB)", type=["json"], key="help_import_file")
        if st.button("Restore file and replace this session's journal", disabled=uploaded is None):
            try:
                restored = loads_journey(uploaded.getvalue())
            except ValueError as error:
                st.error(f"Could not restore the journey: {error}")
            else:
                st.session_state[STATE_KEY] = restored
                for key in list(st.session_state):
                    if key.startswith("help_widget_"):
                        del st.session_state[key]
                st.session_state["help_restored"] = True
                st.rerun()
    if st.session_state.pop("help_restored", False):
        st.success("Journey restored. Your decisions, notes and checkpoints are ready.")
    left, right = st.columns([1.5, 1], gap="large")
    with left:
        st.subheader("Add an experiment or lesson")
        if st.session_state.pop("help_clear_entry", False):
            for field in ("title", "observation", "next_step", "resource"):
                st.session_state["help_entry_" + field] = ""
        with st.form("help_entry_form"):
            title = st.text_input("Entry title", key="help_entry_title", max_chars=300, placeholder="First still / missing model resolved / camera test")
            observation = st.text_area("What did you try, and what happened?", key="help_entry_observation", max_chars=20000)
            next_step = st.text_area("What should the next person do?", key="help_entry_next_step", max_chars=10000)
            resource = st.text_input("Reference or result URL (optional)", key="help_entry_resource", max_chars=2048, placeholder="https://…")
            submitted = st.form_submit_button("Add to field journal", type="primary")
        if submitted:
            if not title.strip() or not observation.strip():
                st.error("Add a title and an observation so this entry is useful to follow.")
            else:
                entry = dict(date=date.today().isoformat(), title=title.strip(), observation=observation.strip(),
                             next_step=next_step.strip(), resource=resource.strip())
                candidate = {**journey, "entries": [*journey["entries"], entry]}
                try:
                    st.session_state[STATE_KEY] = validate_journey(candidate)
                except ValueError as error:
                    st.error(str(error))
                else:
                    st.session_state["help_clear_entry"] = True
                    st.rerun()
    with right:
        st.subheader("Your current recipe")
        st.text(journey["goal"] or "Set a shot brief in Start here.")
        st.write(f'Path: {PATH_BY_ID[journey["chosen_path"]]["name"]}')
        st.write(f'Output: {journey["output_kind"]} · Environment: {journey["environment"]}')
        st.write(f'{len(journey["completed_steps"])} checkpoints · {len(journey["entries"])} journal entries')
        downloads("journal")
    st.divider()
    st.subheader("The trail so far")
    if not journey["entries"]:
        st.caption("No experiments recorded yet. Start with the decision that brought you here, or the first thing you tried.")
    for entry in reversed(journey["entries"]):
        # Render learner content as text; do not interpret it as HTML or Markdown.
        with st.container(border=True):
            st.text(entry["date"] + " / " + entry["title"])
            st.text(entry["observation"])
            if entry["next_step"]:
                st.markdown("**Next step**")
                st.text(entry["next_step"])
            if entry["resource"]:
                st.text(entry["resource"])
    with st.expander("Checkpoint notes"):
        for step in STEPS:
            st.markdown("**" + step["title"] + "**")
            st.text(journey["step_notes"].get(step["id"], "No notes yet."))
