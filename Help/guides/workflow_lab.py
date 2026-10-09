"""Hands-on workflow lessons and learner evidence, separate from foundation progress."""

from datetime import date
from html import escape
import re

import streamlit as st

from Help.content.workflow_lessons import CONCEPTS, EPISODE_TITLE, EPISODE_URL, LESSONS
from Help.guides.workflow_controls import render as render_workflow_controls
from Help.guides.video_handoff import render as render_video_handoff
from Help.guides.image_edit_lab import render as render_image_edit_lab


_STATE_KEY = "help_workflow_lab_draft"
_STATUSES = ("Not started", "Practicing", "Evidence recorded")
_CORE = "https://github.com/Comfy-Org/ComfyUI/blob/master/nodes.py"
_DRILLS = (
    {
        "id": "encode_prompt", "title": "A prompt wire will not connect",
        "before": "Checkpoint.CLIP [CLIP]\n  → KSampler.positive [CONDITIONING]",
        "options": ("Rename the CLIP output to positive", "Insert CLIP Text Encode and enter a prompt", "Change the node's color"),
        "answer": 1,
        "after": "Checkpoint.CLIP → CLIP Text Encode.clip\nCLIP Text Encode.CONDITIONING → KSampler.positive",
        "why": "The text encoder turns the prompt into CONDITIONING. Renaming or coloring a node does not convert the data type.",
        "source": _CORE,
    },
    {
        "id": "decode_output", "title": "The sampler cannot feed Save Image directly",
        "before": "KSampler.LATENT [LATENT]\n  → Save Image.images [IMAGE]",
        "options": ("Add more sampling steps", "Use a reroute to change LATENT into IMAGE", "Add VAE Decode with a compatible VAE"),
        "answer": 2,
        "after": "KSampler.LATENT → VAE Decode.samples\nCheckpoint.VAE → VAE Decode.vae\nVAE Decode.IMAGE → Save Image.images",
        "why": "Decode turns latent samples into pixels. A reroute reorganizes a wire; it does not perform that conversion. Some models need a separate compatible VAE loader.",
        "source": _CORE,
    },
    {
        "id": "missing_vae", "title": "The decoder reports a missing VAE input",
        "before": "KSampler.LATENT → VAE Decode.samples\n                  VAE Decode.vae ← missing",
        "options": ("Supply the matching checkpoint VAE or Load VAE output", "Increase CFG until the red outline disappears", "Attach the checkpoint MODEL output to vae"),
        "answer": 0,
        "after": "Checkpoint.VAE or Load VAE.VAE\n  → VAE Decode.vae [VAE]",
        "why": "Read the missing input named in the error. The decoder needs a VAE component compatible with these latents. Node color is only a UI cue; confirm the actual error and output.",
        "source": "https://docs.comfy.org/troubleshooting/model-issues",
    },
    {
        "id": "branch_image", "title": "You want both a saved image and a preview",
        "before": "VAE Decode.IMAGE → Save Image.images\nYou also want a Preview Image branch.",
        "options": ("Send the sampler LATENT directly to Preview Image", "Branch VAE Decode.IMAGE to both Save Image and Preview Image", "Put the PNG filename into KSampler.model"),
        "answer": 1,
        "after": "VAE Decode.IMAGE\n  ├─→ Save Image.images\n  └─→ Preview Image.images",
        "why": "An output can feed more than one destination. Branching the decoded IMAGE gives both nodes pixel data without depending on the output sockets exposed by a particular Save Image release. Preview is optional when Save Image already shows the output.",
        "source": _CORE,
    },
    {
        "id": "family_match", "title": "The wire fits, but ControlNet has a dimension error",
        "before": "SD 1.5 ControlNet [CONTROL_NET]\n  → Apply ControlNet in an SDXL generation stage",
        "options": ("Hide the wires", "Use an SDXL-compatible ControlNet and its documented control map", "Rename the ControlNet file to include SDXL"),
        "answer": 1,
        "after": "SDXL-compatible ControlNet + required control map\n  → documented Apply node → SDXL generation stage",
        "why": "Matching sockets is a structural check. The model family, variant, control-map type and required components must also fit. The repair still needs an actual small test.",
        "source": "https://docs.comfy.org/troubleshooting/model-issues",
    },
)


def new_workbook():
    return {"workflow": "", "next_step": "", "selected_lesson": LESSONS[0]["id"], "lessons": {
        lesson["id"]: {"status": _STATUSES[0], "evidence": ""} for lesson in LESSONS
    }}


def _draft():
    if _STATE_KEY not in st.session_state:
        st.session_state[_STATE_KEY] = new_workbook()
    return st.session_state[_STATE_KEY]


def _remember(field, key, lesson_id):
    target = _draft() if lesson_id is None else _draft()["lessons"][lesson_id]
    target[field] = st.session_state[key]


def _field(kind, label, field, lesson_id=None, **kwargs):
    key = "help_workbook_widget_" + (lesson_id + "_" if lesson_id else "") + field
    target = _draft() if lesson_id is None else _draft()["lessons"][lesson_id]
    if key not in st.session_state:
        st.session_state[key] = target[field]
    return kind(label, key=key, on_change=_remember, args=(field, key, lesson_id), **kwargs)


def _stamp(seconds):
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


def _lesson_reference(lesson):
    stamp = _stamp(lesson["seconds"])
    if EPISODE_URL:
        return f"[Episode 2 · {stamp}]({EPISODE_URL}&t={lesson['seconds']}s)"
    return f"Episode 2 transcript · {stamp} (video URL not verified)"


def _md(value):
    return re.sub(r"([\\`*_{}\[\]()#+.!|~>-])", r"\\\1", escape(value, quote=False))


def workbook_markdown(workbook):
    lines = ["# Workflow practice workbook", "", EPISODE_TITLE, "",
             "Practice in your own ComfyUI environment. This guide does not execute a graph or verify a render.",
             "Status and evidence are learner-reported. Concept exercises do not complete these milestones.", "",
             "Workflow / version: " + _md(workbook["workflow"]), ""]
    for lesson in LESSONS:
        saved = workbook["lessons"][lesson["id"]]
        lines.extend(["## " + lesson["title"], "", _lesson_reference(lesson), "",
                      lesson["understand"], ""])
        lines.extend(f"{i}. {action}" for i, action in enumerate(lesson["do"], 1))
        lines.extend(["", "**Evidence to keep:** " + lesson["check"], "",
                      "**Watch for:** " + lesson["pitfall"], "",
                      "**My status:** " + _md(saved["status"]), "",
                      "**My evidence:** " + _md(saved["evidence"]), "",
                      "References: " + " · ".join(f"[{title}]({url})" for title, url in lesson["sources"]), ""])
    lines.extend(["## My next experiment", "", _md(workbook["next_step"]), ""])
    return "\n".join(lines)


def workbook_entry(workbook):
    if not any(item["evidence"].strip() for item in workbook["lessons"].values()):
        raise ValueError("Record an observation or result for at least one milestone before saving a snapshot.")
    lines = ["Workflow practice · learner-reported evidence", "",
             "Workflow / version: " + workbook["workflow"], ""]
    for lesson in LESSONS:
        saved = workbook["lessons"][lesson["id"]]
        if saved["status"] == "Evidence recorded" and not saved["evidence"].strip():
            raise ValueError("Add the evidence for '" + lesson["title"] + "' or change its status to Practicing.")
        lines.extend([lesson["title"] + " — " + saved["status"], saved["evidence"], ""])
    return {"date": date.today().isoformat(), "title": "Workflow practice · Episode 2",
            "observation": "\n".join(lines), "next_step": workbook["next_step"],
            "resource": EPISODE_URL or ""}


def _practice_path():
    st.markdown("### Understand it, do it, show it")
    st.caption("Use a copy of a working graph for experiments. The tasks run in ComfyUI; this page holds your instructions and notes.")
    draft = _draft()
    recorded = sum(v["status"] == "Evidence recorded" and bool(v["evidence"].strip()) for v in draft["lessons"].values())
    st.progress(recorded / len(LESSONS), text=f"{recorded} of {len(LESSONS)} milestones with self-reported evidence")
    if "help_workbook_lesson" not in st.session_state:
        st.session_state["help_workbook_lesson"] = draft.get("selected_lesson", LESSONS[0]["id"])
    selected = st.selectbox("Practice a skill", [lesson["id"] for lesson in LESSONS],
                            format_func=lambda key: next(f"{i:02d} / {lesson['title']}" for i, lesson in enumerate(LESSONS, 1) if lesson["id"] == key),
                            key="help_workbook_lesson", on_change=_remember,
                            args=("selected_lesson", "help_workbook_lesson", None))
    lesson = next(item for item in LESSONS if item["id"] == selected)
    st.subheader(lesson["title"])
    st.markdown(_lesson_reference(lesson))
    st.write(lesson["understand"])
    for i, action in enumerate(lesson["do"], 1):
        st.markdown(f"{i}. {action}")
    st.info("Show it: " + lesson["check"])
    with st.expander("A common misunderstanding"):
        st.write(lesson["pitfall"])
    with st.expander("Record what happened", expanded=True):
        _field(st.selectbox, "My practice status", "status", selected, options=_STATUSES)
        _field(st.text_area, "Evidence, error, or observation", "evidence", selected, max_chars=1200,
               placeholder="What did you try? What happened? Name the saved graph/output or explain the error and fix.")
        saved = draft["lessons"][selected]
        if saved["status"] == "Evidence recorded" and not saved["evidence"].strip():
            st.warning("Add the observation that supports this status; it will not count toward progress until evidence is present.")
    st.markdown("Sources: " + " · ".join(f"[{title}]({url})" for title, url in lesson["sources"]))
    with st.expander("See the whole practice path"):
        st.table({"Skill": [item["title"] for item in LESSONS],
                  "What demonstrates it": [item["check"] for item in LESSONS]})
    with st.expander("Six distinctions that make a graph easier to read"):
        for concept in CONCEPTS:
            st.markdown("**" + concept["term"] + "**")
            st.write(concept["meaning"])
            st.caption("Try it: " + concept["try"])


def _repair_bench():
    st.subheader("Diagnose the connection before running")
    st.caption("Concept exercises only. These examples do not inspect your installation, run a graph or mark a practice milestone complete.")
    choice = st.selectbox("Choose a wiring problem", [item["id"] for item in _DRILLS],
                          format_func=lambda key: next(item["title"] for item in _DRILLS if item["id"] == key), key="help_workbook_drill")
    drill = next(item for item in _DRILLS if item["id"] == choice)
    st.code(drill["before"], language="text")
    selected = st.radio("What would you change first?", ["Choose a repair…", *drill["options"]], key="help_workbook_answer_" + choice)
    if selected != "Choose a repair…":
        if selected == drill["options"][drill["answer"]]:
            st.success("That addresses this example's wiring problem.")
            st.code(drill["after"], language="text")
        else:
            st.info("That change does not address this example's missing component or incompatible input.")
        st.write(drill["why"])
        st.markdown(f"[Check the underlying node behavior]({drill['source']})")


def _keep_evidence(save_entry):
    st.subheader("Leave a workbook the next learner can follow")
    _field(st.text_input, "Workflow filename / version or reference", "workflow", max_chars=1000)
    _field(st.text_area, "My next experiment", "next_step", max_chars=2000)
    draft = _draft()
    st.caption("Draft notes survive navigation in this session. Download the workbook, or save a snapshot to Field journal and export its JSON. Restoring a journal restores readable snapshots, not this editable workbook form.")
    if st.button("Save workbook snapshot to Field journal", key="help_workbook_save"):
        try:
            save_entry(workbook_entry(draft))
        except ValueError as error:
            st.error(str(error))
        else:
            st.success("Snapshot saved. Download your journey JSON from Field journal to keep it between visits.")
    st.download_button("Download my practice workbook", workbook_markdown(draft),
                       file_name="comfyui-workflow-practice.md", mime="text/markdown", key="help_workbook_download")
    st.markdown("**Your next destinations:** Workflow anatomy for Size & sampler and Save & load; Node Atlas for individual sockets; Worked example for an inspectable completed still.")
    st.write("Once you can explain and reopen this still-image graph, apply the same questions to the scene-rewrite recipe: what comes in, what changes, what leaves, and what evidence shows that it worked?")


def render(save_entry):
    st.subheader("Workflow lab · from following to understanding")
    st.write("Read a graph, build a small one, explain a failure, and leave a repeatable recipe. Start with Episode 2's seven milestones, then apply them to image edits and video/audio handoffs.")
    st.caption("The supplied 2024 tutorial is the starting point. Episode timestamps point to related passages; the exercises also draw on current documentation and may use different interface commands.")
    if EPISODE_URL:
        st.markdown(f"[{EPISODE_TITLE}]({EPISODE_URL})")
    controls, practice, repairs, image_edit, video, evidence = st.tabs(["Control guide", "Practice path", "Repair bench", "Image to image", "Video & audio", "My workbook"])
    with controls:
        render_workflow_controls()
    with practice:
        _practice_path()
    with repairs:
        _repair_bench()
    with image_edit:
        render_image_edit_lab()
    with video:
        render_video_handoff()
    with evidence:
        _keep_evidence(save_entry)
