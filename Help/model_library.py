"""A small model-selection reference for Pathfinder's setup guide.

Primary sources reviewed on 2026-09-12. This module only renders guidance and a
blank receipt template; it never downloads models or contacts a model service.
"""

import streamlit as st

from Help.catalog import TUTORIAL_URL
from Help.cloud_access import ACCESS_SOURCES, render as render_cloud_access
from Help.model_filters import render as render_model_filters
from Help.generation_settings import render as render_generation_settings


MODEL_TUTORIAL_BOOKMARK = {
    "timestamp": "07:26",
    "url": TUTORIAL_URL + "&t=446s",
    "page": "https://civitai.com/models/133005?modelVersionId=456194",
    "model": "Juggernaut XL",
    "version": "Juggernaut_X_RunDiffusion",
    "filename": "Juggernaut_X_RunDiffusion.safetensors",
    "base": "SDXL 1.0",
    "role": "Checkpoint · trained",
}


MODEL_SOURCES = [
    *ACCESS_SOURCES,
    {
        "title": "Safetensors · tensor storage format",
        "url": "https://huggingface.co/docs/safetensors/index",
        "note": "A tensor-only serialization format designed to avoid pickle's code-execution mechanism.",
    },
    {
        "title": "Hugging Face · pickle loading considerations",
        "url": "https://huggingface.co/docs/hub/security-pickle",
        "note": "Why loading pickle-based weights can execute code; supports the preference for compatible safetensors weights.",
    },
    {
        "title": "ComfyUI · SDXL examples",
        "url": "https://comfyanonymous.github.io/ComfyUI_examples/sdxl/",
        "note": "Official SDXL checkpoint workflow guidance, supporting this guide's chosen starter image-model family.",
    },
    {
        "title": "RunDiffusion · Juggernaut X model card",
        "url": "https://huggingface.co/RunDiffusion/Juggernaut-X-v10",
        "note": "Publisher instructions for Juggernaut X. Verify the exact artifact/version; this is not evidence that X universally outperforms Hyper.",
    },
    {
        "title": "ComfyUI · KSampler settings",
        "url": "https://docs.comfy.org/built-in-nodes/sampling/ksampler",
        "note": "Separate sampler and scheduler fields, steps, CFG, denoise and seed controls; apply the chosen model's inference recommendations.",
    },
    {
        "title": "SDXL · architecture and multi-aspect training",
        "url": "https://arxiv.org/html/2307.01952v1",
        "note": "Original research explaining the architecture and resolution-training changes; a larger canvas alone does not change an SD1.5 model into SDXL.",
    },
    {
        "title": "pixaroma Ep01 · downloading and placing models, 07:26",
        "url": MODEL_TUTORIAL_BOOKMARK["url"],
        "note": "User screenshot shows Juggernaut XL, SDXL 1.0, trained checkpoint and the X RunDiffusion version. Tutorial preference over Hyper is a user-reported opinion, not a measured result here.",
    },
    {
        "title": "Civitai · model discovery",
        "url": "https://civitai.com/",
        "note": "The model-sharing destination flagged in the user's tutorial screenshot. No timestamp was visible.",
    },
    {
        "title": "Civitai · model types and usage",
        "url": "https://github.com/civitai/civitai/wiki/How-to-use-models",
        "note": "Official project wiki. Its older tool-specific instructions are background; use current Comfy instructions for folders and compatibility.",
    },
    {
        "title": "Civitai · model ranking options",
        "url": "https://github.com/civitai/civitai/blob/main/src/server/common/enums.ts",
        "note": "Current source defines Highest Rated and Most Downloaded among model sort options.",
    },
    {
        "title": "Civitai · model filters and ranking period",
        "url": "https://github.com/civitai/civitai/blob/main/src/server/schema/model.schema.ts",
        "note": "Current model query schema supports asset types, base-model families, sort order and time period.",
    },
    {
        "title": "Civitai · website filter controls",
        "url": "https://github.com/civitai/civitai/blob/main/src/components/Model/Infinite/ModelFiltersDropdown.tsx",
        "note": "Current visible filter labels and grouping; the tutorial screenshot records an older interface.",
    },
    {
        "title": "Civitai · model discovery and availability",
        "url": "https://github.com/civitai/civitai-developer-docs/blob/main/site/reference/models.md",
        "note": "Distinguishes on-site generation, models trained on-site, and hidden entries. API behavior should not be assumed identical to the website.",
    },
    {
        "title": "Civitai · website ranking and filtering behavior",
        "url": "https://github.com/civitai/civitai/blob/main/src/server/services/model.service.ts",
        "note": "Current Highest Rated ordering and the publication/statistics distinction; label meanings can change over time.",
    },
    {
        "title": "Civitai · official Comfy node pack",
        "url": "https://github.com/civitai/civitai-comfy-nodes",
        "note": "Optional early-preview integration: cloud recipes, local resource selection and Civitai Link. Source reviewed; not installed or executed here.",
    },
    {
        "title": "Civitai node pack · selectors and socket types",
        "url": "https://github.com/civitai/civitai-comfy-nodes/blob/main/civitai_comfy_nodes/nodes_manual.py",
        "note": "Exact selector names, resource-reference outputs and optional local download/application behavior.",
    },
    {
        "title": "Civitai node pack · local model handling",
        "url": "https://github.com/civitai/civitai-comfy-nodes/blob/main/civitai_comfy_nodes/local_models.py",
        "note": "File-type directory mapping, downloads, cache reuse and application of LoRAs to local weights.",
    },
    {
        "title": "Civitai node pack · authentication configuration",
        "url": "https://github.com/civitai/civitai-comfy-nodes/blob/main/civitai_comfy_nodes/config.py",
        "note": "Authentication resolution from node configuration, environment and stored credentials. No account data is collected by this guide.",
    },
    {
        "title": "Hugging Face · model cards",
        "url": "https://huggingface.co/docs/hub/model-cards",
        "note": "Author descriptions, intended uses, limitations, base-model metadata and license links.",
    },
    {
        "title": "ComfyUI · models and loader types",
        "url": "https://docs.comfy.org/basic-concepts/models",
        "note": "How model weights fit into a workflow and how model types determine loaders and directories.",
    },
    {
        "title": "ComfyUI · model-family compatibility",
        "url": "https://docs.comfy.org/troubleshooting/model-issues",
        "note": "ControlNet weights must support the checkpoint architecture; matching sockets or file extensions is insufficient.",
    },
    {
        "title": "ComfyUI · ControlNet and control images",
        "url": "https://docs.comfy.org/tutorials/controlnet/controlnet",
        "note": "Distinguishes the control model, its loader and the reference-map preparation required by the chosen control type.",
    },
    {
        "title": "ComfyUI · current model directory definitions",
        "url": "https://github.com/Comfy-Org/ComfyUI/blob/master/folder_paths.py",
        "note": "Primary source for checkpoints, loras, vae, diffusion_models and text_encoders folder names.",
    },
    {
        "title": "ComfyUI · first image generation",
        "url": "https://docs.comfy.org/get_started/first_generation",
        "note": "A small SD1.5 learning example, with model selection and missing-model troubleshooting.",
    },
    {
        "title": "ComfyUI · text-to-image node explanation",
        "url": "https://docs.comfy.org/tutorials/basic/text-to-image",
        "note": "Explains checkpoint, diffusion model, text encoder and VAE roles in the basic image workflow.",
    },
]


_MODEL_RECEIPT = """# Pathfinder model receipt

Status: planned / downloaded / loaded / tested (choose the status actually reached)

## Purpose

- Experiment or shot:
- What this model contributes:
- Workflow source and version:
- ComfyUI version:
- Loader node and custom-node version, if applicable:

## Exact asset

- Model name:
- Author or publishing organization:
- Original model page URL:
- Model version / repository revision:
- Exact file URL:
- Exact filename:
- File role (checkpoint / LoRA / ControlNet / VAE / diffusion model / text encoder / other):
- Base model family and compatible version:
- Format, precision or quantization:
- Discovery sort (Highest Rated / Most Downloaded / other):
- Time period, active mode (Published / Statistics) and date viewed:
- Other discovery filters (status / checkpoint type / hidden / archived):
- Rating/download observations for this model and version:
- Additional required files:
- Destination directory from this workflow's instructions:
- Download date:
- File size:
- Publisher hash and algorithm, if supplied:
- Locally calculated hash and algorithm, if checked:
- License / use terms URL and relevant notes:

## ControlNet pairing, if used

- Generation stage and checkpoint filename / base family:
- ControlNet filename / version / supported base family:
- Model-card or workflow URL documenting this pairing:
- Control type (depth / edges / pose / other) and selected mode, if applicable:
- Control-image file and preprocessor / version / settings, if used:
- Apply node, strength and start/end settings:
- Baseline without ControlNet and controlled result for comparison:

## Generation settings for this exact version

- Publisher recommendation URL and date checked:
- Variant (standard / Hyper / Lightning / Turbo / other):
- Width × height and the node that sets them:
- Sampler name:
- Scheduler:
- Steps:
- CFG / guidance value and the node that applies it:
- Denoise:
- Seed and control_after_generate:
- Other required sampling/model settings:
- Saved editor workflow and baseline output:

## What happened

- Loader recognizes file:
- Cloud import result and date, if applicable:
- Provider secret label only (never the token), if needed:
- Automation connection check, or not used:
- Test workflow and saved output:
- Actual hardware and memory observations:
- Settings or trigger words required by the model author:
- Error and fix:
- What remains unverified:

A matching hash identifies the downloaded bytes; it does not establish quality or compatibility.
"""


def _find_model() -> None:
    st.markdown(
        "Start from the workflow you want to run, then find its required model files. "
        "Civitai is a useful place to explore community models and example results; "
        "Hugging Face often holds the author's model card, versioned files and accompanying instructions. "
        "Use each author's model card and example settings to decide whether an upload fits your task."
    )
    st.info(
        "Our starter image preset: Checkpoint · SDXL 1.0 · SafeTensor. "
        "Open Use Civitai filters to plan your search. SD 1.5 and SD3 remain alternative families; "
        "a specific video, lip-sync or specialized workflow determines its own model requirements."
    )
    st.markdown(
        "**Adding ControlNet?** Choose weights that support your checkpoint's base family. "
        "For our SDXL starter, look for an SDXL-compatible ControlNet. Open **Choose the right file** "
        "for the pairing checklist, or choose ControlNet in **Use Civitai filters**. "
        "[Compatibility reference](https://docs.comfy.org/troubleshooting/model-issues)"
    )
    st.markdown(
        "**Build a shortlist from community signals.** First filter by the required file type and "
        "base-model family. Compare **Highest Rated** and **Most Downloaded** views, keeping the "
        "selected time period and whether it applies to publication or statistics in your notes."
    )
    st.caption(
        "Civitai references: [ranking options](https://github.com/civitai/civitai/blob/main/src/server/common/enums.ts) "
        "· [model filters](https://github.com/civitai/civitai/blob/main/src/server/schema/model.schema.ts)."
    )
    st.markdown(
        "For each promising result, open the **exact version**: compare example outputs, release date, "
        "recent comments, recommended settings and required companion files. Ratings and downloads "
        "help you discover candidates; your intended shot, compatible loader and a small trial decide "
        "which one fits. Record the sort, time mode, period and version in the model receipt before downloading."
    )
    cards = [
        ("Model", "Trained weights stored in one or more files. They supply learned behavior."),
        ("Node", "An operation in the graph: load a model, encode text, sample, decode or save."),
        ("Workflow", "The connected graph and settings. Sharing its JSON does not necessarily include its model files or custom nodes."),
    ]
    for column, (title, text) in zip(st.columns(3), cards):
        with column:
            with st.container(border=True):
                st.markdown(f"**{title}**")
                st.write(text)
    st.caption("Concept reference: [ComfyUI models](https://docs.comfy.org/basic-concepts/models).")
    st.markdown(
        "**Start the image branch with SDXL.** Use an SDXL-compatible checkpoint and follow "
        "its author's settings with the [official SDXL examples](https://comfyanonymous.github.io/ComfyUI_examples/sdxl/). "
        "The separate [first-generation guide](https://docs.comfy.org/get_started/first_generation) "
        "uses SD1.5 to teach the basic mechanics; keep each example paired with its intended model."
    )
    _tutorial_model()
    with st.expander("Before running · image size and KSampler"):
        render_generation_settings("help_model_settings")
    st.info(
        "For our scene rewrite, first choose the execution route. A hosted lip-sync partner node uses "
        "the provider's hosted model; a local workflow needs the files its own instructions name. "
        "Browsing image checkpoints alone does not set up dialogue replacement."
    )
    _civitai_node_pack()


def _tutorial_model() -> None:
    note = MODEL_TUTORIAL_BOOKMARK
    with st.expander("Tutorial bookmark · 07:26 / Juggernaut XL and model placement"):
        st.caption("2024 tutorial snapshot, captured in this learning trail on September 12, 2026. No download or test is recorded.")
        st.markdown(f'[Return to the tutorial at {note["timestamp"]}]({note["url"]}) · [Exact Civitai version page]({note["page"]})')
        st.table({
            "Shown in the screenshot": ["Model", "Selected version", "Base model", "File role", "Filename"],
            "Value": [note["model"], note["version"], note["base"], note["role"], note["filename"]],
        })
        st.markdown(
            "**Tutorial opinion to test:** the learner reports that the presenter prefers X's quality "
            "over Hyper. Keep this as a comparison hypothesis for those named versions. Follow each "
            "variant's own recommended sampler, steps and guidance settings; compare the same prompts "
            "and target size, then record visible quality, runtime and settings."
        )
        st.caption("The timestamp anchors the model-selection screenshot; the exact timing of the spoken X-versus-Hyper opinion was not supplied. The Civitai page could not be fetched during this review.")
        st.markdown("[Current publisher model card](https://huggingface.co/RunDiffusion/Juggernaut-X-v10) · Use the version page and exact filename to identify the tutorial artifact.")


def _civitai_node_pack() -> None:
    with st.expander("Optional integration · Civitai Comfy Nodes"):
        st.caption("For Comfy Cloud's model importer, use the Cloud imports & access tab. This optional node pack has its own authentication setup, described below.")
        st.link_button(
            "Open the official Civitai node repository",
            "https://github.com/civitai/civitai-comfy-nodes",
            use_container_width=True,
        )
        st.caption("Early preview · source reviewed September 12, 2026 · installation and generation untested here.")
        st.markdown(
            "The pack has two useful roles: run Civitai cloud recipes inside ComfyUI, "
            "or bring Civitai resources into a local workflow. Cloud jobs use Civitai's compute "
            "and Buzz billing; local generation still uses your own hardware. Its menus group "
            "image, video, audio, text, analysis, training and 3D operations. "
            "[Project overview](https://github.com/civitai/civitai-comfy-nodes)"
        )
        st.table(
            [
                {
                    "Node / feature": "Civitai Model Selector",
                    "Connection and purpose": "air (CIVITAI_AIR) selects a cloud resource; path supplies a local loader's filename input.",
                },
                {
                    "Node / feature": "Civitai LoRA Selector",
                    "Connection and purpose": "loras (CIVITAI_LORAS) describes a cloud stack; connected MODEL + CLIP also enables local download/application.",
                },
                {
                    "Node / feature": "Civitai Embedding Selector / Civitai ControlNet",
                    "Connection and purpose": "CIVITAI_EMBEDDINGS / CIVITAI_CONTROLNETS describe inputs to compatible Civitai recipe nodes.",
                },
                {
                    "Node / feature": "Civitai Auth",
                    "Connection and purpose": "api_config (CIVITAI_CONFIG) supplies optional authentication and endpoint configuration.",
                },
            ]
        )
        st.markdown(
            "**Choose the connection deliberately.** An AIR identifies a resource; it is not a loaded "
            "Comfy `MODEL`. For a local checkpoint, connect the selector's `path` to Load Checkpoint's "
            "`ckpt_name` widget after converting that widget to an input. The selector downloads "
            "only connected file outputs; its `air` output alone leaves weights remote. Current source "
            "also exposes companion encoder/VAE file outputs. "
            "[Selector implementation](https://github.com/civitai/civitai-comfy-nodes/blob/main/civitai_comfy_nodes/nodes_manual.py)"
        )
        st.markdown(
            "**When this helps:** repeated resource selection, LoRA combinations, or mixing cloud operations "
            "with an existing graph. A manual download remains a straightforward way to learn one exact "
            "file and loader. The pack's local downloader maps asset types into Comfy folders and reuses "
            "cached files; model compatibility still needs checking. "
            "[Local resource handling](https://github.com/civitai/civitai-comfy-nodes/blob/main/civitai_comfy_nodes/local_models.py)"
        )
        st.markdown(
            "**If choosing this pack later:**\n\n"
            "1. In ComfyUI Manager, find **Civitai Comfy Nodes**, publisher **civitai**, install and restart. "
            "For a source install, follow the README using the Python environment that runs ComfyUI.\n"
            "2. Connect through the pack's Civitai sidebar or configure `CIVITAI_API_TOKEN` in your "
            "ComfyUI environment. Civitai authentication and Buzz are separate from Comfy partner-node credentials and credits.\n"
            "3. Record the installed revision and test one matching example. Preview node/API behavior can change.\n\n"
            "[Installation](https://github.com/civitai/civitai-comfy-nodes#install) · "
            "[Credential resolution](https://github.com/civitai/civitai-comfy-nodes/blob/main/civitai_comfy_nodes/config.py)"
        )
        st.markdown(
            "**Civitai Link is another optional connection.** Pairing enables model-page downloads into "
            "the local installation. Removing a model through Link can delete its local file; "
            "Link is disabled in hosted Comfy Cloud sessions. "
            "[Link behavior](https://github.com/civitai/civitai-comfy-nodes#civitai-link)"
        )


def _controlnet_compatibility() -> None:
    st.markdown("#### ControlNet: match the family, then the control image")
    st.write(
        "ControlNet adds guidance from a reference such as an edge, depth or pose map. "
        "The ControlNet model is a weights file; Load ControlNet opens it, and Apply ControlNet "
        "adds its guidance to the generation. A preprocessor prepares the control image when needed."
    )
    st.table([
        {"Checkpoint family": "SD 1.5", "ControlNet choice": "Designed for SD 1.5", "Avoid": "Directly attaching SDXL ControlNet weights"},
        {"Checkpoint family": "SDXL — our starter", "ControlNet choice": "Designed for SDXL", "Avoid": "Directly attaching SD 1.5 ControlNet weights"},
        {"Checkpoint family": "Another architecture or specialized variant", "ControlNet choice": "The exact model and Apply node documented by its workflow", "Avoid": "Assuming an SDXL file works because it loads"},
    ])
    st.caption("[ComfyUI model compatibility](https://docs.comfy.org/troubleshooting/model-issues) · [ControlNet workflow and preprocessing](https://docs.comfy.org/tutorials/controlnet/controlnet)")
    st.markdown(
        "**Check before downloading:**\n\n"
        "1. Read the **Base Model** field on both exact version pages. Match the supported architecture; "
        "the model names and authors can differ.\n"
        "2. Match the control input to the model: a depth model expects its documented depth map, "
        "an edge model its edge map. Follow the prescribed preprocessor or supply a prepared map.\n"
        "3. Check the loader, Apply node and any companion files. Matching family is necessary, "
        "but does not prove every variant works.\n"
        "4. Compare a small baseline with and without ControlNet; save both results and settings. "
        "For shape/dimension errors, check compatibility before changing strength."
    )
    st.caption(
        "This pairing applies within the generation stage using ControlNet. A later stage can use "
        "another model family through a documented handoff. Preprocessors and standalone image upscalers "
        "have their own input requirements; they do not all need an SDXL label."
    )
    with st.expander("Tutorial capture · the SD 1.5 warning"):
        st.write(
            "The supplied Ep01 screenshot shows Juggernaut / Reborn with Base Model: SD 1.5 and "
            "a caption about pairing SD 1.5 ControlNet with SD 1.5. This differs from the earlier "
            "Juggernaut XL / SDXL example. Check the exact version's Base Model field each time."
        )
        st.caption(f"[Return to Ep01]({TUTORIAL_URL}) · No playback timestamp is visible in this capture. Recorded September 12, 2026; no ControlNet run is claimed.")
    st.caption("For the connected graph and individual node definitions, open ComfyUI guide → Node Atlas.")


def _choose_file() -> None:
    st.caption("These folder examples apply to a local ComfyUI installation. In Comfy Cloud, use Cloud imports & access and choose the destination in the import dialog.")
    st.caption("Working with a VAE? Open 03 / Workflow anatomy → VAE paths for bundled versus separate VAE sources, the required connections, and image-to-image use.")
    st.info(
        "Home for the tutorial's Juggernaut XL checkpoint: ComfyUI/models/checkpoints/. "
        "The asset's role determines the folder, regardless of whether it came from Civitai or another source."
    )
    st.code("ComfyUI/models/checkpoints/" + MODEL_TUTORIAL_BOOKMARK["filename"], language="text")
    st.caption("Example relative to the active ComfyUI installation. A Portable build normally nests this under ComfyUI_windows_portable/; use your configured model paths when they differ.")
    st.markdown(
        "**Preferred format: SafeTensor (`.safetensors`).** It stores tensors without pickle's arbitrary "
        "code-execution mechanism. Legacy `.ckpt` weights are commonly pickle-based. Prefer a compatible "
        "safetensors release and still check its source, model family and loader. Changing a filename's "
        "extension does not convert its format. "
        "[Safetensors format](https://huggingface.co/docs/safetensors/index) · "
        "[Pickle loading](https://huggingface.co/docs/hub/security-pickle)"
    )
    st.markdown(
        "**Read the model page before downloading.** Match the model family, exact version, file role, "
        "format and precision/quantization to the workflow's loader. Check required companion files "
        "and the author's model card, license and use terms. A similar filename or a shared "
        "`.safetensors` extension does not establish compatibility. "
        "[Model-card reference](https://huggingface.co/docs/hub/model-cards)"
    )
    _controlnet_compatibility()
    st.table(
        [
            {
                "File role": "Checkpoint",
                "What it supplies": "A model package; some image checkpoints bundle model, text encoder and VAE.",
                "Typical ComfyUI folder": "ComfyUI/models/checkpoints",
            },
            {
                "File role": "LoRA",
                "What it supplies": "An adaptation applied to a compatible base model.",
                "Typical ComfyUI folder": "ComfyUI/models/loras",
            },
            {
                "File role": "VAE",
                "What it supplies": "Conversion between image pixels and the model's latent representation.",
                "Typical ComfyUI folder": "ComfyUI/models/vae",
            },
            {
                "File role": "Diffusion model",
                "What it supplies": "The generation/denoising component in a workflow with separate model parts.",
                "Typical ComfyUI folder": "ComfyUI/models/diffusion_models",
            },
            {
                "File role": "Text encoder",
                "What it supplies": "Converts text into a representation the selected model can use.",
                "Typical ComfyUI folder": "ComfyUI/models/text_encoders",
            },
            {
                "File role": "ControlNet weights",
                "What it supplies": "Reference guidance for a compatible base-model family and control-image type.",
                "Typical ComfyUI folder": "ComfyUI/models/controlnet",
            },
            {
                "File role": "Upscaler weights",
                "What it supplies": "A supported image upscaling model.",
                "Typical ComfyUI folder": "ComfyUI/models/upscale_models",
            },
            {
                "File role": "Latent upscaler weights",
                "What it supplies": "Model-specific latent upscaling, such as the spatial upscaler in documented LTX templates; distinct from pixel upscaling.",
                "Typical ComfyUI folder": "ComfyUI/models/latent_upscale_models",
            },
            {
                "File role": "Textual-inversion embedding",
                "What it supplies": "A learned embedding for a compatible model family.",
                "Typical ComfyUI folder": "ComfyUI/models/embeddings",
            },
        ]
    )
    st.caption(
        "Illustrative default folders, relative to your actual installation. Follow the exact workflow/version "
        "instructions and configured model paths when they differ. Folder names: "
        "[official directory definitions](https://github.com/Comfy-Org/ComfyUI/blob/master/folder_paths.py). "
        "Component roles: [official image-workflow explanation](https://docs.comfy.org/tutorials/basic/text-to-image)."
    )
    st.markdown(
        "**Checkpoint is not a universal destination.** Put each file where its loader expects it; "
        "do not move every `.safetensors` file into `checkpoints`. Then refresh the model list or restart "
        "ComfyUI and confirm the exact file appears in the intended loader. "
        "[Model loading guidance](https://docs.comfy.org/get_started/first_generation)"
    )
    st.caption("Workflow JSON describes a graph and is opened/imported in ComfyUI. Custom-node packages contain code and have their own installation instructions. Neither belongs in the checkpoints folder.")
    st.caption("Video example: the [official LTX-2.3 template](https://docs.comfy.org/tutorials/video/ltx/ltx-2-3) separates checkpoint, LoRA, text-encoder and latent-upscaler files. Follow the selected task/variant's exact list rather than combining files from different templates.")
    with st.expander("A file is missing, or a model will not load"):
        st.markdown(
            "1. Confirm the workflow's model family and exact required filename.\n"
            "2. Check the file finished downloading and is in the configured folder for that loader.\n"
            "3. Check whether the workflow expects companion encoders, a VAE or a supported custom loader.\n"
            "4. Refresh/restart, select the file again and save the exact error if it still fails.\n"
            "5. Record what the error revealed before changing model variants."
        )


def _model_receipt() -> None:
    st.markdown(
        "Keep a small receipt alongside each experiment so another person can identify the exact "
        "weights and settings behind a result. Record the author, source URL, version/revision, "
        "filename, role, compatible base family, loader, destination and license link."
    )
    st.markdown(
        "If the publisher supplies a hash, record its algorithm and compare it with the downloaded "
        "file when checking integrity. A hash identifies bytes; it does not prove a model is suitable. "
        "Add the actual test output and status separately so **found**, **downloaded** and **tested** "
        "remain different milestones."
    )
    st.download_button(
        "Download a blank model receipt",
        data=_MODEL_RECEIPT,
        file_name="pathfinder-model-receipt.md",
        mime="text/markdown",
        key="help_models_receipt_download",
        use_container_width=True,
    )
    st.caption("This downloads a blank Markdown worksheet. Fill it in alongside your saved experiment files.")
    with st.expander("Preview the receipt"):
        st.code(_MODEL_RECEIPT, language="markdown")


def render() -> None:
    """Render inside the console's existing themed content area."""
    st.markdown("### Models & files")
    st.write("Know where to look, which file fits, and what to save for the next person.")
    st.caption(
        "Captured from your tutorial screenshot: Civitai as a model source. "
        "The timestamp was not visible. Reference guidance reviewed September 12, 2026."
    )
    for column, label, url in zip(
        st.columns(3),
        ["Explore Civitai", "Browse Hugging Face models", "Read ComfyUI model guidance"],
        ["https://civitai.com/", "https://huggingface.co/models", "https://docs.comfy.org/basic-concepts/models"],
    ):
        with column:
            st.link_button(label, url, use_container_width=True)
    find, filters, choose, access, receipt = st.tabs(["Find a model", "Use Civitai filters", "Choose the right file", "Cloud imports & access", "Keep a model receipt"])
    with find:
        _find_model()
    with filters:
        render_model_filters()
    with choose:
        _choose_file()
    with access:
        render_cloud_access("help_cloud_access_models")
    with receipt:
        _model_receipt()
