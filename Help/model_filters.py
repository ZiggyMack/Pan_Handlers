"""An interactive Civitai browsing plan; no catalog calls or model downloads."""

import html
import re
from datetime import date

import streamlit as st


PURPOSES = (
    "Starter image checkpoint",
    "LoRA for an existing image model",
    "Follow an existing video or specialized workflow",
    "ControlNet for an existing image model",
)
FAMILIES = ("SDXL 1.0", "SD 1.5", "SD3", "Match the exact workflow")
SORTS = ("Highest Rated", "Most Downloaded")
PERIODS = ("Month", "All Time", "Year", "Week", "Day")
PERIOD_BASES = ("Check Civitai current mode", "Published", "Statistics")
_STATE_KEY = "help_model_filter_draft"
_DEFAULTS = {
    "purpose": PURPOSES[0],
    "family": FAMILIES[0],
    "sort": SORTS[0],
    "period": PERIODS[0],
    "period_basis": PERIOD_BASES[0],
}
_SOURCE_LINKS = (
    ("Civitai filter controls", "https://github.com/civitai/civitai/blob/main/src/components/Model/Infinite/ModelFiltersDropdown.tsx"),
    ("Civitai filter definitions", "https://github.com/civitai/civitai-developer-docs/blob/main/site/reference/models.md"),
    ("Website period modes", "https://github.com/civitai/civitai/blob/main/src/server/schema/base.schema.ts"),
    ("Search and favorites period behavior", "https://github.com/civitai/civitai/blob/main/src/components/Filters/FeedFilters/ModelFeedFilters.tsx"),
    ("ComfyUI model roles and loaders", "https://docs.comfy.org/basic-concepts/models"),
    ("ControlNet family compatibility", "https://docs.comfy.org/troubleshooting/model-issues"),
    ("ControlNet control-image requirements", "https://docs.comfy.org/tutorials/controlnet/controlnet"),
)
_CONTROLNET_CHECK = (
    "For ControlNet, match the existing checkpoint's base family (SD 1.5 with SD 1.5; "
    "SDXL with SDXL), then check the exact variant and Apply node. Match the control map "
    "to the trained control type, such as depth or edges. A matching family alone is not a complete compatibility check."
)


def _draft():
    if _STATE_KEY not in st.session_state:
        st.session_state[_STATE_KEY] = dict(_DEFAULTS)
    return st.session_state[_STATE_KEY]


def _remember(field, widget_key):
    _draft()[field] = st.session_state[widget_key]


def _choice(label, field, options, **kwargs):
    key = "help_model_filter_widget_" + field
    if key not in st.session_state:
        st.session_state[key] = _draft()[field]
    st.selectbox(label, options, key=key, on_change=_remember, args=(field, key), **kwargs)


def _recommendations(plan):
    specialized = plan["purpose"] == PURPOSES[2]
    lora = plan["purpose"] == PURPOSES[1]
    controlnet = plan["purpose"] == PURPOSES[3]
    exact_family = specialized or plan["family"] == FAMILIES[3]
    if specialized:
        role = "Use the exact asset roles named by the workflow"
        role_reason = "A video or specialized recipe may require several separate model components."
        destination = "Follow each file's documented folder and loader"
        checkpoint_type = "All, only if the recipe calls for a checkpoint"
    elif controlnet:
        role = "ControlNet"
        role_reason = "Reference guidance for the image model you already use; inspect the supported control type."
        destination = "Usually ComfyUI/models/controlnet; follow the documented loader and Apply node"
        checkpoint_type = "Not needed for a ControlNet search"
    elif lora:
        role = "LoRA"
        role_reason = "An adaptation for the compatible model you already use."
        destination = "Usually ComfyUI/models/loras; use the matching LoRA loader"
        checkpoint_type = "Not needed for a LoRA search"
    else:
        role = "Checkpoint"
        role_reason = "Our starter image search targets a model package, with its contents checked on the version page."
        destination = "Usually ComfyUI/models/checkpoints; confirm the required loader"
        checkpoint_type = "All"
    family = "Match the exact workflow's model identifiers and loaders" if exact_family else plan["family"]
    family_reason = "Architecture must match the loader and companion files."
    if lora:
        family_reason = "Match the existing image model's family and supported version before choosing a LoRA."
    elif controlnet:
        family_reason = "Match the checkpoint used in this generation stage, then verify the exact ControlNet variant and control-image requirements."
    if plan["period_basis"] == PERIOD_BASES[0]:
        basis = "Confirm active time mode in Civitai"
        basis_reason = "A period can control listing recency or statistics; the website view affects its meaning."
    elif plan["period_basis"] == "Published":
        basis = "Published — confirm this mode on Civitai"
        basis_reason = "Treat the period as a cutoff for recently published or updated model versions."
    else:
        basis = "Statistics — confirm this mode on Civitai"
        basis_reason = "Use the chosen statistics window when comparing ranking signals."
    return [
        {"Filter / decision": "Model type", "Set it to": role, "Why": role_reason},
        {"Filter / decision": "Base model", "Set it to": family, "Why": family_reason},
        {"Filter / decision": "File format", "Set it to": "SafeTensor, when supplied and supported by the workflow", "Why": "The format alone does not establish family, loader compatibility or output quality."},
        {"Filter / decision": "Checkpoint type", "Set it to": checkpoint_type, "Why": "All leaves origin unrestricted; Trained and Merge describe origin rather than quality."},
        {"Filter / decision": "Sort", "Set it to": plan["sort"], "Why": "Use community signals to shortlist candidates, then inspect the exact version."},
        {"Filter / decision": "Time period", "Set it to": plan["period"], "Why": "Record the period together with its active mode and the date viewed."},
        {"Filter / decision": "Period basis", "Set it to": basis, "Why": basis_reason},
        {"Filter / decision": "On-site Generation / Made On-site", "Set it to": "Leave off for a general local search", "Why": "Site-generator support and training on Civitai do not establish local ComfyUI compatibility."},
        {"Filter / decision": "Hidden / archived", "Set it to": "Leave off for discovery; revisit for a known missing item", "Why": "These help rediscover items; an archived listing may no longer offer downloads."},
        {"Filter / decision": "Destination after choosing the file", "Set it to": destination, "Why": "The file's role determines where it belongs; Civitai downloads do not all go into checkpoints."},
    ]


def _plain_markdown(value):
    return re.sub(r"([\\`*_{}\[\]()#+.!|~>-])", r"\\\1", html.escape(str(value), quote=False))


def _plan_markdown(plan):
    lines = [
        "# Civitai filter plan", "",
        "This is a browsing plan, not live search results. No model has been selected, downloaded or tested by this planner.",
        "", f"Prepared: {date.today().isoformat()}", "",
        "## My selections", "",
    ]
    for label, field in (
        ("Purpose", "purpose"), ("Image-family preference", "family"),
        ("Sort", "sort"), ("Period", "period"), ("Period basis to check on Civitai", "period_basis"),
    ):
        lines.append(f"- {label}: {_plain_markdown(plan[field])}")
    if plan["purpose"] == PURPOSES[2]:
        lines.extend(["", "The saved image-family preference is inactive for this specialized workflow. Follow the exact project's model identifiers, loaders and required files."])
    lines.extend(["", "## Apply these decisions", ""])
    for row in _recommendations(plan):
        lines.extend([
            "**" + row["Filter / decision"] + ":** " + _plain_markdown(row["Set it to"]),
            "", _plain_markdown(row["Why"]), "",
        ])
    lines.extend([
        "## Before downloading", "",
        "Open the exact model version. Check its family, file role, loader, required companion files and author instructions. Record the version, filename, source and actual test result in the model receipt.",
        "", _CONTROLNET_CHECK,
        "", "The tutorial screenshot shows Month, All checkpoint types, SafeTensor and SDXL 1.0. Checkpoint as the model type is our starter recommendation; that selection was not confirmed in the screenshot. Website labels and available controls can change.",
        "", "## References", "",
    ])
    lines.extend(f"- [{title}]({url})" for title, url in _SOURCE_LINKS)
    return "\n".join(lines) + "\n"


def _filter_groups():
    with st.expander("Read the tutorial's filter panel"):
        st.caption("Visible screenshot choices: Month · All checkpoint types · SafeTensor · SDXL 1.0. Checkpoint as the model type is our starter recommendation; the screenshot does not confirm it was selected. This explains the captured panel, not a complete current menu.")
        st.table([
            {"Group": "Sort", "What it controls": "Highest Rated and Most Downloaded offer different community signals. Neither establishes fit for your shot or hardware."},
            {"Group": "Time period", "What it controls": "Month, All Time and shorter periods depend on the active mode: recently published/updated model versions or statistics. Search and favorites views can use statistics mode. Check the current description."},
            {"Group": "Model type", "What it controls": "The asset's role: a Checkpoint supplies model weights; a LoRA adapts a compatible model. Other roles need their own loaders and folders."},
            {"Group": "Checkpoint type", "What it controls": "All applies no origin restriction. Trained indicates trained/fine-tuned weights; Merge indicates combined checkpoints. These are not quality ranks."},
            {"Group": "Base model", "What it controls": "The architecture family, such as SDXL 1.0, SD 1.5 or SD3. Match the workflow and its companion files; the same file extension does not make families interchangeable."},
            {"Group": "Model status", "What it controls": "On-site Generation means supported by Civitai's generator. Made On-site means trained on Civitai. Early Access concerns access timing. These labels do not prove local compatibility or free access."},
            {"Group": "File format", "What it controls": "SafeTensor refers to the safetensors weight-file format. Prefer it where the selected workflow supports it; follow exact format or quantization requirements for specialized loaders."},
            {"Group": "Hidden / Include Archived", "What it controls": "Hidden refers to models your account has hidden. Archived items are a rediscovery case and may have unavailable files. The screenshot's archive control may differ from today's menu."},
        ])
        st.markdown("Source references: " + " · ".join(f"[{title}]({url})" for title, url in _SOURCE_LINKS[:4]))


def render():
    st.subheader("Turn the filter panel into a small search plan")
    st.write("For our starter image search, begin with SDXL 1.0 and prefer SafeTensor when compatible. Change the plan to match the model or workflow you actually want to use.")
    st.caption("This planner prepares your choices for Civitai. It does not search the live catalog, download files or assess a model's results.")
    _choice("What are you looking for?", "purpose", PURPOSES)
    plan = _draft()
    specialized = plan["purpose"] == PURPOSES[2]
    left, right = st.columns(2)
    with left:
        _choice("Image model family", "family", FAMILIES, disabled=specialized)
        _choice("Sort the shortlist", "sort", SORTS)
    with right:
        _choice("Time period", "period", PERIODS)
        _choice("What does the period mean in this Civitai view?", "period_basis", PERIOD_BASES)
    if specialized:
        st.info("Use the exact workflow's model identifiers, loaders and required files. The saved image-family preference above is inactive for this route; an SDXL image checkpoint does not set up a video or lip-sync workflow.")
    elif plan["purpose"] == PURPOSES[1]:
        st.info("Set the family to the image model you already use. Choose a LoRA that explicitly supports that family and version.")
    elif plan["purpose"] == PURPOSES[3]:
        st.info("Set Image model family to your existing checkpoint's family. " + _CONTROLNET_CHECK)
    elif plan["family"] == "SD3":
        st.info("Use an SD3 workflow that names its exact model version and loader. Confirm the text encoders and VAE it needs before downloading.")
    st.table(_recommendations(plan))
    st.markdown("**Next:** apply these choices on Civitai, open a promising model's exact version, and check its instructions before downloading. Keep the version, file role and destination in the model receipt.")
    st.download_button(
        "Download my Civitai filter plan", _plan_markdown(plan),
        file_name="civitai-filter-plan.md", mime="text/markdown", key="help_model_filter_download",
    )
    st.caption("Choices survive navigation in this session. Download the plan to keep it between visits.")
    _filter_groups()
