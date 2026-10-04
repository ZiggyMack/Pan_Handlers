"""Model-specific generation settings and illustrative image-size comparisons."""

import streamlit as st

from Help.catalog import TUTORIAL_URL


_SIZES = {
    "SDXL · square starting point": (1024, 1024, "Official ComfyUI SDXL example"),
    "Juggernaut X v10 · portrait": (832, 1216, "Current publisher recommendation for X v10"),
    "Juggernaut X v10 · landscape": (1216, 832, "Current publisher recommendation for X v10"),
    "SD 1.5 · tutorial square": (512, 512, "Historical tutorial example"),
    "SD 1.5 · tutorial portrait": (512, 768, "Historical tutorial example"),
    "SD 1.5 · tutorial landscape": (768, 512, "Historical tutorial example"),
}
_MODEL_CARD = "https://huggingface.co/RunDiffusion/Juggernaut-X-v10"
_SDXL = "https://comfyanonymous.github.io/ComfyUI_examples/sdxl/"
_KSAMPLER = "https://docs.comfy.org/built-in-nodes/sampling/ksampler"


def render(key_prefix):
    st.markdown("#### Before Run: match the exact model version's settings")
    st.info(
        "Check image size, sampler, scheduler, steps, CFG and denoise whenever you change models. "
        "Use the publisher's generation recommendations as your baseline. An inference sampler "
        "is not necessarily a sampler the model was trained with."
    )
    st.caption("A recommendation is a starting configuration to reproduce and assess. Once it works, compare supported alternatives deliberately; do not carry a previous model's settings forward without checking them.")
    st.markdown("**Choose the canvas in Empty Latent Image**")
    chosen = st.selectbox("Sizing example — illustration only", list(_SIZES), key=key_prefix + "_size")
    width, height, provenance = _SIZES[chosen]
    left, middle, right = st.columns(3)
    left.metric("Width", f"{width} px")
    middle.metric("Height", f"{height} px")
    right.metric("Pixel count", f"{width * height:,}")
    st.caption(
        f"{provenance}. {width * height / (512 * 512):.2f}× the pixels of 512 × 512. "
        "This compares canvas area, not runtime or VRAM. It does not change a ComfyUI workflow."
    )
    st.markdown(
        "**Why the model family affects size:** SD 1.5 was developed around 512-pixel training, "
        "while SDXL adds higher-resolution, multiple-aspect-ratio training and architecture changes, "
        "including a second text encoder. Changing a canvas size does not change its model family "
        "or make another family's ControlNet compatible. "
        "[SDXL research paper](https://arxiv.org/html/2307.01952v1)"
    )
    st.write(
        "For SDXL, the official examples start near one megapixel; the exact model card can "
        "recommend particular aspect ratios. For the tutorial's SD 1.5 example, start near its "
        "recommended size. A much larger direct generation can change composition or introduce "
        "duplicates; 768 is not a universal hard limit, and 1024 is not universally invalid."
    )
    st.caption(
        "The sizing slide also lists 512 × 576, 640 or 704 and their landscape counterparts. "
        "Those are tutorial starting points, not guaranteed artifact-free outputs. Its multiples-of-64 "
        "suggestion is not a rule for every model. Follow the selected workflow's dimension constraints. "
        "For a larger final image, compare a documented upscale/refinement stage after a good baseline."
    )
    st.markdown(f"[Tutorial sizing discussion · 12:30]({TUTORIAL_URL}&t=750s) · [Official SDXL sizes]({_SDXL}) · [X v10 model card]({_MODEL_CARD})")
    st.markdown("**Translate the model card into KSampler fields**")
    st.table([
        {"Model-card instruction": "DPM++ 2M Karras", "ComfyUI setting": "sampler_name = dpmpp_2m; scheduler = karras", "Check": "These are two separate fields; use this mapping when the selected model recommends it."},
        {"Model-card instruction": "Sampling steps", "ComfyUI setting": "steps", "Check": "Use the range for the exact variant; more steps do not automatically improve a result."},
        {"Model-card instruction": "Guidance / CFG scale", "ComfyUI setting": "cfg in this classic recipe", "Check": "Use the model's range. Other architectures can put guidance in another node."},
        {"Model-card instruction": "Denoising strength", "ComfyUI setting": "denoise", "Check": "Classic text-to-image commonly uses 1.0; image-to-image and refinement need their own settings."},
        {"Model-card instruction": "Comparison seed", "ComfyUI setting": "seed + control_after_generate", "Check": "Fix both for a controlled comparison; record the software and model too."},
    ])
    st.caption(f"[KSampler field reference]({_KSAMPLER}) · [Tutorial mapping · 13:15]({TUTORIAL_URL}&t=795s)")
    with st.expander("Two examples with different evidence"):
        st.table([
            {"Example": "Tutorial Reborn / SD 1.5", "Size": "512 × 768", "Sampler / scheduler": "dpmpp_2m / karras", "Steps": "35", "CFG": "7", "Evidence": "User-supplied historical transcript, 13:03–13:53; not a new test"},
            {"Example": "Publisher Juggernaut X v10 / SDXL", "Size": "832 × 1216 or 1216 × 832", "Sampler / scheduler": "dpmpp_2m / karras", "Steps": "30–40", "CFG": "3–7", "Evidence": "Publisher model card checked September 12, 2026; not a tested result here"},
        ])
        st.markdown(f"[Current X v10 recommendation]({_MODEL_CARD}#recommended-settings)")
        st.write(
            "Check the actual file/version before applying either example. Hyper, Lightning, Turbo "
            "and other accelerated variants can need different settings. The completed CFA Z-Image "
            "example has its own recorded settings; these Juggernaut values do not replace them."
        )
    st.markdown(
        "**Keep the working configuration:** save the model filename/version, width × height, "
        "sampler, scheduler, steps, CFG, denoise, seed and seed-control behavior with the workflow "
        "and output. Reopen that model's saved workflow when switching back. Compare one change at a time."
    )
    st.caption("Practice the next step in Workflow anatomy → Controlled experiment: plan an A/B/C comparison for CFG, steps or seed, and learn how shared controls and output branches affect it.")
