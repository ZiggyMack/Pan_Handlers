"""Episode 4 bookmarks and current context; pure data, with no learner state.

Observations paraphrase the learner-supplied 00:00-17:21 transcript. The title
and URL were verified on Pixaroma's original video page. Technical references
were checked on September 12, 2026. Tutorial preferences and historical timings
are not measurements from this console; upstream UI can differ from a learner's
installed release. No workflow execution or model installation is claimed.
"""

EPISODE_TITLE = "ComfyUI Tutorial Series: Ep04 - IMG2IMG and LoRA Basics"
EPISODE_URL = "https://www.youtube.com/watch?v=xedwjtaPVzw"
SOURCE_KEY = "ep4"  # October 4 archive/hash and user-supplied URL in tutorial_register.

_CORE = "https://github.com/Comfy-Org/ComfyUI/blob/master/nodes.py"
_SAMPLERS = "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/samplers.py"
_VAE_LORA = "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/sd.py"
_RESIZE = "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/utils.py"
_IMG2IMG = "https://docs.comfy.org/tutorials/basic/image-to-image"
_ENCODE = "https://docs.comfy.org/built-in-nodes/VAEEncode"
_SCALE = "https://docs.comfy.org/built-in-nodes/ImageScale"
_LORA = "https://docs.comfy.org/tutorials/basic/lora"
_LORA_NODE = "https://docs.comfy.org/built-in-nodes/LoraLoader"
_CIVITAI_FILTERS = "https://github.com/civitai/civitai/blob/main/src/server/schema/model.schema.ts"
_CIVITAI_VERSION = "https://github.com/civitai/civitai/blob/main/src/server/schema/model-version.schema.ts"
_PASTE = "https://github.com/Comfy-Org/ComfyUI_frontend/blob/main/src/composables/usePaste.ts"
_CLIPSPACE = "https://docs.comfy.org/tutorials/basic/inpaint"
_REPRO = "https://docs.pytorch.org/docs/stable/notes/randomness.html"
_MODES = "https://docs.comfy.org/basic-concepts/nodes#mode"


LESSONS = (
    {
        "seconds": 36,
        "title": "Give the sampler an encoded reference image",
        "takeaway": "Load Image produces pixels; KSampler's latent_image socket needs LATENT.",
        "observed": "Pixaroma replaces Empty Latent Image with a loaded bunny image, adds VAE Encode and connects the checkpoint's bundled VAE.",
        "apply": "Save a copy of the working SDXL graph. Connect Load Image IMAGE to VAE Encode pixels, then its LATENT output to KSampler latent_image. Supply a compatible VAE to both encoding and final decoding; the checkpoint output works when it includes that VAE. Keep the checkpoint MODEL and encoded positive/negative CONDITIONING connected to the sampler. Trace KSampler LATENT through VAE Decode to Save Image. Plain VAE Encode does not take MODEL, CLIP or prompt conditioning as inputs.",
        "keep": "Original input image, baseline workflow JSON and exact checkpoint/VAE. Confirm each required socket before attempting the first image-to-image run.",
        "sources": (("Image-to-image graph", _IMG2IMG), ("VAE Encode sockets", _ENCODE), ("Checkpoint, sampler and decoder definitions", _CORE)),
    },
    {
        "seconds": 90,
        "title": "Treat denoise as a sampling control",
        "takeaway": "Denoise is not opacity, prompt weight or the percentage of the image preserved.",
        "observed": "The first run uses denoise 1.0 and loses the intended bunny structure. The narrator tries lower values and uses a tracing-paper analogy to explain the changing resemblance.",
        "apply": "Keep one reference, prompt, seed, dimensions and sampler setup fixed; compare two denoise values below 1. In standard KSampler, a lower positive denoise selects the later, lower-noise portion of a longer schedule while retaining the configured step count. It usually limits change, but preservation depends on the model, schedule and image. At 1 the full schedule runs; do not promise all reference influence disappears in every workflow. The episode's 0.6 starting point is a preference. Even a minimally changed VAE round trip is not an exact pixel copy.",
        "keep": "Each tested denoise value, actual seed and a specific observation about pose, composition or identity. A value of 0.5 does not mean half the original image survives.",
        "sources": (("KSampler schedule selection and noise scaling", _SAMPLERS), ("VAE encode/decode implementation", _VAE_LORA)),
        "related": ((174, "Tracing-paper analogy"), (210, "Creator's starting value"), (242, "Robot-bunny example")),
    },
    {
        "seconds": 259,
        "title": "Set the reference size before VAE encoding",
        "takeaway": "Upscale Image can resize downward as well as upward.",
        "observed": "The tutorial initially inherits the loaded image's dimensions, then inserts Upscale Image between Load Image and VAE Encode to control the working size.",
        "apply": "Use Load Image → Upscale Image → VAE Encode and choose dimensions supported by your model/template and memory budget. The roughly 1024-pixel SDXL example and multiples-of-64 suggestion are not universal rules. Preview the resized reference: center crop can remove edges, while forcing a different aspect ratio with crop disabled can stretch it. Current ImageScale can preserve aspect ratio by deriving one dimension when it is zero. Verify the actual encoded/output dimensions because a VAE may crop to its compression grid.",
        "keep": "Original and working dimensions, resize method, crop choice and resized reference. Record the subject or edges lost to cropping before attributing that change to denoise.",
        "sources": (("ImageScale controls", _SCALE), ("Aspect-ratio handling", _CORE), ("Center-crop and resize behavior", _RESIZE), ("VAE input cropping", _VAE_LORA)),
        "related": ((324, "Resize before encoding"), (397, "Cropping to a different aspect ratio")),
    },
    {
        "seconds": 281,
        "title": "Locate the memory bottleneck before changing the graph",
        "takeaway": "Tiled VAE processing addresses the VAE stage, not every possible out-of-memory error.",
        "observed": "An image enlarged fourfold triggers a tiled-VAE retry. The creator reports a much slower result and then reduces the input size before encoding.",
        "apply": "Read the failing node and backend log. Current standard VAE encoding/decoding can retry with tiles after an out-of-memory error; explicit tiled nodes are also available. Tiling processes overlapping portions and can change time or image appearance. It does not make a large diffusion model or high-resolution sampler fit automatically. For this starter exercise, reduce working dimensions before VAE Encode, keep one image in the batch and retry one change at a time. Inspect whether the failure occurs during encoding, sampling or decoding.",
        "keep": "Failing stage, dimensions, batch size, error text and the change tested. The tutorial's roughly 4/200/5-second examples describe its historical setup, not an expected runtime on yours.",
        "sources": (("VAE memory handling and tiled fallback", _VAE_LORA), ("Explicit tiled encode/decode nodes", _CORE)),
        "related": ((293, "Inspecting the terminal"), (304, "Cancelling the running job"), (388, "Smaller input comparison")),
    },
    {
        "seconds": 411,
        "title": "Keep iterations traceable when reusing an output",
        "takeaway": "An output reused as input starts another edit and can accumulate drift.",
        "observed": "Pixaroma copies a generated image and uses Ctrl+V to supply the next reference, including a demonstration that creates a new Load Image node.",
        "apply": "Save the original and accepted result before another pass. In a compatible frontend, pasting actual image data can update a selected image node or create Load Image; clipboard contents, focus and UI version matter. Comfy's internal Copy/Paste Clipspace is a separate route. Check the input thumbnail and filename after either operation; upload the saved file if needed. Compare each new edit with both its immediate input and the original. Repeated encode/sample/decode passes can change identity, detail and composition even at a modest denoise.",
        "keep": "Iteration number, source filename, exact settings and saved output. Use original → pass 1 → pass 2 labels so a copied result does not silently replace your baseline.",
        "sources": (("Current image-paste handling", _PASTE), ("Internal Clipspace workflow", _CLIPSPACE), ("Current shortcut settings", "https://docs.comfy.org/interface/shortcuts")),
        "related": ((427, "Pasting the image"), (440, "Creating a Load Image node from the clipboard")),
    },
    {
        "seconds": 467,
        "title": "Distinguish training a LoRA from using one",
        "takeaway": "Load LoRA applies an existing adapter's learned weight updates during generation.",
        "observed": "The episode introduces Low-Rank Adaptation for objects, people and styles, then switches to downloading and using already-trained adapters.",
        "apply": "Treat training and loading as different tasks. LoRA training learns additional low-rank updates with a base model; this lesson loads those existing updates. Loading does not train on your uploaded reference or permanently rewrite the checkpoint file. The adapter must match the intended model architecture and supported loader. Its effects can reach many network layers; it is not a mask restricting edits to one region of your image, and it does not guarantee an exact person, object or style.",
        "keep": "Base checkpoint, adapter filename/version and the behavior you want to test. Label the exercise as inference with a pretrained LoRA, not training or a newly fine-tuned checkpoint.",
        "sources": (("Original LoRA research", "https://arxiv.org/abs/2106.09685"), ("Loading and applying LoRA patches", _VAE_LORA)),
    },
    {
        "seconds": 591,
        "title": "Choose a compatible LoRA version and keep its instructions",
        "takeaway": "A model-page name is not enough; check the selected version's base and guidance.",
        "observed": "Pixaroma filters Civitai for LoRA and SDXL, checks the Aether Cloud and Aether Fire examples, records trigger phrases and saves their files under models/loras.",
        "apply": "Filter by LoRA type and your actual base family, then inspect the exact version's base model, filename, recommended weights and trigger words. SD 1.5, SDXL and other architectures are not interchangeable just because they use LoRAs. A family match is a starting check, not a guarantee of the same results across checkpoints. Follow any documented trigger phrase; some adapters need no special trigger. On a local install, put the downloaded weight file in models/loras or a configured equivalent, refresh the list and select that file. Cloud uses its own supported model-import route.",
        "keep": "Model/version page URL, base family, exact filename, recommended settings and any trigger phrase. The tutorial's filters, time range and example preferences are historical choices.",
        "sources": (("Civitai type and base-model filters", _CIVITAI_FILTERS), ("Version-specific base model and trained words", _CIVITAI_VERSION), ("ComfyUI LoRA folder and loader", _LORA_NODE), ("Cloud model imports", "https://docs.comfy.org/cloud/import-models")),
        "related": ((622, "Checking an example's base and triggers"), (648, "Local LoRA directory"), (695, "Refreshing the model list")),
    },
    {
        "seconds": 705,
        "title": "Route the LoRA's MODEL and CLIP outputs separately",
        "takeaway": "The sampler uses the patched MODEL; prompt encoders use the patched CLIP.",
        "observed": "The creator inserts Load LoRA between the checkpoint and KSampler on the MODEL branch, and before the positive/negative prompt encoders on the CLIP branch.",
        "apply": "For the classic SDXL graph, feed checkpoint MODEL and CLIP into Load LoRA. Route its MODEL output to KSampler model and its CLIP output to both CLIP Text Encode nodes. Their CONDITIONING outputs still go to KSampler positive and negative. Leave the compatible VAE on its encode/decode route. Verify the old direct checkpoint links have been replaced where intended; visual placement alone changes no dependency. Some adapters have no text-encoder updates, and model-only loaders exist for the corresponding recipe.",
        "keep": "A saved graph showing both branches. The positive/negative sockets are CONDITIONING, not CLIP; the LoRA node does not encode the reference image.",
        "sources": (("LoRA example graph and outputs", _LORA), ("LoRA loader socket definitions", _LORA_NODE)),
        "related": ((757, "Routing CLIP through the loader"), (763, "Routing MODEL through the loader")),
    },
    {
        "seconds": 817,
        "title": "Compare LoRA strengths against a fixed baseline",
        "takeaway": "Keep the baseline stable and change one independent control at a time.",
        "observed": "Pixaroma fixes the seed, compares the prompt with the LoRA bypassed and enabled, then experiments with strength_model before returning to random seeds for exploration.",
        "apply": "Save an adapter-off result with the same prompt, actual seed, dimensions and sampler settings. Then enable one LoRA at its documented starting strengths. strength_model scales diffusion-model patches; strength_clip scales available text-encoder patches, so it may have no effect for an adapter without those patches. Changing one strength to zero does not necessarily disable the other branch; both zero gives an explicit no-adapter baseline in the standard loader. Compare one strength at a time. Higher values are not reliably better, and the tutorial's 0.3-1 range is not universal. Fixed seeds aid comparisons but do not guarantee identical pixels across environments.",
        "keep": "Actual seed, adapter state, both strengths, model/version, full sampler settings and paired outputs. If using bypass, verify both MODEL and CLIP pass through; mute is a different mode.",
        "sources": (("LoRA controls", _LORA_NODE), ("Independent patch strengths", _VAE_LORA), ("Zero-strength return behavior", _CORE), ("Bypass and mute", _MODES), ("Reproducibility limits", _REPRO)),
        "related": ((825, "Adapter-off comparison"), (854, "Model strength"), (906, "Random seeds for exploration")),
    },
    {
        "seconds": 912,
        "title": "Combine the adapter with an encoded reference deliberately",
        "takeaway": "LoRA strength and image-to-image denoise control different parts of the workflow.",
        "observed": "The final exercise keeps the LoRA branches, replaces the empty latent with a resized and encoded bunny image, and lowers denoise for a fire-themed variation.",
        "apply": "Start from the verified LoRA graph and add Load Image → resize → VAE Encode → KSampler latent_image. Supply the compatible VAE and preserve the patched MODEL/CLIP routes. Use any documented trigger phrase and begin with an image-to-image denoise below 1. Hold adapter strengths fixed while testing denoise; then hold the chosen denoise fixed for a strength comparison. Judge whether the desired style and source composition both survive. For an AI-assisted 3D shot, retain the editable scene and original render: this route changes image pixels, not the scene geometry.",
        "keep": "Original/resized reference, base and LoRA versions, both strengths, denoise, prompt, seed, workflow JSON and output. Record one accepted result and a concrete limitation before handing the recipe to another learner.",
        "sources": (("Image-to-image baseline", _IMG2IMG), ("LoRA branch wiring", _LORA), ("Denoise schedule", _SAMPLERS)),
        "related": ((959, "Lowering denoise"), (976, "Final workflow recap")),
    },
)
