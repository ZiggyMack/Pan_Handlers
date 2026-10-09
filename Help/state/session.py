"""Shared journey state and callbacks used by the shell and page modules.

Widget keys and the exported journal schema remain independent of file layout.
"""

import streamlit as st

from Help.content.catalog import PATHS, STEPS
from Help.state.journey import new_journey, validate_journey


STATE_KEY = "help_journey"
PATH_BY_ID = {path["id"]: path for path in PATHS}


def get_journey():
    if STATE_KEY not in st.session_state:
        st.session_state[STATE_KEY] = new_journey()
    return st.session_state[STATE_KEY]


def go(section):
    st.session_state["help_section"] = section


def set_field(field, widget_key):
    save_change({field: st.session_state[widget_key]})


def save_change(changes):
    try:
        st.session_state[STATE_KEY] = validate_journey({**get_journey(), **changes})
    except ValueError as error:
        st.session_state["help_save_error"] = f"Latest edit was not saved: {error} Download the existing journey before shortening this edit."
    else:
        st.session_state.pop("help_save_error", None)


def set_step(step_id, widget_key):
    done = set(get_journey()["completed_steps"])
    if st.session_state[widget_key]:
        done.add(step_id)
    else:
        done.discard(step_id)
    save_change({"completed_steps": [s["id"] for s in STEPS if s["id"] in done]})


def set_note(step_id, widget_key):
    save_change({"step_notes": {**get_journey()["step_notes"], step_id: st.session_state[widget_key]}})


def field(kind, label, field, options=None, **kwargs):
    """Keep durable values separate from Streamlit's page-scoped widget keys."""
    key = "help_widget_" + field
    if key not in st.session_state:
        st.session_state[key] = get_journey()[field]
    kwargs.update(key=key, on_change=set_field, args=(field, key))
    if options is not None:
        return kind(label, options=options, **kwargs)
    return kind(label, **kwargs)


def append_journal_entry(entry):
    journey = get_journey()
    st.session_state[STATE_KEY] = validate_journey({**journey, "entries": [*journey["entries"], entry]})


def select_step(step_id):
    st.session_state["help_step_select"] = step_id
