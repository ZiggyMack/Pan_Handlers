"""Classic image-to-image and LoRA practice, with a session-only trial planner."""

from html import escape
import math
import re

import streamlit as st

from Help.content.episode_four import EPISODE_TITLE, EPISODE_URL
from Help.guides import workflow_decision


_STATE = "help_image_edit_draft"
_IMG2IMG = "https://comfyanonymous.github.io/ComfyUI_examples/img2img/"
_LORA = "https://comfyanonymous.github.io/ComfyUI_examples/lora/"
_CORE = "https://github.com/Comfy-Org/ComfyUI/blob/master/nodes.py"
_SAMPLING = "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/samplers.py"
VARIABLES = {"denoise": "Denoise", "strength_model": "LoRA model strength", "strength_clip": "LoRA CLIP strength"}
_DEFAULTS = {
    "recipe": "", "input_image": "", "seed": "42", "lora_enabled": False,
    "variable": "denoise", "denoise": 0.5, "strength_model": 1.0, "strength_clip": 1.0,
    "denoise_values": "0.35, 0.65", "strength_model_values": "0.5, 0.8",
    "strength_clip_values": "0.5, 0.8",
}


def _draft():
    if _STATE not in st.session_state:
        st.session_state[_STATE] = dict(_DEFAULTS)
    return st.session_state[_STATE]


def _remember(field, key):
    _draft()[field] = st.session_state[key]


def _field(kind, label, field, **kwargs):
    key = "help_image_edit_widget_" + field
    if key not in st.session_state:
        st.session_state[key] = _draft()[field]
    return kind(label, key=key, on_change=_remember, args=(field, key), **kwargs)


def _number(name, value):
    upper = 1.0 if name == "denoise" else 2.0
    try:
        parsed = float(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"{VARIABLES[name]} must be a finite number from 0 to {upper:g} in this lesson.") from error
    if isinstance(value, bool) or not math.isfinite(parsed) or not 0 <= parsed <= upper:
        raise ValueError(f"{VARIABLES[name]} must be a finite number from 0 to {upper:g} in this lesson.")
    return parsed


def build_trials(draft):
    """Vary one active control; preserve the exact seed and leave draft untouched."""
    variable = draft["variable"]
    if variable not in VARIABLES or (variable != "denoise" and not draft["lora_enabled"]):
        raise ValueError("Enable the LoRA path to compare its strengths, or choose Denoise.")
    seed = str(draft["seed"]).strip()
    if not re.fullmatch(r"[0-9]{1,20}", seed) or int(seed) > 2**64 - 1:
        raise ValueError("Use a whole seed from 0 to 18446744073709551615; keep its exact digits.")
    seed = str(int(seed))
    active = VARIABLES if draft["lora_enabled"] else {"denoise": VARIABLES["denoise"]}
    baseline = {name: _number(name, draft[name]) for name in active}
    raw = draft[variable + "_values"].split(",")
    if len(raw) != 2:
        raise ValueError("Enter two alternative values separated by a comma.")
    values = [_number(variable, value.strip()) for value in raw]
    return [dict(case=label, seed=seed, **{**baseline, **change}) for label, change in (
        ("A / Baseline", {}), ("B / Alternative", {variable: values[0]}),
        ("C / Alternative", {variable: values[1]}),
    )]


def _md(value):
    return re.sub(r"([\\`*_{}\[\]()#+.!|~>-])", r"\\\1", escape(str(value), quote=False))


def plan_markdown(draft, trials, decision=None):
    fields = ["denoise", "strength_model", "strength_clip"] if draft["lora_enabled"] else ["denoise"]
    lines = ["# Image-to-image comparison plan", "", "Planned settings only; no generated image or preservation score is implied.", "",
             "Baseline workflow / exact model and LoRA version: " + _md(draft["recipe"] or "Not recorded"),
             "Original input / prepared image: " + _md(draft["input_image"] or "Not recorded"), "",
             "Path: " + ("Image to image + compatible LoRA" if draft["lora_enabled"] else "Image to image, no LoRA"),
             "Changed control: " + VARIABLES[draft["variable"]], "",
             "| Trial | Exact seed | " + " | ".join(VARIABLES[name] for name in fields) + " |",
             "| --- | --- | " + " | ".join("---" for _ in fields) + " |"]
    for trial in trials:
        lines.append("| " + trial["case"] + " | " + trial["seed"] + " | " + " | ".join(str(trial[name]) for name in fields) + " |")
    lines.extend(["", "## Run each trial from the same starting point", "",
                  "1. Save the original input, prepared/resized image and baseline editor JSON. Record resize method, width, height and crop mode.",
                  "2. Hold model/LoRA files, VAE, prompts and trigger words, sampler, scheduler, steps, CFG, seed control and batch size steady. Only the chosen control changes.",
                  "3. Use a fixed seed and batch size 1. Feed the same prepared source into every trial; do not use A's output as B's input.",
                  "4. Save separate outputs with names such as img2img_A, img2img_B and img2img_C. Record the actual settings submitted.", "",
                  "| Trial | Output or exact error | What changed as intended? | What drifted? | Runtime / memory notes |", "| --- | --- | --- | --- | --- |",
                  "| A | | | | |", "| B | | | | |", "| C | | | | |", "",
                  "Denoise is not a percentage of pixels changed or identity retained. Model and CLIP strengths affect different LoRA branches. Zero model strength alone is not an off baseline when CLIP strength is nonzero.",
                  "For a separate LoRA on/off comparison, hold the prompt and all other controls fixed and bypass the whole adapter or set both strengths to zero, checking the model and CLIP routes.", "",
                  "Keep the input, outputs, workflow and exact dependency versions together. Record actual observations in My workbook or Field journal; the plan itself does not mark progress complete.", "",
                  f"[Image-to-image example]({_IMG2IMG}) · [LoRA example]({_LORA}) · [Node definitions]({_CORE})", ""])
    if decision is not None:
        lines.extend([workflow_decision.decision_markdown(decision)])
    return "\n".join(lines)


def _build_path():
    st.markdown("### Begin with your image")
    st.code("Load Image.IMAGE → Upscale Image.image (resize if needed)\nUpscale Image.IMAGE → VAE Encode.pixels\nCompatible VAE → VAE Encode.vae\nVAE Encode.LATENT → KSampler.latent_image\nKSampler.LATENT → VAE Decode.samples\nThe same compatible VAE → VAE Decode.vae\nVAE Decode.IMAGE → Save Image.images", language="text")
    st.write("Keep the sampler's MODEL and both prompt CONDITIONING inputs. Replace the Empty Latent Image branch with the encoded source. If resizing is unnecessary, Load Image can feed VAE Encode directly.")
    st.info("This is the classic SDXL/SD1.5 image-to-image pattern. Choose a checkpoint and its compatible VAE. Whole-image resampling can change faces, text and background; masks, ControlNet and model-specific image-editing workflows are separate control paths.")
    st.markdown(f"[Official image-to-image example]({_IMG2IMG}) · [Core node definitions]({_CORE})")
    with st.expander("Set the canvas before VAE Encode", expanded=True):
        st.write("In this branch, the prepared input determines the latent dimensions. Changing a disconnected Empty Latent Image has no effect. Inspect width and height after preprocessing and again in the saved result; the VAE may crop to dimensions its compression requires.")
        st.table([
            {"Decision": "Upscale Image / ImageScale", "What to know": "Ordinary resizing can shrink or enlarge an image. It does not load a learned upscaler model."},
            {"Decision": "Keep the aspect ratio", "What to know": "Use matching width/height proportions, or the node's supported zero-dimension auto-sizing option for one dimension. Inspect the result."},
            {"Decision": "crop = disabled", "What to know": "With both target dimensions set, a changed aspect ratio stretches the image."},
            {"Decision": "crop = center", "What to know": "Fills the requested aspect ratio by cropping; important edges or subjects may be removed."},
            {"Decision": "Supported working size", "What to know": "Start with the exact model's documented size. SDXL commonly uses roughly 1024-scale canvases; that is not a universal requirement for every model or aspect ratio."},
        ])
        st.caption("Four times the width and four times the height means 16 times as many pixels, not a predicted 16× runtime. The tutorial's 4/5/200-second runs belong to that demonstration. A tiled VAE fallback can reduce VAE memory demand but does not fix sampler memory, unsupported sizes or composition drift.")
        st.markdown(f"[Resize implementation and VAE inputs]({_CORE}) · [VAE cropping and memory handling](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/sd.py)")
    with st.expander("Iterate without losing the original"):
        st.write("Copy/paste can make the next iteration quicker where the browser and frontend support it. Save the actual input and workflow too; a clipboard image or screenshot may lose workflow metadata. If paste is unavailable, load the saved image through Load Image.")
        st.code("Comparison: original → A   original → B   original → C\nIteration:  original → v01 → v02 → v03", language="text")
        st.write("Chaining results changes the input every time and can accumulate drift. Use that deliberately for iterations; return to the original prepared input when comparing settings.")
        st.caption("For your scene-rewrite goal, a pleasing edited still is a reference candidate. It does not prove temporal consistency, mouth synchronization or preservation of the whole movie scene.")


def _lora_path():
    st.markdown("### Add a LoRA after the baseline works")
    st.write("Loading a LoRA applies already-trained adapter weights during inference. It does not train or overwrite your checkpoint. Match the base family and exact supported variant, then read the adapter's trigger words and recommended settings.")
    st.code("Checkpoint.MODEL → Load LoRA.model → KSampler.model\nCheckpoint.CLIP  → Load LoRA.clip\nLoad LoRA.CLIP   → both CLIP Text Encode.clip inputs\nBoth encoders' CONDITIONING → KSampler.positive / negative\nCheckpoint.VAE  → VAE Encode.vae and VAE Decode.vae", language="text")
    st.info("Select LoraLoader, the node with both MODEL and CLIP inputs/outputs. Current upstream names it ‘Load LoRA (Model and CLIP)’; the similarly named model-only loader has a different role. Some LoRAs contain no text-encoder weights, so CLIP strength may have no effect for that file.")
    st.table([
        {"Control": "denoise", "Influences": "The img2img sampling schedule and how strongly the source can be reinterpreted."},
        {"Control": "strength_model", "Influences": "Adapter patches applied to the diffusion model."},
        {"Control": "strength_clip", "Influences": "Adapter patches applied to the text encoder, when the LoRA provides them."},
        {"Control": "Trigger words", "Influences": "Prompt tokens recommended for that adapter; requirements differ by LoRA."},
    ])
    st.markdown("**Find and place the file:** Setup routes → Models & files → filter planner → LoRA for an existing image model. Match the family first, shortlist with ratings/downloads, then inspect the exact version and its instructions.")
    st.code("Local default: ComfyUI/models/loras/<compatible-adapter>.safetensors\nCloud: supported model catalog / import → select in the LoRA loader", language="text")
    st.caption("The tutorial's cloud/fire adapters are examples, not required dependencies. Trigger wording and 0.3–1 strength preferences belong to those examples. Begin with one compatible LoRA; stacking adapters introduces more interactions.")
    st.markdown(f"[LoRA loading and chaining]({_LORA}) · [Model/CLIP loader implementation]({_CORE}) · [Cloud imports](https://docs.comfy.org/cloud/import-models)")


def _compare():
    st.markdown("### Compare source preservation and the intended edit")
    st.write("Lower denoise generally leaves more source structure recognizable; higher values allow broader reinterpretation. The useful value depends on the source, prompt, model and sampling settings.")
    st.caption("Denoise changes the sampling schedule, not an image-opacity blend or a measured preservation percentage. At zero, the classic sampler makes no sampling change; resizing and the VAE round trip can still alter pixels. At one, substantial drift is possible, not guaranteed total independence from the source.")
    st.markdown(f"[Sampling behavior]({_SAMPLING})")
    _field(st.text_input, "Baseline workflow / exact model and LoRA version", "recipe", max_chars=1000)
    _field(st.text_input, "Original input / prepared image filename", "input_image", max_chars=1000)
    _field(st.text_input, "Fixed seed (exact digits)", "seed", max_chars=20)
    use_lora = _field(st.checkbox, "Include the compatible LoRA path in this plan", "lora_enabled")
    cols = st.columns(3 if use_lora else 1)
    with cols[0]:
        _field(st.number_input, "Baseline denoise", "denoise", min_value=0.0, max_value=1.0, step=0.05)
    if use_lora:
        with cols[1]:
            _field(st.number_input, "Baseline LoRA model strength", "strength_model", min_value=0.0, max_value=2.0, step=0.1)
        with cols[2]:
            _field(st.number_input, "Baseline LoRA CLIP strength", "strength_clip", min_value=0.0, max_value=2.0, step=0.1)
    st.caption("Prefilled values are comparison examples, not a model preset. This introductory planner explores LoRA strengths from 0 to 2; the actual node permits a wider range. Use the selected adapter's recommendations.")
    options = list(VARIABLES) if use_lora else ["denoise"]
    if _draft()["variable"] not in options:
        _draft()["variable"] = "denoise"
        st.session_state["help_image_edit_widget_variable"] = "denoise"
    variable = _field(st.selectbox, "Change one image-edit control", "variable", options=options, format_func=VARIABLES.get)
    _field(st.text_input, "Two image-edit alternatives, separated by a comma", variable + "_values", max_chars=100)
    try:
        trials = build_trials(_draft())
    except ValueError as error:
        st.error(str(error))
        return
    st.table([{"Trial": trial["case"], "Exact seed": trial["seed"],
               **{VARIABLES[name]: trial[name] for name in options}} for trial in trials])
    if len({trial[variable] for trial in trials}) < 3:
        st.info("Some values repeat. This can test repeatability, but is not a three-value comparison.")
    if any(trial["denoise"] == 0 for trial in trials):
        st.info("A zero-denoise trial is a sampling-off reference. It does not promise an exact copy of the source pixels, and LoRA sampling effects cannot be judged there.")
    st.info("For A, B and C, keep the same prepared input, fixed seed, prompts, resize/crop, files and all other controls. Give each result its own output name. Shared Primitive controls can hold the fixed values across multiple KSamplers; leave the comparison variable independent.")
    if use_lora:
        st.caption("For a separate LoRA on/off test, bypass the entire adapter or set both strengths to zero while preserving the same prompt. Zero model strength with active CLIP strength is not a full off baseline.")
    st.caption("Use A and one alternative B for the first check; C is optional. None of these rows queues a Cloud job. Keep the original prepared source for every comparison.")
    workflow_decision.render_operating_steps()
    decision = workflow_decision.render(
        "help_image_edit_decision",
        "ComfyUI guide / Workflow lab / Image to image / Compare edits; Episode 4. "
        "https://www.youtube.com/watch?v=xedwjtaPVzw ; CFA Image Refinement SDXL v2 is validated, not rendered. "
        "Help/CFA_TUTORIAL_LEDGER.md PH TUT 04; reviewed October 4, 2026.",
    )
    st.download_button("Download this image-edit comparison", plan_markdown(_draft(), trials, decision),
                       file_name="comfyui-image-edit-comparison.md", mime="text/markdown", key="help_image_edit_download")
    st.caption("The draft and optional outcome notes survive navigation in this session. Download them to keep them; they are not automatically included in journey JSON. Actual outputs and failures stay separate from the proposed trial settings and do not establish acceptance.")


def render():
    st.subheader("Image to image · keep a starting point, change its treatment")
    st.write("Episode 4 becomes a three-part practice: prepare the source, compare denoise, then add one compatible LoRA. Save the original so every choice can be compared honestly.")
    st.markdown(f"[{EPISODE_TITLE}]({EPISODE_URL})")
    path, comparison, lora = st.tabs(["Prepare the input", "Compare edits", "LoRA connections"])
    with path:
        _build_path()
    with comparison:
        _compare()
    with lora:
        _lora_path()
