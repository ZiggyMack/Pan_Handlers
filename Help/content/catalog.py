"""Learning content for the AI video pathfinder, reviewed on 2026-09-12.

Coverage describes this guide, not the readiness of an upstream application.
Path suitability and milestone design are editorial judgments; linked primary
sources describe the underlying tools. No render is claimed as locally tested.
"""

REVIEWED_ON = "2026-09-12"
TUTORIAL_URL = "https://www.youtube.com/watch?v=Zko_s2LO9Wo"
REQUIREMENTS_BOOKMARK = {
    "title": "System requirements",
    "timestamp": "03:20",
    "seconds": 200,
    "url": TUTORIAL_URL + "&t=200s",
    "provenance": "User-shared screenshot from pixaroma Episode 1 (2024 tutorial), captured in our learning trail on 2026-09-12.",
    "status": "Tutorial observation; hardware suitability and setup completion have not been verified.",
    "rows": [
        {
            "area": "Operating system",
            "minimum": "Windows 10+; macOS 10.15+; recent Linux",
            "recommended": "Windows 10+; macOS 10.15+; recent Linux",
            "check": "Check your chosen install route and platform support. Current macOS guidance focuses on Apple Silicon.",
        },
        {
            "area": "Processor",
            "minimum": "Intel Core i5 or AMD Ryzen 5",
            "recommended": "Intel Core i7 or AMD Ryzen 7 or higher",
            "check": "Record the exact CPU model; these family names alone do not identify its generation or capabilities.",
        },
        {
            "area": "System RAM",
            "minimum": "8 GB",
            "recommended": "16 GB or more",
            "check": "Record system RAM separately from GPU memory. Check the intended model and workflow, including offloading needs.",
        },
        {
            "area": "Graphics / VRAM",
            "minimum": "NVIDIA CUDA GPU with 4 GB+ VRAM; slide also mentions AMD via ROCm",
            "recommended": "NVIDIA GPU with 8 GB+ VRAM; RTX 2070 given as an example",
            "check": "Choose the supported backend for your GPU. Treat 4 GB / 8 GB as slide guidance, not a guarantee for a video model.",
        },
        {
            "area": "Free storage",
            "minimum": "20 GB for installation and models",
            "recommended": "50 GB for installation and additional models",
            "check": "Budget for the selected model downloads, environment and outputs rather than treating either number as a fixed total.",
        },
        {
            "area": "Software dependencies",
            "minimum": "Python 3.8+ and required Python libraries",
            "recommended": "Python 3.8+ and required Python libraries",
            "check": "The Python guidance is dated. Follow the current route's environment instructions and hardware-specific dependencies.",
        },
    ],
}
COMFY_REPO_URL = "https://github.com/Comfy-Org/ComfyUI"
COMFY_PROJECT_LINKS = [
    {
        "title": "Official repository & README",
        "url": COMFY_REPO_URL,
        "note": "ComfyUI source, feature overview and installation entry points. Record the version or commit used for your experiment.",
    },
    {
        "title": "Releases & changes",
        "url": COMFY_REPO_URL + "/releases",
        "note": "Check release notes and assets for the version and installation route you use.",
    },
    {
        "title": "Known issues",
        "url": COMFY_REPO_URL + "/issues",
        "note": "Search existing reports for your error; compare versions, hardware and reproduction details before applying a suggested fix.",
    },
]

PATHS = [
    {
        "id": "automatic1111",
        "name": "AUTOMATIC1111",
        "tagline": "Explore images through familiar controls.",
        "interaction": "Forms and tabs",
        "strengths": [
            "Text-to-image, image-to-image, inpainting and upscaling in one interface.",
            "Prompt experiments, batches and an extension ecosystem.",
        ],
        "tradeoffs": [
            "Check the exact model and extension compatibility for your project.",
            "Its core image workflow needs an additional route for animation and 3D scene rendering.",
        ],
        "video_fit": "A possible starting point for concept art, reference frames and image treatment; document the chosen video extension separately.",
        "status": "Planned",
        "url": "https://github.com/AUTOMATIC1111/stable-diffusion-webui",
    },
    {
        "id": "forge",
        "name": "Forge UI",
        "tagline": "Keep the WebUI approach with resource-focused engineering.",
        "interaction": "Forms and tabs, derived from A1111",
        "strengths": [
            "Designed around resource management and inference performance.",
            "Offers supported Flux workflows and familiar WebUI controls.",
        ],
        "tradeoffs": [
            "Performance depends on hardware, model and settings; compare your own results.",
            "Check extension compatibility; its maintainers note that the interface and documentation can change.",
        ],
        "video_fit": "A viable image preparation path. Select and document a compatible animation workflow before treating it as a video pipeline.",
        "status": "Planned",
        "url": "https://github.com/lllyasviel/stable-diffusion-webui-forge",
    },
    {
        "id": "invoke",
        "name": "Invoke / InvokeAI",
        "tagline": "Shape the image with a creative canvas.",
        "interaction": "Canvas, layers and node workflows",
        "strengths": [
            "Brush tools and inpainting/outpainting support hands-on image refinement.",
            "A workflow editor provides reusable node-based image operations.",
        ],
        "tradeoffs": [
            "Plan an animation or rendering stage around its image creation workflow.",
            "Confirm the models and workflow features you need in the installed version.",
        ],
        "video_fit": "A useful route for art direction, reference images and paintovers of renders, followed by a chosen video or 3D tool.",
        "status": "Planned",
        "url": "https://github.com/invoke-ai/InvokeAI",
    },
    {
        "id": "comfyui",
        "name": "ComfyUI",
        "tagline": "Make the process visible, then make it repeatable.",
        "interaction": "Connected nodes and reusable workflow files",
        "strengths": [
            "Inspect each stage and share the workflow behind an output.",
            "Official examples cover image generation, video and 3D assets.",
        ],
        "tradeoffs": [
            "Learning nodes, models and connections takes some practice.",
            "Local workflows need compatible models and dependencies; cloud catalogues have their own limits.",
        ],
        "video_fit": "Our active path: choose a source-video control workflow, preserve the performance through a visual change, then finish an accepted take in HD and 4K. Still-image lessons support the task.",
        "status": "Guide available",
        "url": COMFY_REPO_URL,
    },
]

COMFY_TRADEOFFS = [
    {
        "benefit": "Visual clarity",
        "unlock": "A node graph exposes how inputs, models and outputs connect so you can inspect the process.",
        "cost": "A large graph exposes many details at once and can be difficult to read before you know the node roles.",
        "mitigation": "Trace the small first-image graph from its model and prompts to its saved output before opening a larger example.",
        "alternative": "AUTOMATIC1111 and Forge provide forms and tabs; Invoke offers a creative canvas and also has node workflows.",
    },
    {
        "benefit": "Flexible iteration",
        "unlock": "Reusing and rearranging workflow stages can make it quicker to try a new idea once you understand the graph.",
        "cost": "That flexibility invites repeated tweaking; faster workflow iteration does not guarantee faster rendering.",
        "mitigation": "Duplicate a working baseline and change just one prompt or setting for the next comparison.",
        "alternative": "Consider AUTOMATIC1111 or Forge when their existing controls cover the experiment; consider Invoke for canvas-based image refinement.",
    },
    {
        "benefit": "Shareable recipes",
        "unlock": "A saved workflow lets another person inspect and reopen the structure behind an output.",
        "cost": "Shared graphs can use unfamiliar layouts, and a workflow file does not bundle all required models, nodes or dependencies.",
        "mitigation": "Package the workflow with a short input list, model identifiers, node versions and a labeled reference output.",
        "alternative": "All four paths need setup notes for reproducibility; weigh ComfyUI's graph sharing against the interaction style you prefer.",
    },
    {
        "benefit": "Start without coding",
        "unlock": "You can run and adjust a supported basic workflow through the interface without writing application code.",
        "cost": "You still learn node concepts, model choices and compatible inputs, and installation issues can involve dependencies.",
        "mitigation": "Complete the official first-image example with its prescribed model before adding custom nodes.",
        "alternative": "The other three tools also provide graphical controls; choose between forms, canvas work and visible graphs rather than treating no-code use as exclusive to ComfyUI.",
    },
    {
        "benefit": "Room to customize",
        "unlock": "Additional nodes and models let you adapt a workflow to a more specific creative process.",
        "cost": "Combining workflows or extending a working setup adds integration work, version checks and maintenance overhead.",
        "mitigation": "Add one required extension to a saved baseline and rerun that baseline before integrating the next change.",
        "alternative": "Check whether AUTOMATIC1111, Forge or Invoke already covers the operation you need, and compare its compatibility work before switching.",
    },
    {
        "benefit": "Video and 3D paths",
        "unlock": "Official workflows provide routes from images to video experiments or generated 3D assets within the same tool family.",
        "cost": "Memory use and generation time depend on the model, resolution, frame count and hardware; an interface choice alone does not solve those limits.",
        "mitigation": "Run the selected template's small supported example and record memory limits and runtime before increasing the shot's scope.",
        "alternative": "All four paths depend on their compute environment; the others remain useful for image preparation, while an editable animated scene still needs its scene and rendering stage.",
    },
]

ENVIRONMENT_GUIDES = {
    "Desktop": {
        "summary": "A local launcher that manages ComfyUI installations and their Python environments. Start here if you want managed setup on a supported computer.",
        "steps": [
            "Open the official Desktop guide and choose Windows, Apple Silicon macOS or Linux.",
            "Check the platform requirements, download its installer and complete setup.",
            "Launch Desktop, create a ComfyUI installation and note its model/output locations.",
            "Open that installation and continue to the first-image stage.",
        ],
        "tradeoff": "You use your own compute and storage. Workflow models need additional space, and demanding video can exceed your hardware's practical capacity.",
        "url": "https://docs.comfy.org/installation/desktop/overview",
    },
    "Portable": {
        "summary": "A Windows folder-based package with embedded Python. Choose the official package matching your GPU.",
        "steps": [
            "Read the official Portable page and select the package for your hardware.",
            "Extract the archive into a dedicated folder with room for model downloads.",
            "Read its included README and launch the matching GPU batch file; the CPU launcher is available but slower.",
            "Open the local address shown by the launcher and record the installation folder.",
        ],
        "tradeoff": "You manage updates, models and custom-node dependencies inside the portable environment. Keep a working workflow backup before changing it.",
        "url": "https://docs.comfy.org/installation/comfyui_portable_windows",
    },
    "Manual": {
        "summary": "A configurable installation for people comfortable maintaining a Python environment and hardware-specific dependencies.",
        "steps": [
            "Use the current manual guide's section for your operating system and accelerator.",
            f"Create a separate environment, obtain ComfyUI from the [official repository]({COMFY_REPO_URL}) and install the documented device-specific dependencies.",
            "Run the documented launch command and open the address it reports.",
            "Record the ComfyUI revision and environment details alongside your first successful workflow.",
        ],
        "tradeoff": "This offers control and asks you to diagnose environment compatibility. Follow current commands in the source rather than an older video's package versions.",
        "url": "https://docs.comfy.org/installation/manual_install",
    },
    "Cloud": {
        "summary": "The official paid browser service supplies managed compute and supported models and custom nodes.",
        "steps": [
            "Open the official Cloud page and review the current plan and usage terms.",
            "Check that the intended template, models and nodes are supported before committing to that route.",
            "For model imports, follow the access checklist below: save any required provider token in Cloud Settings → Secrets, import the exact file's download link and confirm it in My Models. Check automation login separately if using Codex.",
            "Open a supported template, supply its inputs and inspect the service's displayed usage information before running.",
            "Download your output and workflow so the experiment can travel with your notes.",
        ],
        "tradeoff": "You exchange local setup work for service costs, internet access and the platform's model/node availability. Uploaded inputs and remote processing should suit your project.",
        "url": "https://docs.comfy.org/get_started/cloud",
    },
}

STEPS = [
    {
        "id": "brief",
        "title": "Define the shot",
        "summary": "Decide whether the result is a generated clip, an editable 3D scene, or a hybrid of the two.",
        "actions": [
            "Write one sentence describing the subject, setting and intended motion.",
            "Choose the output: a video file, an editable scene with geometry, or both. A video with a 3D look does not by itself contain a 3D model.",
            "Set a first experiment small enough to inspect: one shot, one subject and one change in motion.",
            "Record aspect ratio, intended duration, available hardware and a rough time or spending limit.",
        ],
        "checkpoint": "A saved shot brief stating what you want to make and how you will judge the first result.",
        "sources": [
            ("Video workflow examples", "https://docs.comfy.org/tutorials/video/wan/wan2_2"),
            ("3D asset workflow examples", "https://docs.comfy.org/tutorials/3d/hunyuan3D-2"),
        ],
    },
    {
        "id": "setup",
        "title": "Choose where ComfyUI runs",
        "summary": "Select Desktop, Portable, Manual or Cloud, then record enough detail for another person to follow the same route.",
        "actions": [
            "Use the environment guide here to compare setup effort, control and ongoing cost.",
            "For local use, note OS, GPU and VRAM if known, and check requirements for the actual workflow you intend to run.",
            "Follow your selected route's official instructions and open the ComfyUI interface.",
            "For Cloud imports, complete the provider-access checklist and record the import result. If controlling Cloud through Codex, separately verify its connection with a read-only call. Keep credential values out of these notes.",
            "Write down the route and version, plus where you will keep inputs, workflows and outputs.",
        ],
        "checkpoint": "ComfyUI opens, and your notes identify the chosen environment. Opening the interface is a setup milestone, not a completed render.",
        "sources": [
            ("Official ComfyUI repository and README", COMFY_REPO_URL),
            ("Current hardware and platform requirements", "https://docs.comfy.org/installation/system_requirements"),
            ("Tutorial bookmark — system requirements at 03:20 (2024)", REQUIREMENTS_BOOKMARK["url"]),
            ("Desktop overview", "https://docs.comfy.org/installation/desktop/overview"),
            ("Cloud overview", "https://docs.comfy.org/get_started/cloud"),
            ("Cloud model imports and Secrets", "https://docs.comfy.org/cloud/import-models"),
        ],
    },
    {
        "id": "first_image",
        "title": "Generate your first still",
        "summary": "A simple image confirms the basic workflow before you add motion or geometry.",
        "actions": [
            "Start our image branch with an SDXL-compatible checkpoint and workflow; use the official SDXL examples and the exact model author's settings.",
            "Prefer a compatible safetensors checkpoint, place it in the configured checkpoints folder, and select it in Load Checkpoint. Keep alternative examples paired with their own required model family.",
            "Before Run, check the exact version's recommended width/height, sampler, scheduler, steps, CFG and denoise. Open Workflow anatomy → Size & sampler for the model-card mapping. Record seed and after-generation control for comparisons.",
            "Enter a simple prompt related to your shot and use Run. If loading fails, check model location and refresh the model list.",
            "Save the result and export the workflow JSON. Add the prompt, seed, model name and generation settings to your notes.",
        ],
        "checkpoint": "One saved still and its matching workflow file. Record errors and fixes if the first attempt needs repair.",
        "sources": [
            ("ComfyUI SDXL examples", "https://comfyanonymous.github.io/ComfyUI_examples/sdxl/"),
            ("ComfyUI first generation", "https://docs.comfy.org/get_started/first_generation"),
            ("pixaroma Ep01 — first image at 09:52", TUTORIAL_URL + "&t=592s"),
        ],
    },
    {
        "id": "workflow",
        "title": "Understand and repeat the workflow",
        "summary": "Turn an output into a recipe someone else can inspect and use.",
        "actions": [
            "Trace the default graph: model and prompt conditioning feed the sampler; latent data is decoded into an image and saved.",
            "Use 07 / Workflow lab for the Episode 2 practice path: read, trace, build, debug, compare, organize and hand off a graph. Keep observed evidence in its workbook; it does not automatically complete this foundation checkpoint.",
            "Use Workflow anatomy → Save & load to export a named editor workflow, optionally clear the canvas, then reopen it. Confirm the intended model, size, sampler/scheduler, steps, CFG and seed controls were restored before running.",
            "Keep a baseline copy and fix the seed while comparing a single prompt or setting change. The graph file does not bundle its model weights or custom-node packages.",
            "Record what changed and compare the two outputs. Identical settings can still behave differently across environments or software versions.",
            "List any extra models or custom nodes needed. Keep the first baseline simple before extending it.",
        ],
        "checkpoint": "A baseline workflow plus one documented comparison, with enough inputs and environment details for a repeat attempt.",
        "sources": [
            ("Workflow loading and export", "https://docs.comfy.org/get_started/first_generation"),
            ("pixaroma Ep01 — saving/loading at 14:32", TUTORIAL_URL + "&t=872s"),
        ],
    },
    {
        "id": "first_video",
        "title": "Make one short video experiment",
        "summary": "For the active source-video task, use Video workshop to select a control or performance-transfer recipe. A still-image start uses an image-to-video branch instead.",
        "actions": [
            "Choose by the input you actually have: a source clip for motion preservation, or a still for newly generated motion. Video workshop gives the task-specific workflow links and prerequisites.",
            "Confirm the exact graph, model files, control adapter and node versions in your Cloud workspace. Keep its supported dimensions, frame count and timing requirements.",
            "Save a working copy, prepare one continuous source interval and change one major visual element. Check the run estimate before a modest-resolution fixed-seed preview.",
            "Compare source and result at matching timecodes for gesture, contact, camera movement, identity and flicker. Record defects, runtime and observed cost.",
            "Retain the source, output and exact workflow. Accept a take explicitly before the HD master and reviewed 4K derivative; save failed attempts and the next targeted change too.",
        ],
        "checkpoint": "A playable clip and an honest quality note. If generation fails, preserve the error and attempted fix before marking this stage complete.",
        "sources": [
            ("Official Wan2.2 video templates and model instructions", "https://docs.comfy.org/tutorials/video/wan/wan2_2"),
        ],
    },
    {
        "id": "bridge_3d",
        "title": "Optional future branch: editable 3D",
        "summary": "Use this branch when your shot needs geometry, materials and a camera you can edit in Blender.",
        "actions": [
            "Start with one clearly framed object and load the official Hunyuan3D-2 single-view or multi-view example.",
            "Supply the requested image views, load its specified model and run. The documented native example produces geometry without textures/materials.",
            "Find the generated .glb mesh in the output/mesh folder and import it into Blender using File > Import > glTF 2.0.",
            "Inspect scale and geometry, refine what the shot needs, add materials, lighting and a camera, then animate a simple turntable or camera move.",
            "Save the .blend file and preview the motion. If your target only needs a generated clip, document why you are skipping this optional branch.",
        ],
        "checkpoint": "An inspectable mesh and saved Blender scene with a short motion preview, or a recorded reason this branch does not apply.",
        "sources": [
            ("Native Hunyuan3D-2 workflow and limitations", "https://docs.comfy.org/tutorials/3d/hunyuan3D-2"),
            ("Blender glTF import/export", "https://docs.blender.org/manual/en/4.3/addons/import_export/scene_gltf2.html"),
        ],
    },
    {
        "id": "publish",
        "title": "Package the result and the recipe",
        "summary": "Make the journey useful to the next person, including the choices and failures that shaped it.",
        "actions": [
            "For a Blender scene, render an image sequence, then assemble and edit it into a video; keep the source frames for revisions.",
            "For a generated clip, review the complete export, trim it if needed and confirm it plays in the intended destination.",
            "Bundle the brief, input references, workflow JSON, model identifiers, settings, environment notes and output locations.",
            "Export your field notes from this console. Include what worked, what failed, time/cost observations and why you chose this path.",
            "Share only after checking that the package includes the files and permissions another person needs to use it.",
        ],
        "checkpoint": "A final video and a readable recipe that connects each major decision to its evidence. Exporting here prepares a package; it does not publish it online.",
        "sources": [
            ("Blender animation rendering and image sequences", "https://docs.blender.org/manual/en/latest/render/output/animation.html"),
        ],
    },
]

SOURCES = [
    *COMFY_PROJECT_LINKS,
    {
        "title": "ComfyUI — App Mode",
        "url": "https://docs.comfy.org/interface/app-mode",
        "note": "Present selected workflow inputs and outputs in a simpler interface after the underlying workflow works. Check the guide's frontend requirements.",
    },
    {
        "title": "ComfyUI — reusable subgraphs",
        "url": "https://docs.comfy.org/interface/features/subgraph",
        "note": "Organize related nodes into reusable components. This helps graph structure; models and dependencies still need to match.",
    },
    {
        "title": "pixaroma — ComfyUI Tutorial Series, Ep01",
        "url": TUTORIAL_URL,
        "note": "Inspiration, published July 9, 2024. Its description covers installation, models, first image and workflow sharing. Pair older setup steps with current official docs.",
    },
    {
        "title": "pixaroma — ComfyUI Tutorial Series, Ep02",
        "url": "https://www.youtube.com/watch?v=JE5eykLuTXI",
        "note": "The supplied Nodes and Workflow Basics transcript informs Workflow lab's seven exercises. The July 2024 interface is paired with current node, link and export documentation.",
    },
    {
        "title": "pixaroma — ComfyUI Tutorial Series, Ep03",
        "url": "https://www.youtube.com/watch?v=g8UlYE_HM2M",
        "note": "TXT2IMG Basics, published July 16, 2024. Ten annotated lessons cover sampling controls, batches, shared widgets and branches. Controlled experiment turns these ideas into a comparison plan.",
    },
    {
        "title": "Max Novak — Ultimate Beginner Guide to Learning ComfyUI (2026)",
        "url": "https://www.youtube.com/watch?v=l4CiwGS2ewY",
        "note": "The supplied 00:00–21:52 transcript informs ten additional annotations and the Video & audio lesson. Covers LTX-2.3, subgraphs, export, prompt expansion, upscaling and image editing. NVIDIA sponsorship and the creator's preferences remain attributed; these are not our performance measurements.",
    },
    {
        "title": "pixaroma — ComfyUI Tutorial Series, Ep04",
        "url": "https://www.youtube.com/watch?v=xedwjtaPVzw",
        "note": "IMG2IMG and LoRA Basics, published July 24, 2024. Ten annotations and Workflow lab's Image to image practice cover source preparation, denoise, both LoRA branches, fixed comparisons and iterative drift. Historical preferences are checked against current node behavior.",
    },
    {
        "title": "ComfyUI — native LTX-2.3 task-specific templates",
        "url": "https://docs.comfy.org/tutorials/video/ltx/ltx-2-3",
        "note": "Alternative video paths with exact component manifests. Image + audio-to-video and structural control solve different tasks; generating a new clip does not establish preservation of an existing scene.",
    },
    {
        "title": "AUTOMATIC1111 — official repository",
        "url": PATHS[0]["url"],
        "note": "Primary source for features and installation; the guide here remains planned.",
    },
    {
        "title": "Forge UI — official repository",
        "url": PATHS[1]["url"],
        "note": "Primary source for Forge's scope and compatibility notes. Performance statements are project aims, not our benchmarks.",
    },
    {
        "title": "InvokeAI — official repository",
        "url": PATHS[2]["url"],
        "note": "Primary source for its canvas and workflow capabilities.",
    },
    {
        "title": "Invoke — workflow editor",
        "url": "https://invoke.ai/features/workflows/editor-interface/",
        "note": "Documents its node workflow interface; preserve this option for future guide expansion.",
    },
    {
        "title": "ComfyUI — current system requirements",
        "url": "https://docs.comfy.org/installation/system_requirements",
        "note": "Platform and accelerator guidance changes. Check this source for your hardware and the selected workflow; there is no single VRAM requirement for every task.",
    },
    {
        "title": "Comfy Desktop — overview",
        "url": ENVIRONMENT_GUIDES["Desktop"]["url"],
        "note": "Managed local installation; follow the linked instructions for your platform.",
    },
    {
        "title": "ComfyUI Portable — Windows",
        "url": ENVIRONMENT_GUIDES["Portable"]["url"],
        "note": "Embedded environment and hardware-specific package instructions.",
    },
    {
        "title": "ComfyUI — manual installation",
        "url": ENVIRONMENT_GUIDES["Manual"]["url"],
        "note": "Use this live source for device-specific dependency commands.",
    },
    {
        "title": "Comfy Cloud — official service",
        "url": ENVIRONMENT_GUIDES["Cloud"]["url"],
        "note": "Review current pricing and supported models/nodes before selecting a cloud workflow.",
    },
    {
        "title": "ComfyUI — first generation",
        "url": "https://docs.comfy.org/get_started/first_generation",
        "note": "Baseline image generation and workflow import/export guidance.",
    },
    {
        "title": "ComfyUI — Wan2.2 video examples",
        "url": "https://docs.comfy.org/tutorials/video/wan/wan2_2",
        "note": "A documented example family, not a claim that it is the newest or best model. Match its exact model and workflow requirements.",
    },
    {
        "title": "ComfyUI — Hunyuan3D-2 examples",
        "url": "https://docs.comfy.org/tutorials/3d/hunyuan3D-2",
        "note": "Mesh-generation branch. The texture limitation described here belongs to this native example, not every 3D workflow.",
    },
    {
        "title": "Blender — glTF import/export",
        "url": "https://docs.blender.org/manual/en/4.3/addons/import_export/scene_gltf2.html",
        "note": "Versioned Blender 4.3 documentation for the .glb/.gltf handoff; check your installed version for interface differences.",
    },
    {
        "title": "Blender — rendering animations",
        "url": "https://docs.blender.org/manual/en/latest/render/output/animation.html",
        "note": "Reference for rendering frames and assembling the final movie.",
    },
]

GLOSSARY = {
    "Workflow": "A connected recipe of operations and settings. Save the recipe alongside the result.",
    "Node": "One operation in a workflow, such as loading a model, processing data or saving an output.",
    "Model / checkpoint": "Learned weights used for a generation task. A workflow needs models of the architecture it expects.",
    "Prompt": "Text describing what the model should produce; some workflows also accept negative instructions.",
    "Conditioning": "The processed guidance from text, images or other inputs that shapes generation.",
    "Latent": "An internal compressed representation used during generation, before decoding into viewable media.",
    "Sampler": "The part of a diffusion workflow that iteratively transforms noisy latent data toward an output.",
    "VAE": "A model component that translates between image space and a compressed latent representation.",
    "Seed": "A number controlling a source of randomness. Record it for comparisons; it alone does not guarantee identical output.",
    "VRAM": "Memory on the graphics processor. Resolution, frame count, model and workflow all affect demand.",
    "Custom node": "An additional workflow operation supplied by an extension, with its own compatibility requirements.",
    "Image-to-video": "Generate moving frames using a still image as guidance.",
    "Temporal consistency": "How steadily subjects, shapes and details remain recognizable as a video moves.",
    "Mesh": "Editable 3D geometry made of vertices, edges and faces.",
    "GLB / glTF": "Formats for transferring 3D assets between tools; .glb is the binary form.",
    "Render": "Compute an image from a scene. A finished 3D animation combines many rendered frames.",
    "Image sequence": "An ordered set of frame files that can be edited and assembled into a movie.",
}

FUTURE_CHECKLIST = [
    "Write a current installation guide with hardware and environment choices for this path.",
    "Create a first-image exercise and capture a reproducible baseline on a documented setup.",
    "Select and verify a compatible video workflow, including any extensions and model requirements.",
    "Document the handoff to an editable 3D scene or explain the image/video-only scope.",
    "Run the same small shot brief and record output quality, effort, runtime and costs.",
    "Capture common failures, fixes and the files another learner needs to repeat the result.",
    "Add a worked example and update the comparison using evidence from completed experiments.",
]
