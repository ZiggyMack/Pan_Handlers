"""Episode 2 practice curriculum, with current ComfyUI source corrections.

Pure presentation data: no imports, renderer, persistence, or completion state.
``seconds`` identifies a related passage in the supplied transcript, not the
duration of an exercise. Lesson order is pedagogical, so timestamps need not
increase. The deliberate experiments extend the video; none is claimed tested.

Sources reviewed 2026-09-12. Interface commands and socket behavior can differ
between the 2024 video, current upstream code, and an installed release.
"""


EPISODE_TITLE = "ComfyUI Tutorial Series: Ep02 - Nodes and Workflow Basics"
EPISODE_URL = "https://www.youtube.com/watch?v=JE5eykLuTXI"

_CORE = "https://github.com/Comfy-Org/ComfyUI/blob/master/nodes.py"
_TYPES = "https://docs.comfy.org/custom-nodes/backend/datatypes"
_NODES = "https://docs.comfy.org/basic-concepts/nodes"
_WORKFLOW = "https://docs.comfy.org/get_started/first_generation"
_SHORTCUTS = "https://docs.comfy.org/interface/shortcuts"


LESSONS = (
    {
        "id": "orient",
        "title": "Find your way around a borrowed workflow",
        "seconds": 144,
        "understand": "The canvas is a view of a connected graph. Moving your viewpoint, arranging boxes, editing connections and running the graph are different operations.",
        "do": (
            "Open a small official text-to-image workflow. Save a learning copy and keep the original file so you can return to it.",
            "Locate the model selector, prompts, sampler, decoder and saved output. Write down any missing model or node names before replacing anything.",
            "Move one node, then pan and zoom. Use Zoom to fit to find the graph again; compare the connections before and after moving it.",
            "Find the Node Library, Run/queue controls, workflow export and the current Shortcuts or Keybinding panel in your installation.",
        ),
        "check": "Keep the original and learning-copy filenames plus a screenshot showing the graph. You can point to its model and output, and confirm that moving the node did not change its connections.",
        "pitfall": "Reset View restores canvas zoom and pan; it does not rearrange nodes. Zoom to fit is a separate command. The episode's menu placement, Alt gestures and resize behavior may differ from your current keybindings and interface.",
        "sources": (
            ("Episode 2 · menu and canvas", EPISODE_URL + "&t=144s"),
            ("Current interface overview", "https://docs.comfy.org/interface/overview"),
            ("Current shortcuts and custom keybindings", _SHORTCUTS),
            ("Reset View and Fit View implementation", "https://github.com/Comfy-Org/ComfyUI_frontend/blob/main/src/services/litegraphService.ts#L918"),
        ),
    },
    {
        "id": "trace",
        "title": "Read a node and trace what its wires carry",
        "seconds": 443,
        "understand": "A node has an identity, input sockets, output sockets and settings called widgets. A wire carries a declared data type; the receiving input gives that data its role in this recipe.",
        "do": (
            "Inspect KSampler. Find its MODEL, CONDITIONING and LATENT inputs, its LATENT output, and the seed, steps and cfg widgets.",
            "Trace checkpoint CLIP into a CLIP Text Encode node, then CONDITIONING into KSampler.positive. Write that chain with the type at each connection.",
            "Trace the second encoder into KSampler.negative. Rename the two encoders Positive and Negative, then confirm their connections still determine their roles.",
            "On your learning copy, inspect the menu for a simple widget such as seed. If conversion to an input is offered, convert it, inspect the new socket, then Undo; otherwise record that this interface does not offer it.",
        ),
        "check": "Your notes identify one widget and one required socket, explain the CLIP-to-CONDITIONING conversion, and correctly trace both prompt branches without relying on node color or title.",
        "pitfall": "KSampler does not receive only latents: MODEL and CONDITIONING are different inputs. Matching socket types is a first check, not proof of model compatibility. A converted required widget needs a value from a connection; not every socket can become a widget.",
        "sources": (
            ("Episode 2 · node parts and links", EPISODE_URL + "&t=443s"),
            ("ComfyUI data types", _TYPES),
            ("Inputs, outputs and widgets", "https://docs.comfy.org/custom-nodes/js/javascript_objects_and_hijacking"),
            ("Required inputs and validation", "https://docs.comfy.org/custom-nodes/backend/server_overview"),
            ("KSampler inputs and settings", "https://docs.comfy.org/built-in-nodes/sampling/ksampler"),
        ),
    },
    {
        "id": "build",
        "title": "Build the classic graph: seven boxes, six node types",
        "seconds": 685,
        "understand": "This classic SDXL example uses six node types and seven instances because CLIP Text Encode appears twice. The model, both prompt branches and the starting latent meet at the sampler; the VAE makes its result viewable.",
        "do": (
            "Create a separate blank workflow. Add Load Checkpoint, two CLIP Text Encode nodes, Empty Latent Image, KSampler, VAE Decode and Save Image.",
            "Choose a compatible, complete SDXL checkpoint and the settings and dimensions specified by its model instructions. Start with latent batch_size 1 and queue/run count 1.",
            "Connect checkpoint MODEL to KSampler.model, CLIP to both encoders, and VAE to the decoder. Connect the encoders' CONDITIONING outputs to the sampler's positive and negative inputs.",
            "Connect Empty Latent Image to KSampler.latent_image, the sampler's LATENT output to VAE Decode.samples, and the decoder's IMAGE to Save Image.images. Enter a simple prompt, run once, and save the graph and result.",
        ),
        "check": "Keep an exported seven-box graph and its saved image. Record the actual checkpoint filename, dimensions and sampler settings, and identify the two instances that share one node type.",
        "pitfall": "Coloring an encoder green or red does not make its prompt positive or negative; its destination does. The default example may use SD1.5, and a similarly named model is not automatically compatible. Use this classic SDXL recipe only with the components it requires.",
        "sources": (
            ("Episode 2 · build the SDXL workflow", EPISODE_URL + "&t=685s"),
            ("Official text-to-image explanation", "https://docs.comfy.org/tutorials/basic/text-to-image"),
            ("Checkpoint components and compatibility", "https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple"),
            ("Prompt encoding", "https://docs.comfy.org/built-in-nodes/ClipTextEncode"),
            ("Model compatibility troubleshooting", "https://docs.comfy.org/troubleshooting/model-issues"),
        ),
    },
    {
        "id": "decode",
        "title": "Diagnose the boundary between latent data and pixels",
        "seconds": 1108,
        "understand": "Preview Image consumes IMAGE data. KSampler produces LATENT data, so a matching VAE decoder must sit between them. The decoder also has a required VAE input that supplies the conversion model.",
        "do": (
            "Duplicate your working graph for a debugging exercise. Keep its existing Save Image branch and add a Preview Image node beside it.",
            "Try connecting the sampler's LATENT directly to Preview Image. Note the type mismatch, then insert another VAE Decode between them and deliberately leave its vae socket empty.",
            "Run once and read the actual validation message. Record the node and required input it names; do not infer success from another node's color.",
            "Use Workflow anatomy → VAE paths to choose the checkpoint's usable VAE or the separate VAE specified by your model. Connect it to the decoder and run again. Keep the error-and-fix note and resulting preview; point to where LATENT becomes IMAGE.",
        ),
        "check": "You have the observed missing-input message, the corrected branch and a visible preview. You can distinguish a type mismatch from a missing compatible VAE.",
        "pitfall": "VAE encoding and decoding are learned, lossy transformations, not an exact ZIP round trip. An invalid required input can prevent an output branch from validating; other branches are not guaranteed to run. Use the error message rather than the video's particular red/green sequence.",
        "sources": (
            ("Episode 2 · inspect and repair a preview branch", EPISODE_URL + "&t=1108s"),
            ("VAE Decode inputs and output", "https://docs.comfy.org/built-in-nodes/VAEDecode"),
            ("Input validation behavior", "https://docs.comfy.org/custom-nodes/backend/server_overview"),
            ("Latent diffusion and learned image compression", "https://arxiv.org/abs/2112.10752"),
        ),
    },
    {
        "id": "experiment",
        "title": "Change one variable and explain the result",
        "seconds": 1189,
        "understand": "A useful comparison records the actual settings and changes one input at a time. Seed affects sampling noise, dimensions affect the latent batch, and unchanged calculations may be reused from cache.",
        "do": (
            "Return to the working baseline. Set the seed's control to fixed, disable automatic queuing, keep batch_size and queue/run count at 1, and record the seed, model, prompts, dimensions and sampler settings.",
            "Run the unchanged graph once more. Note whether sampling visibly ran or was reused; record unknown if your interface gives no evidence. Keep the baseline result.",
            "Change just one prompt detail and save result B. Restore the baseline prompt, change only the seed and save result C. Record each actual seed and describe the visible differences.",
            "Before increasing either setting, explain the difference between queue/run count 2 with batch_size 1 and queue/run count 1 with batch_size 2. Predict the queued jobs and latents per job without launching the larger batch.",
        ),
        "check": "Keep named baseline/B/C outputs and a short comparison listing the single changed variable for each. Your note distinguishes two one-latent jobs from one two-latent job and records any observed cache reuse without claiming a benchmark.",
        "pitfall": "Empty Latent Image creates zero-filled latent data; sampling prepares the noise using the seed. It is not a random-noise image generator. Queue count and latent batch_size are different controls, and a fixed seed alone does not guarantee identical pixels across environments.",
        "sources": (
            ("Episode 2 · changing image dimensions", EPISODE_URL + "&t=1189s"),
            ("Empty latent initialization", _CORE + "#L1125"),
            ("Noise preparation and KSampler", _CORE + "#L1420"),
            ("Cached outputs and changed inputs", "https://docs.comfy.org/custom-nodes/backend/server_overview"),
            ("Fixed and automatic seed controls", "https://docs.comfy.org/custom-nodes/v3_migration#control_after_generate"),
            ("Queue batch count", "https://docs.comfy.org/interface/settings/comfy#batch-count-limit"),
        ),
    },
    {
        "id": "organize",
        "title": "Branch and organize without changing the recipe",
        "seconds": 1215,
        "understand": "A readable layout helps someone follow the data. Output fan-out creates another consumer; reroutes guide wires; group frames label and move related boxes. Layout and execution logic remain separate concerns.",
        "do": (
            "Save another copy. Arrange inputs, sampling and output areas; give the two prompts clear titles and optional colors while keeping their original connections.",
            "Connect the final VAE Decode IMAGE output to both Save Image and Preview Image. This adds a preview branch without depending on an output socket on Save Image.",
            "Use your interface's native reroute or a Reroute node on a long wire. Trace it end to end to confirm it still joins the same producer and consumer.",
            "Add and name group frames for the areas, then move a frame. Recheck links and fixed settings, run the graph, and save an overview with its result.",
        ),
        "check": "Your organized copy retains the baseline generation settings and includes the intended preview branch. An overview shows readable groups and a rerouted connection; both the saved output and preview are available after the test.",
        "pitfall": "A frame is not an execution unit or a reusable subgraph, and changing titles, colors or wire shapes does not change prompt roles. Saving does not stop other branches: fan out the upstream IMAGE. Current Save Image may also pass IMAGE through; older releases may not.",
        "sources": (
            ("Episode 2 · arrange and group nodes", EPISODE_URL + "&t=1215s"),
            ("Links and native reroutes", "https://docs.comfy.org/basic-concepts/links"),
            ("Group and link presentation settings", "https://docs.comfy.org/interface/settings/lite-graph"),
            ("Reusable subgraphs are a separate feature", "https://docs.comfy.org/interface/features/subgraph"),
            ("Current Save Image behavior", _CORE + "#L1501"),
        ),
    },
    {
        "id": "handoff",
        "title": "Reopen the graph and leave a usable handoff",
        "seconds": 170,
        "understand": "The graph, the files it depends on and the observed result are different artifacts. A portable learning record makes those relationships explicit so the next person can rebuild the experiment.",
        "do": (
            "Export the normal editable workflow JSON from your final copy. Keep the untouched source workflow and source URL alongside it; retain the layout and groups rather than exporting only an API prompt.",
            "Add a short receipt: ComfyUI/backend and frontend versions, custom-node pack versions if used, exact model and VAE filenames with source links, prompts, actual seed, dimensions, settings and any input-file names.",
            "Include a representative output and a note describing the experiment, the change you made and the result you observed. Record where another learner can obtain required files; a workflow JSON does not bundle model weights.",
            "Open the exported JSON in a fresh workflow tab. Check its model selections and inputs, run one small test, and record either the observed result or the exact dependency or validation problem that still prevents the handoff.",
        ),
        "check": "Keep the original graph, final editable JSON, dependency receipt and example output together. Consider the handoff verified only after reopening and successfully running the exported graph; document any remaining portability limits.",
        "pitfall": "Saving a workflow is not proof it can run elsewhere. PNG workflow metadata can be disabled or stripped, and a graph export does not include its models or extensions. Reopening successfully verifies the graph can be read, not that generation or exact reproduction has succeeded.",
        "sources": (
            ("Episode 2 · save and load the workflow", EPISODE_URL + "&t=170s"),
            ("Workflow import and editable JSON export", _WORKFLOW),
            ("Separate workflow and API representations", "https://docs.comfy.org/custom-nodes/js/javascript_objects_and_hijacking"),
            ("Save Image and optional PNG metadata", _CORE + "#L1501"),
            ("Missing-node states", _NODES),
        ),
    },
)


CONCEPTS = (
    {
        "term": "Node type / node instance",
        "meaning": "The type defines the operation. Each box is one instance with its own settings and connections.",
        "try": "Find the two CLIP Text Encode instances and explain why this graph has seven boxes but six types.",
    },
    {
        "term": "Socket / widget",
        "meaning": "A socket receives linked data; a widget supplies a setting in the node. Some widgets can become sockets.",
        "try": "Point to KSampler.model and its seed setting, and describe how each receives its value.",
    },
    {
        "term": "LATENT / IMAGE",
        "meaning": "LATENT holds a model-space representation. IMAGE holds pixels. A compatible VAE translates between these representations.",
        "try": "Trace KSampler to VAE Decode to Preview Image and name the type on both wires.",
    },
    {
        "term": "Seed / noise / cache",
        "meaning": "A seed helps control sampling noise. Cache reuse can avoid recomputing unchanged work; it is a separate mechanism.",
        "try": "Compare an unchanged fixed-seed run with a seed-only change, and record what your interface actually reports.",
    },
    {
        "term": "Queue count / latent batch_size",
        "meaning": "Queue count submits repeated workflow jobs. Latent batch_size sets the number of latent images inside a job.",
        "try": "Explain two jobs with one latent each versus one job with two latents before increasing either setting.",
    },
    {
        "term": "Group frame / subgraph",
        "meaning": "A frame organizes boxes visually. A subgraph packages connected operations behind a reusable interface.",
        "try": "Move a named group and confirm its nodes still use their original sockets; do not mistake the frame for a new node.",
    },
)
