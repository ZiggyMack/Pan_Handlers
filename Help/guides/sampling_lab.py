"""Plan controlled KSampler comparisons; no generation or completion claims."""

from html import escape
import math
import re

import streamlit as st

from Help.guides.shared_controls import render as render_shared_controls
from Help.guides import workflow_decision


_STATE = "help_sampling_draft"
VARIABLES = {"cfg": "CFG", "steps": "Steps", "seed": "Seed"}
_DOCS = "https://docs.comfy.org/built-in-nodes/sampling/ksampler"


def _value(variable, value):
    raw = str(value).strip()
    if variable in {"seed", "steps"}:
        if not re.fullmatch(r"[0-9]+", raw):
            raise ValueError(f"{VARIABLES[variable]} must be a whole nonnegative number.")
        parsed = int(raw)
        lower, upper = (0, 2**64 - 1) if variable == "seed" else (1, 10000)
        if not lower <= parsed <= upper:
            raise ValueError(f"{VARIABLES[variable]} must be between {lower} and {upper} for this classic KSampler reference.")
        # Preserve seed digits in browser-facing tables and exports.
        return str(parsed) if variable == "seed" else parsed
    try:
        parsed = float(raw)
    except ValueError as error:
        raise ValueError("CFG must be a finite number from 0 to 100.") from error
    if not math.isfinite(parsed) or not 0 <= parsed <= 100:
        raise ValueError("CFG must be a finite number from 0 to 100.")
    return parsed


def build_cases(variable, baseline, alternatives):
    """Make A/B/C plans that vary exactly the selected setting from the baseline."""
    if variable not in VARIABLES:
        raise ValueError("Choose CFG, Steps or Seed for this comparison.")
    values = alternatives.split(",")
    if len(values) != 2:
        raise ValueError("Enter exactly two alternative values separated by a comma.")
    base = {key: _value(key, baseline[key]) for key in VARIABLES}
    variants = [_value(variable, value) for value in values]
    return [dict(case=label, **{**base, **change}) for label, change in (
        ("A / Baseline", {}), ("B / Alternative", {variable: variants[0]}),
        ("C / Alternative", {variable: variants[1]}),
    )]


def _draft():
    if _STATE not in st.session_state:
        st.session_state[_STATE] = {
            "variable": "cfg", "seed": "42", "steps": 30, "cfg": 7.0,
            "cfg_values": "6, 6.5", "steps_values": "32, 36", "seed_values": "43, 44",
            "recipe": "", "sampler": "dpmpp_2m", "scheduler": "karras",
        }
    return st.session_state[_STATE]


def _remember(field, key):
    _draft()[field] = st.session_state[key]


def _field(kind, label, field, **kwargs):
    key = "help_sampling_widget_" + field
    if key not in st.session_state:
        st.session_state[key] = _draft()[field]
    return kind(label, key=key, on_change=_remember, args=(field, key), **kwargs)


def _md(value):
    return re.sub(r"([\\`*_{}\[\]()#+.!|~>-])", r"\\\1", escape(str(value), quote=False))


def plan_markdown(draft, cases, decision=None):
    lines = ["# KSampler comparison plan", "", "Planned only; no generation or result is implied.", "",
             "Saved baseline graph / model receipt: " + _md(draft["recipe"] or "Not yet recorded"), "",
             "Changed variable: " + VARIABLES[draft["variable"]], "",
             "Shared sampler: " + _md(draft["sampler"]), "Shared scheduler: " + _md(draft["scheduler"]), "",
             "Keep model and companion files, positive/negative prompts, dimensions, denoise, inputs and environment unchanged. Record those in the baseline graph/receipt.",
             "Set seed control to fixed, queue count 1 and latent batch_size 1. Restore the baseline before each alternative.", "",
             "| Case | Seed | Steps | CFG | Suggested Save Image prefix |", "| --- | --- | --- | --- | --- |"]
    for case in cases:
        lines.append(f"| {case['case']} | {case['seed']} | {case['steps']} | {case['cfg']} | sampling_{case['case'][0]} |")
    lines.extend(["", "## Record after each run", "",
                  "| Case | Actual seed/settings | Output or error | Elapsed time | Cache / warm-up notes |", "| --- | --- | --- | --- | --- |",
                  "| A | | | | |", "| B | | | | |", "| C | | | | |", "",
                  "## Decide what to change next", "",
                  "Describe prompt adherence, unwanted artifacts and useful detail. Treat quality as an observation, not a value computed from steps or CFG.",
                  "Repeat a promising comparison across additional seeds before treating it as a general conclusion.", "",
                  "Keep this plan with the editor JSON and original outputs. Record observed results in Workflow lab's Change one variable milestone or Field journal, then export the journal to retain it.", "",
                  f"[KSampler controls and bounds]({_DOCS})", ""])
    if decision is not None:
        lines.extend([workflow_decision.decision_markdown(decision)])
    return "\n".join(lines)


def _comparison():
    st.write("Copy a known working recipe, choose one variable, and plan two alternatives. Run these comparisons in ComfyUI and keep their actual outputs.")
    st.caption("The prefilled 30 steps / CFG 7 / dpmpp_2m / karras values illustrate the tutorial's classic workflow. Replace them with your exact model/version's working settings, especially for accelerated variants.")
    _field(st.text_input, "Saved baseline workflow / model receipt", "recipe", max_chars=1000,
           placeholder="Filename and exact model/version; keep its inputs and settings alongside it.")
    seed, steps, cfg = st.columns(3)
    with seed:
        _field(st.text_input, "Baseline seed (exact digits)", "seed", max_chars=20)
    with steps:
        _field(st.number_input, "Baseline steps", "steps", min_value=1, max_value=10000, step=1)
    with cfg:
        _field(st.number_input, "Baseline CFG", "cfg", min_value=0.0, max_value=100.0, step=0.5)
    sampler, scheduler = st.columns(2)
    with sampler:
        _field(st.text_input, "Shared sampler_name", "sampler", max_chars=80)
    with scheduler:
        _field(st.text_input, "Shared scheduler", "scheduler", max_chars=80)
    variable = _field(st.selectbox, "Change one setting", "variable", options=list(VARIABLES), format_func=VARIABLES.get)
    raw = _field(st.text_input, "Two alternative values, separated by a comma", variable + "_values", max_chars=100)
    try:
        cases = build_cases(variable, _draft(), raw)
    except ValueError as error:
        st.error(str(error))
        return
    st.table([{"Case": case["case"], "Seed": case["seed"], "Steps": case["steps"], "CFG": case["cfg"],
               "Save Image prefix": "sampling_" + case["case"][0]} for case in cases])
    if len({case[variable] for case in cases}) != 3:
        st.info("Some planned values repeat. That can explore cache or repeatability, but it is not a three-value comparison.")
    st.info("Hold the seed control at fixed, queue count at 1 and latent batch_size at 1. Keep the model, prompts, dimensions, denoise, sampler, scheduler and inputs unchanged except for your selected variable. Record the seed actually submitted; UI controls can update before or after a run.")
    if not _draft()["sampler"].strip() or not _draft()["scheduler"].strip() or not _draft()["recipe"].strip():
        st.caption("The baseline record is still incomplete. Add its graph reference, sampler and scheduler before running; the downloaded plan remains a draft.")
    st.caption("This planner validates basic numeric bounds, not whether these settings suit your model. It does not predict image quality, elapsed time or VRAM.")
    st.caption("Begin with A and one alternative B. C is an optional follow-up, not a request to queue three jobs. Stop and review when the chosen success check is answered.")
    workflow_decision.render_operating_steps()
    decision = workflow_decision.render(
        "help_sampling_decision",
        "ComfyUI guide / Workflow anatomy / Controlled experiment; Episode 3 sampling and canvas operations. "
        "Help/CFA_TUTORIAL_LEDGER.md PH TUT 04; reviewed October 4, 2026.",
    )
    st.download_button("Download the A/B/C comparison plan", plan_markdown(_draft(), cases, decision),
                       file_name="comfyui-sampling-comparison.md", mime="text/markdown", key="help_sampling_download")
    st.write("The download keeps your planned settings and separately labeled observations together. These session drafts are separate from journey JSON; download them before leaving. You can also summarize the lesson in 07 / Workflow lab → Change one variable or Field journal.")


def _controls():
    st.table({
        "Control": ["Fixed / randomize / increment / decrement seed", "Steps", "CFG", "Sampler and scheduler", "Denoise"],
        "What to learn": [
            "Fixed supports comparisons; the other modes vary seeds. Neighboring seed numbers do not mean visually neighboring images. Keep the actual submitted seed.",
            "Steps affect the sampling trajectory and work. Quality can plateau or worsen; the model variant's documented range is the starting point.",
            "CFG scales conditioning guidance. It is not a contrast slider, and increasing it does not guarantee better prompt adherence or quality.",
            "These select a method and noise schedule. Begin with the model's documented pair; test supported alternatives deliberately.",
            "Classic text-to-image commonly uses 1.0. Input-image preservation is a separate experiment; see VAE paths for Encode → sample → Decode.",
        ],
    })
    st.caption("A fixed seed does not guarantee identical pixels across software, hardware, precision or model changes. An unchanged graph may reuse cached work rather than recompute it.")
    st.markdown(f"[KSampler]({_DOCS}) · [Reproducibility limits](https://docs.pytorch.org/docs/stable/notes/randomness.html) · [Cache behavior](https://docs.comfy.org/custom-nodes/backend/server_overview)")
    st.markdown("**Expose a widget only when that helps the experiment**")
    st.write("The tutorial converts CFG, steps and scheduler widgets into inputs and attaches a Primitive node. Newer frontends can show sockets and widgets together. A shared Primitive can drive compatible parameter inputs on several nodes. They then change together; use separate values when comparing those settings. The Shared controls tab walks through the pattern and its compatibility checks.")
    st.markdown("[Primitive and reroute behavior](https://docs.comfy.org/custom-nodes/backend/datatypes#primitive-and-reroute)")
    st.markdown("**Batching measures throughput; it does not prove quality or speed**")
    st.write("Queue count repeats jobs; latent batch_size holds multiple images within a job. Compare actual elapsed time and memory on your own setup. The narrator's RTX 4090 timings describe that demonstration. A batch can need more memory, and it is not guaranteed faster on every graph.")


def _branches():
    st.markdown("**Build a comparison branch before simplifying it**")
    st.code("Shared MODEL + prompt CONDITIONING + starting LATENT\n  |- KSampler A -> VAE Decode A -> Save Image (sampling_A)\n  |- KSampler B -> VAE Decode B -> Save Image (sampling_B)\n  `- KSampler C -> VAE Decode C -> Save Image (sampling_C)\n\nCompatible VAE -> all three decoders' vae inputs", language="text")
    st.write("Duplicate KSampler + VAE Decode + Save Image together. In current default keybindings, paste with incoming connections uses Ctrl+Shift+V (Cmd+Shift+V on macOS). Inspect the copied wires. Shared prompt nodes mean shared prompts; add a separate encoder pair for a prompt-only comparison. Keep every required sampler input connected.")
    st.caption("Multiple branches are not a promise of simultaneous GPU execution. For the first experiment, use one graph and run A, B and C separately; change only the chosen setting.")
    st.table({
        "Action": ["Group frame", "Legacy Group Node / modern subgraph", "Hide a widget", "Bypass", "Mute", "Partial execution"],
        "Effect and limit": [
            "Labels and moves related boxes. A frame alone does not create a new computational operation.",
            "Packages connected operations behind a smaller interface. The tutorial's Group Node menus differ from today's subgraphs; retain an expanded copy and inspect exposed inputs/outputs.",
            "Changes presentation; the underlying setting still affects execution.",
            "Skips an operation by routing compatible input data onward where possible. Bypassing an encoder cannot convert CLIP into required CONDITIONING.",
            "Disables a node rather than forwarding its operation. Downstream required inputs can become unavailable; it is not a universal repair for a branch.",
            "Where supported, select an output node and run its required branch. Check frontend requirements and the actual run; do not assume every box on the canvas must execute.",
        ],
    })
    st.write("Give each output a distinct prefix. Preserve the expanded graph before creating a compact interface, then reopen the export and confirm that the intended branches still produce their labeled outputs.")
    st.info("To inspect only inputs, mute every terminal output that depends on sampling, including generated-result previews as well as Save Image. Muting only Save while leaving a sampler-dependent Preview enabled can still request generation. Inspect the compiled dependencies; a collapsed group still runs.")
    st.markdown("[Copy/paste and mode shortcuts](https://docs.comfy.org/interface/shortcuts) · [Subgraphs](https://docs.comfy.org/interface/features/subgraph) · [Partial execution](https://docs.comfy.org/interface/features/partial-execution)")


def render():
    st.subheader("Controlled experiment · explain the difference")
    plan, controls, shared, branches = st.tabs(["A/B/C plan", "Understand the controls", "Shared controls", "Branches & compact graphs"])
    with plan:
        _comparison()
    with controls:
        _controls()
    with shared:
        render_shared_controls("help_sampling_shared")
    with branches:
        _branches()
    st.caption("Episode 3's timestamped observations and source corrections are under Workflow anatomy → Tutorial notes → Episode 3.")
