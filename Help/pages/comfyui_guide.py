"""ComfyUI guide: foundations, setup, workflow anatomy and nested practice lessons."""

from html import escape

import streamlit as st

from Help.content.catalog import (
    COMFY_PROJECT_LINKS, COMFY_REPO_URL, COMFY_TRADEOFFS, ENVIRONMENT_GUIDES,
    GLOSSARY, REQUIREMENTS_BOOKMARK, STEPS,
)
from Help.guides.cloud_access import render as render_cloud_access
from Help.guides.generation_settings import render as render_generation_settings
from Help.guides.model_library import render as render_model_library
from Help.guides.node_atlas import render as render_node_atlas
from Help.guides.prompt_wiring import render as render_prompt_wiring
from Help.guides.sampling_lab import render as render_sampling_lab
from Help.guides.tutorial_notes import render as render_tutorial_notes
from Help.guides.vae_paths import render as render_vae_paths
from Help.guides.worked_example import render as render_worked_example
from Help.guides.workflow_files import render as render_workflow_files
from Help.guides.workflow_lab import render as render_workflow_lab
from Help.state.journey import ENVIRONMENTS
from Help.state.session import (
    PATH_BY_ID, append_journal_entry, field, get_journey, go, select_step,
    set_note, set_step,
)
from Help.ui.components import hero, html, route_strip


def _steps():
    journey = get_journey()
    count = len(journey["completed_steps"])
    st.progress(count / len(STEPS), text=f"{count} of {len(STEPS)} checkpoints recorded · mark a step when you have its evidence")
    selected = st.selectbox(
        "Open a checkpoint", options=[s["id"] for s in STEPS], key="help_step_select",
        format_func=lambda value: next(f'{i:02d} / {s["title"]}' for i, s in enumerate(STEPS, 1) if s["id"] == value),
    )
    step = next(s for s in STEPS if s["id"] == selected)
    st.caption(f'COMFYUI / CHECKPOINT {next(i for i, s in enumerate(STEPS, 1) if s["id"] == selected):02d} / {step["title"].upper()}')
    instructions, evidence, trail = st.tabs(["Instructions", "Evidence & notes", "Trail overview"])
    with instructions:
        st.subheader(step["title"])
        st.write(step["summary"])
        if selected == "bridge_3d":
            st.caption("Optional for a pixels-only video. You can satisfy this checkpoint by recording why your project does not need an editable scene.")
        for i, action in enumerate(step["actions"], 1):
            st.markdown(f"{i}. {action}")
        html(f'<div class="help-callout"><strong>Keep this evidence</strong><p>{escape(step["checkpoint"])}</p></div>')
        for label, url in step["sources"]:
            st.markdown(f"[{label}]({url})")
        if selected == "first_video":
            st.info("Open Video workshop for the current source-clip transformation path. For frames, sound and export timing, use 07 / Workflow lab → Video & audio. Earlier tutorial examples retain their own versioned model requirements.")
        if selected == "bridge_3d":
            st.info("Another practice branch: render a simple Blender scene as a structure reference, then explore image editing with a style reference. Open 07 / Workflow lab → Video & audio. Generated image detail does not become editable geometry.")
        st.caption("Use Evidence & notes to record your result and mark this checkpoint.")
    with evidence:
        st.subheader("Leave the evidence with the step")
        st.write(step["checkpoint"])
        note_key = "help_widget_note_" + selected
        if note_key not in st.session_state:
            st.session_state[note_key] = journey["step_notes"].get(selected, "")
        st.text_area("My settings, result, or obstacle", key=note_key, max_chars=20000,
                     on_change=set_note, args=(selected, note_key),
                     placeholder="Record model names, workflow filename, settings, and what happened.")
        done_key = "help_widget_done_" + selected
        if done_key not in st.session_state:
            st.session_state[done_key] = selected in journey["completed_steps"]
        label = ("I saved the 3D evidence, or documented why this step does not apply" if selected == "bridge_3d"
                 else "I have completed this checkpoint and saved the evidence")
        st.checkbox(label, key=done_key,
                    on_change=set_step, args=(selected, done_key))
    with trail:
        st.subheader("The whole route, at a glance")
        st.table({
            "Checkpoint": [f'{i:02d} / {s["title"]}' for i, s in enumerate(STEPS, 1)],
            "Status": ["Recorded" if s["id"] in journey["completed_steps"] else "To explore" for s in STEPS],
            "Evidence to keep": [s["checkpoint"] for s in STEPS],
        })
        st.caption("Use the checkpoint selector above to move through the route. The 3D branch accepts a documented skip when the goal is a video clip only.")
    current = next(i for i, s in enumerate(STEPS) if s["id"] == selected)
    back, forward = st.columns(2)
    back.button("← Previous checkpoint", disabled=current == 0, use_container_width=True,
                on_click=select_step, args=(STEPS[max(0, current - 1)]["id"],))
    forward.button("Next checkpoint →", disabled=current == len(STEPS) - 1, use_container_width=True,
                   on_click=select_step, args=(STEPS[min(len(STEPS) - 1, current + 1)]["id"],))
    st.caption("Progress is self-reported. This guide does not inspect your renderer or verify files on your computer.")


def _setup():
    st.subheader("Choose where ComfyUI runs")
    st.write("The workflow is the recipe; the environment is where you run it. Choose these separately.")
    field(st.selectbox, "My ComfyUI environment", "environment", options=ENVIRONMENTS)
    st.markdown("[Check current OS and hardware requirements](https://docs.comfy.org/installation/system_requirements)")
    with st.expander("Tutorial bookmark · 03:20 / system requirements"):
        bookmark = REQUIREMENTS_BOOKMARK
        st.markdown(f'[Return to Episode 1 at {bookmark["timestamp"]}]({bookmark["url"]})')
        st.caption(bookmark["provenance"])
        st.info("These are the 2024 tutorial's minimum/recommended figures. Use them to understand the categories to check; use current official instructions for your actual setup.")
        st.table({
            "Category": [row["area"] for row in bookmark["rows"]],
            "Tutorial minimum (2024)": [row["minimum"] for row in bookmark["rows"]],
            "Tutorial recommended (2024)": [row["recommended"] for row in bookmark["rows"]],
            "What to check for your setup": [row["check"] for row in bookmark["rows"]],
        })
        st.markdown("**The lesson to carry forward:** distinguish system RAM from VRAM, check the exact workflow's requirements, and keep model/output storage in the plan. A successful first still is a separate milestone from a successful video.")
        st.markdown("[Current platform, Python and accelerator guidance](https://docs.comfy.org/installation/system_requirements) · "
                    "[Current manual environment instructions](https://docs.comfy.org/installation/manual_install)")
        st.caption(bookmark["status"])
    route_tabs = st.tabs([*ENVIRONMENT_GUIDES, "Models & files"])
    for tab, (name, guide) in zip(route_tabs, ENVIRONMENT_GUIDES.items()):
        with tab:
            st.markdown("**" + name + " / setup route**")
            st.write(guide["summary"])
            for i, action in enumerate(guide["steps"], 1):
                st.markdown(f"{i}. {action}")
            st.markdown("**Tradeoff:** " + guide["tradeoff"])
            st.markdown(f'[Current official {name} instructions]({guide["url"]})')
            if name == "Manual":
                st.caption(f"[Repository README]({COMFY_REPO_URL}#readme) · [Release notes]({COMFY_REPO_URL}/releases)")
            if name == "Cloud":
                render_cloud_access("help_cloud_access_route")
    with route_tabs[-1]:
        render_model_library()
    st.info("There is no single GPU-memory requirement for every workflow. Check the exact model, resolution, frame count and install route before downloading large files or paying for cloud time.")


def _anatomy():
    st.subheader("Read the first workflow")
    st.caption("A classic checkpoint-based text-to-image example. Video and newer model workflows can use different loaders and nodes.")
    st.info("Loading an existing recipe? Open Save & load below for the file-opening walkthrough, restored-settings checklist and a real practice workflow.")
    st.caption("Ready to practice Episode 2? Open 07 / Workflow lab for seven exercises, connection repairs and a workbook you can keep.")
    node_map, vae, settings, files, experiment, notes, glossary = st.tabs(["Node map", "VAE paths", "Size & sampler", "Save & load", "Controlled experiment", "Tutorial notes", "Glossary"])
    with node_map:
        html('<div class="help-pipeline"><span>Checkpoint + prompts</span><span>→</span>'
              '<span>Latent + sampler</span><span>→</span><span>VAE decode</span><span>→</span><span>Saved image</span></div>')
        st.table({
            "Node": ["Load Checkpoint", "CLIP Text Encode (positive / negative)", "Empty Latent Image", "KSampler", "VAE Decode", "Save Image"],
            "What it contributes": [
                "Model, text encoder and VAE outputs feed different parts of the graph.",
                "Encode the prompts as conditioning for the sampler.",
                "Sets the size and batch of the starting latent representation.",
                "Uses the model, conditioning, latent and seed to produce sampled latents.",
                "Converts sampled latents into visible pixels.",
                "Writes the image. Export the workflow separately as well.",
            ],
        })
        render_prompt_wiring("help_anatomy_prompts")
    with vae:
        render_vae_paths("help_anatomy_vae")
    with settings:
        render_generation_settings("help_anatomy_settings")
    with files:
        render_workflow_files("help_anatomy_files")
    with experiment:
        render_sampling_lab()
    with notes:
        render_tutorial_notes("help_anatomy_tutorial")
    with glossary:
        for term, definition in GLOSSARY.items():
            with st.expander(term):
                st.write(definition)
    st.markdown("[Official first-generation walkthrough](https://docs.comfy.org/get_started/first_generation)")


def _troubleshooting():
    for title, guidance in (
        ("The workflow asks for a missing model", "Read the model name and destination in the official template's instructions. Download the correct model variant, put it in the requested model folder, refresh the model list, and select it in the loader. A similarly named file may use a different architecture."),
        ("ControlNet fails with shape or dimension errors", "Check the exact checkpoint and ControlNet base families first: SD 1.5 pairs with SD 1.5, SDXL with SDXL. Also check the documented Apply node, companion files and expected control-map type. Matching socket colors do not establish model compatibility. See Models & files → Choose the right file and Node Atlas for the pairing walkthrough."),
        ("Nodes are missing or red", "Start with an official native template. Match its documented ComfyUI version and dependencies. Custom nodes are executable packages: review their source before installing, and record each installed version. Cloud only supports its available catalogue."),
        ("GPU out of memory", "Stop other GPU work, return to the template's documented settings, and check its hardware notes. Try a smaller supported resolution or frame count, batch size 1, or a smaller supported model. Do not assume that arbitrary dimensions or frame counts are valid."),
        ("The video flickers or the subject changes", "Simplify the shot to one subject and one motion, improve the reference image, and compare one change at a time. Keep failure clips too. For exact camera or geometry control, explore the Blender branch."),
        ("The tutorial's interface differs from mine", "The inspiration video dates from 2024. Match the idea to the current official documentation and record your app version. Avoid mixing instructions for Desktop, Portable and Manual installs."),
    ):
        with st.expander(title):
            st.write(guidance)
    st.markdown("[Official troubleshooting](https://docs.comfy.org/troubleshooting/overview)")
    st.markdown("[Model-family mismatch troubleshooting](https://docs.comfy.org/troubleshooting/model-issues)")
    st.markdown(f"[Search the ComfyUI issue tracker]({COMFY_REPO_URL}/issues)")
    st.caption("Compare the reported version, hardware and exact error with your setup. Keep those details in your checkpoint notes.")


def _fit():
    st.subheader("What ComfyUI unlocks — and what it asks of you")
    st.write("ComfyUI makes the recipe visible and reusable. For this project, that is a reason to explore it first: the process itself becomes something another person can follow.")
    benefits, alternatives, experiment = st.tabs(["Unlocks & costs", "When another route fits", "A small first experiment"])
    with benefits:
        st.table({
            "Advantage": [item["benefit"] for item in COMFY_TRADEOFFS],
            "What it unlocks": [item["unlock"] for item in COMFY_TRADEOFFS],
            "What you take on": [item["cost"] for item in COMFY_TRADEOFFS],
        })
        st.caption("Workflow iteration and rendering speed are different things. Runtime depends on the model, graph, settings and hardware. These benefits are not all exclusive to ComfyUI.")
        with st.expander("Make the downsides manageable", expanded=True):
            for item in COMFY_TRADEOFFS:
                st.markdown(f'**{item["benefit"]}:** {item["mitigation"]}')
        with st.expander("Later: make a working graph easier to use and share"):
            st.markdown("**[App Mode](https://docs.comfy.org/interface/app-mode):** Present selected inputs and outputs through a simpler interface once the workflow works.")
            st.markdown("**[Reusable subgraphs](https://docs.comfy.org/interface/features/subgraph):** Organize related nodes into named components that can be reused and opened for detail.")
            st.caption("Check each feature's frontend requirements. A simpler view still relies on the underlying workflow, models and dependencies. Worked examples for these features are a future guide expansion.")
    with alternatives:
        st.write("Keep the output and your preferred way of working in view. Choosing a simpler interaction for today's job is a valid decision.")
        for item in COMFY_TRADEOFFS:
            with st.expander(item["benefit"] + " / compare the options"):
                st.write(item["alternative"])
        st.button("Return to the full four-path comparison →", on_click=go, args=("Compare paths",))
        field(st.selectbox, "My chosen path", "chosen_path", options=list(PATH_BY_ID),
               format_func=lambda value: PATH_BY_ID[value]["name"])
        field(st.text_area, "Why this route? What am I trading off?", "decision_reason", max_chars=10000)
    with experiment:
        st.markdown("**Find out whether the graph helps you think.**")
        st.write("Use the setup and first-image checkpoints to open one official workflow and save a still. Fix the seed, change one prompt detail, and compare the results. Save the workflow and note whether you can explain its main connections.")
        st.write("If the graph makes the process clearer, continue to a short video. If navigating it gets in the way of your task, compare the forms in AUTOMATIC1111 or Forge and the canvas in Invoke before investing further.")
        st.info("Next: open 01 / Follow the steps. Start with the shot brief, then choose where ComfyUI runs. Your first success is one image plus its workflow.")
    st.markdown("Sources: [ComfyUI first generation](https://docs.comfy.org/get_started/first_generation) · "
                "[Workflow templates](https://docs.comfy.org/interface/features/template) · "
                "[System requirements](https://docs.comfy.org/installation/system_requirements) · "
                "[Invoke workflow editor](https://invoke.ai/features/workflows/editor-interface/)")


def render():
    hero("ACTIVE GUIDE / COMFYUI", "From first image to a repeatable shot.",
          "A small experiment at each step. Save what worked, what failed, and what someone else needs to reproduce it.")
    route_strip()
    st.markdown(" · ".join(f'[{link["title"]}]({link["url"]})' for link in COMFY_PROJECT_LINKS))
    if get_journey()["chosen_path"] != "comfyui":
        st.caption(f'Your recorded choice is {PATH_BY_ID[get_journey()["chosen_path"]]["name"]}. Browsing this guide does not change it.')
    st.subheader("ComfyUI command center")
    st.button("Apply these lessons to the video experiment →", on_click=go, args=("Video workshop",), key="help_scene_from_comfy")
    tabs = st.tabs(["00 / Fit & tradeoffs", "01 / Follow the steps", "02 / Setup routes", "03 / Workflow anatomy", "04 / Troubleshooting", "05 / Node Atlas", "06 / Worked example", "07 / Workflow lab"])
    for tab, renderer in zip(tabs, (_fit, _steps, _setup, _anatomy, _troubleshooting, render_node_atlas,
                                    lambda: render_worked_example("help_comfy_example"),
                                    lambda: render_workflow_lab(append_journal_entry))):
        with tab:
            renderer()
