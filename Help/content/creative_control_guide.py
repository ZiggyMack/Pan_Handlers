"""English annotations of the supplied Spanish transcript, 00:00–13:53.

The title below is an editorial label, not a verified YouTube title. The public
NKD project corroborates techniques, but not availability in our Cloud account.
"""

GUIDE_TITLE = "Creative control with ComfyUI · Spanish creator guide"
GUIDE_URL = "https://www.youtube.com/watch?v=4jO_0Ce0q6o"
GUIDE_CREATOR = "NKD / Nekodificador project"
REVIEWED = "October 4, 2026"
GUIDE_PROVENANCE = (
    "English translation and paraphrase of your supplied Spanish transcript (00:00–13:53). "
    "Its NKD Klein Tools project matches Nekodificador's public repository. The YouTube page "
    "could not be retrieved, so the exact video title, date and complete linked download pack "
    "remain unverified. The creator describes a collaboration with NVIDIA Spain. His demos "
    "and preferences are distinct from our own runs; current repository features can be newer than the recording."
)

_NKD = "https://github.com/Nekodificador/ComfyUI-NKD-Klein-Tools"
_INPUTS = _NKD + "/blob/master/docs/inputs.md"
_CHANGES = _NKD + "/blob/master/docs/changelog.md"
_EXAMPLE = _NKD + "/blob/master/example_workflows/NKD%20Klein%20Tools.json"
_FOCAL = "https://huggingface.co/Nekodificador/NKD_Klein_9B_Focal_Lenght_Slider_V1"
_KLEIN = "https://docs.comfy.org/tutorials/flux/flux-2-klein"
_CLOUD = "https://support.comfy.org/articles/6791455062-custom-nodes-on-cloud"
_IMPORT = "https://docs.comfy.org/cloud/import-models"
_LTX_AUDIO = "https://docs.ltx.io/open-source-model/usage-guides/audio-to-video"
_LTX_PIPELINES = "https://github.com/Lightricks/LTX-2#available-pipelines"
_UNION = "https://docs.ltx.io/open-source-model/feature-guides/structural-control/union-control"

TRANSLATION_NOTES = (
    "The automatic transcript spells ComfyUI as Confir/Confi/Confai and NVIDIA as Envidia. FLUX Claim/Clink is interpreted as FLUX Klein, matching the named project.",
    "The ceramic-repair example appears to mean kintsugi. The samurai's face covering at 07:22 is an object in the image; the later editing mask is a separate concept.",
    "At 10:26, 'tensión' likely transcribes 'atención' or reference influence. The audio text alone cannot identify the exact widget; current NKD documentation distinguishes several reference controls.",
    "At 11:15, 'manipulación local' means editing a limited region of the picture. It does not mean that we must run Comfy on this PC. 'Sin painting' is interpreted as inpainting.",
)

CLOUD_TRANSLATION = (
    ("Install nodes with Manager / Git / pip", "Check managed Cloud's supported nodes first. Public code and a workflow JSON do not establish Cloud availability; keep an unsupported package as a candidate."),
    ("Put weights in models/...", "Treat these as model roles in the remote workflow. Reuse the Cloud catalog or import a supported exact file through Cloud; keep weights off the local PC."),
    ("A 4090/5090, CUDA, VRAM or a quantization variant", "Those describe the execution host. Check the selected Cloud model/loader and service limits; the tutorial does not establish the GPU or performance of our account."),
    ("Load a file or open the output folder", "Upload necessary input media from D: to the Cloud workflow. Download review copies and JSON to D:; a path on this computer is not a Cloud asset."),
)

APPLY_MAP = (
    {"Creative decision": "What should stay recognizable?", "Control to inspect": "Ordered design/identity references and the actual crop", "First evidence": "An input preview, then a reviewed clean still", "Limit": "Reference conditioning does not lock pixels or guarantee identity."},
    {"Creative decision": "Where may the picture change?", "Control to inspect": "A mask and the recipe's compositing/edit-region behavior", "First evidence": "Outside-region comparison and boundary inspection", "Limit": "A still mask is not a tracked, temporally stable video mask."},
    {"Creative decision": "How much influence should each input have?", "Control to inspect": "The selected graph's real reference control; separate it from LoRA and denoise", "First evidence": "One changed control, fixed baseline and side-by-side result", "Limit": "Our current CFA graph does not expose every NKD control."},
    {"Creative decision": "What look should the shot have?", "Control to inspect": "One lighting/style instruction or a compatible concept LoRA", "First evidence": "No-style baseline versus one change", "Limit": "A style text selector and a trained concept LoRA are different mechanisms."},
    {"Creative decision": "What motion or timing must survive?", "Control to inspect": "Driving video for performance; prepared audio for an audio-conditioned experiment", "First evidence": "Matched timecodes, gesture/contact or sound-event review", "Limit": "Audio-driven generation is not proof of source-performance preservation or exact lip sync."},
)

PRACTICE_STEPS = (
    "Begin with one candidate still or one short shot, its exact recipe, original inputs and a written list of details to preserve. Keep the clean version.",
    "Inspect the effective prompt and reference crops before generation. Label each reference by job: design/composition, identity, style, motion or audio timing.",
    "Choose one control the actual Cloud graph exposes. Start with one style/prompt change if a custom reference-strength or mask control is unavailable; do not invent a missing knob.",
    "Hold the other settings and original inputs fixed. Record the requested value, compiled graph value, result and visible tradeoff. CFA caught stale named-widget values overriding visible edits, so inspect the submitted settings. A seed aids comparison but does not promise identical output across environments.",
    "Review the clean identity before adding tattoos, accessories or other detailed finishing. For regional work, compare unchanged areas as well as the edited area. Keep rejected variants and the reason.",
    "Promote an accepted still into a separate video experiment with a driving clip or prepared audio appropriate to the goal. Judge all frames and sound; success on a still does not establish video consistency.",
)

LESSONS = (
    {
        "seconds": 38, "title": "Put artistic decisions ahead of random generation",
        "takeaway": "Use AI to develop an intention you can describe and evaluate.",
        "observed": "The creator proposes amplifying the artist's process and complains that unpredictable results and constant rewiring interrupt it. His claim that ComfyUI is the only sensible tool is a personal assessment.",
        "apply": "Write what should change and what must remain before choosing a graph. Borrow a suitable workflow and expose a small set of useful controls. Keep the four application paths visible in Pathfinder; this video does not invalidate the alternatives.",
        "keep": "The source, the intended change, preservation criteria and why this workflow fits.",
        "sources": (("Creator's NKD project", _NKD),),
    },
    {
        "seconds": 109, "title": "Translate the hardware discussion to our Cloud setup",
        "takeaway": "Resource requirements belong to the execution environment and exact model variant.",
        "observed": "The NVIDIA collaboration leads into CUDA, VRAM, local GPUs and BF16/MXFP8/NVFP4 filenames. The creator presents small-memory and fast-generation examples without a reproducible benchmark in the transcript.",
        "apply": "We use managed Comfy Cloud. Do not turn this section into a PC shopping or local installation requirement. ComfyUI supports non-NVIDIA backends too. BF16 is a numeric format, not by itself evidence of a quantized model; reduced-precision variants require compatible loaders and hardware. Record the selected remote variant and measured runtime only after a real run.",
        "keep": "Cloud template, exact model/precision, resolved size/frame count, observed runtime or error; mark unknown host details unknown.",
        "sources": (("ComfyUI supported platforms", "https://github.com/Comfy-Org/ComfyUI"), ("Tensor data types", "https://docs.pytorch.org/docs/stable/tensor_attributes.html"), ("Cloud model import", _IMPORT)),
        "related": ((154, "VRAM and model variants"), (202, "NVFP4 discussion")),
    },
    {
        "seconds": 268, "title": "Give auxiliary models a clear job",
        "takeaway": "Depth, segmentation and other preparation stages provide different kinds of control.",
        "observed": "The creator describes normal/depth maps, segmentation or rotoscoping with a Segment Anything-like tool, and an object-location tool named Locate Anything. The transcript does not identify their exact package versions.",
        "apply": "Name the artifact a stage produces: depth sequence, mask sequence or reference crop. Inspect that artifact before connecting generation. For our wolf capability test, depth is a scene-structure hypothesis; for a local visual edit, a correctly aligned region mask addresses a different problem. Verify the actual Cloud node and its model dependencies rather than installing a guessed package.",
        "keep": "Preprocessor name/version, preview of the control signal, dimensions and frame alignment, and failures around occlusion or contact.",
        "sources": (("Official structural control choices", _UNION), ("Managed Cloud nodes", _CLOUD)),
    },
    {
        "seconds": 345, "title": "Expose the controls the artist needs",
        "takeaway": "A simpler front panel should retain an inspectable underlying graph.",
        "observed": "The creator treats the node graph as a system of interacting variables and wants to reduce the time spent rewiring it.",
        "apply": "Group a working graph into input preparation, generation and output review. Surface only connected controls with clear names. Use CFA's input-check workflow to inspect prompts/crops independently, then transfer the chosen settings explicitly into the render workflow. A preview output still needs execution; it does not predict a future render. CFA's SDXL v2 repair also shows why we inspect compiled values: stale named-widget metadata had overridden canvas edits before conversion was corrected.",
        "keep": "Which control drives which input, actual values, graph revision and evidence that a UI-only change preserved the execution graph.",
        "sources": (("ComfyUI subgraphs", "https://docs.comfy.org/interface/features/subgraph"), ("Creator's node design", _NKD)),
    },
    {
        "seconds": 409, "title": "Refine a material without losing the design",
        "takeaway": "Use a reference to explain the desired change, then judge what drifted.",
        "observed": "In the ceramic-armour samurai example, the creator dislikes the dark face covering, tries another image for colour/reflections, then returns to the dark design with stronger specular highlights. He values keeping the underlying structure.",
        "apply": "Separate composition, identity and material/lighting references. Keep the original and an explicit baseline rather than feeding every output into the next edit indefinitely. Compare silhouette, face, wardrobe and lighting after each change. A convincing reference-driven still remains a candidate until reviewed.",
        "keep": "Reference order and role, original/edited pair, desired material change and any unwanted identity or composition change.",
        "sources": (("FLUX.2 Klein reference workflows", _KLEIN),),
        "related": ((442, "Face-covering revision"), (509, "Sketches, layouts and renders")),
    },
    {
        "seconds": 521, "title": "Use dynamic NKD nodes as a candidate simplification",
        "takeaway": "Flexible inputs can reduce rewiring, but still depend on a compatible node package.",
        "observed": "NKD Klein Tools is presented as adapting its inputs and exposed controls to connected material, with support for the surrounding Klein ecosystem.",
        "apply": "The public repository includes an example editor workflow. Its current input documentation describes automatically expanding references and multiple operating modes. Inspect that example and its version before adopting it; do not assume current repository features were in this recording. In managed Cloud, first confirm the package is available. Until then, apply the organization ideas to the already working CFA graph.",
        "keep": "Example URL/revision, required node classes and exact model family; record Cloud availability as unchecked until discovered.",
        "sources": (("Public NKD example JSON", _EXAMPLE), ("Current input modes", _INPUTS), ("Version history", _CHANGES), ("Cloud node policy", _CLOUD)),
    },
    {
        "seconds": 569, "title": "Distinguish concept sliders from text styles",
        "takeaway": "A trained concept LoRA is a model-specific control, not a universal photo slider.",
        "observed": "The creator describes LoRAs for focal-length appearance, haze and white balance, comparing them to photography sliders. The focal-length slider has a verified public model card; the other two remain transcript descriptions here.",
        "apply": "Check the exact compatible base and reference settings. Try one adapter at a time against a no-adapter baseline. CFA's numbered style choices append text; they are not trained concept LoRAs. Its [paired Civitai comparison v4](https://cloud.comfy.org/#1ee8615b-5586-42fd-bf3d-3d202b2377eb) shares inputs and sampling across A baseline / B Candid Film 0.5; it passed validation but has not rendered. Earlier separate stills remain unaccepted. Candid Film's examples target Klein 9B base while CFA uses distilled 9B: loading successfully does not establish variant compatibility or quality. Apparent focal-length changes can alter composition, and white-balance changes can conflict with retaining the original lighting.",
        "keep": "Exact LoRA/version, base model, weight, fixed comparison settings and the intended versus observed change.",
        "sources": (("Creator's Klein 9B focal-length slider", _FOCAL),),
    },
    {
        "seconds": 623, "title": "Control reference influence without confusing the knobs",
        "takeaway": "Reference influence, LoRA strength and denoise describe different operations.",
        "observed": "The transcript's likely reference-attention discussion describes deciding how much the model should reinterpret a sketch. The noisy transcription cannot establish the exact node or numeric scale shown.",
        "apply": "Read the specific control's documentation. Current NKD input docs distinguish overall Reference Strength from per-reference Control/Weight; scheduling or regional options depend on version. Do not assume those controls exist in CFA's current Klein recipe, or copy an SDXL denoise setting into it. CFA now has a separate [Image Refinement SDXL v2](https://cloud.comfy.org/#2a60a23f-f68a-4a66-92c6-0e30aa0d5e03): original pixels feed VAE Encode, then KSampler's starting latent with denoise 0.30. That graph passed validation but has not rendered. It has one image input and active positive/negative conditioning, with no second likeness input or mask; its denoise is not an identity lock. Change one available control and compare adherence and freedom.",
        "keep": "Exact node/input name, package revision, scope (all references or one), tested values and side effects; never label an untested value as a preservation percentage.",
        "sources": (("NKD control definitions", _INPUTS), ("NKD version changes", _CHANGES)),
    },
    {
        "seconds": 675, "title": "Edit a region and protect the clean checkpoint",
        "takeaway": "Constrain where changes happen and inspect the supposedly unchanged areas.",
        "observed": "The creator describes masks, inpainting, removal and addition, then claims repeated edits do not degrade the image. Here 'local manipulation' refers to an image region, not where the computer runs.",
        "apply": "Treat the no-degradation statement as a claim to test. Current NKD documentation describes compositing detected edits over the original; this can preserve untouched pixels without guaranteeing that edited regions or blended boundaries never deteriorate. CFA's current whole-image reference workflow is not a masked editor. Save and approve a clean identity before detailed finishing, and use a compatible regional recipe when preservation demands it.",
        "keep": "Original and clean checkpoint, edit mask or detected region, crop/boundary comparison, drift and approval status. For video, add mask tracking and temporal review.",
        "sources": (("NKD region/edit behavior", _INPUTS), ("FLUX.2 Klein example scope", _KLEIN)),
    },
    {
        "seconds": 713, "title": "Explore audio as a timing input for a separate video experiment",
        "takeaway": "Prepared audio can condition video; precise synchronization still needs measurement.",
        "observed": "The creator introduces an experimental LTX workflow and says he discussed directing animation timing through sound with the model's developers. He promises a shared workflow and a separate detailed tutorial; this transcript does not supply its graph or settings.",
        "apply": "Keep this as a useful music-video branch: prepare a short audio excerpt and an event sheet, then evaluate an audio-conditioned LTX recipe that the Cloud environment supports. Official LTX pipelines confirm audio-conditioned video, but do not identify this creator's exact pack. Choose source-video controls when preserving an existing performance is the requirement. Beat response, mouth sync and character identity are separate things to review.",
        "keep": "Exact model and workflow version, prepared audio and timecodes, requested event, observed event time, lip/gesture error and identity/flicker notes. No frame-accurate synchronization or rap result is established by this lesson.",
        "sources": (("LTX audio-conditioned pipelines", _LTX_PIPELINES), ("Official audio-to-video guide", _LTX_AUDIO)),
        "related": ((742, "Timing through sound"), (771, "Experimental workflow and resources")),
    },
    {
        "seconds": 814, "title": "Keep the source package and the execution evidence separate",
        "takeaway": "Capture a usable recipe, its prerequisites and what actually happened.",
        "observed": "The creator points to description downloads, installation documentation, laboratory tutorials and courses. Those materials are not reproduced in the supplied transcript.",
        "apply": "Use the verified public NKD example as a source candidate, not as a claim that we recovered the complete advertised pack. Keep models and execution remote, necessary JSON/media on D:, and credentials out of handoffs. Let CFA return exact graphs, input roles, outputs, failures and acceptance decisions; bring the reusable method into Pathfinder.",
        "keep": "Creator/source URL, exact editor JSON and revision, Cloud compatibility, result path, cost if measured, review decision and next experiment.",
        "sources": (("Public NKD project and documentation", _NKD), ("Cloud import procedure", _IMPORT)),
    },
)


def practice_markdown():
    """Portable practice guidance; contains no installed-capability claims."""
    lines = ["## Translate the tutorial to our Cloud workflow", ""]
    for local, cloud in CLOUD_TRANSLATION:
        lines.extend([f"- **Tutorial: {local}.** Our route: {cloud}"])
    lines.extend(["", f"[Managed Cloud nodes]({_CLOUD}) · [Model imports]({_IMPORT})", "",
                  "## One controlled creative experiment", ""])
    lines.extend(f"{i}. {step}" for i, step in enumerate(PRACTICE_STEPS, 1))
    lines.extend(["", "Record: source and recipe / changed control / preserved details / observed drift / accepted or rejected / next change.", "",
                  "## Translation notes", ""])
    lines.extend("- " + note for note in TRANSLATION_NOTES)
    return "\n".join(lines) + "\n"
