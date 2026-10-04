"""Additional guide bookmarks; pure content with no execution or learner state.

Observations paraphrase the learner-supplied 00:00-21:52 transcript. The title,
creator and URL were matched to the primary YouTube page. Technical references
were checked on September 12, 2026; current upstream features can precede an
installed stable release. The guide's preferences and sponsored demonstrations
are attributed to its creator, not presented as this learner's measured results.
"""

GUIDE_TITLE = "Ultimate Beginner Guide to Learning ComfyUI (2026)"
GUIDE_URL = "https://www.youtube.com/watch?v=l4CiwGS2ewY"
GUIDE_CREATOR = "Max Novak"
GUIDE_PROVENANCE = (
    "Paraphrased from your supplied 00:00-21:52 transcript; title and creator "
    "verified against the linked video. The video discloses NVIDIA sponsorship. "
    "These are learning notes and proposed checks, not runs performed by this console."
)

_CORE = "https://github.com/Comfy-Org/ComfyUI"
_PORTABLE = "https://docs.comfy.org/installation/comfyui_portable_windows"
_MANAGER = "https://docs.comfy.org/manager/install"
_CUSTOM = "https://docs.comfy.org/installation/install_custom_node"
_LTX_DOC = "https://docs.comfy.org/tutorials/video/ltx/ltx-2-3"
_LTX_MODEL = "https://huggingface.co/Lightricks/LTX-2.3"
_LTX_CORE = "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_lt.py"
_SAMPLING = "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_custom_sampler.py"
_SUBGRAPH = "https://docs.comfy.org/interface/features/subgraph"
_VIDEO = "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_video.py"
_VHS = "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite"
_ENHANCER = "https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/en.md"
_PROMPT = "https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/system_prompts/gemma_t2v_system_prompt.txt"
_RTX = "https://github.com/Comfy-Org/Nvidia_RTX_Nodes_ComfyUI"
_RTX_CODE = "https://github.com/Comfy-Org/Nvidia_RTX_Nodes_ComfyUI/blob/main/__init__.py"
_KLEIN = "https://docs.comfy.org/tutorials/flux/flux-2-klein"
_QWEN_EDIT = "https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit-2511"
_PARTNER = "https://docs.comfy.org/tutorials/partner-nodes/overview"


LESSONS = (
    {
        "seconds": 20,
        "title": "Choose a route with a realistic resource budget",
        "takeaway": "Free local software still uses hardware, memory, storage and time.",
        "observed": "Max introduces local ComfyUI, discloses NVIDIA sponsorship, gives broad VRAM tiers and names rented cloud GPUs as another route. His speed examples use his own RTX 5090.",
        "apply": "Record your actual GPU/VRAM, RAM, free disk space and installation route before choosing a template. Match requirements to the exact model variant, precision, resolution, frame count and offloading settings. The video's 8/12-16/24 GB tiers do not guarantee that a particular workflow fits. CUDA is an NVIDIA route; ComfyUI also supports other hardware backends. Local work has a queue and operating costs; rented GPUs, Cloud and hosted API calls can add charges.",
        "keep": "The proposed workflow and resource budget. Add runtime, peak memory or an error only after your own run; keep the creator's recommendations separately attributed.",
        "sources": (("ComfyUI hardware backends and installation", _CORE), ("Comfy Cloud", "https://docs.comfy.org/get_started/cloud"), ("Hosted Partner Nodes", _PARTNER)),
        "related": ((50, "Sponsorship disclosure"), (61, "Creator's hardware recommendations"), (96, "Rented GPU option")),
    },
    {
        "seconds": 120,
        "title": "Use installation instructions for your own distribution",
        "takeaway": "Portable, Desktop and Cloud have different setup responsibilities.",
        "observed": "The creator chooses Windows Portable, clones the legacy Manager into custom_nodes and launches the NVIDIA batch file. He presents Portable versus Desktop as a personal preference.",
        "apply": "Use official installation links and the current Manager instructions for your route. Desktop includes Manager; current Portable/manual setups require its dependencies and enable flag. A Git clone retrieves node code, not every model weight or dependency. Portable dependencies belong in its embedded Python environment. Restart the backend after adding node packages, then refresh the browser and inspect startup errors. Keep the Portable server terminal running while using its browser interface; Cloud setup follows Cloud's supported tools.",
        "keep": "Installation route, ComfyUI/frontend versions, model directory, optional package versions and any actual startup error. A copied installation command is not evidence of a successful setup.",
        "sources": (("Official Portable setup", _PORTABLE), ("Current Manager installation", _MANAGER), ("Custom-node dependencies and restart", _CUSTOM)),
        "related": ((155, "Legacy Manager installation"), (224, "Launching the local server")),
    },
    {
        "seconds": 262,
        "title": "Resolve one template's exact model set",
        "takeaway": "A missing model and a missing node require different fixes.",
        "observed": "The LTX-2.3 template lists a checkpoint, LoRAs, an upscaler and a text encoder. The creator uses each download's category to choose its model folder.",
        "apply": "Save the original template and inventory its exact filenames, variants and folders before changing it. Follow that template's model manifest; do not mix native ComfyUI and an extension's different loader formats. Refresh model lists after downloads and check paths if a selection is absent; a visible filename alone does not prove compatibility. Current native LTX-2.3 templates need no custom nodes, but availability depends on the installed version. Trace empty latent allocation, separate seeded noise, sampling and model-specific video/audio decoding inside the graph.",
        "keep": "Original workflow JSON, template source/version and model filenames. Empty LTX video latents allocate zeros; the noise source supplies randomness. A generic 20-30-step explanation is not a setting for every distilled pipeline.",
        "sources": (("Native LTX-2.3 workflows and model manifests", _LTX_DOC), ("Empty LTX latent and conditioning nodes", _LTX_CORE), ("Noise and custom sampling", _SAMPLING)),
        "related": ((301, "Models and folders"), (752, "Latent, noise, sampler and decoder explanation")),
    },
    {
        "seconds": 375,
        "title": "Inspect the subgraph's handoff before replacing an output",
        "takeaway": "A compact outer graph can contain many operations with different socket types.",
        "observed": "The creator enters the LTX subgraph, then exposes decoded images and audio so Video Helper Suite's Video Combine can consume them. He also recommends rgthree for workflow feedback.",
        "apply": "On a copy, identify the subgraph inputs, internal decoder and output boundary. Native SaveVideo already supports a video preview in current ComfyUI; VHS is an optional output route. For VHS, expose IMAGE frames and AUDIO, or split a VIDEO with GetVideoComponents. Preserve the original working output while checking the replacement. Matching socket types is only the first check: frame order, dimensions, audio and FPS must agree. Optional packs add conveniences; core ComfyUI already reports execution progress and errors.",
        "keep": "Before/after workflow JSON, output socket names/types, optional package versions and a playable result when tested. A group frame is not a subgraph with exposed inputs and outputs.",
        "sources": (("Subgraph boundaries", _SUBGRAPH), ("Native video outputs and components", _VIDEO), ("Video Helper Suite", _VHS), ("Core execution messages", "https://docs.comfy.org/development/comfyui-server/comms_messages")),
        "related": ((415, "Optional workflow conveniences"), (482, "Video Combine preference"), (527, "Expose subgraph outputs")),
    },
    {
        "seconds": 585,
        "title": "Keep length, generation FPS and export FPS consistent",
        "takeaway": "The frame count and frame rate together determine playback duration.",
        "observed": "The creator chooses H.264 MP4, reduces the clip to 81 frames and sets both generation and output to 24 fps. Later he identifies the generated resolution as 1280 by 704.",
        "apply": "Start from the exact template's valid dimensions and frame count. The LTX-2.3 model card requires width/height multiples of 32 and a frame count of 8n+1; a multistage workflow may impose additional constraints. Here, 81 frames at 24 fps means about 3.38 seconds of playback, not a measured runtime. Keep generation conditioning, audio duration and export FPS aligned. Changing only export FPS changes playback timing; it does not generate new motion frames. Inspect the saved MP4's dimensions, duration and audio sync.",
        "keep": "Requested and actual frame count, generation/export FPS, pixel dimensions, codec, duration and whether audio was present. 24 fps is this example's setting, not a universal LTX requirement.",
        "sources": (("LTX-2.3 dimension and frame constraints", _LTX_MODEL), ("LTX frame-rate conditioning", _LTX_CORE), ("Native video assembly", _VIDEO)),
        "related": ((597, "81-frame test"), (841, "Reported source dimensions")),
    },
    {
        "seconds": 654,
        "title": "Inspect enhanced prompts before testing exact dialogue",
        "takeaway": "Prompt expansion is a controllable text step, not a guarantee of correct speech.",
        "observed": "The creator bypasses Generate LTX2 Prompt because he wants to preserve a short spoken line, while recommending enhancement for other shots.",
        "apply": "Keep the original prompt and inspect the enhancer's returned text, including every spoken word. This is language-model prompt expansion with optional image context, not a generic CLIP Vision requirement. Lightricks' Gemma prompt instructions explicitly preserve supplied dialogue; actual expansion and generated speech still need checking. Compare enhanced and direct text on a copied workflow while holding other settings fixed. If bypassing, verify that the intended STRING still reaches text encoding; do not remove required model or encoder inputs. Use a short line that fits the clip.",
        "keep": "Original and enhanced text, enhancer mode, seed/settings, intended line and what you actually hear. The creator's bypass choice is an experiment to evaluate, not an always-on or always-off rule.",
        "sources": (("Generate LTX2 Prompt behavior", _ENHANCER), ("Lightricks dialogue-preservation instructions", _PROMPT), ("Bypass versus mute", "https://docs.comfy.org/basic-concepts/nodes#mode")),
        "related": ((608, "Prompting a short spoken line"), (694, "Creator bypasses the enhancer")),
    },
    {
        "seconds": 830,
        "title": "Upscale a selected result and preserve its timing",
        "takeaway": "Spatial upscaling changes pixel dimensions; it cannot promise lossless recovered detail.",
        "observed": "The guide adds NVIDIA RTX Video Super Resolution after decoded frames, describing a larger delivery output from a smaller LTX generation.",
        "apply": "Keep the original clip and test a short copy before choosing an upscaler. The RTX node is NVIDIA RTX-specific and consumes IMAGE frames; follow its current package/runtime requirements rather than assuming the recording's installer steps still apply. Reassemble the upscaled frames with the intended audio and FPS. Specify exact output dimensions instead of an ambiguous 2K label. Compare faces, text, edges and flicker; added pixels can contain artifacts and do not restore every detail that was absent from the source.",
        "keep": "Source and output dimensions, upscaler/version, scale or target size, quality setting, runtime and a visible comparison. Spatial upscaling alone does not increase frame count or recover editable 3D geometry.",
        "sources": (("RTX node and hardware scope", _RTX), ("RTX IMAGE input and output dimensions", _RTX_CODE), ("Video assembly and audio", _VIDEO)),
        "related": ((875, "Version-specific installation demonstration"), (929, "Placing the upscaler in the frame route"), (1104, "Other optional image upscalers")),
    },
    {
        "seconds": 960,
        "title": "Pick a control recipe for the shot you need",
        "takeaway": "Depth, edges, pose, reference images and audio solve different control problems.",
        "observed": "The creator points to LTX motion-control and IC-LoRA Union workflows, then names Wan Animate as a personal favorite for character animation.",
        "apply": "Write the shot's constraint first: camera structure, pose, appearance or spoken timing. Choose one documented recipe and inspect its required reference files and matching model/adapter versions. LTX-2.3 Union uses aligned structural signals such as depth, pose or edges; an audio-driven recipe is a separate route. Do not attach every available control pack to the starter graph. Compare the resulting motion and identity against the reference before treating that recipe as suitable for your scene.",
        "keep": "Shot requirement, chosen recipe, source video/image/audio and aligned control inputs. Record observed preservation or drift; the creator's favorite model is not a comparative benchmark for your task.",
        "sources": (("LTX-2.3 control and audio-driven recipes", _LTX_DOC), ("Lightricks example workflows", "https://github.com/Lightricks/ComfyUI-LTXVideo")),
        "related": ((974, "Structural guidance"), (992, "Wan Animate mention")),
    },
    {
        "seconds": 1010,
        "title": "Separate image model families from the 3D reference",
        "takeaway": "Use the exact image-edit recipe and retain the editable scene that produced its reference.",
        "observed": "Qwen and Z-Image are mentioned, but the demonstrated local image workflow uses FLUX.2 Klein. Max later combines low-poly 3D renders with a photographic style reference and shows a separate older FLUX.1 inpainting graph.",
        "apply": "Record Klein's parameter size, base/distilled variant and precision separately: FP8 describes precision; distillation describes the trained variant. Use that template's encoder, VAE and sampler settings instead of copying its near-1 CFG to another model. Qwen-Image-Edit is another model family with its own matching files; a Qwen text encoder in a Klein graph does not make it a Qwen image-edit graph. For a 3D reference exercise, keep the scene/camera and compare the edited pixels with the original render. Reference editing does not return an editable 3D scene or guarantee unchanged geometry.",
        "keep": "Scene file, camera settings, original render, style reference, exact model/template and saved result. Inspect identity and background changes even when the prompt asks to keep everything else unchanged.",
        "sources": (("FLUX.2 Klein variants and editing recipes", _KLEIN), ("Separate Qwen-Image-Edit recipe", _QWEN_EDIT)),
        "related": ((1047, "Precision and distilled variant"), (1148, "Targeted outfit edit"), (1170, "3D-render and style references"), (1202, "Separate FLUX.1 inpainting graph")),
    },
    {
        "seconds": 1229,
        "title": "Mark hosted services in an otherwise local workflow",
        "takeaway": "A local editor can still send inputs to a paid remote model.",
        "observed": "Max describes using Nano Banana and other API nodes inside ComfyUI, acknowledges credits and shares his preference for reference-based likeness editing over some training workflows.",
        "apply": "Identify the provider and execution location for each hosted node before choosing it. Built-in Comfy Partner Nodes use a Comfy account and credits; remote integrations may use a Comfy API key, while other custom providers can require their own credentials. Follow the actual node's authentication instructions. Record which inputs leave the machine and the applicable price before a run, then retain actual usage afterward. Judge identity preservation on your own outputs; the creator's preference does not establish that LoRA training is universally unnecessary.",
        "keep": "Provider/model, local-versus-hosted boundary, estimated and actual cost kept distinct, input assets and returned output. Save workflow JSON and versions alongside downloaded media; keep credentials out of shared notes and files.",
        "sources": (("Partner-node execution, accounts and credits", _PARTNER), ("Partner pricing reference", "https://docs.comfy.org/tutorials/partner-nodes/pricing")),
        "related": ((1248, "What API nodes change"), (1283, "Other audio and 3D template possibilities")),
    },
)
