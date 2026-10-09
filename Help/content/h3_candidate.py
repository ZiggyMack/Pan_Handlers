"""A sourced H3 research candidate, separate from verified Cloud execution.

Static teaching data only. CFA's October 3 discovery is a dated catalog record;
this module neither reads that checkout nor queries accounts at runtime.
"""

_OVERVIEW = "https://docs.comfy.org/tutorials/video/minimax/minimax-h3"
_NATIVE = "https://docs.comfy.org/tutorials/video/minimax/minimax-h3-native"
_ROLES = "https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md"

H3_CANDIDATE = {
    "title": "MiniMax H3 · native Reference to Video candidate",
    "reviewed": "October 4, 2026",
    "status": "Official recipe reviewed; CFA catalog presence recorded October 3. Dependencies and execution remain untested. No accepted H3 shot.",
    "docs": _NATIVE,
    "sources": (
        ("Official H3 overview and core requirements", _OVERVIEW),
        ("Native R2V dependencies and workflow", _NATIVE),
        ("MiniMax reference roles and audio semantics", _ROLES),
        ("Managed Cloud node policy", "https://support.comfy.org/articles/6791455062-custom-nodes-on-cloud"),
    ),
    "roles": (
        {
            "Input": "Appearance image",
            "Job": "Describe the intended character, costume or setting from the corresponding <Picture N>. Keep a reviewed clean reference.",
            "Review": "Identity, wardrobe and texture across the whole shot; an image reference is not a pixel lock.",
        },
        {
            "Input": "Performance / source video",
            "Job": "Name <Video N> as the editing source, or as a motion/camera reference. Specify which relationship you mean.",
            "Review": "Matched timecodes, movement, expressions, contact and framing; a reference-guided generation need not reproduce every source frame.",
        },
        {
            "Input": "Prepared audio",
            "Job": "State whether <Audio N> supplies the same soundtrack to reuse or only voice, rhythm or style guidance. Video-file audio is not automatically an enabled audio reference.",
            "Review": "Compare the actual soundtrack, words, timing and mouth motion. A reuse instruction alone is not proof that the signal or lip sync was preserved.",
        },
        {
            "Input": "Prompt / shot brief",
            "Job": "Assign each connected reference its role, then state the desired change and preservation criteria in the existing reference and brief fields.",
            "Review": "The compiled reference order and effective text must match the intended experiment.",
        },
    ),
    "dependencies": (
        "Native template: video_minimax_h3_r2v; core ComfyUI 0.30.0 or later. Managed Cloud updates follow stable releases; verify the live workspace's actual nodes.",
        "Diffusion: minimax_h3_ref2va_pruned_int8_convrot.safetensors. Native T2V/I2V use fl2va weights instead; the model roles are not interchangeable.",
        "Text encoder: qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors.",
        "Video VAE: minimax_h3_video_vae_int8_convrot.safetensors; audio VAE: minimax_h3_audio_vae_fp32.safetensors.",
        "Template scan also lists minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors for the optional Lightning LoRA. Confirm it resolves even when turbo is off.",
        "Current native R2V documentation lists up to 9 image, 3 video and 3 audio references. Check the loaded node schema and combined limits before preparing a large set.",
    ),
    "steps": (
        "Choose native R2V explicitly in Cloud's Template Library. API / H3 Max templates are separate recipes; a familiar title does not identify the same runtime or model.",
        "Record the exact editor JSON/revision, live node schemas and remote model selections. CFA currently has the H3 catalog discovery only, not a saved validated H3 execution graph.",
        "Resolve dependencies on the Cloud host. Keep only needed input media and review/export files on D:; local GPU purchases, pip installs and local weight folders do not provision managed Cloud.",
        "Prepare one short shot with a reviewed appearance image and the chosen source-performance excerpt. Add audio only after deciding whether to reuse its signal or reference its sound. Inspect uploads, trims and ordered reference labels.",
        "Inspect converted inputs, exact dimensions, frame count/duration, conditioning, model variant and output settings; obtain the current account estimate and validate. Start with the loaded official baseline, not SDXL/Klein sampler defaults.",
        "Perform the chosen bounded preview only after those checks. Keep the original input and actual output; review identity, motion/contact, soundtrack and synchronization before accepting a take or beginning HD/4K finishing.",
    ),
    "caveat": (
        "This optional candidate does not replace the current recommended route. The reviewed native recipe generates around a 768-pixel short edge at 24 fps; hosted/API 2K output is a different offering. "
        "The official baseline uses 20 steps with reference turbo off; its four-step turbo can weaken reference adherence. These are recipe defaults, not a measured optimum for our shot. "
        "The supplied tutorial's 12-total-input claim differs from the current per-type limits, so the live schema must settle the usable combination. "
        "CFA has not verified the workspace dependencies, audio reuse, performance fidelity, lip sync, cost or a rendered result. A catalog listing and creator demonstration establish none of those outcomes."
    ),
}
