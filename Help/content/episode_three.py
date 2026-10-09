"""Episode 3 bookmarks and current context; pure data, with no learner state.

The observations paraphrase the learner-supplied 00:21-20:26 transcript.
References were checked on September 12, 2026. Upstream features can precede
an installed stable frontend; the notes do not claim a workflow was executed.
"""

EPISODE_TITLE = "ComfyUI Tutorial Series: Ep03 - TXT2IMG Basics"
EPISODE_URL = "https://www.youtube.com/watch?v=g8UlYE_HM2M"
SOURCE_KEY = "ep3"  # October 4 archive/hash and URL evidence in tutorial_register.

_CORE = "https://github.com/Comfy-Org/ComfyUI/blob/master/nodes.py"
_SAMPLER = "https://docs.comfy.org/built-in-nodes/sampling/ksampler"
_NOISE = "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/sample.py"
_REPRO = "https://docs.pytorch.org/docs/stable/notes/randomness.html"
_CACHE = "https://docs.comfy.org/custom-nodes/backend/server_overview"
_EVENTS = "https://docs.comfy.org/development/comfyui-server/comms_messages"
_COMMANDS = "https://github.com/Comfy-Org/ComfyUI_frontend/blob/main/src/composables/useCoreCommands.ts"
_WIDGETS = "https://docs.comfy.org/custom-nodes/js/javascript_objects_and_hijacking"
_PRIMITIVE = "https://github.com/Comfy-Org/ComfyUI_frontend/blob/main/src/extensions/core/widgetInputs.ts"
_SHORTCUTS = "https://docs.comfy.org/interface/shortcuts"
_SUBGRAPH = "https://docs.comfy.org/interface/features/subgraph"
_LEGACY_GROUP = "https://github.com/Comfy-Org/ComfyUI_frontend/blob/main/src/extensions/core/groupNode.ts"
_MODES = "https://docs.comfy.org/basic-concepts/nodes#mode"
_PARTIAL = "https://docs.comfy.org/interface/features/partial-execution"
_FIRST = "https://docs.comfy.org/get_started/first_generation"


LESSONS = (
    {
        "seconds": 21,
        "title": "Keep a working text-to-image baseline",
        "takeaway": "Trace the existing graph before changing its controls.",
        "observed": "The episode starts with the previous SDXL graph: checkpoint, two text encoders, empty latent, KSampler, VAE Decode and Save Image.",
        "apply": "Save a baseline and trace MODEL, CONDITIONING, LATENT and VAE into their required sockets. Empty Latent Image allocates zeros; sampling introduces seeded noise. Keep denoise at the classic text-to-image baseline of 1.0. Lower denoise is useful with an encoded reference in image-to-image; it is not a universal quality adjustment. Hiding its widget later does not disable its value.",
        "keep": "The baseline JSON, exact checkpoint/VAE, dimensions and a saved reference output.",
        "sources": (("Core nodes and empty latent", _CORE), ("Sampler noise preparation", _NOISE), ("Denoise in image-to-image", "https://docs.comfy.org/tutorials/basic/image-to-image")),
        "related": ((758, "Hiding the denoise widget"),),
    },
    {
        "seconds": 44,
        "title": "Use seed controls deliberately",
        "takeaway": "Fix the seed for a comparison; vary it for exploration.",
        "observed": "The narrator switches among randomize, increment, decrement and fixed, and demonstrates queued jobs and automatic queueing.",
        "apply": "Start with one queued job and a fixed seed. Record the seed actually submitted, since the displayed value may advance for the next job. Then change only the seed for one exploration run. A seed controls randomness, but identical pixels are not guaranteed across hardware, software versions or nondeterministic operations. Neighboring seed numbers do not imply neighboring-looking images. Turning off automatic queueing stops new submissions; inspect pending jobs separately and interrupt an active run if needed.",
        "keep": "Actual run seed, seed-control mode, environment/version and output; note any queued jobs still outstanding.",
        "sources": (("Seeded noise", _NOISE), ("Reproducibility limits", _REPRO), ("Queue, interrupt and pending-task commands", _COMMANDS)),
        "related": ((134, "Increment and queue"), (168, "Automatic queue"), (191, "Fixed seed")),
    },
    {
        "seconds": 207,
        "title": "Tell cached work from a fresh generation",
        "takeaway": "An unchanged repeat can reuse results; a fast run is not proof of new sampling.",
        "observed": "An unchanged fixed-seed repeat reports almost no execution time. Editing the prompt makes affected work run again.",
        "apply": "Repeat the baseline and inspect completion, cached-node messages and the output. Then change one meaningful prompt attribute, such as eye color, and compare. Cached intermediate results and already-loaded model weights are different benefits. Behavior depends on node inputs, change detection and cache availability. Do not treat an added space as a reliable no-op or cache-control method; preserve the exact prompt used.",
        "keep": "What changed, cached versus executed work when visible, elapsed time, and the actual image or error.",
        "sources": (("Node caching and change detection", _CACHE), ("Execution and cache messages", _EVENTS)),
        "related": ((221, "Prompt edit triggers work"), (233, "Change eye color")),
    },
    {
        "seconds": 260,
        "title": "Compare steps and CFG without chasing bigger numbers",
        "takeaway": "Use the exact model's recipe, then test one setting at a time.",
        "observed": "The narrator varies steps and CFG, later demonstrates very low step counts, and treats roughly 30-40 steps and CFG 5-7 as useful for the demonstrated model.",
        "apply": "Keep seed, prompt, dimensions, sampler and scheduler fixed while comparing two documented step values; restore the baseline before comparing CFG. Steps set the sampling iteration budget. CFG adjusts classifier-free guidance, not a direct contrast slider. More of either does not guarantee more detail, prompt accuracy or better quality. Small changes need not produce subtle changes. Accelerated variants can require very different settings; use their own workflow instead of inheriting this episode's numbers.",
        "keep": "Each tested value, model/variant, complete sampler settings, runtime and a specific visual observation.",
        "sources": (("KSampler controls", _SAMPLER), ("Why variant-specific settings matter: SDXL-Turbo", "https://huggingface.co/stabilityai/sdxl-turbo")),
        "related": ((303, "CFG comparison"), (493, "Step-count experiment"), (578, "Sampler and scheduler choices")),
    },
    {
        "seconds": 373,
        "title": "Promote one widget into a shared control",
        "takeaway": "A Primitive supplies a compatible value; it does not perform the sampler's job.",
        "observed": "CFG, scheduler and steps are converted into inputs. A Primitive adapts to the connected setting and can feed several nodes or advance a value between runs.",
        "apply": "On a copy, expose or connect CFG's parameter input and add a compatible Primitive. Older frontends use Convert widget to input; newer ones can show sockets and widgets together. Start fixed. Connect a second sampler only if both should share that value, then verify both resolved settings. Use one Primitive per independently controlled parameter. Numeric and dropdown constraints still apply; a Primitive cannot supply a MODEL or arbitrary incompatible socket. Keep required inputs supplied and inspect the saved settings.",
        "keep": "The shared control's type/value, every node it drives, and its fixed or advancing behavior.",
        "sources": (("Widget/input conversion", _WIDGETS), ("Primitive adaptation and connection checks", _PRIMITIVE)),
        "related": ((440, "Advancing a shared value"), (453, "Convert back to a widget"), (475, "Scheduler dropdown")),
    },
    {
        "seconds": 596,
        "title": "Separate latent batch size from queue count",
        "takeaway": "Images within one generation and repeated queued jobs are different controls.",
        "observed": "The empty latent's batch size produces four, then eight images. The speed comparison is measured on the narrator's RTX 4090.",
        "apply": "In the simple one-output graph, compare batch_size 1 and 2 with one queued job. Count the saved images and record time and memory behavior. Queue count repeats submissions; latent batch_size controls samples inside a run. Larger batches can need more memory and are not guaranteed faster. Batch noise comes from the seed and batch structure; do not label each item as a separate seed-plus-one run or assume batch changes reproduce a serial sequence.",
        "keep": "Batch size, queue count, actual seed, total outputs, elapsed time and any memory error.",
        "sources": (("Empty Latent Image batch allocation", _CORE), ("Queue count", _COMMANDS), ("Batch noise generation", _NOISE)),
    },
    {
        "seconds": 663,
        "title": "Name results so another learner can follow them",
        "takeaway": "Keep the output, editable graph and experiment record together.",
        "observed": "The Save Image prefix becomes robot; later, separate branches use V1 and V2 to distinguish their files.",
        "apply": "Use descriptive prefixes such as robot-baseline and robot-cfg-test, then open the saved files to confirm their identity. Export the editor workflow JSON and keep the exact model/node versions alongside it. A prefix is a label, not a complete settings record. Preview Image serves inspection; retain a Save Image result and download Cloud outputs you need locally. Image metadata can be stripped, so keep an explicit JSON copy.",
        "keep": "Original output files, workflow JSON, branch labels, tested values and a short conclusion.",
        "sources": (("Save Image and Preview Image", _CORE), ("Workflow opening and saving", _FIRST), ("Saving Cloud outputs", "https://docs.comfy.org/get_started/cloud")),
        "related": ((1194, "Name branch outputs"),),
    },
    {
        "seconds": 685,
        "title": "Distinguish frames, legacy group nodes and Subgraphs",
        "takeaway": "Organizing the canvas and packaging a reusable component are different operations.",
        "observed": "Convert to group node wraps selected nodes into a compact interface. Manage group node reorders or hides controls; the narrator keeps Save Image outside. Later, colored group frames organize whole branches.",
        "apply": "Keep an unpacked baseline. A frame organizes visible nodes; it does not itself create a reusable node or change their logic. For a compact component, follow the modern Subgraph guide and expose only useful controls. Current upstream treats legacy group nodes as migration data, so the old menu may be absent. Inspect internal wires and hidden values after conversion, then reopen and test a saved copy. Hiding a setting changes its visibility, not its effect.",
        "keep": "Original and packaged JSON, frontend version, exposed controls and one checked output from each.",
        "sources": (("Modern Subgraphs", _SUBGRAPH), ("Legacy group-node migration", _LEGACY_GROUP), ("Frames and current shortcuts", _SHORTCUTS)),
        "related": ((735, "Manage the old group interface"), (780, "Unpack to inspect connections"), (872, "Add group frames")),
    },
    {
        "seconds": 828,
        "title": "Choose which output to run",
        "takeaway": "Partial execution, bypass and mute solve different problems.",
        "observed": "Two branches are demonstrated. Group bypass disables one branch, while bypassing the required negative encoder produces an error.",
        "apply": "For a branch-only test, select its Save Image output and use partial execution when available; required upstream work still runs or uses cache. Bypass skips a node and tries to pass suitable upstream data through. Mute/Never supplies no result. A required text encoder cannot be replaced by bypass because its inputs do not provide the CONDITIONING the sampler needs. Restore normal mode after experimenting. Multiple output branches can be requested together without guaranteeing parallel execution.",
        "keep": "Selected output, node modes, expected files and whether that branch completed or reported a missing input.",
        "sources": (("Partial execution from output nodes", _PARTIAL), ("Never and Bypass modes", _MODES), ("Output-driven execution and caching", _CACHE)),
        "related": ((901, "Bypass a group"), (953, "Required-node bypass failure"), (976, "Optional preview branch")),
    },
    {
        "seconds": 1004,
        "title": "Build a small comparison branch, then simplify",
        "takeaway": "Share stable inputs and isolate the one difference you want to inspect.",
        "observed": "KSampler, VAE Decode and Save Image are copied with incoming connections. A branch gets its own prompt encoders; a missing negative connection is repaired before comparing robot variants.",
        "apply": "Duplicate one sampler/decode/save branch using the installed frontend's paste-with-connections command, then inspect every incoming wire. Give outputs distinct prefixes. Keep the seed and other settings fixed and change one prompt attribute or sampler setting. Shared encoders affect every attached branch; duplicate an encoder only where prompts should differ. Restore the negative connection if validation reports it missing. Compare actual outputs before packaging the working graph into a Subgraph.",
        "keep": "A/B output files, the one intended difference, shared versus independent controls, and the reopenable final graph.",
        "sources": (("Paste with incoming connections", _SHORTCUTS), ("Required sampler inputs", _SAMPLER), ("Package a working component", _SUBGRAPH)),
        "related": ((1065, "Give a branch its own prompts"), (1123, "Repair missing conditioning"), (1155, "Simplify the working interface")),
    },
)
