"""A curated ComfyUI teaching atlas, independent of the learner's journal.

Node identities and sockets were checked against ComfyUI and pack-maintainer
upstream sources on 2026-09-12. This static reference does not inspect an installation,
execute workflows, or contact a renderer. It only depends on Streamlit.
"""

from html import escape

import streamlit as st

from Help.prompt_wiring import render as render_prompt_wiring


_SOURCE = "https://github.com/Comfy-Org/ComfyUI/blob/master/"
_LIBRARY_DOCS = "https://support.comfy.org/articles/7675456845-the-comfyui-interface"
_TYPE_DOCS = "https://docs.comfy.org/custom-nodes/backend/datatypes"
_MODEL_DOCS = "https://docs.comfy.org/troubleshooting/model-issues"
_PARTNER_DOCS = "https://docs.comfy.org/tutorials/partner-nodes/faq"
_CONTROLNET_DOCS = "https://docs.comfy.org/tutorials/controlnet/controlnet"
_SUBGRAPH_DOCS = "https://docs.comfy.org/interface/features/subgraph"
_CANVAS_DOCS = "https://docs.comfy.org/interface/settings/lite-graph"
_LATENT_PAPER = "https://arxiv.org/html/2112.10752v2#S3.SS1"
_VIDEO_SOURCE = _SOURCE + "comfy_extras/nodes_video.py"
_VHS_REPO = "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite"
_VHS_SOURCE = _VHS_REPO + "/blob/main/videohelpersuite/nodes.py"
_VHS_TYPES = _VHS_REPO + "/blob/main/videohelpersuite/utils.py#L43"
_IMG2IMG_DOCS = "https://docs.comfy.org/tutorials/basic/image-to-image"
_RESIZE_SOURCE = _SOURCE + "comfy/utils.py#L1012"

# ``inputs`` contains the main data sockets; ``controls`` lists user settings
# separately. Hidden execution metadata and conditional advanced controls are
# deliberately outside this starter reference and its connection explorer.
NODES = {
    "CheckpointLoaderSimple": {
        "name": "Load Checkpoint",
        "category": "Models & prompts",
        "source_category": "model/loaders",
        "purpose": "Open a checkpoint and make its model, text encoder and VAE available to the graph.",
        "inputs": {},
        "outputs": {"MODEL": "MODEL", "CLIP": "CLIP", "VAE": "VAE"},
        "controls": {"ckpt_name": "COMBO · checkpoint file"},
        "caveat": "Use the checkpoint and supporting components expected by the recipe. Some models need separate loaders or do not include a usable text encoder or VAE.",
        "availability": "Built-in node; checkpoint files are separate.",
        "source": _SOURCE + "nodes.py#L555",
        "docs": "https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple",
    },
    "LoraLoader": {
        "name": "Load LoRA (Model and CLIP)",
        "category": "Models & prompts",
        "source_category": "model/loaders",
        "purpose": "Apply a compatible LoRA's learned adjustments to MODEL and applicable CLIP weights before sampling and prompt encoding.",
        "inputs": {"model": "MODEL", "clip": "CLIP"},
        "outputs": {"MODEL": "MODEL", "CLIP": "CLIP"},
        "controls": {
            "lora_name": "COMBO · LoRA file from models/loras or a configured LoRA path",
            "strength_model": "FLOAT · diffusion-model adjustment strength",
            "strength_clip": "FLOAT · text-encoder adjustment strength, where weights are present",
        },
        "caveat": "Both model and clip are required by LoraLoader. Match the LoRA to the checkpoint family and exact version requirements, then follow its strength and trigger-word instructions. Some adapters modify only the diffusion model; their templates may use LoraLoaderModelOnly instead. Loading a LoRA applies existing weights; it does not train a new adapter.",
        "availability": "Built-in node; LoRA weights are separate. Current display name distinguishes this two-input loader from the model-only Load LoRA variant.",
        "source": _SOURCE + "nodes.py#L640",
        "docs": "https://docs.comfy.org/built-in-nodes/LoraLoader",
    },
    "CLIPTextEncode": {
        "name": "CLIP Text Encode (Prompt)",
        "category": "Models & prompts",
        "source_category": "model/conditioning",
        "purpose": "Turn prompt text into conditioning using the supplied text encoder.",
        "inputs": {"clip": "CLIP"},
        "outputs": {"CONDITIONING": "CONDITIONING"},
        "controls": {"text": "STRING · prompt"},
        "caveat": "The classic recipe uses this node twice, for positive and negative prompts. Two instances of one node type can do different jobs; newer model templates may handle prompts differently.",
        "availability": "Built-in node.",
        "source": _SOURCE + "nodes.py#L52",
        "docs": "https://docs.comfy.org/built-in-nodes/ClipTextEncode",
    },
    "VAELoader": {
        "name": "Load VAE",
        "category": "Models & prompts",
        "source_category": "model/loaders",
        "purpose": "Load a separate VAE model for encoding image pixels into latents or decoding latents into pixels.",
        "inputs": {},
        "outputs": {"VAE": "VAE"},
        "controls": {"vae_name": "COMBO · VAE file or supported VAE option"},
        "caveat": "Use the VAE specified for this model family and workflow. A checkpoint's usable built-in VAE can feed the same sockets; a separate loader is needed only when the recipe calls for it. Local VAE weights normally belong in models/vae or a configured VAE path.",
        "availability": "Built-in node; separate VAE weights must be available in the selected environment.",
        "source": _SOURCE + "nodes.py#L695",
        "docs": "https://docs.comfy.org/built-in-nodes/VAELoader",
    },
    "LoadImage": {
        "name": "Load Image",
        "category": "Reference control",
        "source_category": "image",
        "purpose": "Open source image pixels for image-to-image work, or a prepared ControlNet map such as depth, edges or a pose drawing.",
        "inputs": {},
        "outputs": {"IMAGE": "IMAGE", "MASK": "MASK"},
        "controls": {"image": "COMBO · image file upload or selection"},
        "caveat": "Loading a photograph does not automatically calculate a depth, canny or pose control map. Prepare the representation expected by the chosen ControlNet first. The MASK output is separate from that control image.",
        "availability": "Built-in node; preprocessing is a separate operation when needed.",
        "source": _SOURCE + "nodes.py#L1573",
        "docs": "https://docs.comfy.org/built-in-nodes/LoadImage",
    },
    "ImageScale": {
        "name": "Upscale Image",
        "category": "Reference control",
        "source_category": "image/upscaling",
        "purpose": "Resize IMAGE pixels to prepare a source for encoding; this node can shrink or enlarge using ordinary resampling.",
        "inputs": {"image": "IMAGE"},
        "outputs": {"IMAGE": "IMAGE"},
        "controls": {
            "upscale_method": "COMBO · nearest-exact, bilinear, area, bicubic or lanczos",
            "width": "INT · target width; 0 derives it from height and source aspect ratio",
            "height": "INT · target height; 0 derives it from width and source aspect ratio",
            "crop": "COMBO · disabled or center",
        },
        "caveat": "Despite the name, Upscale Image can downsize and does not load a learned upscaler. With both dimensions set, disabled crop resizes to that ratio and may stretch the image; center crop removes edges to fit it. Both dimensions at 0 leave the size unchanged. Choose dimensions compatible with the model and VAE before VAE Encode.",
        "availability": "Built-in image node; no separate upscaler weights required.",
        "source": _SOURCE + "nodes.py#L1706",
        "docs": "https://docs.comfy.org/built-in-nodes/ImageScale",
    },
    "ControlNetLoader": {
        "name": "Load ControlNet Model",
        "category": "Reference control",
        "source_category": "model/loaders",
        "purpose": "Load ControlNet weights matched to this generation stage's base family, such as SD1.5 or SDXL.",
        "inputs": {},
        "outputs": {"CONTROL_NET": "CONTROL_NET"},
        "controls": {"control_net_name": "COMBO · file from the controlnet model folder"},
        "caveat": "SD1.5 ControlNet weights pair with an SD1.5 checkpoint; SDXL weights pair with a supported SDXL checkpoint. Also match the trained control type, such as depth or canny. This loader does not produce a control map or apply guidance by itself.",
        "availability": "Built-in node; ControlNet model files are separate.",
        "source": _SOURCE + "nodes.py#L783",
        "docs": "https://docs.comfy.org/built-in-nodes/ControlNetLoader",
    },
    "ControlNetApplyAdvanced": {
        "name": "Apply ControlNet",
        "category": "Reference control",
        "source_category": "model/conditioning/controlnet",
        "purpose": "Attach ControlNet guidance from a control image to positive and negative conditioning before sampling.",
        "inputs": {
            "positive": "CONDITIONING", "negative": "CONDITIONING",
            "control_net": "CONTROL_NET", "image": "IMAGE", "vae": "VAE",
        },
        "outputs": {"positive": "CONDITIONING", "negative": "CONDITIONING"},
        "controls": {
            "strength": "FLOAT · guidance influence",
            "start_percent": "FLOAT · start within the sampling process, 0–1",
            "end_percent": "FLOAT · end within the sampling process, 0–1",
        },
        "caveat": "The vae input is optional in this node's schema; supply it when the selected ControlNet requires it. Matching socket types cannot establish checkpoint-family or control-map compatibility. The older ControlNetApply node is deprecated; current Apply ControlNet uses ControlNetApplyAdvanced.",
        "availability": "Built-in node; model-specific Apply variants may be needed by other workflows.",
        "source": _SOURCE + "nodes.py#L842",
        "docs": "https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced",
    },
    "EmptyLatentImage": {
        "name": "Empty Latent Image",
        "category": "Latents & sampling",
        "source_category": "model/latent",
        "purpose": "Create a zero-filled latent batch at the selected image dimensions for a classic image workflow.",
        "inputs": {},
        "outputs": {"LATENT": "LATENT"},
        "controls": {"width": "INT", "height": "INT", "batch_size": "INT"},
        "caveat": "Empty Latent Image supplies zeros; the classic KSampler path prepares seeded noise separately. Decoding this empty latent does not show the sampler's random noise. Follow the model's template for latent layout, dimensions and frame count; specialized image and video models may need another initializer.",
        "availability": "Built-in node.",
        "source": _SOURCE + "nodes.py#L1125",
        "docs": "https://docs.comfy.org/built-in-nodes/EmptyLatentImage",
    },
    "KSampler": {
        "name": "KSampler",
        "category": "Latents & sampling",
        "source_category": "model/sampling",
        "purpose": "Use MODEL and positive/negative CONDITIONING to sample an input LATENT. The result is still latent data.",
        "inputs": {
            "model": "MODEL", "positive": "CONDITIONING", "negative": "CONDITIONING",
            "latent_image": "LATENT",
        },
        "outputs": {"LATENT": "LATENT"},
        "controls": {
            "seed": "INT", "steps": "INT", "cfg": "FLOAT",
            "sampler_name": "COMBO", "scheduler": "COMBO", "denoise": "FLOAT",
        },
        "caveat": "Only latent_image takes LATENT: model takes MODEL, and positive/negative take CONDITIONING. Keep settings, model and latent format aligned with the template. A fixed seed helps comparisons but does not guarantee identical results across model, software and hardware changes.",
        "availability": "Built-in node.",
        "source": _SOURCE + "nodes.py#L1444",
        "docs": "https://docs.comfy.org/built-in-nodes/sampling/ksampler",
    },
    "VAEEncode": {
        "name": "VAE Encode",
        "category": "Latents & sampling",
        "source_category": "model/latent",
        "purpose": "Encode image pixels into LATENT data using a compatible VAE, for example as an image-to-image starting point.",
        "inputs": {"pixels": "IMAGE", "vae": "VAE"},
        "outputs": {"LATENT": "LATENT"},
        "controls": {},
        "caveat": "Both pixels and vae are required. Match the VAE to the model and latent format used by the next stage. In the classic Stable Diffusion pipeline this is learned, lossy compression; decoding reconstructs an image rather than restoring every original pixel exactly.",
        "availability": "Built-in node; requires image data and compatible VAE weights.",
        "source": _SOURCE + "nodes.py#L342",
        "docs": "https://docs.comfy.org/built-in-nodes/VAEEncode",
    },
    "VAEDecode": {
        "name": "VAE Decode",
        "category": "Decode & save",
        "source_category": "model/latent",
        "purpose": "Convert sampled latents into images with the matching VAE.",
        "inputs": {"samples": "LATENT", "vae": "VAE"},
        "outputs": {"IMAGE": "IMAGE"},
        "controls": {},
        "caveat": "Both samples and vae are required, even for a preview. Use the VAE expected by the model family and latent format; matching socket labels alone cannot establish compatibility. Classic VAE decoding is learned reconstruction, not exact ZIP-style restoration. The result is image data, not an editable 3D scene.",
        "availability": "Built-in node.",
        "source": _SOURCE + "nodes.py#L285",
        "docs": "https://docs.comfy.org/built-in-nodes/VAEDecode",
    },
    "PreviewImage": {
        "name": "Preview Image",
        "category": "Decode & save",
        "source_category": "image",
        "purpose": "Display IMAGE data through temporary preview files so you can inspect a branch's pixels.",
        "inputs": {"images": "IMAGE"},
        "outputs": {"images": "IMAGE"},
        "controls": {},
        "caveat": "LATENT cannot connect directly: decode it with a compatible VAE first. Previews are temporary; use Save Image and keep the exported file for a durable result. Current upstream inherits an IMAGE passthrough output from Save Image; older releases may have no output socket.",
        "availability": "Built-in output node; preview files are temporary and socket behavior depends on release.",
        "source": _SOURCE + "nodes.py#L1558",
        "docs": "https://docs.comfy.org/built-in-nodes/PreviewImage",
    },
    "SaveImage": {
        "name": "Save Image",
        "category": "Decode & save",
        "source_category": "image",
        "purpose": "Write images as PNG files in ComfyUI's output directory.",
        "inputs": {"images": "IMAGE"},
        "outputs": {"images": "IMAGE"},
        "controls": {"filename_prefix": "STRING"},
        "caveat": "Save Image can finish one branch while the upstream IMAGE also feeds other branches. Current upstream additionally passes IMAGE through after saving; older releases may have no output socket. Save the workflow separately as well; image metadata can be disabled or removed.",
        "availability": "Built-in output node; socket behavior depends on release.",
        "source": _SOURCE + "nodes.py#L1501",
        "docs": "https://docs.comfy.org/built-in-nodes/SaveImage",
    },
    "LoadVideo": {
        "name": "Load Video",
        "category": "Video & audio",
        "source_category": "video",
        "purpose": "Open a video file as a VIDEO object for later processing.",
        "inputs": {},
        "outputs": {"VIDEO": "VIDEO"},
        "controls": {"file": "COMBO · video file upload or selection"},
        "caveat": "VIDEO is different from an IMAGE batch. This loads existing footage; it does not generate motion from a still.",
        "availability": "Built-in video node in the checked upstream source; check your installed release.",
        "source": _SOURCE + "comfy_extras/nodes_video.py#L322",
        "docs": None,
    },
    "GetVideoComponents": {
        "name": "Get Video Components",
        "category": "Video & audio",
        "source_category": "video",
        "purpose": "Extract IMAGE frames, available AUDIO and frame rate from a VIDEO object for separate processing or export.",
        "inputs": {"video": "VIDEO"},
        "outputs": {
            "images": "IMAGE", "audio": "AUDIO", "fps": "FLOAT",
            "bit_depth": "COMBO", "color_space": "COMBO",
        },
        "controls": {},
        "caveat": "A source with no audio does not acquire speech here. Keep its fps with the extracted frames; IMAGE alone does not carry playback timing. Current upstream also exposes bit depth and color space; preserve these when relevant, and check your release's sockets.",
        "availability": "Built-in video node in the checked upstream source; decoding frames may use substantial memory.",
        "source": _VIDEO_SOURCE + "#L292",
        "docs": None,
    },
    "CreateVideo": {
        "name": "Create Video",
        "category": "Video & audio",
        "source_category": "video",
        "purpose": "Assemble IMAGE frames and optional AUDIO into a VIDEO object at the selected frame rate.",
        "inputs": {"images": "IMAGE", "audio": "AUDIO"},
        "outputs": {"VIDEO": "VIDEO"},
        "controls": {
            "fps": "FLOAT · default 30; use the source or workflow's actual rate",
            "bit_depth": "COMBO · optional; auto, 8 or 10",
            "color_space": "COMBO · optional; sRGB, HDR or HDR PQ",
            "codec": "COMBO · optional encoding; none keeps frames in tensor form",
        },
        "caveat": "The audio input is optional. This node assembles media; send its VIDEO to Save Video to keep a file. Changing fps alone changes frame playback speed and duration, without creating intermediate frames or retiming speech. Preserve the source's color settings when needed.",
        "availability": "Built-in video node in the checked upstream source; options depend on release.",
        "source": _VIDEO_SOURCE + "#L194",
        "docs": None,
    },
    "LoadAudio": {
        "name": "Load Audio",
        "category": "Video & audio",
        "source_category": "audio",
        "purpose": "Read a file into audio samples and their sample rate.",
        "inputs": {},
        "outputs": {"AUDIO": "AUDIO"},
        "controls": {"audio": "COMBO · audio file upload or selection"},
        "caveat": "The file must contain decodable audio. Loading a replacement voice track does not align it with the scene; prepare the performance and timing first.",
        "availability": "Built-in audio node in the checked upstream source.",
        "source": _SOURCE + "comfy_extras/nodes_audio.py#L332",
        "docs": None,
    },
    "SyncLipSyncNode": {
        "name": "sync.so Lip Sync",
        "category": "Partner processing",
        "source_category": "partner/video/sync.so",
        "purpose": "Send footage and speech audio to sync.so to change mouth movement for the new dialogue.",
        "inputs": {"video": "VIDEO", "audio": "AUDIO"},
        "outputs": {"VIDEO": "VIDEO"},
        "controls": {
            "seed": "INT · rerun control, not deterministic generation",
            "model": "DYNAMIC COMBO · model and its supported options",
        },
        "caveat": "This partner node uses a remote service and credits, with cost affected by duration. It may be absent from your installed release. Model options govern timing and speaker selection; inspect the result rather than assuming the whole scene is preserved.",
        "availability": "Partner API node; supported release, account, network access and credits required.",
        "source": _SOURCE + "comfy_api_nodes/nodes_sync_so.py#L24",
        "docs": _PARTNER_DOCS,
    },
    "SaveVideo": {
        "name": "Save Video",
        "category": "Decode & save",
        "source_category": "video",
        "purpose": "Save a VIDEO object using the selected output container and codec settings.",
        "inputs": {"video": "VIDEO"},
        "outputs": {"video": "VIDEO"},
        "controls": {
            "filename_prefix": "STRING", "format": "DYNAMIC COMBO · container and codec options",
        },
        "caveat": "Current upstream passes the input VIDEO through; older releases may expose no output socket. Its returned object is not proof of the saved file's encoding. Play the exported file to check picture, sound and timing.",
        "availability": "Built-in output node in the checked upstream source; options depend on release.",
        "source": _SOURCE + "comfy_extras/nodes_video.py#L125",
        "docs": None,
    },
    "VHS_VideoCombine": {
        "name": "Video Combine (VHS)",
        "category": "Decode & save",
        "source_category": "Video Helper Suite 🎥🅥🅗🅢",
        "purpose": "Export decoded IMAGE frames with optional AUDIO using the Video Helper Suite pack's formats and frame-rate settings.",
        "inputs": {"images": "IMAGE", "audio": "AUDIO", "vae": "VAE"},
        "outputs": {"Filenames": "VHS_FILENAMES"},
        "controls": {
            "frame_rate": "FLOAT · accepts INT too; default 8, use the workflow's rate",
            "loop_count": "INT · default 0",
            "filename_prefix": "STRING · base filename and optional subfolder",
            "format": "COMBO · format-specific encoding options",
            "pingpong": "BOOLEAN · default False; adds reversed playback",
            "save_output": "BOOLEAN · default True: output directory; False: temp directory",
        },
        "caveat": "This atlas teaches the decoded IMAGE route; audio and vae are optional. The pack also accepts LATENT at images when a compatible VAE is supplied, outside this simplified checker's scope. VIDEO needs Get Video Components first. Filenames are file references, not a VIDEO object; choose an audio-capable video format to keep speech.",
        "availability": "Custom node from ComfyUI-VideoHelperSuite; requires the pack in this environment and the dependencies for the chosen format. Its video encoding uses FFmpeg.",
        "source": _VHS_SOURCE + "#L233",
        "docs": _VHS_REPO + "#video-combine",
    },
}


RECIPES = {
    "classic_still": {
        "task": "Make a first still image",
        "name": "Classic checkpoint → prompt → image",
        "result": "A saved PNG and an understandable chain from a prompt to pixels.",
        "scope": "A teaching map for a classic checkpoint-based still. Choose the actual model and settings from its official template before running a workflow.",
        "nodes": (
            "CheckpointLoaderSimple", "CLIPTextEncode", "EmptyLatentImage", "KSampler", "VAEDecode", "SaveImage",
        ),
        "stages": (
            ("Prepare inputs", "Checkpoint, two encoded prompts, blank latent", "MODEL + CONDITIONING + LATENT"),
            ("Sample", "KSampler", "LATENT"),
            ("Decode", "VAE Decode + checkpoint's VAE", "IMAGE"),
            ("Keep the result", "Save Image", "PNG file"),
        ),
        "steps": (
            "Load one compatible checkpoint. Its MODEL feeds the sampler; its CLIP feeds both prompt encoders; its VAE feeds the decoder.",
            "Use two CLIP Text Encode instances for the positive and negative prompts. Combine their conditioning with the blank latent at KSampler.",
            "Decode the sampled latent and save the image. Keep the workflow, checkpoint name and settings alongside the PNG.",
        ),
        "connections": (
            ("Checkpoint.MODEL", "MODEL", "KSampler.model"),
            ("Checkpoint.CLIP", "CLIP", "Positive encoder.clip"),
            ("Checkpoint.CLIP", "CLIP", "Negative encoder.clip"),
            ("Positive encoder.CONDITIONING", "CONDITIONING", "KSampler.positive"),
            ("Negative encoder.CONDITIONING", "CONDITIONING", "KSampler.negative"),
            ("Empty Latent Image.LATENT", "LATENT", "KSampler.latent_image"),
            ("KSampler.LATENT", "LATENT", "VAE Decode.samples"),
            ("Checkpoint.VAE", "VAE", "VAE Decode.vae"),
            ("VAE Decode.IMAGE", "IMAGE", "Save Image.images"),
        ),
        "source": "https://docs.comfy.org/get_started/first_generation",
    },
    "scene_lipsync": {
        "task": "Fit replacement dialogue to a scene",
        "name": "Scene clip + replacement speech → lip-sync pass",
        "result": "A candidate video with mouth movement adjusted for a prepared replacement voice track.",
        "scope": "A conceptual scene-rewrite stage. The source clip and replacement performance must already exist. This map does not write dialogue, clone a voice, separate a soundtrack, or finish the scene edit.",
        "nodes": ("LoadVideo", "LoadAudio", "SyncLipSyncNode", "SaveVideo"),
        "stages": (
            ("Prepare two inputs", "Load Video + Load Audio", "VIDEO + AUDIO"),
            ("Adjust mouth movement", "sync.so Lip Sync · remote partner service", "VIDEO"),
            ("Save and review", "Save Video", "Video file"),
        ),
        "steps": (
            "Prepare a short speaker clip and a timed replacement voice track. Load them separately; keep the source scene for comparison.",
            "Feed VIDEO and AUDIO into sync.so Lip Sync. Confirm that the node is available, review the current credit cost, and choose its supported timing and speaker options in ComfyUI.",
            "Save the returned VIDEO. Review mouth alignment, identity, duration and sound, then bring the candidate back into the scene edit for the final mix.",
        ),
        "connections": (
            ("Load Video.VIDEO", "VIDEO", "sync.so Lip Sync.video"),
            ("Load Audio.AUDIO", "AUDIO", "sync.so Lip Sync.audio"),
            ("sync.so Lip Sync.VIDEO", "VIDEO", "Save Video.video"),
        ),
        "source": _SOURCE + "comfy_api_nodes/nodes_sync_so.py#L24",
    },
    "reference_control": {
        "task": "Guide a still with a ControlNet reference",
        "name": "Matching checkpoint + ControlNet + prepared control map",
        "result": "A still-image candidate guided by a chosen structure, such as edges, depth or pose.",
        "scope": "A conceptual extension of the classic still recipe, not a runnable workflow or tested result. Start with an already prepared control image and an official template for the exact checkpoint and ControlNet pair.",
        "nodes": (
            "ControlNetLoader", "ControlNetApplyAdvanced", "LoadImage",
            "CheckpointLoaderSimple", "CLIPTextEncode", "EmptyLatentImage",
            "KSampler", "VAEDecode", "SaveImage",
        ),
        "stages": (
            ("Match this generation stage", "Checkpoint family + ControlNet family + trained control type", "MODEL + CONTROL_NET"),
            ("Prepare the reference", "Load Image · an already prepared control map", "IMAGE"),
            ("Add guidance", "Positive/negative prompt encoders → Apply ControlNet", "CONDITIONING"),
            ("Sample and save", "KSampler → VAE Decode → Save Image", "LATENT → IMAGE → PNG"),
        ),
        "steps": (
            "Choose the base checkpoint for this stage. Pair SD1.5 with a supported SD1.5 ControlNet, or SDXL with a supported SDXL ControlNet. Check the exact model instructions as well as the family label.",
            "Choose the trained control type. Prepare its expected depth, canny, pose or other map with the appropriate preprocessor, or use a supplied prepared map. Load that map with Load Image; preprocessing is outside this teaching map.",
            "Load the ControlNet weights. Send CONTROL_NET and the map's IMAGE to Apply ControlNet, along with both prompt encoders' CONDITIONING. Supply a compatible VAE when the selected ControlNet requires it.",
            "Connect Apply ControlNet's positive and negative outputs to the sampler. The checkpoint MODEL and blank LATENT still feed KSampler; sampled latents still pass through VAE Decode and Save Image.",
            "Use the template's strength and start/end settings for a first comparison. Keep the control map, model names, settings and resulting image together; matching connections do not prove the guidance worked.",
        ),
        "connections": (
            ("Checkpoint.MODEL", "MODEL", "KSampler.model"),
            ("Checkpoint.CLIP", "CLIP", "Positive encoder.clip"),
            ("Checkpoint.CLIP", "CLIP", "Negative encoder.clip"),
            ("Positive encoder.CONDITIONING", "CONDITIONING", "Apply ControlNet.positive"),
            ("Negative encoder.CONDITIONING", "CONDITIONING", "Apply ControlNet.negative"),
            ("Load ControlNet Model.CONTROL_NET", "CONTROL_NET", "Apply ControlNet.control_net"),
            ("Load Image.IMAGE", "IMAGE", "Apply ControlNet.image"),
            ("Checkpoint.VAE", "VAE", "Apply ControlNet.vae"),
            ("Apply ControlNet.positive", "CONDITIONING", "KSampler.positive"),
            ("Apply ControlNet.negative", "CONDITIONING", "KSampler.negative"),
            ("Empty Latent Image.LATENT", "LATENT", "KSampler.latent_image"),
            ("KSampler.LATENT", "LATENT", "VAE Decode.samples"),
            ("Checkpoint.VAE", "VAE", "VAE Decode.vae"),
            ("VAE Decode.IMAGE", "IMAGE", "Save Image.images"),
        ),
        "source": _CONTROLNET_DOCS,
    },
    "video_export": {
        "task": "Bridge video, frames and audio for export",
        "name": "VIDEO → frames + sound → a saved video",
        "result": "An understandable export path that keeps frames, audio, playback timing and saved files distinct.",
        "scope": "A conceptual media bridge for an existing clip or a generated VIDEO. It does not generate footage, synchronize a new performance or claim a tested export. If you only need to save an existing VIDEO, connect it directly to Save Video.",
        "nodes": ("LoadVideo", "GetVideoComponents", "CreateVideo", "SaveVideo", "VHS_VideoCombine"),
        "stages": (
            ("Start with media", "Load Video or an existing generated output", "VIDEO"),
            ("Inspect components", "Get Video Components", "IMAGE + available AUDIO + fps"),
            ("Assemble native output", "Create Video · retain the source rate", "VIDEO"),
            ("Keep and review", "Save Video", "Video file"),
        ),
        "steps": (
            "Use a short existing VIDEO. To inspect its frames or audio separately, connect it to Get Video Components. Check whether audio is actually present and record the source fps.",
            "For the native route, connect images to Create Video.images and available audio to Create Video.audio. Set Create Video.fps to the extracted rate rather than accepting its default; preserve relevant bit depth and color space too.",
            "Connect Create Video.VIDEO to Save Video.video. Choose a supported container and codec, then save and play the actual exported file in your ComfyUI environment. Compare picture duration, speech timing and sound with the source.",
            "When an LTX or other subgraph already exposes decoded IMAGE and AUDIO, those can feed Create Video directly. Carry the generation workflow's fps into the export settings. For the optional VHS route, use the same decoded components as explained below.",
        ),
        "connections": (
            ("Load Video.VIDEO", "VIDEO", "Get Video Components.video"),
            ("Get Video Components.images", "IMAGE", "Create Video.images"),
            ("Get Video Components.audio (when present)", "AUDIO", "Create Video.audio"),
            ("Create Video.VIDEO", "VIDEO", "Save Video.video"),
        ),
        "source": _VIDEO_SOURCE + "#L194",
    },
    "image_to_image": {
        "task": "Transform an existing image, with an optional LoRA",
        "name": "Source image → resize → encode → a new image",
        "result": "A new still guided by a prepared source image and prompts, with a separate optional LoRA comparison.",
        "scope": "A teaching map for a compatible classic checkpoint workflow. This guide starts with SDXL and its documented settings; the linked basic example uses SD1.5. Use the components and dimensions required by your chosen model. This map is not a runnable graph or a tested result.",
        "nodes": (
            "LoadImage", "ImageScale", "VAEEncode", "CheckpointLoaderSimple",
            "CLIPTextEncode", "KSampler", "VAEDecode", "SaveImage", "LoraLoader",
        ),
        "stages": (
            ("Prepare the source", "Load Image → Upscale Image", "IMAGE"),
            ("Encode the starting image", "VAE Encode + compatible VAE", "LATENT"),
            ("Guide the change", "KSampler + model + encoded prompts", "LATENT"),
            ("Decode and keep", "VAE Decode + compatible VAE → Save Image", "IMAGE → PNG"),
        ),
        "steps": (
            "Save a copy of a working checkpoint graph. Replace the Empty Latent Image connection with Load Image → Upscale Image → VAE Encode → KSampler.latent_image. The prepared source image now supplies the starting latent.",
            "Choose the source dimensions in Upscale Image before encoding. Decide whether to preserve its aspect ratio or crop it, and follow the model/VAE sizing requirements. An unused Empty Latent Image node does not control this branch's dimensions.",
            "Supply the compatible VAE to both VAE Encode.vae and VAE Decode.vae, using the checkpoint's VAE or the separate VAE required by its template. Keep MODEL and both encoded prompt branches connected to KSampler.",
            "Use the model's image-to-image settings. With a fixed seed and other settings held steady, compare denoise values below 1: lower values usually retain more source structure, while higher values permit larger changes. Check the actual result; no value guarantees identity or composition preservation.",
            "Decode the sampled latent and save the output, source image and workflow together. Record the resize/crop settings, actual seed and denoise. Once the baseline works, make a separate LoRA comparison using the optional insertion below.",
        ),
        "connections": (
            ("Load Image.IMAGE", "IMAGE", "Upscale Image.image"),
            ("Upscale Image.IMAGE", "IMAGE", "VAE Encode.pixels"),
            ("Checkpoint.VAE", "VAE", "VAE Encode.vae"),
            ("VAE Encode.LATENT", "LATENT", "KSampler.latent_image"),
            ("Checkpoint.MODEL", "MODEL", "KSampler.model"),
            ("Checkpoint.CLIP", "CLIP", "Positive encoder.clip"),
            ("Checkpoint.CLIP", "CLIP", "Negative encoder.clip"),
            ("Positive encoder.CONDITIONING", "CONDITIONING", "KSampler.positive"),
            ("Negative encoder.CONDITIONING", "CONDITIONING", "KSampler.negative"),
            ("KSampler.LATENT", "LATENT", "VAE Decode.samples"),
            ("Checkpoint.VAE", "VAE", "VAE Decode.vae"),
            ("VAE Decode.IMAGE", "IMAGE", "Save Image.images"),
        ),
        "source": _IMG2IMG_DOCS,
    },
}

_IMG2IMG_LORA_CONNECTIONS = (
    ("Checkpoint.MODEL", "MODEL", "LoraLoader.model"),
    ("Checkpoint.CLIP", "CLIP", "LoraLoader.clip"),
    ("LoraLoader.MODEL", "MODEL", "KSampler.model"),
    ("LoraLoader.CLIP", "CLIP", "Positive encoder.clip"),
    ("LoraLoader.CLIP", "CLIP", "Negative encoder.clip"),
)


def find_nodes(query="", category="All categories"):
    """Find curated node IDs by every search term and an optional category."""
    terms = query.casefold().split()
    results = []
    for node_id, node in NODES.items():
        if category != "All categories" and node["category"] != category:
            continue
        searchable = " ".join((
            node_id, node["name"], node["category"], node["source_category"], node["purpose"],
            *node["inputs"], *node["inputs"].values(),
            *node["outputs"], *node["outputs"].values(),
            *node["controls"], *node["controls"].values(),
        )).casefold()
        if all(term in searchable for term in terms):
            results.append(node_id)
    return results


def connection_types_match(source_id, output_name, target_id, input_name):
    """Check this reference's socket-type equality, never runtime compatibility.

    VHS is represented by its decoded IMAGE teaching route. Its additional
    LATENT-with-VAE path uses custom type handling outside this comparison.
    """
    return NODES[source_id]["outputs"][output_name] == NODES[target_id]["inputs"][input_name]


def _node_label(node_id):
    return f"{NODES[node_id]['name']} · {node_id}"


def _selection(label, options, key, **kwargs):
    # Dependent selectors must discard an old socket when its node changes.
    if key in st.session_state and st.session_state[key] not in options:
        del st.session_state[key]
    return st.selectbox(label, options=options, key=key, **kwargs)


def _port_table(ports, label):
    if ports:
        st.table({label: list(ports), "Declared type": list(ports.values())})
    else:
        st.caption("No data sockets here; use the file selector or settings below.")


def _node_detail(node_id, expanded=False):
    node = NODES[node_id]
    with st.expander(_node_label(node_id), expanded=expanded):
        st.caption(f"{node['availability']} · Source category: {node['source_category']}")
        st.write(node["purpose"])
        left, right = st.columns(2)
        with left:
            st.markdown("**Inputs from other nodes**")
            _port_table(node["inputs"], "Input socket")
        with right:
            st.markdown("**Outputs to other nodes**")
            _port_table(node["outputs"], "Output socket")
        if node["controls"]:
            st.markdown("**Settings on the node**")
            st.table({"Setting": list(node["controls"]), "Type / role": list(node["controls"].values())})
            st.caption("Main controls are shown here. Some settings can become sockets; advanced, conditional and hidden fields are described in the source.")
        st.info(node["caveat"])
        if node_id in {"VAELoader", "VAEEncode", "VAEDecode"}:
            st.caption("For the checkpoint and separate-loader wiring paths, open 03 / Workflow anatomy → VAE paths. Choose whether you are decoding a sampler result or starting from an existing image.")
        if node_id == "KSampler":
            st.caption("For coordinated settings across samplers, open 03 / Workflow anatomy → Controlled experiment → Shared controls. Primitive controls are frontend parameter helpers, distinct from the MODEL, CONDITIONING and LATENT inputs above.")
        if node_id in {"ImageScale", "LoraLoader"}:
            st.caption("Practice the source-image chain and an optional LoRA comparison in Workflow lab → Image to image.")
        st.markdown(f"[Official node source]({node['source']})")
        if node["docs"]:
            st.markdown(f"[Official documentation]({node['docs']})")


def _recipe_map(recipe):
    tiles = []
    for index, (title, names, data) in enumerate(recipe["stages"], start=1):
        tiles.append(
            '<div class="help-atlas-stage">'
            f'<div class="help-kicker">{index:02d} / {escape(title)}</div>'
            f'<p>{escape(names)}</p><code>{escape(data)}</code></div>'
        )
    st.markdown(
        "<style>"
        ".help-atlas-map{display:flex;gap:.65rem;flex-wrap:wrap;margin:1rem 0;}"
        ".help-atlas-stage{flex:1 1 170px;padding:1rem;border:1px solid var(--help-line,#d7ddd4);"
        "border-top:3px solid var(--help-accent,#2a9d8f);border-radius:6px;"
        "background:var(--help-surface,#fffefa);min-width:0;}"
        ".help-atlas-stage .help-kicker{margin:0;}"
        ".help-atlas-stage p{font-size:.9rem;margin:.6rem 0;}"
        ".help-atlas-stage code{font-size:.75rem;white-space:normal;}"
        "</style><div class=\"help-atlas-map\">" + "".join(tiles) + "</div>",
        unsafe_allow_html=True,
    )
    st.caption("Read the stages from left to right. The connection table below shows the branches and exact sockets.")


def _recipes():
    recipe_id = _selection(
        "What are you trying to do?", list(RECIPES), "help_atlas_recipe",
        format_func=lambda value: RECIPES[value]["task"],
    )
    recipe = RECIPES[recipe_id]
    st.subheader(recipe["name"])
    st.write(recipe["result"])
    st.caption(recipe["scope"])
    if recipe_id == "classic_still":
        st.caption("This guide starts the image branch with an SDXL-compatible checkpoint. Follow its settings and the [official SDXL examples](https://comfyanonymous.github.io/ComfyUI_examples/sdxl/); the general map also describes other compatible checkpoint workflows.")
    if recipe_id == "scene_lipsync":
        st.info("The lip-sync stage is a remote partner service. Check availability in your release, account access and current credit cost before running it.")
    if recipe_id == "reference_control":
        _controlnet_lesson()
    _recipe_map(recipe)
    if recipe_id == "classic_still":
        render_prompt_wiring("help_atlas_prompts")
    for index, step in enumerate(recipe["steps"], start=1):
        st.markdown(f"{index}. {step}")
    with st.expander("Trace each connection"):
        st.table({
            "From": [edge[0] for edge in recipe["connections"]],
            "Carries": [edge[1] for edge in recipe["connections"]],
            "Into": [edge[2] for edge in recipe["connections"]],
        })
        if recipe_id == "classic_still":
            st.caption("Positive encoder and negative encoder are two CLIPTextEncode instances. The number of node types differs from the number of boxes on a canvas.")
        if recipe_id == "reference_control":
            st.caption("The connection to Apply ControlNet.vae is conditional: use it when that ControlNet requires a VAE. This classic map uses a compatible checkpoint VAE; follow the exact template if it requires a separate loader.")
        if recipe_id == "video_export":
            st.caption("Carry Get Video Components.fps into Create Video's fps setting. Some interfaces let you convert that widget to a socket and connect it; this explorer lists the main media sockets separately from settings. Audio is optional.")
        if recipe_id == "image_to_image":
            st.caption("This table is the baseline without LoRA. The same compatible checkpoint VAE supplies both encoding and decoding; use a separate Load VAE output for both when the model's template requires it. Source-image preprocessing supplies the dimensions.")
    if recipe_id == "video_export":
        _video_export_lesson()
    if recipe_id == "image_to_image":
        _image_to_image_lesson()
    st.markdown(f"[Official reference for this recipe]({recipe['source']})")
    render_recipe_nodes(recipe_id)


def _image_to_image_lesson():
    with st.expander("Optional LoRA · route both MODEL and CLIP through the adapter"):
        st.write("Select LoraLoader, displayed in current upstream as Load LoRA (Model and CLIP). Replace the baseline MODEL and CLIP connections with these five links; keep the source-image, VAE and conditioning-to-sampler connections.")
        st.table({
            "From": [edge[0] for edge in _IMG2IMG_LORA_CONNECTIONS],
            "Carries": [edge[1] for edge in _IMG2IMG_LORA_CONNECTIONS],
            "Into": [edge[2] for edge in _IMG2IMG_LORA_CONNECTIONS],
        })
        st.write("Use a LoRA compatible with this checkpoint family and follow that file version's trigger-word and strength guidance. strength_model controls the diffusion-model adjustments; strength_clip controls applicable text-encoder adjustments. A model-only adapter may have no CLIP adjustments and may use a different loader in its template.")
        st.caption("Keep the seed, source, crop, dimensions, prompts and denoise fixed for the comparison. Record both strengths. A larger strength is not a quality score, and a LoRA does not guarantee that the source subject will remain unchanged.")
        st.markdown(f"[LoraLoader and model-only variant]({_SOURCE}nodes.py#L640) · [Current display names]({_SOURCE}nodes.py#L1949)")
    st.caption("Upscale Image is a resizer, including for downsizing large inputs. Inspect the prepared source before encoding: center cropping may remove part of the subject, while disabled cropping can stretch a changed aspect ratio.")
    st.markdown(f"[Resize and crop implementation]({_RESIZE_SOURCE}) · [Image-to-image reference]({_IMG2IMG_DOCS})")
    st.caption("Continue in Workflow lab → Image to image for the guided practice. Keep the original source, baseline output and LoRA comparison as separate evidence; this atlas does not run them.")


def _video_export_lesson():
    st.markdown("**Optional exporter · Video Combine from Video Helper Suite**")
    st.code("Decoded IMAGE frames → VHS Video Combine.images\nAvailable AUDIO      → VHS Video Combine.audio\nWorkflow fps         → frame_rate setting", language="text")
    st.write("Use this route when your environment provides the VHS pack and you want its export options. Its Filenames output is VHS_FILENAMES, so it cannot feed Save Video.video. VHS already writes the output file.")
    st.caption("Check save_output in your saved workflow: current source defaults to True for the server's output directory; False writes temporary files. A preview is not proof that you downloaded a durable copy. For speech, choose a supported audio-capable video format such as video/h264-mp4, not GIF or WebP.")
    st.info("Keep the workflow's frame rate. The same 96 frames play for 4 seconds at 24 fps or 2 seconds at 48 fps. Changing export FPS alone does not interpolate extra frames or retime the audio; check the saved file's synchronization.")
    with st.expander("Expose subgraph outputs without confusing the types"):
        st.write("Open a learning copy of the subgraph and find its actual decoded IMAGE and AUDIO outputs. Expose those through the subgraph's output slots, then connect them to the exporter. Renaming a VIDEO output does not turn it into IMAGE.")
        st.write("If the subgraph already returns VIDEO, put Get Video Components after it to obtain frames, available audio and fps. This provides the bridge without changing the subgraph's internal wiring.")
        st.markdown(f"[Official subgraph output slots]({_SUBGRAPH_DOCS}) · [Native video components]({_VIDEO_SOURCE}#L292)")
    st.markdown(f"[VHS export reference]({_VHS_REPO}#video-combine) · [Accepted IMAGE/LATENT types]({_VHS_TYPES}) · [H.264/MP4 audio preset]({_VHS_REPO}/blob/main/video_formats/h264-mp4.json)")
    st.caption("Continue in Workflow lab → Video & audio for the guided lesson and export checks. These maps describe connections; they do not inspect installed packs or run a workflow.")


def _controlnet_lesson():
    st.markdown("**ControlNet weights, nodes and a preprocessor do different jobs.**")
    st.table({
        "Part": ["Model weights", "Load / Apply nodes", "Control-image preprocessor"],
        "Job": [
            "The learned control model. Match its base family and supported control type to this generation stage.",
            "Load ControlNet opens those weights; Apply ControlNet combines them with a control image and prompt conditioning.",
            "Turns a reference into the required map, such as edges, depth or pose. It does not replace the ControlNet weights.",
        ],
    })
    st.info("For an SDXL image stage, select an SDXL-compatible ControlNet; an SD1.5 ControlNet is not interchangeable. A depth map also needs a model that supports depth control. Check each stage's own recipe in a larger workflow; different stages can use different model families.")
    st.caption("The model family is the architecture, not the author's brand. Preprocessors have their own requirements; some need extra nodes or weights. This map starts from an already prepared control image and claims no installation or generation.")
    st.markdown(f"[Official family compatibility guidance]({_MODEL_DOCS}) · [Control maps and preprocessing]({_CONTROLNET_DOCS})")


def render_recipe_nodes(recipe_id, key_prefix="help_atlas"):
    """Inspect a recipe's nodes in place, with a namespace for each caller."""
    recipe = RECIPES[recipe_id]
    selected = _selection(
        "Open a node in this recipe", list(recipe["nodes"]),
        key_prefix + "_recipe_node_" + recipe_id, format_func=_node_label,
    )
    _node_detail(selected, expanded=True)


def _find():
    left, right = st.columns([2, 1])
    with left:
        query = st.text_input(
            "Find by name, job or data type", key="help_atlas_search", max_chars=200,
            placeholder="Try prompt, latent, audio, ControlNet, or KSampler",
        )
    with right:
        category = st.selectbox(
            "Node family", ["All categories", *dict.fromkeys(n["category"] for n in NODES.values())],
            key="help_atlas_category",
        )
    results = find_nodes(query, category)
    st.caption(f"{len(results)} of {len(NODES)} curated node types match. These families group nodes by their job in this guide.")
    if not results:
        st.info("No starter entry matches. Try one word or another family, or search the Node Library in your ComfyUI installation.")
        return
    for family in dict.fromkeys(NODES[node_id]["category"] for node_id in results):
        st.markdown("**" + family + "**")
        for node_id in results:
            if NODES[node_id]["category"] == family:
                _node_detail(node_id)


def _connections():
    st.subheader("Follow what each connection carries")
    st.write("A connection sends one node's output to another node's input. Start with a recipe, then inspect the data type at the point you want to change.")
    st.table({
        "Type": ["MODEL / CLIP / VAE", "CONTROL_NET", "CONDITIONING", "LATENT", "IMAGE", "MASK", "AUDIO", "VIDEO", "FLOAT / COMBO", "VHS_FILENAMES"],
        "What to look for": [
            "Different model components; choose the component needed by the receiving socket.",
            "A loaded ControlNet model. Its family and trained control type must match the stage using it.",
            "Encoded guidance, such as the positive or negative prompt.",
            "A model-space representation that may need decoding before it is viewable.",
            "Image pixels or a batch of frames; a batch alone does not define a timed video.",
            "Mask values. Load Image's mask output is separate from its IMAGE control map.",
            "Audio samples and a sample rate; check how they align with the shot.",
            "A video object with timing and its available media components.",
            "Values such as fps, bit depth and color space. Record them alongside frames and apply them to the exporter's corresponding settings.",
            "Video Helper Suite's output-location flag and generated file paths. These references are not a VIDEO object.",
        ],
    })
    st.markdown(f"[Official data type reference]({_TYPE_DOCS})")
    with st.expander("Shared Primitive controls · coordinate multiple KSamplers"):
        from Help.shared_controls import render as render_shared_controls
        render_shared_controls("help_atlas_shared")
    with st.expander("Episode 2 · latent, pixels and the required VAE"):
        st.write("KSampler combines different kinds of input: MODEL, CONDITIONING and LATENT. The classic Empty Latent Image node creates zeros; the sampler prepares its seeded noise separately.")
        st.code("IMAGE + VAE → VAE Encode → LATENT\nLATENT + VAE → VAE Decode → IMAGE → Preview Image / Save Image", language="text")
        st.write("Connect both inputs on VAE Encode or VAE Decode. Use the VAE specified for that model and latent format, from the checkpoint or a separate Load VAE node. A missing vae connection remains a missing input even when the other wires fit.")
        st.caption("In classic Stable Diffusion, the VAE learns a compressed representation. Encoding then decoding is lossy reconstruction; an exact copy of every original pixel is not promised. One IMAGE output can feed preview, save and further processing branches.")
        st.markdown(f"[Built-in node definitions]({_SOURCE}nodes.py) · [Latent diffusion: perceptual image compression]({_LATENT_PAPER})")
    st.subheader("Connection example")
    left, right = st.columns(2)
    source_options = [node_id for node_id, node in NODES.items() if node["outputs"]]
    target_options = [node_id for node_id, node in NODES.items() if node["inputs"]]
    with left:
        source_id = _selection(
            "Source node", source_options, "help_atlas_source_node",
            index=source_options.index("LoadVideo"), format_func=_node_label,
        )
        source = NODES[source_id]
        output_name = _selection(
            "Source output", list(source["outputs"]), "help_atlas_source_output",
            format_func=lambda value: f"{value} · {source['outputs'][value]}",
        )
    with right:
        target_id = _selection(
            "Target node", target_options, "help_atlas_target_node",
            index=target_options.index("SyncLipSyncNode"), format_func=_node_label,
        )
        target = NODES[target_id]
        input_name = _selection(
            "Target input", list(target["inputs"]), "help_atlas_target_input",
            format_func=lambda value: f"{value} · {target['inputs'][value]}",
        )
    source_type = source["outputs"][output_name]
    target_type = target["inputs"][input_name]
    st.code(f"{source_id}.{output_name} [{source_type}]\n    → {target_id}.{input_name} [{target_type}]", language="text")
    if source_id == target_id:
        st.warning("These selectors describe node types. A node instance cannot feed itself in a normal acyclic workflow; separate instances would still need a valid recipe.")
    if connection_types_match(source_id, output_name, target_id, input_name):
        st.info(f"Declared types match: {source_type}. This is a preliminary structural check only; it does not validate or run a workflow.")
    elif target_id == "VHS_VideoCombine" and input_name == "images" and source_type == "LATENT":
        st.info("Outside this atlas's decoded IMAGE route: current VHS also accepts LATENT with a compatible VAE through custom type handling. This simplified equality check does not validate that advanced path. Follow the pack's model-specific requirements.")
        st.markdown(f"[VHS accepted types]({_VHS_TYPES}) · [VAE handling in Video Combine]({_VHS_SOURCE}#L285)")
    else:
        st.warning(f"Declared types differ: {source_type} → {target_type}. This pair has no direct type match in the starter reference.")
    if target_id == "VHS_VideoCombine" and input_name == "images" and source_type == "VIDEO":
        st.caption("Use Get Video Components to extract IMAGE frames and available AUDIO first, or expose the subgraph's actual decoded components. Keep its fps with the frames.")
    st.write("Even matching types can fail: model architecture, latent shape, dimensions, frame rate, audio duration and node versions must agree. Check the receiving node's requirements and test a small example.")
    st.caption("For example, CONTROL_NET sockets can connect while an SD1.5 ControlNet is incompatible with the SDXL checkpoint in that generation stage. IMAGE sockets also cannot tell a depth map from a canny map; match the trained control type.")
    st.markdown(f"[Official model compatibility troubleshooting]({_MODEL_DOCS})")
    with st.expander("Read the caveats for this pair"):
        for node_id in dict.fromkeys((source_id, target_id)):
            st.markdown("**" + NODES[node_id]["name"] + "**")
            st.write(NODES[node_id]["caveat"])
            st.markdown(f"[Official {NODES[node_id]['name']} source]({NODES[node_id]['source']})")
    with st.expander("Build combinations without memorizing the catalog"):
        st.markdown("1. Pick the result and start from a working template for the exact model or service.")
        st.markdown("2. Trace one branch: what supplies this input, what does this node change, and who consumes its output?")
        st.markdown("3. Change one compatible stage, run a short test, and keep the baseline for comparison.")
        st.markdown("4. Save the graph, model names, node versions and result together. Add a new recipe when that combination proves useful.")
        st.caption("The explorer compares the main declared data sockets only. It does not model widget conversions, wildcard or union types, custom validation, cycles, or your installed node catalog.")
    with st.expander("Layout tools · reroutes, groups and subgraphs"):
        st.table({
            "Tool": ["Reroute", "Group frame", "Subgraph"],
            "What it does": [
                "Organizes a wire's path on the canvas. It carries the connected type and does not convert or modify its value; it is a frontend tool, not another model node.",
                "Labels and organizes related nodes in a visual frame. Moving, resizing or recoloring the frame does not change their operations.",
                "Packages connected nodes behind selected inputs and outputs as a reusable component. Open it to inspect the internal operations and dependencies.",
            ],
        })
        st.caption("Keep the same endpoints when tidying wires. Reconnecting a wire or editing a subgraph's internal nodes changes the workflow; layout alone does not make it faster or model-compatible. Available controls vary by frontend version.")
        st.markdown(f"[Reroute and client-side types]({_TYPE_DOCS}#primitive-and-reroute) · [Canvas and group settings]({_CANVAS_DOCS}) · [Subgraphs]({_SUBGRAPH_DOCS})")


def render():
    """Render the task → recipe → node reference without changing journal data."""
    st.subheader("Node atlas")
    st.write("Choose a task, follow its recipe, then open the node you want to understand. Search is the next layer when you need a particular operation.")
    st.info(f"Curated starter: {len(NODES)} node types across {len(RECIPES)} teaching recipes. This is not a count or list of all installed nodes.")
    st.caption("Your available catalog depends on the ComfyUI version, enabled extensions and environment. This atlas does not inspect your installation. The maps explain combinations; they are not runnable workflow files.")
    st.markdown(f"[Find available built-in and installed custom nodes in ComfyUI's Node Library]({_LIBRARY_DOCS})")
    with st.expander("Optional packs · Civitai"):
        st.markdown("[Civitai Comfy Nodes](https://github.com/civitai/civitai-comfy-nodes) supports hosted recipes and local model selection. Choose a recipe before exploring the pack. For its two roles and connection types, open **ComfyUI guide → 02 / Setup routes → Models & files → Find a model → Optional integration · Civitai Comfy Nodes**.")
    tabs = st.tabs(["Recipes", "Find a node", "How connections work"])
    for tab, renderer in zip(tabs, (_recipes, _find, _connections)):
        with tab:
            renderer()
    st.caption("Reference checked against ComfyUI and pack-maintainer sources on September 12, 2026. Source links follow upstream branches; names, sockets and options may differ in your installed release.")
