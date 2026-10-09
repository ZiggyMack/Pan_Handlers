"""Curated video candidates, checked against primary sources on 2026-10-02.

These are instructional handoffs, not account inventory or executed renders.
The remote JSON links are mutable: retain the downloaded revision with a run.
"""

RESEARCH_DATE = "2026-10-02"
_LTX = "https://raw.githubusercontent.com/Lightricks/ComfyUI-LTXVideo/master/example_workflows/2.5/"
_TEMPLATES = "https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/"
_SHELF = "https://github.com/Lightricks/ComfyUI-LTXVideo/blob/master/example_workflows/2.5/README.md"
_COMPAT = "https://docs.ltx.io/open-source-model/reference/workflow-asset-compatibility"
_CLOUD = "https://support.comfy.org/articles/6791455062-custom-nodes-on-cloud"

ROUTES = {
    "ltx_union": {
        "title": "LTX-2.5 Union Control · start with depth",
        "why": "A source video's depth supplies the changing scene structure while your prompt describes the new appearance. This is our first candidate for the woman-and-wolf shot: depth can represent both subjects and their surroundings, where a human pose skeleton would omit much of the scene.",
        "inputs": [
            "One continuous source MP4, trimmed to a clear gesture; record time range, frame count, FPS and dimensions.",
            "A visual change brief and explicit preservation criteria. Begin with a lighting/look change before changing the location or cast.",
            "Optional first-frame look reference. Without one, turn off 'use image input' in Input Parameters.",
        ],
        "dependencies": [
            "Current compatible ComfyUI plus ComfyUI-LTXVideo; the supplied graph includes Video Depth Anything and comfyui_controlnet_aux annotators. Check the actual Cloud workspace before importing models.",
            "diffusion_models/ltx-2.5-22b-distilled-transformer-bf16.safetensors",
            "text_encoders/gemma4-12b-with-proj-ltx-2.5-bf16.safetensors; the supplied enhancer branch also names gemma4_e2b_it_bf16.safetensors.",
            "vae/ltx-2.5-video-vae-bf16.safetensors and vae/ltx-2.5-audio-vae-bf16.safetensors. The graph documents a convolutional video-VAE alternative; use its explicit compatibility instructions.",
            "latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors",
            "loras/ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors: this specific 2.3 adapter is explicitly reused by the official 2.5 recipe; that does not make all 2.3 components interchangeable.",
            "Depth branch: yuvraj108c/ComfyUI-Video-Depth-Anything, including video_depth_anything_vits.pth. Other annotators have their own model files. Keep all weights remote; accept any required Hugging Face model access in the provider account.",
        ],
        "steps": [
            "Download the official editor JSON to D:, open or drag it into Comfy Cloud, and save a named working copy. Inspect every active subgraph for missing nodes and model selections; opening a graph is not a successful run.",
            "Load the prepared source in LoadVideo. Open Reference Video and inspect the depth sequence before sampling. It resizes the reference; record resolved generation dimensions rather than assuming source resolution is retained.",
            "Verify source FPS reaches conditioning and video assembly, and frame count satisfies the selected recipe's 8n+1 constraint. Trim or resample deliberately when needed; changing only export FPS changes playback speed.",
            "Set a fixed seed, one visual change and a modest preview size. Keep the graph's intrinsic refinement; defer optional finishing. Inspect the effective prompt and current node settings before the bounded run.",
            "Compare source and output at matching timecodes and normal speed: gesture, contact, identity, camera path, texture stability and intended visual change. Save the graph, settings, output and actual run/cost record.",
            "The inspected Union graph generates audio; its source-audio output is unconnected. Keep the original track separately and audition/remux it after visual acceptance if it still fits.",
        ],
        "caveat": "Structural guidance is not a pixel or identity lock. Depth can also preserve background geometry you wanted to change. The current JSON has two sampling stages; upstream summaries disagree on stage/refinement counts, so inspect the downloaded graph's active schedules. Cloud package availability and a successful render remain unverified.",
        "docs": "https://docs.ltx.io/open-source-model/feature-guides/structural-control/union-control",
        "workflow": _LTX + "LTX-2.5_ICLoRA_Union_Control_Distilled.json",
        "workflow_name": "LTX-2.5_ICLoRA_Union_Control_Distilled.json",
        "kind": "Official editor workflow · untested here",
        "alternatives": [
            "Localized change: evaluate LTX-2.5_ICLoRA_Inpaint_Two_Stage_Distilled.json with an aligned mask sequence.",
            "Task-specific RGB edit: LTX-2.5_V2V_ICLoRA_Single_Stage_Distilled.json needs an adapter trained for the desired edit; its shipped Instant Shave example is not a general relighting adapter.",
            "For a replacement character, choose Wan2.2 Animate Mix when the source background matters; choose Wan Animate 2 when generating a new setting is acceptable.",
        ],
    },
    "wan_mix": {
        "title": "Wan2.2 Animate · Mix character replacement",
        "why": "Mix combines a replacement-character image with the source performance and background. It fits replacing a performer while trying to keep the existing environment; review the subject boundary and contact carefully.",
        "inputs": ["Source performance video.", "Clear replacement-character image.", "Pose/face controls and character mask prepared by the template; inspect them throughout the shot."],
        "dependencies": [
            "Current ComfyUI, ComfyUI-KJNodes and comfyui_controlnet_aux; verify their current Cloud availability.",
            "Wan2.2 Animate 14B model: the documented FP8 candidate is Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors; follow the selected graph for FP8 versus BF16.",
            "umt5_xxl_fp8_e4m3fn_scaled.safetensors, clip_vision_h.safetensors, wan_2.1_vae.safetensors and lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors; keep each in its declared remote model category.",
            "Resolve the template's preprocessing dependencies/model files too; a loaded diffusion model alone is insufficient.",
        ],
        "steps": [
            "Open the official JSON or search 'Wan2.2 Animate' in Comfy Templates, then save a copy. Resolve models and nodes before a paid run.",
            "Load source and reference image; inspect DWPose and the Points Editor/mask. Keep background_video and character_mask connected for Mix.",
            "Choose dimensions divisible by16 and a short preview. Check source-to-output timing and the template's extension segments before using the entire eight seconds.",
            "Compare expression, pose, contact, masking and lighting frame by frame; retain only a take that also holds up in motion.",
        ],
        "caveat": "A human performance-transfer workflow is not evidence that animal identity or woman/wolf contact will survive. Test the human replacement separately. Do not confuse Mix with Move, which disconnects background and mask. Source/output FPS and extension length need explicit checking.",
        "docs": "https://docs.comfy.org/tutorials/video/wan/wan2-2-animate",
        "workflow": _TEMPLATES + "video_wan2_2_14B_animate.json",
        "workflow_name": "video_wan2_2_14B_animate.json",
        "kind": "Official editor workflow · untested here",
        "alternatives": ["Wan Animate 2 for a new background and independently directed camera.", "LTX masked editing when only a bounded region should change."],
    },
    "wan_animate": {
        "title": "Wan Animate 2 · character and driving performance",
        "why": "This newer, distinct model reads driving-video frames directly and animates the reference character. It fits a new character and setting when exact background/camera preservation is not required.",
        "inputs": ["A still image of the target character.", "A driving video supplying performance.", "Prompt describing scene, background and intended camera behavior."],
        "dependencies": [
            "Current ComfyUI with Wan Animate 2 support; Cloud may lag newly released core nodes. Confirm the real workspace's template and node inventory.",
            "wan_animate_2_int8_convrot.safetensors, umt5_xxl_fp8_e4m3fn_scaled.safetensors, clip_vision_h.safetensors and Wan2_1_VAE_bf16.safetensors from the official Comfy-Org/Wan-Animate-2 package.",
            "The published template includes lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors. Follow the actual template rather than swapping in Wan2.2 Animate weights.",
        ],
        "steps": [
            "Open the official JSON or search 'Wan Animate 2' in Templates and save a working copy.",
            "Load the character image and driving video directly; this route does not require the older skeleton-extraction stage.",
            "Set the scene/camera prompt; verify input trim, frame rate and resolved output duration in the graph. Begin with one short motion segment.",
            "Compare likeness, facial performance and gesture timing; treat changes in background and viewpoint as intentional only when they match your brief.",
        ],
        "caveat": "Wan Animate 2 generates a fresh background and allows camera changes. It is not our default for preserving the original whole scene. No CFA performance-transfer render or Cloud compatibility check is recorded.",
        "docs": "https://docs.comfy.org/tutorials/video/wan/wan-animate-2",
        "workflow": _TEMPLATES + "video_wan_animate2.json",
        "workflow_name": "video_wan_animate2.json",
        "kind": "Official editor workflow · untested here",
        "alternatives": ["Wan2.2 Animate Mix when retaining the source environment matters.", "LTX Union depth when whole-scene structure matters more than a replacement-character reference."],
    },
    "image_to_video": {
        "title": "LTX-2.5 image-to-video · create motion from a still",
        "why": "A still supplies appearance and composition, but contains no complete performance to preserve. Use image-to-video to make a new shot, or add a driving clip and choose a performance-transfer route.",
        "inputs": ["Prepared starting image.", "Prompt for the action, setting and camera."],
        "dependencies": ["Use the exact current native LTX-2.5 image-to-video template manifest; its model set and loader layout can differ from the advanced Union graph.", "Cloud template/node availability and gated Lightricks model access must be checked before execution."],
        "steps": ["Open the official LTX-2.5 page, select its image-to-video template and save a copy.", "Load the first image, define one simple action and render a short preview with the template's supported dimensions/frame count.", "Judge temporal consistency before attempting a longer clip or higher resolution."],
        "caveat": "This generates new motion. It cannot demonstrate preservation of an existing video's performance, and recovered image-to-video examples may depend on a missing starting image.",
        "docs": "https://docs.comfy.org/tutorials/video/ltx/ltx-2-5",
        "workflow": "",
        "workflow_name": "Native LTX-2.5 image-to-video template (select on official page)",
        "kind": "Official template handoff · untested here",
        "alternatives": ["Supply a driving video for Wan Animate 2.", "Use an existing scene clip for LTX Union Control."],
    },
    "render_first": {
        "title": "Render the 3D scene into a source clip first",
        "why": "An editable scene can supply a controlled camera and performance. Rendering gives the video workflow the frames it consumes while retaining the original 3D project for later changes.",
        "inputs": ["Editable scene, or a mesh plus materials, rig/action, lights and camera.", "A short rendered clip or frame sequence with declared timing."],
        "dependencies": ["A compatible remote 3D render environment and the scene's referenced assets.", "After rendering, use the selected video route's separate Comfy dependencies."],
        "steps": ["Keep the editable source and collect referenced assets.", "Render a modest preview with the intended camera and action.", "Re-enter this planner with the rendered video and select which look/setting changes to make."],
        "caveat": "A mesh alone has no timed performance. AI video output is pixels, not an edited rig or playable game. Game development remains a future branch.",
        "docs": "https://docs.blender.org/manual/en/5.1/render/introduction.html",
        "workflow": "",
        "workflow_name": "3D render → video-source handoff",
        "kind": "Instructional handoff",
        "alternatives": ["Start from an existing video to reach the current milestone faster."],
    },
    "brief_first": {
        "title": "Choose or record one source performance",
        "why": "Preserving motion needs a motion reference. The available guardian clip is a candidate; otherwise record or select one continuous shot before choosing an editing graph.",
        "inputs": ["A one-sentence visual change.", "A short source shot with a clear gesture and a list of elements that must remain recognizable."],
        "dependencies": ["A source asset and its usage permission; no model download is needed to write the brief."],
        "steps": ["Choose a continuous 4–8-second scene and review it at normal speed.", "Record trim, FPS, dimensions and preservation criteria.", "Return with video selected to prepare the transformation workflow."],
        "caveat": "A written brief is planning evidence, not a generated result.",
        "docs": _SHELF,
        "workflow": "",
        "workflow_name": "Source-and-brief preparation",
        "kind": "Instructional handoff",
        "alternatives": ["With only a still, use image-to-video and accept that motion will be generated."],
    },
    "dialogue": {
        "title": "Dialogue branch · source video plus replacement speech",
        "why": "Use the existing Rewrite a scene guide when the requested change is spoken words and mouth movement rather than appearance or setting.",
        "inputs": ["One source shot.", "Clean replacement speech WAV aligned to its timing, including silent beats."],
        "dependencies": ["The existing guide's sync.so partner-node candidate requires a compatible Comfy workspace and credits; reconfirm current availability."],
        "steps": ["Open Rewrite a scene and prepare the soundtrack-only baseline.", "Select a lip-sync candidate only when changing mouth motion is required.", "Compare timing, face stability and final sound mix."],
        "caveat": "This is the preserved dialogue branch, not the selected visual-transformation experiment. Its earlier research does not establish current runtime availability.",
        "docs": "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_api_nodes/nodes_sync_so.py",
        "workflow": "",
        "workflow_name": "Existing Rewrite a scene guide",
        "kind": "Instructional handoff · earlier researched candidate",
        "alternatives": ["Keep the source pictures unchanged if a soundtrack-only replacement meets the brief."],
    },
}

FINISHING = {
    "title": "Accepted take → HD master → reviewed 4K derivative",
    "docs": _SHELF,
    "workflow": _LTX + "LTX-2.5_V2V_TiledFusion_Upscale.json",
    "name": "LTX-2.5_V2V_TiledFusion_Upscale.json",
    "dependencies": [
        "A visually accepted source take with recorded timing and retained original.",
        "Current ComfyUI-LTXVideo with LTXVTiledFusionSampler, the graph's exact LTX-2.5 transformer/text encoder/VAEs, and ltx-2.5-22b-ic-lora-refine-details-1.0.safetensors.",
        "Resolve the actual remote graph manifest, active enhancer branch, hardware capacity and estimated cost before finishing.",
    ],
    "caveat": "This generative finishing candidate can invent detail or worsen flicker. Its FullHD/4K presets use model-aligned canvases: inspect resolved dimensions and choose crop or letterbox for the delivery target. Preserve FPS/audio timing and compare full-size moving footage before accepting. No HD or 4K CFA video master exists yet.",
}

SOURCES = (
    ("LTX Union Control guide", ROUTES["ltx_union"]["docs"]),
    ("LTX workflow and asset compatibility", _COMPAT),
    ("LTX-2.5 workflow shelf", _SHELF),
    ("Wan2.2 Animate Mix and Move", ROUTES["wan_mix"]["docs"]),
    ("Wan Animate 2", ROUTES["wan_animate"]["docs"]),
    ("Managed Cloud custom-node availability", _CLOUD),
)
