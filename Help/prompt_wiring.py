"""A small interactive wiring lesson, shared without changing journal progress."""

import streamlit as st

from Help.catalog import TUTORIAL_URL


_LESSONS = {
    "1 / Supply both encoders": (
        "Load Checkpoint.CLIP\n"
        "  ├─→ Positive encoder.clip\n"
        "  └─→ Negative encoder.clip",
        "Drag from the checkpoint's CLIP output to the clip input on each encoder. "
        "One output can feed both nodes. CLIP supplies the text encoder; the words go "
        "in each node's text box. MODEL and VAE serve other parts of the graph.",
    ),
    "2 / Route the two prompts": (
        "Positive encoder.CONDITIONING\n"
        "  └─→ KSampler.positive\n\n"
        "Negative encoder.CONDITIONING\n"
        "  └─→ KSampler.negative",
        "Connect each CONDITIONING output to its intended sampler input. "
        "These are two instances of the same CLIP Text Encode node type. "
        "Their destination gives them the positive or negative role; moving or "
        "renaming a node does not change its connection.",
    ),
    "3 / Complete the image path": (
        "Load Checkpoint.MODEL → KSampler.model\n"
        "Empty Latent Image.LATENT → KSampler.latent_image\n\n"
        "KSampler.LATENT → VAE Decode.samples\n"
        "Load Checkpoint.VAE → VAE Decode.vae\n"
        "VAE Decode.IMAGE → Save Image.images",
        "The four prompt connections are one branch of the full recipe. "
        "The sampler also needs a compatible model and starting latent. "
        "Decode the sampled latent into pixels, then save the image.",
    ),
}


def render(key_prefix):
    st.markdown("#### First connections: two prompts, one node type")
    st.caption(f"[Tutorial bookmark · Ep01, 11:36]({TUTORIAL_URL}&t=696s) · Captured from the learner's screenshot. This is a wiring lesson, not an executed workflow.")
    selected = st.radio("Trace the connections", list(_LESSONS), key=key_prefix + "_stage")
    diagram, explanation = _LESSONS[selected]
    st.code(diagram, language="text")
    st.write(explanation)
    st.caption("These diagrams show two separate encoder instances. Use the socket names and types to follow the wires; colors and canvas positions can vary.")
    with st.expander("Try the bottle prompt and check the wiring"):
        positive, negative = st.columns(2)
        with positive:
            st.markdown("**Positive · what to encourage**")
            st.code("a glass bottle containing a purple nebula,\non a stone, soft forest background", language="text")
        with negative:
            st.markdown("**Negative · what to discourage**")
            st.code("text, watermark", language="text")
        st.caption("Our practice wording follows the screenshot's bottle idea. Negative conditioning influences guidance; it does not guarantee that an unwanted feature disappears, and its effect depends on the model and settings.")
        st.markdown(
            "1. Trace both CLIP inputs back to the compatible checkpoint.\n"
            "2. Trace each CONDITIONING output to the intended positive or negative socket. "
            "Swapped wires can still have matching types; feeding both sampler inputs from "
            "one encoder repeats the same conditioning instead of using two prompts.\n"
            "3. Save a baseline. Fix the seed and its after-generation control, then change one "
            "positive prompt detail. Restore it before testing a negative-prompt change. Keep "
            "the images and settings to compare the actual effect."
        )
        st.caption("The screenshot uses Juggernaut Reborn (SD 1.5) at 512 × 512. Our SDXL starter uses its own compatible checkpoint and recommended settings. This connection pattern does not make the families interchangeable; other model recipes may handle prompts differently.")
    st.markdown(
        "[CLIP Text Encode inputs and output](https://docs.comfy.org/built-in-nodes/ClipTextEncode) · "
        "[Official image-workflow connections](https://docs.comfy.org/tutorials/basic/text-to-image) · "
        "[Guidance implementation](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/samplers.py)"
    )
