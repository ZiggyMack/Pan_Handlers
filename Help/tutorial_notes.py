"""Annotated learner transcript bookmarks; no installation or rendering actions."""

import streamlit as st

from Help.catalog import TUTORIAL_URL
from Help.episode_three import EPISODE_TITLE as EP3_TITLE, EPISODE_URL as EP3_URL, LESSONS as EP3_LESSONS
from Help.episode_four import EPISODE_TITLE as EP4_TITLE, EPISODE_URL as EP4_URL, LESSONS as EP4_LESSONS
from Help.additional_guide import GUIDE_TITLE, GUIDE_URL, GUIDE_CREATOR, GUIDE_PROVENANCE, LESSONS as ADDITIONAL_LESSONS
from Help import creative_control_guide as creative
from Help import cfa_learning


REVIEWED = "September 12, 2026"
_FIRST = "https://docs.comfy.org/get_started/first_generation"
_CORE = "https://github.com/Comfy-Org/ComfyUI/blob/master/nodes.py"
_CACHE = "https://docs.comfy.org/custom-nodes/backend/server_overview"
_EXECUTION = "https://docs.comfy.org/development/comfyui-server/comms_messages"
_SAMPLER = "https://docs.comfy.org/built-in-nodes/sampling/ksampler"
_CARDS = "https://huggingface.co/docs/hub/model-cards"
_MANAGER = "https://docs.comfy.org/manager/install"
_PACKS = "https://docs.comfy.org/manager/pack-management"
_CLOUD = "https://docs.comfy.org/get_started/cloud"
_PORTABLE = "https://docs.comfy.org/installation/comfyui_portable_windows"

LESSONS = (
    {
        "seconds": 593, "title": "Refresh after adding a model",
        "takeaway": "A downloaded file and a refreshed loader list are separate steps.",
        "observed": "The narrator refreshes the already-open interface so the newly downloaded Reborn and SDXL models appear.",
        "apply": "Wait for the file to finish downloading into the folder for its role. Refresh model lists and select the exact file in the loader. Current first-generation docs describe R to refresh object definitions; if the file remains absent, check its location and restart if needed. Use Cloud's import/catalog route for a Cloud model.",
        "keep": "The exact filename, destination, and whether the loader now recognizes it.",
        "sources": (("Refresh and model locations", _FIRST),),
    },
    {
        "seconds": 620, "title": "Execution, loading and caching",
        "takeaway": "Watch the run, then inspect the saved output; measure cold and repeat runs separately.",
        "observed": "The tutorial follows highlighted nodes, switches models, and reports a much quicker repeat generation after an initial load.",
        "apply": "A repeat may benefit from an already-loaded model or cached node outputs. Those are separate effects; the transcript does not establish their individual contribution. ComfyUI can reuse unchanged results, so every node need not visibly run again. Check run completion/errors and open the saved file. Node colors and the narrator's timing do not establish your own result or speed.",
        "keep": "First-run and repeat timings, what changed (including the seed), and the actual output or error.",
        "sources": (("How node caching works", _CACHE), ("Completion, cached execution and errors", _EXECUTION)),
    },
    {
        "seconds": 679, "title": "Follow the prompt through the graph",
        "takeaway": "Encode text, sample latents, decode pixels, then save.",
        "observed": "Two CLIP Text Encode instances describe the wanted bottle and unwanted features, then feed KSampler; VAE Decode and Save Image finish the chain.",
        "apply": "The checkpoint's CLIP can feed both encoders. Their CONDITIONING connections to KSampler's positive and negative inputs determine their roles. The sampler returns LATENT data; VAE Decode turns it into IMAGE data. Negative guidance depends on the model/settings and does not guarantee removal.",
        "keep": "A graph whose prompt branches you can trace, plus its saved image. Trace the four prompt connections in Workflow anatomy → Node map.",
        "sources": (("Core encoder and sampler definitions", _CORE), ("KSampler controls", _SAMPLER)),
    },
    {
        "seconds": 717, "title": "Read the exact model version's instructions",
        "takeaway": "Resolution and generation settings belong with the chosen model and variant.",
        "observed": "The narrator reads recommended dimensions and generation settings on the model page before changing the graph.",
        "apply": "Check the selected version's model card, example workflow, supported dimensions and companion files. Treat SD1.5 and SDXL as separate model choices. Use the selected model's recommended starting settings and compare a small result; dimensions in this tutorial are examples, not universal ceilings or guarantees.",
        "keep": "Model/version, normal or accelerated variant, source page and the settings actually tested.",
        "sources": (("Model cards and usage context", _CARDS), ("ComfyUI model compatibility", "https://docs.comfy.org/troubleshooting/model-issues")),
        "related": ((750, "Model-specific sizing"), (795, "KSampler settings")),
    },
    {
        "seconds": 795, "title": "Sampler and scheduler are different controls",
        "takeaway": "Translate a model-page preset into the correct fields.",
        "observed": "For the historical Reborn example, the narrator chooses 512 × 768, sampler dpmpp_2m, scheduler karras, 35 steps and CFG 7. Example prompts are copied while the seed is left random.",
        "apply": "The sampler selects the sampling method; the scheduler sets the noise schedule. A page's DPM++ 2M Karras preset therefore spans two fields in this classic KSampler. Keep these numbers attached to the tutorial's Reborn example. Follow an SDXL or specialized model's own instructions instead of inheriting the preset. Fix the seed for a controlled comparison; matching prompts alone does not reproduce an example.",
        "keep": "Sampler, scheduler, steps, CFG, dimensions, seed and seed-control behavior together.",
        "sources": (("KSampler parameter meanings", _SAMPLER), ("Current core settings", _CORE + "#L1445")),
    },
    {
        "seconds": 872, "title": "Save a recipe for each model and variant",
        "takeaway": "Name and reopen the working graph before changing models.",
        "observed": "At 14:32 the Reborn workflow is saved. At 15:09 the narrator checks the SDXL normal variant's instructions separately from Hyper, then saves that workflow at 16:14. The preference for its image quality is the narrator's assessment.",
        "apply": "Export a descriptively named workflow JSON for each useful model/variant recipe, then reopen it to check settings. For example: reborn-sd15-portrait-v01.json and my-sdxl-still-v01.json. The JSON records a graph; model weights, source files and custom-node dependencies still need to be available. Save a baseline before updates or experiments.",
        "keep": "Workflow JSON, exact model/variant and node versions, input files and a reference output.",
        "sources": (("Export and open workflow JSON", _FIRST),),
        "related": ((909, "SDXL normal versus Hyper"), (974, "Save the SDXL workflow")),
    },
    {
        "seconds": 1004, "title": "Keep the image and its workflow metadata",
        "takeaway": "A PNG can carry a recipe; keep an explicit JSON copy too.",
        "observed": "The narrator opens the local output folder and drags generated images onto the canvas to restore their different workflows.",
        "apply": "Save Image normally writes to the configured ComfyUI output directory, and a PNG with workflow metadata can reopen its graph. Metadata may be disabled or stripped by image processing or sharing, so test the original file and keep the exported JSON separately. A screenshot of the picture is not the original metadata-bearing PNG. Download Cloud outputs to retain a local copy.",
        "keep": "The original PNG and exported workflow JSON, reopened once to confirm what they contain.",
        "sources": (("Open workflows from images or JSON", _FIRST), ("Save Image and optional metadata", _CORE + "#L1502")),
    },
    {
        "seconds": 1046, "title": "The local server and its launcher",
        "takeaway": "A browser tab depends on the ComfyUI process behind it.",
        "observed": "In the Windows Portable demonstration, closing the command window stops ComfyUI. A desktop shortcut to run_nvidia_gpu.bat makes reopening that installation easier.",
        "apply": "For that Portable route, keep the launched server running while using its browser interface. A shortcut should target your actual installation's supported launcher; it does not install another copy. Desktop uses its app launcher and Comfy Cloud uses its hosted service, so follow the route you chose. Save a workflow before shutting down.",
        "keep": "Install route, version, launcher location and the saved workflow to reopen.",
        "sources": (("Current Windows Portable launchers", _PORTABLE), ("Cloud versus local", _CLOUD)),
    },
    {
        "seconds": 1128, "title": "Manager helps with dependencies; opening JSON is built in",
        "takeaway": "Use the Manager instructions for your installation and inspect missing packages.",
        "observed": "The older tutorial clones Manager into custom_nodes, restarts, and demonstrates updates and finding missing custom nodes from another person's workflow.",
        "apply": "Opening an ordinary workflow JSON is a built-in feature. Manager helps manage custom-node packages when the graph needs them. Current Desktop includes Manager; current Portable and manual instructions describe installing its dependencies and enabling the built-in Manager. The old clone method is a legacy route. Cloud provides a managed node catalog, so a local Manager install does not add nodes to Cloud.",
        "keep": "Missing node/package names, required versions and the selected install route. Review the package instructions, preserve a working baseline, and make a deliberate update before testing again.",
        "sources": (("Manager by installation route", _MANAGER), ("Find and manage missing nodes", _PACKS), ("Cloud's managed node catalog", _CLOUD), ("Built-in JSON opening", _FIRST)),
    },
)


def _stamp(seconds):
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


_EPISODES = {
    "ep1": {"label": "Episode 1 · Introduction and installation", "number": 1,
            "title": "Episode 1 · annotated tutorial notes", "download": "Episode 1",
            "filename": "comfyui-episode-1-annotated-notes.md",
            "url": TUTORIAL_URL, "lessons": LESSONS, "coverage": "09:53–21:06"},
    "ep3": {"label": "Episode 3 · TXT2IMG Basics", "number": 3,
            "title": "Episode 3 · annotated tutorial notes", "download": "Episode 3",
            "filename": "comfyui-episode-3-annotated-notes.md",
            "url": EP3_URL, "lessons": EP3_LESSONS, "coverage": "00:21–20:26"},
    "additional": {"label": "Max Novak · Video, audio and editing workflows",
                   "title": GUIDE_TITLE + " · annotated notes", "download": "Max Novak guide",
                   "filename": "comfyui-max-novak-annotated-notes.md",
                   "url": GUIDE_URL, "lessons": ADDITIONAL_LESSONS, "coverage": "00:00–21:52",
                   "provenance": GUIDE_PROVENANCE},
    "ep4": {"label": "Episode 4 · IMG2IMG and LoRA Basics", "number": 4,
            "title": "Episode 4 · annotated tutorial notes", "download": "Episode 4",
            "filename": "comfyui-episode-4-annotated-notes.md",
            "url": EP4_URL, "lessons": EP4_LESSONS, "coverage": "00:00–17:21"},
    "nkd": {"label": "Spanish creator · Creative control / NKD", "title": creative.GUIDE_TITLE,
            "download": "Spanish creative-control guide", "filename": "comfyui-creative-control-translated-notes.md",
            "url": creative.GUIDE_URL, "lessons": creative.LESSONS, "coverage": "00:00–13:53",
            "provenance": creative.GUIDE_PROVENANCE, "reviewed": creative.REVIEWED},
}


def _video_link(seconds, label=None, url=TUTORIAL_URL):
    if not url:
        return f"Transcript · {_stamp(seconds)} (video URL not verified)"
    separator = "&" if "?" in url else "?"
    return f'[{label or _stamp(seconds)}]({url}{separator}t={seconds}s)'


def notes_markdown(episode="ep1"):
    """Export the same annotations shown in the guide, without learner state."""
    selected = _EPISODES[episode]
    lines = [
        "# " + selected["title"], "",
        selected.get("provenance", f"Based on the learner-supplied {selected['coverage']} transcript. Historical demonstrations are separate from current instructions."),
        "", f"Primary references reviewed {selected.get('reviewed', REVIEWED)}. These notes do not confirm an installation or generated result.", "",
    ]
    if episode == "nkd":
        lines.extend([creative.practice_markdown(), "## CFA lessons already supported by records", "",
                      cfa_learning.SUMMARY, "", "Source record: " + cfa_learning.SOURCE_PATH, ""])
        for lesson in cfa_learning.LESSONS:
            lines.extend(["### " + lesson["title"], "", "**Recorded observation:** " + lesson["observation"], "",
                          "**Reusable method:** " + lesson["apply"], "", "Evidence path relative to Help: " + lesson["evidence"], ""])
        lines.extend(["## Timestamped English annotations", ""])
    for lesson in selected["lessons"]:
        lines.extend([
            f'## {_stamp(lesson["seconds"])} · {lesson["title"]}', "",
            _video_link(lesson["seconds"], "Return to the tutorial", selected["url"]), "",
            "**Takeaway:** " + lesson["takeaway"], "",
            "**In the supplied transcript:** " + lesson["observed"], "",
            "**Apply it today:** " + lesson["apply"], "",
            "**Keep with your experiment:** " + lesson["keep"], "",
        ])
        if lesson.get("related"):
            lines.extend(["Related moments: " + " · ".join(_video_link(seconds, _stamp(seconds) + " · " + label, selected["url"]) for seconds, label in lesson["related"]), ""])
        lines.extend(["References: " + " · ".join(f"[{title}]({url})" for title, url in lesson["sources"]), ""])
    return "\n".join(lines)


def _creative_context():
    st.markdown(f"[Open the supplied Spanish video]({creative.GUIDE_URL})")
    st.caption(creative.GUIDE_PROVENANCE)
    st.info("Our execution environment is managed Comfy Cloud. Translate the local installation and GPU advice before applying it. NKD custom-node availability in our Cloud workspace is not established by these notes.")
    practice, evidence, translation = st.tabs(["Apply creative control", "CFA evidence", "Translation & Cloud"])
    with practice:
        st.table(creative.APPLY_MAP)
        for number, step in enumerate(creative.PRACTICE_STEPS, 1):
            st.markdown(f"{number}. {step}")
        st.caption("Record the resulting experiment in Video workshop → Preview & compare or Field journal. Reading these notes does not record a render, acceptance or completed checkpoint.")
    with evidence:
        st.caption("Local CFA records reviewed " + cfa_learning.REVIEWED + "; a dated snapshot, not a live account check.")
        st.write(cfa_learning.SUMMARY)
        st.table(cfa_learning.STATUS_ROWS)
        for lesson in cfa_learning.LESSONS:
            with st.expander(lesson["title"]):
                st.markdown("**What happened in CFA**")
                st.write(lesson["observation"])
                st.markdown("**What the next learner can reuse**")
                st.write(lesson["apply"])
                st.caption("Evidence path relative to Help: " + lesson["evidence"])
        st.caption("Canonical workflow index: " + cfa_learning.SOURCE_PATH)
    with translation:
        for note in creative.TRANSLATION_NOTES:
            st.write(note)
        st.table([{"Tutorial instruction": local, "Our Cloud route": cloud} for local, cloud in creative.CLOUD_TRANSLATION])
        st.markdown("[Managed Cloud node support](https://support.comfy.org/articles/6791455062-custom-nodes-on-cloud) · [Cloud model imports](https://docs.comfy.org/cloud/import-models)")


def render(key_prefix="help_tutorial_notes", initial_episode="nkd"):
    st.subheader("Tutorial notes · observations you can apply")
    episode = st.selectbox("Choose tutorial notes", list(_EPISODES), index=list(_EPISODES).index(initial_episode),
                           format_func=lambda value: _EPISODES[value]["label"], key=key_prefix + "_episode")
    selected = _EPISODES[episode]
    st.caption(f"Captured from your supplied {selected['coverage']} transcript. Each bookmark separates the historical demonstration from instructions to apply now.")
    if episode == "nkd":
        _creative_context()
    if episode == "ep3" and EP3_URL:
        st.markdown(f"[{EP3_TITLE}]({EP3_URL})")
        st.info("Try these ideas in Workflow anatomy → Controlled experiment: plan a CFG, steps or seed comparison; inspect shared controls; then organize the working branches.")
    if episode == "additional":
        st.markdown(f"[{GUIDE_TITLE}]({GUIDE_URL}) · {GUIDE_CREATOR}")
        st.caption(GUIDE_PROVENANCE)
        st.info("Practice these handoffs in 07 / Workflow lab → Video & audio: inspect subgraph outputs, choose an export route, explore FPS, and protect the intended dialogue. Node Atlas includes the individual video sockets.")
    if episode == "ep4":
        st.markdown(f"[{EP4_TITLE}]({EP4_URL})")
        st.info("Try 07 / Workflow lab → Image to image: prepare the reference, compare denoise, then wire a compatible LoRA through MODEL and CLIP. Node Atlas includes the full image-to-image recipe and its optional LoRA insertion.")
    st.caption("Episode 2's guided exercises and control map are in 07 / Workflow lab.")
    st.table({"Time": [_stamp(lesson["seconds"]) for lesson in selected["lessons"]],
              "Lesson": [lesson["takeaway"] for lesson in selected["lessons"]]})
    for lesson in selected["lessons"]:
        with st.expander(_stamp(lesson["seconds"]) + " · " + lesson["title"]):
            st.markdown(_video_link(lesson["seconds"], "Return to this moment", selected["url"]))
            st.markdown("**In the supplied transcript**")
            st.write(lesson["observed"])
            st.markdown("**Apply it today**")
            st.write(lesson["apply"])
            st.markdown("**Keep with your experiment**")
            st.write(lesson["keep"])
            if lesson.get("related"):
                st.markdown("Related moments: " + " · ".join(_video_link(seconds, _stamp(seconds) + " · " + label, selected["url"]) for seconds, label in lesson["related"]))
            st.markdown("References: " + " · ".join(f"[{title}]({url})" for title, url in lesson["sources"]))
    st.download_button(f"Download annotated {selected['download']} notes", notes_markdown(episode),
                       file_name=selected["filename"], mime="text/markdown",
                       key=key_prefix + "_download")
    st.caption(f"Official references reviewed {selected.get('reviewed', REVIEWED)}. These notes do not mark your setup or render checkpoints complete.")
