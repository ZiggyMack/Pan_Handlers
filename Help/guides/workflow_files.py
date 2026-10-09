"""A shared guide to saving and reopening graphs; no canvas or renderer actions."""

import streamlit as st

from Help.content.catalog import TUTORIAL_URL
from Help.guides.worked_example import CASE_DIR


_FIRST = "https://docs.comfy.org/get_started/first_generation"
_MODELS = "https://docs.comfy.org/troubleshooting/model-issues"
_CORE = "https://github.com/Comfy-Org/ComfyUI/blob/master/nodes.py#L1502"
_API = "https://docs.comfy.org/development/cloud/overview"
_MANAGER = "https://docs.comfy.org/manager/install"
_CLOUD = "https://docs.comfy.org/get_started/cloud"
_PRACTICE_FILE = "pump_concept_v001.editor.json"

STEPS = (
    ("Save", "Use Workflows → Export to download the editor workflow JSON. Give each useful model/version recipe a clear filename, such as my-sdxl-portrait-v01.json, and keep its input files and reference output nearby."),
    ("Clear — optional", "Save or export the work currently on the canvas first. Clear resets the displayed graph; it does not remove model weights or uninstall nodes. You can open another workflow directly without clearing first. Menu labels vary by frontend version."),
    ("Load", "In ComfyUI, choose Workflows → Open (Ctrl+O, or Cmd+O on macOS) and select the saved editor JSON. You can also drag a supported editor JSON or an original PNG containing workflow metadata onto the canvas. Ordinary JSON opening does not require Manager."),
    ("Verify", "Inspect the loaded graph and its exact model/variant before running. Check the preset, input files, companion models and available nodes. Save a new copy before changing a working recipe; opening a graph alone is not a successful render."),
)

VERIFY_ROWS = (
    ("Model and components", "Exact model/version and file role; matching text encoder, VAE and any LoRA or ControlNet; loader compatibility."),
    ("Generation preset", "Width/height, sampler, scheduler, steps, CFG, seed value and fixed/randomize control; denoise and model-specific controls where present."),
    ("Inputs and environment", "Source images/audio/video, missing custom-node packages and versions, and local versus Cloud availability."),
    ("Effective compiled settings", "Trace linked controls and inspect resolved prompt/model/sampling values in the current compiled graph. Stale named-widget values or old embedded API metadata can disagree with the visible canvas."),
    ("Output branches after reopening", "Reopen the actual exported editor JSON in a separate tab. Check shared wires, fixed seed control, active/muted Preview and Save nodes, and distinct output prefixes."),
)

BOOKMARKS = (
    (872, "14:32 · Save the working recipe"),
    (974, "16:14 · Save the SDXL version"),
    (983, "16:23 · Clear and load another graph"),
    (1020, "17:00 · Restore from image metadata"),
)

MANAGER_ROUTES = (
    ("Comfy Cloud", "Use its managed node catalog. Installing Manager on your PC does not add nodes to Cloud."),
    ("ComfyUI Desktop", "Current Desktop includes and enables Manager by default; use the included interface."),
    ("Current Portable / manual", "Follow the official guide for your version: install Manager dependencies in ComfyUI's Python environment and enable the built-in Manager."),
    ("Older local releases", "Use the version's supported installation method; the tutorial's custom_nodes clone method is a legacy route."),
)


def _bookmarks_markdown():
    return " · ".join(f"[{label}]({TUTORIAL_URL}&t={seconds}s)" for seconds, label in BOOKMARKS)


def checklist_markdown():
    lines = [
        "# Loading a saved workflow", "",
        "Save → optionally Clear → Load → Verify", "",
        "This is a practice checklist. No workflow has been opened, cleared or executed by this guide.", "",
    ]
    for number, (title, detail) in enumerate(STEPS, 1):
        lines.extend([f"## {number}. {title}", "", detail, ""])
    lines.extend(["## Check the restored recipe", ""])
    lines.extend(f"- [ ] {title}: {detail}" for title, detail in VERIFY_ROWS)
    lines.extend([
        "", "## Choose the right file", "",
        "Use the editor workflow JSON for this canvas exercise. An API submission graph stores execution inputs in a different structure; import/conversion handling depends on the client. It is not the preferred file for preserving the editor layout.", "",
        "A screenshot or an image with stripped metadata cannot restore the original graph. Use the original metadata-bearing PNG or exported JSON. A workflow does not bundle its model weights or custom-node packages.", "",
        "## Do I need ComfyUI Manager?", "",
        "Opening an ordinary workflow JSON does not require Manager. Manager helps manage local custom-node packages; manual package installation is another route.", "",
        *(f"- {route}: {guidance}" for route, guidance in MANAGER_ROUTES), "",
        f"[Manager installation by route]({_MANAGER}) · [Cloud node availability]({_CLOUD})", "",
        "## Practice with the real CFA sample", "",
        "Download pump_concept_v001.editor.json from Pathfinder's Save & load guide, or ComfyUI guide → 06 / Worked example → Open the recipe. Inspect it in ComfyUI without queuing a run.", "",
        "This example uses Z-Image with separate diffusion-model, text-encoder and VAE loaders. Its settings differ from the SDXL starter preference, and no weights are bundled. The saved seed control is randomize; for a controlled comparison, explicitly restore seed 42 and fixed control. Check the worked example's full recipe before running.", "",
        "## My reopening evidence", "",
        "- Workflow filename and version:", "- Loaded model/variant and preset:",
        "- Missing files or nodes, if any:", "- Copy saved before changes:",
        "- Effective compiled settings / exact graph revision:", "- Active outputs and unique prefixes:",
        "- Actual run/output result, only if tested:", "- Next decision and reason:", "",
        "Reopening checks the saved graph; it does not execute or accept a result. In the Controlled experiment or Image-to-image comparison, keep problem, lesson/source, recipe rationale, one changed variable, success check and self-reported outcome with the downloadable plan. Journal v1 stays separate.", "",
        "## Tutorial bookmarks", "", _bookmarks_markdown(), "",
        "These moments describe the learner's 2024 tutorial. Use current menu and installation guidance for your version.", "",
        "## Official references", "",
        f"- [Export, open and restore workflows]({_FIRST})",
        f"- [Model compatibility]({_MODELS})",
        f"- [Save Image and optional PNG metadata]({_CORE})",
        f"- [API submission and output handling]({_API})", "",
    ])
    return "\n".join(lines)


def render(key_prefix="help_workflow_files"):
    st.subheader("Loading a saved workflow")
    st.info("To reopen your recipe: ComfyUI → Workflows → Open → select your editor workflow JSON. Clear is optional; save the current canvas first.")
    st.markdown("**Save → optionally Clear → Load → Verify**")
    for number, (title, detail) in enumerate(STEPS, 1):
        st.markdown(f"**{number}. {title}**")
        st.write(detail)
    st.caption(f"[Current official save/open instructions]({_FIRST})")
    st.table({"After loading, check": [row[0] for row in VERIFY_ROWS],
              "What to inspect": [row[1] for row in VERIFY_ROWS]})
    with st.expander("Do I need ComfyUI Manager?"):
        st.write("Ordinary workflow JSON opens without Manager. Manager helps install, update and inspect local custom-node packages when a workflow needs them; manual installation is another route.")
        st.table({"Your setup": [row[0] for row in MANAGER_ROUTES], "What to do": [row[1] for row in MANAGER_ROUTES]})
        st.markdown(f"[Current Manager installation instructions]({_MANAGER}) · [Find missing nodes](https://docs.comfy.org/manager/pack-management) · [Cloud versus local]({_CLOUD})")
    with st.expander("The file opens differently than expected"):
        st.markdown("**Editor JSON versus API graph:** choose the editor-save file for this canvas exercise. API submission JSON describes execution inputs in another structure; client support for importing or converting it varies. Use the editor file when you want the saved layout.")
        st.markdown("**An image does not restore the graph:** use the original PNG with workflow metadata. Screenshots and images whose metadata was stripped do not carry that recipe. Keep an exported JSON copy too.")
        st.markdown("**The graph opens with missing items:** loading JSON does not install model weights or custom-node packages. Read the missing item names and the recipe's instructions. Manager can help with local custom nodes; check Cloud's available catalog for a Cloud workflow. Open Do I need ComfyUI Manager? above for your install route.")
        st.markdown(f"[PNG metadata behavior]({_CORE}) · [Model compatibility and missing files]({_MODELS}) · [API workflow context]({_API})")
    with st.expander("Practice loading our real worked example"):
        st.write("Download this editor graph and open it in ComfyUI to inspect the canvas. The full evidence and settings are in ComfyUI guide → 06 / Worked example → Open the recipe.")
        st.download_button("Download practice editor workflow", (CASE_DIR / _PRACTICE_FILE).read_bytes(),
                           file_name=_PRACTICE_FILE, mime="application/json", key=key_prefix + "_practice_editor")
        st.caption("This CFA pump example uses Z-Image and separate model, text-encoder and VAE loaders. It is a different recipe from the SDXL starter branch. No model weights are bundled, and downloading it does not queue a run.")
        st.write("Its saved seed control is randomize. For a controlled comparison, explicitly restore seed 42 and fixed control; review the worked example's full model/settings list before running.")
    st.markdown("**Follow the tutorial moments**")
    st.markdown(_bookmarks_markdown())
    st.caption("Bookmarks describe the 2024 tutorial. Menu labels and installation behavior may differ in your current version.")
    st.download_button("Download the save / load checklist", checklist_markdown(),
                       file_name="comfyui-save-load-checklist.md", mime="text/markdown",
                       key=key_prefix + "_checklist")
