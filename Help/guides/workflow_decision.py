"""Optional decision/outcome notes shared by the existing comparison exercises.

These session drafts are separate from journal v1. Nothing here operates Comfy.
"""

from html import escape
import re

import streamlit as st


EVIDENCE_STATES = {
    "not_run": "Planned / no execution reported",
    "input_check": "Input-only check reported; no generation",
    "validated": "Validation / dry-run reported; no generation",
    "executed": "Generation reported; acceptance not established",
}
_FIELDS = (
    ("problem", "Problem to solve / what must stay unchanged"),
    ("lesson", "Lesson or source / section and review date"),
    ("rationale", "Why this recipe fits / reason for departing from its baseline"),
    ("success", "Success criterion before the comparison"),
    ("effective", "Actual compiled settings / graph revision and active outputs"),
    ("record", "Actual input-check, validation or run record / output paths"),
    ("result", "Observed result or exact error / unwanted changes"),
    ("next", "Next decision and reason"),
)

OPERATING_STEPS = (
    "Keep the original prepared input and exported baseline. Use a fixed seed, queue count 1 and batch size 1; leave automatic queuing off. If seed is the chosen variable, fix each trial to its specified seed. Restore the baseline before changing one control.",
    "Copy the whole output branch: sampler, VAE Decode and Save Image. Paste with incoming connections where supported, then inspect every wire. Give A, B and C distinct filename prefixes. Unlink only the comparison variable from a shared Primitive so it can differ; retain the fixed controls.",
    "Separate input inspection from generation. Crops and assembled-text previews show their last upstream execution. For an input-only check, mute every terminal Preview/Save that depends on sampling and inspect the remaining dependencies. A separate input-only graph is easier to audit. Cloud runtime can still apply.",
    "Inspect the compiled effective prompt, files, dimensions and sampling values before submission. A connected scalar or stale named-widget metadata can override a visible widget. Read the resolved graph, not just the canvas labels; an old embedded API prompt can also be stale.",
    "Request only the intended output branch for a small comparison. A result preview receives generated pixels; it cannot reveal a future image. Enabled Preview and Save nodes can both run without a review pause. Record the actual submitted settings, output/error and cache or warm-up notes.",
    "Export the actual editor JSON and reopen that file in a separate tab. Inspect its references, shared controls, branch modes and output prefixes again. Keep the original inputs, execution graph and results with it; reopening alone establishes neither generation nor acceptance.",
)


def _md(value):
    return re.sub(r"([\\`*_{}\[\]()#+.!|~>-])", r"\\\1", escape(str(value), quote=False))


def decision_markdown(decision=None):
    """Export optional learner notes without changing or upgrading their evidence."""
    notes = decision or {}
    status = EVIDENCE_STATES.get(notes.get("evidence_state"), EVIDENCE_STATES["not_run"])
    lines = ["## Decision and actual observations", "",
             "Learner-reported notes only. This guide does not execute, verify or accept a result.", "",
             "The trial table is planned settings. The actual-settings and record fields below identify what was really checked or submitted; later plan edits do not rewrite that evidence.", "",
             "Evidence state: " + status, ""]
    for field, label in _FIELDS:
        lines.extend(["**" + label + ":**", "", _md(notes.get(field) or "Not recorded"), ""])
    lines.extend(["## Copy, inspect, compare and reopen", ""])
    lines.extend(f"{number}. {step}" for number, step in enumerate(OPERATING_STEPS, 1))
    lines.extend(["", "Collapsing changes presentation. Muting disables a node; bypass forwards compatible inputs where possible. Bypassing an optional adapter can be useful, but is not a universal switch for a generation branch.", "",
                  "Operating lesson: Help/CFA_TUTORIAL_LEDGER.md, PH TUT 04; CFA workflows/README.md, Choose by problem and Quick controls from episode 3 (reviewed October 4, 2026). Canonical recipe/run records remain in CFA; these notes do not read that repository at runtime.", "",
                  "[Comfy shortcuts](https://docs.comfy.org/interface/shortcuts) · [Preview Image](https://docs.comfy.org/built-in-nodes/PreviewImage)", ""])
    return "\n".join(lines)


def _remember(state_key, field, widget_key):
    st.session_state[state_key][field] = st.session_state[widget_key]


def render(key_prefix, lesson):
    """Return context-scoped notes, retaining them when widget pages disappear."""
    state_key = key_prefix + "_draft"
    if state_key not in st.session_state:
        st.session_state[state_key] = {**dict.fromkeys((field for field, _ in _FIELDS), ""),
                                       "lesson": lesson, "evidence_state": "not_run"}
    draft = st.session_state[state_key]

    def field(kind, label, name, **kwargs):
        key = key_prefix + "_" + name
        if key not in st.session_state:
            st.session_state[key] = draft[name]
        return kind(label, key=key, on_change=_remember, args=(state_key, name, key), **kwargs)

    with st.expander("Give this comparison a purpose and keep its outcome", expanded=False):
        st.write("Use the baseline and single changed variable above. Add the problem, the lesson behind your recipe choice and a concrete success check before running anything.")
        for name, label in _FIELDS[:4]:
            field(st.text_area, label, name, max_chars=3000, height=85)
        st.markdown("**After an actual check in Comfy**")
        field(st.selectbox, "Evidence you are reporting", "evidence_state",
              options=list(EVIDENCE_STATES), format_func=EVIDENCE_STATES.get)
        for name, label in _FIELDS[4:]:
            field(st.text_area, label, name, max_chars=4000, height=85)
        st.caption("Self-reported notes are included in this exercise's download. Record actual settings beside the output; the planned table can change later. This does not mark journal progress, submit a Cloud job or declare an accepted take.")
    return dict(draft)


def render_operating_steps():
    with st.expander("Small exercise: copy → inspect inputs → compare → reopen"):
        for number, step in enumerate(OPERATING_STEPS, 1):
            st.markdown(f"**{number}.** {step}")
        st.caption("CFA operating notes reviewed October 4, 2026. These are instructions to carry out deliberately in your own Cloud workflow, not actions performed here.")
