"""One guide renderer, shared by the standalone app and operations dashboard."""

from datetime import date
from html import escape

import streamlit as st

from Help.catalog import (
    COMFY_PROJECT_LINKS, COMFY_REPO_URL, COMFY_TRADEOFFS, ENVIRONMENT_GUIDES,
    FUTURE_CHECKLIST, GLOSSARY, PATHS, REQUIREMENTS_BOOKMARK, SOURCES,
    STEPS, TUTORIAL_URL,
)
from Help.journey import (
    ENVIRONMENTS, OUTPUT_KINDS, dumps_journey, journey_markdown,
    loads_journey, new_journey, validate_journey,
)
from Help.theme import apply_theme
from Help.scene_content import SCENE_SOURCES
from Help.scene_lab import render as render_scene_lab
from Help.node_atlas import render as render_node_atlas
from Help.model_library import MODEL_SOURCES, render as render_model_library
from Help.cloud_access import render as render_cloud_access
from Help.worked_example import render as render_worked_example
from Help.prompt_wiring import render as render_prompt_wiring
from Help.generation_settings import render as render_generation_settings
from Help.tutorial_notes import render as render_tutorial_notes
from Help.workflow_files import render as render_workflow_files
from Help.workflow_lab import render as render_workflow_lab
from Help.vae_paths import render as render_vae_paths
from Help.sampling_lab import render as render_sampling_lab
from Help.video_workshop import render as render_video_workshop, render_entry as render_video_entry
from Help.video_routes import SOURCES as VIDEO_SOURCES
from Help.cfa_learning import SUMMARY as CFA_SUMMARY


SECTIONS = ("Start here", "Video workshop", "Rewrite a scene", "Compare paths", "ComfyUI guide", "Field journal", "Sources & roadmap")
PATH_BY_ID = {path["id"]: path for path in PATHS}
STATE_KEY = "help_journey"


def _journey():
    if STATE_KEY not in st.session_state:
        st.session_state[STATE_KEY] = new_journey()
    return st.session_state[STATE_KEY]


def _go(section):
    st.session_state["help_section"] = section


def _set_field(field, widget_key):
    _save_change({field: st.session_state[widget_key]})


def _save_change(changes):
    try:
        st.session_state[STATE_KEY] = validate_journey({**_journey(), **changes})
    except ValueError as error:
        st.session_state["help_save_error"] = f"Latest edit was not saved: {error} Download the existing journey before shortening this edit."
    else:
        st.session_state.pop("help_save_error", None)


def _set_step(step_id, widget_key):
    done = set(_journey()["completed_steps"])
    if st.session_state[widget_key]:
        done.add(step_id)
    else:
        done.discard(step_id)
    _save_change({"completed_steps": [s["id"] for s in STEPS if s["id"] in done]})


def _set_note(step_id, widget_key):
    _save_change({"step_notes": {**_journey()["step_notes"], step_id: st.session_state[widget_key]}})


def _field(kind, label, field, options=None, **kwargs):
    """Keep durable values separate from Streamlit's page-scoped widget keys."""
    key = "help_widget_" + field
    if key not in st.session_state:
        st.session_state[key] = _journey()[field]
    kwargs.update(key=key, on_change=_set_field, args=(field, key))
    if options is not None:
        return kind(label, options=options, **kwargs)
    return kind(label, **kwargs)


def _html(content):
    st.markdown(content, unsafe_allow_html=True)


def _hero(eyebrow, title, description):
    _html(f'<div class="help-hero"><div class="help-eyebrow">{escape(eyebrow)}</div>'
          f'<h1>{escape(title)}</h1><p>{escape(description)}</p></div>')


def _route_strip():
    labels = "".join(
        f'<span>{escape(path["name"])} · {"guide available" if path["id"] == "comfyui" else "guide planned"}</span>'
        for path in PATHS
    )
    _html(f'<div class="help-route-strip">{labels}</div>')


def _path_cards():
    """The Armada pattern: parallel path headers and compact tagged rows."""
    capabilities = {
        "automatic1111": [("Interface", "Forms & tabs", "strength"), ("Images", "Generate & refine", "strength"),
                          ("Extend", "Extension ecosystem", "strength"), ("Tradeoff", "Check compatibility", "tradeoff"),
                          ("Video", "Choose an extension / handoff", "tradeoff")],
        "forge": [("Interface", "Familiar WebUI", "strength"), ("Compute", "Resource management focus", "strength"),
                  ("Models", "Supported Flux workflows", "strength"), ("Tradeoff", "Benchmark on your hardware", "tradeoff"),
                  ("Video", "Choose a compatible workflow", "tradeoff")],
        "invoke": [("Interface", "Canvas & node workflows", "strength"), ("Control", "Brushes & inpainting", "strength"),
                   ("Refine", "Art direction & paintovers", "strength"), ("Tradeoff", "Image-centered workspace", "tradeoff"),
                   ("Video", "Plan an animation handoff", "tradeoff")],
        "comfyui": [("Interface", "Visible node graph", "strength"), ("Repeat", "Save & share workflows", "strength"),
                    ("Outputs", "Image, video & 3D examples", "strength"), ("Tradeoff", "Nodes & dependencies to learn", "tradeoff"),
                    ("Video", "Guided first-clip experiment", "strength")],
    }
    with st.expander("Pipeline capabilities · 4 paths / ComfyUI unpacked first", expanded=True):
        columns = []
        for path in PATHS:
            rows = []
            for badge, label, kind in capabilities[path["id"]]:
                rows.append(
                    f'<div class="help-capability-row" data-kind="{kind}">'
                    '<span class="help-status-dot" aria-hidden="true"></span>'
                    f'<span class="help-capability-tag">{escape(badge)}</span>'
                    f'<span class="help-capability-text">{escape(label)}</span></div>'
                )
            active = path["id"] == "comfyui"
            rows.append('<div class="help-capability-row" data-kind="next">'
                        f'<span class="help-status-dot{ "" if active else " planned"}" aria-hidden="true"></span>'
                        '<span class="help-capability-tag">Guide</span>'
                        f'<span class="help-capability-text">{"7 checkpoints available" if active else "Walkthrough planned"}</span></div>')
            columns.append(
                f'<article class="help-pipeline-column" data-path="{path["id"]}">'
                f'<div class="help-pipeline-head"><h3>{escape(path["name"])}</h3>'
                f'<p>{"First to unpack" if active else "Alternative path"}</p></div>'
                + "".join(rows) + f'<p class="help-column-note">{escape(path["tagline"])}</p></article>'
            )
        _html('<div class="help-armada-grid">' + "".join(columns) + '</div>')
        st.caption("Badges describe capabilities and tradeoffs. Guide status describes our coverage, not whether the tool is available.")
        st.button("Unpack ComfyUI →", on_click=_go, args=("ComfyUI guide",), type="primary", key="help_unpack_comfy")


def _downloads(location):
    journey = _journey()
    st.download_button(
        "Download journey · JSON", dumps_journey(journey),
        file_name="pathfinder-journey.json", mime="application/json",
        key="help_download_json_" + location, use_container_width=True,
    )
    st.download_button(
        "Download field guide · Markdown", journey_markdown(journey),
        file_name="pathfinder-field-guide.md", mime="text/markdown",
        key="help_download_md_" + location, use_container_width=True,
    )


def _sidebar():
    with st.sidebar:
        st.markdown("### 🧭 Pathfinder")
        st.caption("PAN HANDLERS / THE FIELD GUIDE")
        st.markdown("**A task. Several paths. A trail to follow.**")
        st.divider()
        for group, sections in (
            ("ORIENT", ("Start here", "Compare paths")),
            ("ACTIVE MISSION", ("Video workshop",)),
            ("OTHER SCENE TOOLS", ("Rewrite a scene",)),
            ("MAKE", ("ComfyUI guide", "Field journal")),
            ("KEEP EXPLORING", ("Sources & roadmap",)),
        ):
            st.caption(group)
            for section in sections:
                st.button(section, key="help_nav_" + section, use_container_width=True,
                          type="primary" if st.session_state["help_section"] == section else "secondary",
                          on_click=_go, args=(section,))
        st.divider()
        st.toggle("Matrix mode", key="help_matrix")
        count = len(_journey()["completed_steps"])
        st.caption(f"COMFYUI FOUNDATIONS · {count} / {len(STEPS)} CHECKPOINTS")
        st.progress(count / len(STEPS))
        with st.expander("Take your journey with you"):
            st.caption("Notes stay in this session. Download JSON before closing; restore it in Field journal next time.")
            _downloads("sidebar")
        st.caption("Active task: lifelike video · preserve the performance")


def _start():
    _hero("VIDEO FIRST / THE NEXT EXPERIMENT", "Keep the performance. Change the world.",
          "Start with your source material, borrow the right workflow, and work toward one convincing shot before finishing it in HD and 4K.")
    st.caption("PROJECT MEMORY / Pump worked example · newer CFA reference-edit stills awaiting acceptance · video production still ahead in the reviewed records.")
    render_video_entry(_go)
    st.divider()
    left, right = st.columns([1.5, 1], gap="large")
    with left:
        st.subheader("Keep the larger goal in view")
        _field(st.text_input, "Your shot or task", "goal", max_chars=4000,
               placeholder="Transform an existing clip while preserving its motion and performance")
        _field(st.radio, "What should the result contain?", "output_kind", options=OUTPUT_KINDS)
        kind = _journey()["output_kind"]
        if kind == "AI video":
            st.info("Generate a clip or edit an existing scene. Scene dialogue replacement starts with footage and speech; editable 3D geometry is a separate deliverable.")
        elif kind == "Editable 3D + AI":
            st.info("Plan for meshes, materials, cameras and an animation scene. Use ComfyUI for concepts or assets, then assemble and render in Blender.")
        else:
            st.info("Choose the kind of experiment: rewrite an existing scene, generate a new clip, or build an editable 3D scene. Each has a different first step.")
        buttons = st.columns(2)
        buttons[0].button("Compare all four paths →", on_click=_go, args=("Compare paths",),
                          use_container_width=True)
        buttons[1].button("What does ComfyUI unlock? →", on_click=_go, args=("ComfyUI guide",),
                          type="primary", use_container_width=True)
    with right:
        _html('<div class="help-callout"><div class="help-kicker">THE METHOD</div>'
              '<h3>Learn it. Try it. Leave a recipe.</h3>'
              '<p>01 / Compare the options and record your decision.</p>'
              '<p>02 / Make one small, repeatable experiment.</p>'
              '<p>03 / Keep the settings, result and lesson together.</p></div>')
        st.markdown("**Your first milestone**")
        st.write("One short source shot, one controlled visual change and a saved comparison. Accept the performance before making an HD master and reviewing a 4K derivative.")
        st.caption("This console is a guide and notebook. Rendering happens in the tool you choose.")
    with st.expander("Keep the other paths visible"):
        _path_cards()
        st.caption("All four tools remain valid options. ComfyUI is the first deep guide. Editable 3D and game development remain future branches.")
        st.button("Explore the dialogue-rewrite branch →", on_click=_go, args=("Rewrite a scene",), key="help_scene_home")
    st.divider()
    with st.expander("Where the idea started · pixaroma's ComfyUI series"):
        st.markdown(f"[Ep01 · Introduction and Installation]({TUTORIAL_URL})")
        st.markdown(f'**Captured learning point:** [{REQUIREMENTS_BOOKMARK["timestamp"]} · {REQUIREMENTS_BOOKMARK["title"]}]({REQUIREMENTS_BOOKMARK["url"]})')
        st.caption("The slide and its current setup considerations are saved in ComfyUI guide → Setup routes. This bookmark records where the learning conversation reached; it does not mark your setup complete.")
        st.caption("Published July 9, 2024. Use the series for concepts and the linked current docs for installation. The chapter references come from the public video description.")
        if st.checkbox("Load the YouTube player", key="help_video_player"):
            st.video(TUTORIAL_URL)
        st.write("00:00 Introduction · 02:40 Windows installation · 06:22 Models · 09:52 First image · 14:32 Save/load workflows · 18:47 Manager")


def _compare():
    _hero("DECISION DESK / FOUR VALID ROUTES", "Choose the path that fits.",
          "Compare the interaction, the strengths, and the work each route asks of you.")
    _path_cards()
    st.caption("Fit assessments are editorial judgments based on the official feature documentation, not performance benchmarks. “Planned” means the walkthrough here is still to be written.")
    st.table({
        "Path": [p["name"] for p in PATHS],
        "How you work": [p["interaction"] for p in PATHS],
        "Role in this video project": [p["video_fit"] for p in PATHS],
        "Our coverage": [p["status"] for p in PATHS],
    })
    for path in PATHS:
        with st.expander(path["name"] + " · strengths & tradeoffs", expanded=path["id"] == "comfyui"):
            left, right = st.columns(2)
            with left:
                st.markdown("**Reasons to choose it**")
                for item in path["strengths"]:
                    st.markdown("- " + item)
            with right:
                st.markdown("**What you take on**")
                for item in path["tradeoffs"]:
                    st.markdown("- " + item)
            st.markdown(f'[Official {path["name"]} project]({path["url"]})')
            if path["id"] != "comfyui":
                st.caption("Expansion reserved: setup → first output → video handoff → reproducible example. See Sources & roadmap.")
    with st.container(border=True):
        st.subheader("Keep the decision visible")
        _field(st.selectbox, "My chosen path", "chosen_path", options=list(PATH_BY_ID),
               format_func=lambda value: PATH_BY_ID[value]["name"])
        _field(st.text_area, "Why this route? What am I trading off?", "decision_reason", max_chars=10000,
               placeholder="For example: I want to see and share each step, so the node learning curve is worth it.")
        if _journey()["chosen_path"] != "comfyui":
            st.info("Your choice is recorded. This route's walkthrough is planned; its official project link is available above. The ComfyUI walkthrough remains available for comparison.")
        else:
            st.button("Follow the ComfyUI path →", on_click=_go, args=("ComfyUI guide",), type="primary")


def _append_journal_entry(entry):
    journey = _journey()
    st.session_state[STATE_KEY] = validate_journey({**journey, "entries": [*journey["entries"], entry]})


def _scene():
    _hero("RELATED BRANCH / SCENE DIALOGUE REWRITE", "Same scene. New dialogue.",
          "Understand what to preserve, what to replace, and how to turn one short experiment into a recipe someone else can follow.")
    _route_strip()
    st.caption("Start with the editing approach; choose tools for its individual stages. The ComfyUI foundations remain available alongside this dedicated mission.")
    render_scene_lab(_append_journal_entry)


def _video():
    _hero("ACTIVE MISSION / VIDEO WORKSHOP", "From source clip to accepted take.",
          "Choose an existing workflow for the change you want. Preserve the performance, compare honestly, and finish the take that earns it.")
    render_video_workshop(_append_journal_entry, _go)


def _steps():
    journey = _journey()
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
        _html(f'<div class="help-callout"><strong>Keep this evidence</strong><p>{escape(step["checkpoint"])}</p></div>')
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
                     on_change=_set_note, args=(selected, note_key),
                     placeholder="Record model names, workflow filename, settings, and what happened.")
        done_key = "help_widget_done_" + selected
        if done_key not in st.session_state:
            st.session_state[done_key] = selected in journey["completed_steps"]
        label = ("I saved the 3D evidence, or documented why this step does not apply" if selected == "bridge_3d"
                 else "I have completed this checkpoint and saved the evidence")
        st.checkbox(label, key=done_key,
                    on_change=_set_step, args=(selected, done_key))
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
                on_click=_select_step, args=(STEPS[max(0, current - 1)]["id"],))
    forward.button("Next checkpoint →", disabled=current == len(STEPS) - 1, use_container_width=True,
                   on_click=_select_step, args=(STEPS[min(len(STEPS) - 1, current + 1)]["id"],))
    st.caption("Progress is self-reported. This guide does not inspect your renderer or verify files on your computer.")


def _select_step(step_id):
    st.session_state["help_step_select"] = step_id


def _setup():
    st.subheader("Choose where ComfyUI runs")
    st.write("The workflow is the recipe; the environment is where you run it. Choose these separately.")
    _field(st.selectbox, "My ComfyUI environment", "environment", options=ENVIRONMENTS)
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
        _html('<div class="help-pipeline"><span>Checkpoint + prompts</span><span>→</span>'
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
        st.button("Return to the full four-path comparison →", on_click=_go, args=("Compare paths",))
        _field(st.selectbox, "My chosen path", "chosen_path", options=list(PATH_BY_ID),
               format_func=lambda value: PATH_BY_ID[value]["name"])
        _field(st.text_area, "Why this route? What am I trading off?", "decision_reason", max_chars=10000)
    with experiment:
        st.markdown("**Find out whether the graph helps you think.**")
        st.write("Use the setup and first-image checkpoints to open one official workflow and save a still. Fix the seed, change one prompt detail, and compare the results. Save the workflow and note whether you can explain its main connections.")
        st.write("If the graph makes the process clearer, continue to a short video. If navigating it gets in the way of your task, compare the forms in AUTOMATIC1111 or Forge and the canvas in Invoke before investing further.")
        st.info("Next: open 01 / Follow the steps. Start with the shot brief, then choose where ComfyUI runs. Your first success is one image plus its workflow.")
    st.markdown("Sources: [ComfyUI first generation](https://docs.comfy.org/get_started/first_generation) · "
                "[Workflow templates](https://docs.comfy.org/interface/features/template) · "
                "[System requirements](https://docs.comfy.org/installation/system_requirements) · "
                "[Invoke workflow editor](https://invoke.ai/features/workflows/editor-interface/)")


def _comfy():
    _hero("ACTIVE GUIDE / COMFYUI", "From first image to a repeatable shot.",
          "A small experiment at each step. Save what worked, what failed, and what someone else needs to reproduce it.")
    _route_strip()
    st.markdown(" · ".join(f'[{link["title"]}]({link["url"]})' for link in COMFY_PROJECT_LINKS))
    if _journey()["chosen_path"] != "comfyui":
        st.caption(f'Your recorded choice is {PATH_BY_ID[_journey()["chosen_path"]]["name"]}. Browsing this guide does not change it.')
    st.subheader("ComfyUI command center")
    st.button("Apply these lessons to the video experiment →", on_click=_go, args=("Video workshop",), key="help_scene_from_comfy")
    tabs = st.tabs(["00 / Fit & tradeoffs", "01 / Follow the steps", "02 / Setup routes", "03 / Workflow anatomy", "04 / Troubleshooting", "05 / Node Atlas", "06 / Worked example", "07 / Workflow lab"])
    for tab, renderer in zip(tabs, (_fit, _steps, _setup, _anatomy, _troubleshooting, render_node_atlas,
                                    lambda: render_worked_example("help_comfy_example"),
                                    lambda: render_workflow_lab(_append_journal_entry))):
        with tab:
            renderer()


def _journal():
    _hero("FIELD JOURNAL / YOUR FOOTSTEPS", "Keep the useful details.",
          "A result becomes a guide when the next person can see your decisions, settings, mistakes and next steps.")
    journey = _journey()
    st.info("Your journal lives in this browser session. Download JSON before closing or refreshing the app; restore that file below next time. Markdown gives you a readable copy to share.")
    with st.expander("Restore a saved journey"):
        uploaded = st.file_uploader("Journey JSON (up to 1 MB)", type=["json"], key="help_import_file")
        if st.button("Restore file and replace this session's journal", disabled=uploaded is None):
            try:
                restored = loads_journey(uploaded.getvalue())
            except ValueError as error:
                st.error(f"Could not restore the journey: {error}")
            else:
                st.session_state[STATE_KEY] = restored
                for key in list(st.session_state):
                    if key.startswith("help_widget_"):
                        del st.session_state[key]
                st.session_state["help_restored"] = True
                st.rerun()
    if st.session_state.pop("help_restored", False):
        st.success("Journey restored. Your decisions, notes and checkpoints are ready.")
    left, right = st.columns([1.5, 1], gap="large")
    with left:
        st.subheader("Add an experiment or lesson")
        if st.session_state.pop("help_clear_entry", False):
            for field in ("title", "observation", "next_step", "resource"):
                st.session_state["help_entry_" + field] = ""
        with st.form("help_entry_form"):
            title = st.text_input("Entry title", key="help_entry_title", max_chars=300, placeholder="First still / missing model resolved / camera test")
            observation = st.text_area("What did you try, and what happened?", key="help_entry_observation", max_chars=20000)
            next_step = st.text_area("What should the next person do?", key="help_entry_next_step", max_chars=10000)
            resource = st.text_input("Reference or result URL (optional)", key="help_entry_resource", max_chars=2048, placeholder="https://…")
            submitted = st.form_submit_button("Add to field journal", type="primary")
        if submitted:
            if not title.strip() or not observation.strip():
                st.error("Add a title and an observation so this entry is useful to follow.")
            else:
                entry = dict(date=date.today().isoformat(), title=title.strip(), observation=observation.strip(),
                             next_step=next_step.strip(), resource=resource.strip())
                candidate = {**journey, "entries": [*journey["entries"], entry]}
                try:
                    st.session_state[STATE_KEY] = validate_journey(candidate)
                except ValueError as error:
                    st.error(str(error))
                else:
                    st.session_state["help_clear_entry"] = True
                    st.rerun()
    with right:
        st.subheader("Your current recipe")
        st.text(journey["goal"] or "Set a shot brief in Start here.")
        st.write(f'Path: {PATH_BY_ID[journey["chosen_path"]]["name"]}')
        st.write(f'Output: {journey["output_kind"]} · Environment: {journey["environment"]}')
        st.write(f'{len(journey["completed_steps"])} checkpoints · {len(journey["entries"])} journal entries')
        _downloads("journal")
    st.divider()
    st.subheader("The trail so far")
    if not journey["entries"]:
        st.caption("No experiments recorded yet. Start with the decision that brought you here, or the first thing you tried.")
    for entry in reversed(journey["entries"]):
        # Render learner content as text; do not interpret it as HTML or Markdown.
        with st.container(border=True):
            st.text(entry["date"] + " / " + entry["title"])
            st.text(entry["observation"])
            if entry["next_step"]:
                st.markdown("**Next step**")
                st.text(entry["next_step"])
            if entry["resource"]:
                st.text(entry["resource"])
    with st.expander("Checkpoint notes"):
        for step in STEPS:
            st.markdown("**" + step["title"] + "**")
            st.text(journey["step_notes"].get(step["id"], "No notes yet."))


def _sources():
    _hero("SOURCEBOOK / ROOM TO GROW", "Keep the alternatives alive.",
          "ComfyUI gets the first walkthrough. Every other path keeps its place, its tradeoffs and a clear expansion plan.")
    _route_strip()
    tabs = st.tabs(["Expansion roadmap", "Sources", "About this console"])
    with tabs[0]:
        for path in PATHS:
            with st.expander(path["name"] + " · " + path["status"], expanded=path["id"] != "comfyui"):
                if path["id"] == "comfyui":
                    st.write("Available: environment choices, first still, workflow anatomy, video experiment, optional 3D branch, checkpoint notes and an exportable journal.")
                    st.write("Active mission: transform a source video's look, setting or characters while preserving motion and performance. Video workshop routes to researched templates, captures review evidence and leads from an accepted take to HD and reviewed 4K. The dialogue guide remains a related branch.")
                    st.write(CFA_SUMMARY)
                    st.write("Next video evidence: a reviewed output and its exact execution recipe. Game development remains a future branch.")
                else:
                    for item in FUTURE_CHECKLIST:
                        st.markdown("- " + item)
                st.markdown(f'[Official project]({path["url"]})')
    with tabs[1]:
        st.caption("Video workshop sources checked October 2, 2026. Earlier foundations and dialogue research retain their September 12 context. Public documentation does not verify an account's installed nodes or model access.")
        source_tabs = st.tabs(["Video workshop", "Toolkit & foundations", "Scene rewrite", "Models & files"])
        with source_tabs[0]:
            for title, url in VIDEO_SOURCES:
                st.markdown(f'[{title}]({url})')
        for source_tab, source_group in zip(source_tabs[1:], (SOURCES, SCENE_SOURCES, MODEL_SOURCES)):
            with source_tab:
                for source in source_group:
                    st.markdown(f'**[{source["title"]}]({source["url"]})**')
                    st.write(source["note"])
    with tabs[2]:
        st.write("Pathfinder is the reusable guide in Pan Handlers; CFA keeps the production experiments. The active task is high-resolution, lifelike video: change an existing shot while preserving motion and performance. Dialogue rewriting and editable 3D remain available branches; game development is parked for a later return.")
        st.write("The guide is shared; each visitor's journal belongs to their session. Download and restore JSON to carry your progress between visits, or share the Markdown field guide.")
        st.write("Visual roots: the Nyquist Ledger's teal palette, dark sidebar, serif headings and layered menus, with Pan Handlers' optional Matrix mode.")


def render(standalone=False):
    _journey()
    st.session_state.setdefault("help_section", SECTIONS[0])
    st.session_state.setdefault("help_matrix", False)
    if standalone:
        _sidebar()
        matrix = st.session_state["help_matrix"]
    else:
        matrix = st.session_state.get("matrix_mode", False)
    apply_theme(matrix_mode=matrix)
    if st.session_state.get("help_save_error"):
        st.error(st.session_state["help_save_error"])
    if not standalone:
        st.radio("Pathfinder / turn the page", SECTIONS, key="help_section", horizontal=True)
    renderers = dict(zip(SECTIONS, (_start, _video, _scene, _compare, _comfy, _journal, _sources)))
    renderers[st.session_state["help_section"]]()
    _html('<div class="help-footer">PAN HANDLERS / PATHFINDER · Compare honestly. Record the experiment. Pass it on.</div>')
