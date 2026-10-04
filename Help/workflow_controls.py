"""A task-based map of the tutorial menu; these controls only select explanations."""

import streamlit as st

from Help.workflow_lessons import EPISODE_URL


_OVERVIEW = "https://docs.comfy.org/interface/overview"
_KEYS = "https://docs.comfy.org/interface/shortcuts"
_FIRST = "https://docs.comfy.org/get_started/first_generation"
_SETTINGS = "https://docs.comfy.org/interface/settings/comfy"
_VIEW = "https://github.com/Comfy-Org/ComfyUI_frontend/blob/main/src/services/litegraphService.ts"
GROUPS = ("Run & inspect", "Save & exchange", "Canvas & navigation", "Models & nodes")

# Stable IDs keep selections distinct when the groups or renderer placement change.
CONTROLS = (
    {
        "id": "run", "group": GROUPS[0], "label": "Queue Prompt / Run",
        "role": "Submit generation", "now": "Run and queue controls; the current default shortcut is Ctrl+Enter (Cmd+Enter on macOS).",
        "meaning": "Submits the graph for validation and execution. A queued job can still fail before producing an output.",
        "try": "For your next planned test, start with one job and latent batch_size 1. Record the result or exact error.",
        "caution": "Running is separate from saving the workflow. Keep the graph and the generated output together.",
        "sources": (("Shortcuts", _KEYS), ("Interface overview", _OVERVIEW)),
    },
    {
        "id": "extra", "group": GROUPS[0], "label": "Extra options / Batch count / Auto Queue",
        "role": "Control repeated jobs", "now": "Look beside the Run control for batch count and available queue modes; labels vary by frontend.",
        "meaning": "The tutorial's batch count repeats queued jobs. Empty Latent Image's batch_size controls latent images within each job. Automatic queuing can keep submitting work.",
        "try": "Keep automatic queuing off while learning. Predict two jobs with one latent each versus one job with two latents before increasing either control.",
        "caution": "Job count alone does not tell you the number of saved files: that also depends on the graph's output branches and batches.",
        "sources": (("Queue settings", _SETTINGS + "#batch-count-limit"), ("Empty Latent Image", "https://docs.comfy.org/built-in-nodes/EmptyLatentImage")),
    },
    {
        "id": "queue", "group": GROUPS[0], "label": "Queue Front / View Queue / View History",
        "role": "Inspect work and queue order", "now": "Use the queue/history panel; the default Q shortcut toggles it. Queue-front has its own command.",
        "meaning": "Queue Front prioritizes a new submission ahead of pending jobs. Queue and history views help distinguish waiting, running and completed work.",
        "try": "Locate your last test and compare its status with the actual output or error. Find the Interrupt command before experimenting with repeated runs.",
        "caution": "Queue Front does not mean interrupt the job already running. History is not a substitute for exported graphs and retained outputs.",
        "sources": (("Queue and interrupt commands", _KEYS), ("Queue/history panel", _OVERVIEW)),
    },
    {
        "id": "save", "group": GROUPS[1], "label": "Save / Export workflow",
        "role": "Keep the recipe", "now": "Use the workflow's Save action for the workspace copy and Export for a portable editor JSON; menus vary.",
        "meaning": "Records the connected graph and its settings. It is different from the Save Image node that writes a generated image.",
        "try": "Export a named editor JSON, then reopen it in a separate workflow tab. Use Workflow anatomy → Save & load for the full checklist.",
        "caution": "A workflow export does not bundle model weights or custom-node packages. Keep dependencies and input files with your receipt.",
        "sources": (("Workflow export and opening", _FIRST),),
    },
    {
        "id": "load", "group": GROUPS[1], "label": "Load / Open workflow",
        "role": "Bring in a recipe", "now": "Workflows → Open, or the current Ctrl+O / Cmd+O shortcut. Supported editor JSON can also be dropped onto the canvas.",
        "meaning": "Opens an existing graph. An original PNG can also carry workflow metadata; a screenshot or stripped image cannot supply the missing graph.",
        "try": "Open the editable CFA example from 06 / Worked example. Inspect its requirements before attempting a run.",
        "caution": "Opening a workflow needs no Manager. Missing models or node packages are separate dependencies; successful opening does not prove generation works.",
        "sources": (("Opening workflows", _FIRST), ("Workflow metadata implementation", "https://github.com/Comfy-Org/ComfyUI/blob/master/nodes.py")),
    },
    {
        "id": "clear", "group": GROUPS[1], "label": "Clear",
        "role": "Remove the displayed graph", "now": "Find Clear workflow in your interface; a confirmation setting may be enabled.",
        "meaning": "Empties the graph on the canvas. It does not uninstall models or node packages.",
        "try": "Export your learning copy first. Use a separate blank workflow when you simply want room to practice.",
        "caution": "Clearing is optional before loading another graph. Export the current work before replacing or clearing it.",
        "sources": (("Clear confirmation", _SETTINGS + "#require-confirmation-when-clearing-workflow"),),
    },
    {
        "id": "share", "group": GROUPS[1], "label": "Share",
        "role": "Hand work to another person", "now": "Local sharing destinations depend on the installed integration. Comfy Cloud has a separate Share feature that creates a workflow link with referenced media.",
        "meaning": "Manager supplies the tutorial's Share button. For a portable handoff, retain the editor JSON, example output and dependency receipt.",
        "try": "Prepare those three artifacts and reopen the exported graph. See the Handoff milestone before using a service's publishing controls.",
        "caution": "A Cloud share link lets anyone with the link view its included inputs, outputs and media. Review that bundle first. Sharing also does not guarantee the recipient has every dependency.",
        "sources": (("Workflow export", _FIRST), ("Legacy Share integration", "https://github.com/Comfy-Org/ComfyUI-Manager/blob/main/js/comfyui-manager.js#L1556"), ("Comfy Cloud sharing", "https://docs.comfy.org/cloud/share-workflow")),
    },
    {
        "id": "default", "group": GROUPS[2], "label": "Load Default / Templates",
        "role": "Start from an example graph", "now": "The tutorial uses Load Default. Current interfaces also provide a Templates library.",
        "meaning": "Loads an example workflow, including that graph's nodes and settings. It is not a factory reset of your installation or preferences.",
        "try": "Keep your current graph, then open a simple template. Inspect the model family instead of assuming the default is SDXL.",
        "caution": "An example graph can still require model files you do not have.",
        "sources": (("Legacy Load Default", "https://github.com/Comfy-Org/ComfyUI_frontend/blob/main/src/scripts/ui.ts#L672"), ("Workflow templates", "https://docs.comfy.org/interface/features/template")),
    },
    {
        "id": "reset", "group": GROUPS[2], "label": "Reset View",
        "role": "Reset the viewpoint", "now": "Use the Reset View command when available; canvas controls and names depend on your frontend.",
        "meaning": "Resets canvas pan and zoom. The nodes retain their positions and connections.",
        "try": "Pan away from a learning graph, then compare Reset View with Zoom to fit. Observe which makes your graph visible.",
        "caution": "The screenshot's claim about restoring element positions is misleading. Reset View does not automatically arrange the nodes.",
        "sources": (("Reset View and Fit View implementation", _VIEW),),
    },
    {
        "id": "fit", "group": GROUPS[2], "label": "Zoom to fit / Fit View",
        "role": "Find the nodes on screen", "now": "Use the fit-view command or canvas control. Current shortcuts also provide fitting to selected nodes.",
        "meaning": "Adjusts the viewport to frame nodes. It changes what you see, not the graph's recipe.",
        "try": "Select a small connected section and fit the view to it. To frame the whole recipe, select all nodes first.",
        "caution": "Fitting, arranging boxes and changing wires are three different actions.",
        "sources": (("Fit View implementation", _VIEW), ("Configurable shortcuts", _KEYS)),
    },
    {
        "id": "clipspace", "group": GROUPS[2], "label": "Clipspace / Mask editing",
        "role": "Reuse or edit image inputs", "now": "Clipspace belongs to the older image-copy/edit flow; current image context menus offer mask-editing actions.",
        "meaning": "Provides an image clipboard and an editing handoff where supported. It is separate from CLIP text encoding.",
        "try": "Where available, use Copy(Clipspace) on Save Image, then Paste(Clipspace) on Load Image and open the Mask Editor. Keep the original image.",
        "caution": "Clipspace does not save your complete workflow. The available image actions depend on the node and frontend.",
        "sources": (("Clipspace and mask editing", "https://docs.comfy.org/tutorials/basic/inpaint#using-the-mask-editor"),),
    },
    {
        "id": "refresh", "group": GROUPS[3], "label": "Refresh",
        "role": "Refresh node definitions and model choices", "now": "Refresh node definitions is currently bound to R; consult Settings → Keybinding for your setup.",
        "meaning": "Updates the definitions and model choices available to the frontend, which can reveal a newly added local model.",
        "try": "After adding a model to its correct local folder, refresh and check the intended loader's exact filename. Cloud uses its import/catalog route.",
        "caution": "This is different from reloading the browser page or updating ComfyUI. It does not install a missing custom-node package.",
        "sources": (("Models and refresh", _OVERVIEW), ("Refresh command", _KEYS)),
    },
    {
        "id": "manager", "group": GROUPS[3], "label": "Manager",
        "role": "Manage supported local extensions", "now": "Desktop includes Manager. Portable/manual setups follow their version's Manager instructions. Cloud manages its available catalog.",
        "meaning": "Helps manage custom-node packages and related dependencies in supported local setups.",
        "try": "First identify your environment. For a missing node, find its exact package and check whether that environment supports it.",
        "caution": "Installing Manager on your PC does not add nodes to Comfy Cloud. Ordinary workflow opening does not require it.",
        "sources": (("Manager by installation route", "https://docs.comfy.org/manager/install"), ("Cloud node availability", "https://docs.comfy.org/get_started/cloud")),
    },
    {
        "id": "nodes", "group": GROUPS[3], "label": "Node Library / Add node search",
        "role": "Find operations already available", "now": "Open Nodes in the sidebar, or use the canvas's double-click quick search. Check your configured shortcuts.",
        "meaning": "Finds node types that your ComfyUI environment exposes. Each box you add is an instance of its selected type.",
        "try": "Find CLIP Text Encode and add two instances to a learning copy. Follow their separate prompt connections in the Trace milestone.",
        "caution": "Finding a node is different from installing its package. A model weight file is different again.",
        "sources": (("Node Library", _OVERVIEW), ("Node concepts", "https://docs.comfy.org/basic-concepts/nodes")),
    },
)


def controls_markdown():
    lines = ["# ComfyUI control guide", "", "A guide to the Episode 2 menu and current equivalents. Reviewed 2026-09-12.",
             "Interface placement and available actions vary by environment and version.", "",
             f"[Episode 2 menu walkthrough]({EPISODE_URL}&t=144s)", ""]
    for group in GROUPS:
        lines.extend(["## " + group, ""])
        for item in CONTROLS:
            if item["group"] != group:
                continue
            lines.extend(["### " + item["label"], "", "**Purpose:** " + item["role"], "",
                          item["meaning"], "", "**Find it:** " + item["now"], "",
                          "**Try it:** " + item["try"], "", "**Distinction:** " + item["caution"], "",
                          " · ".join(f"[{label}]({url})" for label, url in item["sources"]), ""])
    return "\n".join(lines)


def render(key_prefix="help_workflow_controls"):
    st.subheader("Know what a control changes")
    st.write("Use the tutorial's menu as a map: run work, keep the recipe, navigate the canvas, or manage available components.")
    st.caption("Select a control to read its explanation. This reference does not operate ComfyUI. Menu placement varies between the older tutorial, Desktop and Cloud.")
    group = st.radio("What are you trying to do?", GROUPS, horizontal=True, key=key_prefix + "_group")
    choices = [item for item in CONTROLS if item["group"] == group]
    index, detail = st.columns([1, 2])
    with index:
        selected = st.radio("Explore a control", [item["id"] for item in choices],
                            format_func=lambda value: next(item["label"] for item in choices if item["id"] == value),
                            key=key_prefix + "_item_" + str(GROUPS.index(group)))
        st.markdown(f"[Episode 2 · menu walkthrough]({EPISODE_URL}&t=144s)")
    item = next(item for item in choices if item["id"] == selected)
    with detail:
        with st.container(border=True):
            st.subheader(item["label"])
            st.caption(item["role"])
            st.write(item["meaning"])
            st.markdown("**Where to look now**")
            st.write(item["now"])
            st.info(item["caution"])
            st.markdown("**A small exercise**")
            st.write(item["try"])
            st.markdown(" · ".join(f"[{label}]({url})" for label, url in item["sources"]))
    with st.expander("See the whole control map"):
        st.table({"Area": [item["group"] for item in CONTROLS],
                  "Control": [item["label"] for item in CONTROLS],
                  "Purpose": [item["role"] for item in CONTROLS]})
    st.download_button("Download the control guide", controls_markdown(),
                       file_name="comfyui-control-guide.md", mime="text/markdown", key=key_prefix + "_download")
    st.caption("Next: Practice path → Find your way around a borrowed workflow. Record the controls you located in your own environment.")
