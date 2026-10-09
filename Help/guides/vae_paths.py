"""Explain VAE source and purpose independently; never load weights or run a graph."""

import streamlit as st

from Help.content.workflow_lessons import EPISODE_URL


SOURCES = {
    "checkpoint": "Use the checkpoint's VAE",
    "separate": "Use a separate Load VAE node",
}
PURPOSES = {
    "decode": "Turn sampled latents into an image",
    "edit": "Start from an existing image",
}
_NAMES = {
    "CheckpointLoaderSimple": "Load Checkpoint", "VAELoader": "Load VAE",
    "LoadImage": "Load Image", "VAEEncode": "VAE Encode",
    "KSampler": "KSampler", "VAEDecode": "VAE Decode",
    "SaveImage": "Save Image", "PreviewImage": "Preview Image",
}
_DECODE = "https://docs.comfy.org/built-in-nodes/VAEDecode"
_LOAD = "https://docs.comfy.org/built-in-nodes/VAELoader"
_ENCODE = "https://docs.comfy.org/built-in-nodes/VAEEncode"
_IMG2IMG = "https://docs.comfy.org/tutorials/basic/image-to-image"
_TILED = "https://docs.comfy.org/built-in-nodes/VAEDecodeTiled"
_VIDEO = "https://docs.comfy.org/tutorials/video/wan/wan2_2"
_CORE = "https://github.com/Comfy-Org/ComfyUI/blob/master/nodes.py"


def connections(source, purpose):
    """Return this branch's typed-node connections, not an executable workflow."""
    if source not in SOURCES or purpose not in PURPOSES:
        raise ValueError("Choose a listed VAE source and purpose.")
    loader = "CheckpointLoaderSimple" if source == "checkpoint" else "VAELoader"
    edges = []
    if purpose == "edit":
        edges.extend([
            ("LoadImage", "IMAGE", "VAEEncode", "pixels"),
            (loader, "VAE", "VAEEncode", "vae"),
            ("VAEEncode", "LATENT", "KSampler", "latent_image"),
        ])
    edges.extend([
        ("KSampler", "LATENT", "VAEDecode", "samples"),
        (loader, "VAE", "VAEDecode", "vae"),
        ("VAEDecode", "IMAGE", "SaveImage", "images"),
        ("VAEDecode", "IMAGE", "PreviewImage", "images"),
    ])
    return tuple(edges)


def _wire_text(source, purpose):
    return "\n".join(f"{_NAMES[a]}.{out} → {_NAMES[b]}.{into}" for a, out, b, into in connections(source, purpose))


def _diagram(source):
    label = "Load Checkpoint" if source == "checkpoint" else "Load VAE"
    # Static SVG uses the existing theme palette. Socket names also identify color-coded wires.
    st.markdown(f"""
<svg viewBox="0 0 760 210" width="100%" role="img" aria-label="KSampler LATENT enters samples; {label} VAE enters vae; VAE Decode produces IMAGE for Save Image or Preview Image." xmlns="http://www.w3.org/2000/svg">
<g fill="var(--help-surface-soft, #f4f6f5)" stroke="var(--help-line, #d7ddd4)" stroke-width="2">
<rect x="10" y="15" width="205" height="70" rx="10"/>
<rect x="10" y="120" width="205" height="70" rx="10"/>
<rect x="300" y="40" width="180" height="130" rx="10"/>
<rect x="575" y="60" width="175" height="90" rx="10"/>
</g>
<g fill="none" stroke-width="3">
<path d="M215 65 H255 V90 H300" stroke="#bf65b0"/>
<path d="M215 155 H270 V140 H300" stroke="#d8814c"/>
<path d="M480 105 H575" stroke="#518ce0"/>
</g>
<g fill="var(--help-ink, #243936)" font-family="system-ui, sans-serif" font-size="16">
<text x="26" y="43">KSampler</text><text x="26" y="69">LATENT output</text>
<text x="26" y="147">{label}</text><text x="26" y="175">VAE output</text>
<text x="317" y="68" font-weight="700">VAE Decode</text>
<text x="317" y="100">samples · LATENT</text><text x="317" y="148">vae · VAE</text>
<text x="493" y="95" font-size="13">IMAGE →</text>
<text x="590" y="92">Save Image</text><text x="590" y="123">Preview Image</text>
</g></svg>""", unsafe_allow_html=True)


def reference_markdown(source, purpose):
    lines = ["# VAE wiring reference", "", SOURCES[source] + " · " + PURPOSES[purpose], "",
             "Conceptual branch only. Rebuild it inside a compatible working graph; no render has been executed by Pathfinder.", "",
             "```text", _wire_text(source, purpose), "```", "",
             "The sampler still needs its model, conditioning and settings. Preview is optional; use Save Image for the retained result.", "",
             "## Before running", "",
             "- Confirm the exact VAE specified by the model/workflow; matching socket types alone cannot establish compatibility.",
             "- Connect both decoder inputs: sampled LATENT to samples, compatible VAE to vae.",
             "- If encoding an input image, supply the same compatible VAE to Encode and Decode in this classic route.",
             "- Local standalone VAE weights normally go in ComfyUI/models/vae/ or a configured VAE path. In Cloud, use its supported model catalog/import route.",
             "- Keep the actual VAE source and filename with the model receipt, graph and output.", "",
             "## One small experiment", "",
             "Keep a working baseline and test one change. Record the result or exact error in Workflow lab's Decode milestone.",
             "For an existing-image experiment, compare one denoise change with a fixed seed and other settings held steady; lower denoise generally preserves more of the input.", "",
             "## If decoding runs out of memory", "",
             "Confirm the error occurs during decoding. VAE Decode (Tiled) uses the same LATENT/VAE inputs and splits decoding into overlapping chunks. It can reduce peak decode memory while adding work; it does not fix sampler memory demand or a wrong VAE. Core decoding may already retry using tiles. Compare the resulting image when testing a change.", "",
             "## When the next step is video", "",
             "Follow the exact model variant's VAE and decoding recipe. Decoded IMAGE frames still need the workflow's video assembly/output stage and timing. An SDXL VAE is not a universal video decoder.", "",
             f"[VAE Decode]({_DECODE}) · [Load VAE]({_LOAD}) · [VAE Encode]({_ENCODE}) · [Image-to-image]({_IMG2IMG})",
             f"[Tiled decoder]({_TILED}) · [Core decoding](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/sd.py) · [Video example]({_VIDEO})", ""]
    return "\n".join(lines)


def render(key_prefix):
    st.subheader("VAE paths · from latent data to pixels")
    st.write("VAE means variational autoencoder. The node performs the conversion; the VAE input supplies the learned model it uses. VAE Encode takes pixels into latent space. VAE Decode reconstructs pixels from latents.")
    st.info("At this point in your tutorial screenshot, KSampler is connected to samples, but the decoder's vae socket is empty. Connect the checkpoint's usable VAE output there, or use the separate-loader route required by your model. Then connect IMAGE to an output node.")
    st.caption(f"[Episode 2 · VAE explanation around 16:14]({EPISODE_URL}&t=974s) · Classic image workflow. These are wiring guides; they do not run a model.")
    source_col, purpose_col = st.columns(2)
    with source_col:
        source = st.selectbox("Where does the VAE come from?", list(SOURCES), format_func=SOURCES.get, key=key_prefix + "_source")
    with purpose_col:
        purpose = st.selectbox("What are you starting with?", list(PURPOSES), format_func=PURPOSES.get, key=key_prefix + "_purpose")
    _diagram(source)
    st.caption("The sampled LATENT and the VAE model enter different required sockets. The decoded IMAGE can branch to both preview and save.")
    if source == "checkpoint":
        st.markdown("**Use the bundled component when the checkpoint supplies the VAE the recipe expects.** Connect Load Checkpoint.VAE to the decoder. Some checkpoints lack usable VAE weights even though the loader exposes that socket; follow the model's instructions.")
        st.markdown(f"[Checkpoint loader]({_CORE}#L555)")
    else:
        st.markdown("**Use the separate VAE specified by the workflow.** Add Load VAE, select its exact file in `vae_name`, and connect VAE to the decoder's `vae` input. A separate file is not automatically a quality upgrade.")
        local, cloud = st.columns(2)
        with local:
            st.markdown("**Local file path**")
            st.code("ComfyUI/models/vae/<required-vae-file>", language="text")
            st.caption("Use the active installation or configured VAE path. Refresh model choices after the file is available; select it in Load VAE.")
        with cloud:
            st.markdown("**Comfy Cloud path**")
            st.write("Use an available model or a supported import, then select it in the workflow's VAE loader. A file on your PC is not automatically available to Cloud.")
            st.markdown("[Cloud imports and destinations](https://docs.comfy.org/cloud/import-models)")
        st.markdown(f"[Load VAE and configured paths]({_LOAD})")
    if purpose == "edit":
        st.info("For the full Episode 4 practice, open 07 / Workflow lab → Image to image: resize before encoding, compare denoise, then add an optional LoRA.")
        st.markdown("**Encode → sample → decode.** Load Image supplies pixels to VAE Encode. Its LATENT becomes the sampler's `latent_image` instead of Empty Latent Image. In this classic route, branch the same compatible VAE to both Encode and Decode.")
        st.write("Keep the sampler's model and prompt-conditioning inputs connected. Use the workflow's documented denoise setting; compare one change with a fixed seed. Lower denoise generally preserves more of the reference, while high denoise can change it substantially.")
        st.caption("Encoding and decoding are learned, lossy transformations. A round trip does not promise an exact copy of every input pixel.")
        st.markdown(f"[VAE Encode]({_ENCODE}) · [Official image-to-image walkthrough]({_IMG2IMG})")
    st.markdown("**Connect this branch, socket by socket**")
    st.code(_wire_text(source, purpose), language="text")
    st.caption("This branch assumes the rest of the generation graph is connected. Preview Image is optional; Save Image retains the output. Export the editor workflow separately.")
    with st.expander("If it fails: identify which part failed"):
        st.table({
            "Observed problem": ["Missing vae input", "VAE file absent from the loader", "Wrong shape, channels or latent format", "Memory error during decode", "No retained image"],
            "Next check": [
                "Connect the required VAE socket; a LATENT wire supplies different data.",
                "Check the local VAE folder/configuration or Cloud availability, then refresh and select the exact file.",
                "Match the exact VAE to the generation model and variant. A wire fitting is not enough.",
                "Try the supported tiled decoder described below. A sampler-stage memory error needs a different fix.",
                "Connect the decoder's IMAGE to Save Image and inspect the actual result; a preview or open graph is not a saved file.",
            ],
        })
        st.markdown("[Model and component troubleshooting](https://docs.comfy.org/troubleshooting/model-issues)")
    with st.expander("Memory path · VAE Decode (Tiled)"):
        st.write("If memory fails during decoding, a compatible tiled decoder can process overlapping chunks with smaller peak decode demand. Keep the same LATENT and VAE connections. Tile size and overlap are decoding controls; they do not change the sampler or make incompatible VAE weights fit.")
        st.code("KSampler.LATENT → VAE Decode (Tiled).samples\nCompatible VAE → VAE Decode (Tiled).vae\nVAE Decode (Tiled).IMAGE → Save Image.images", language="text")
        st.caption("Ordinary core decoding already retries with tiles after some out-of-memory failures. Tiling can add work, and the full output still needs memory. Follow supported settings; compare boundaries and detail with the ordinary output when feasible. No universal tile-size or identical-output promise.")
        st.markdown(f"[Tiled node]({_TILED}) · [Decode fallback](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/sd.py) · [Output assembly](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/utils.py)")
    with st.expander("Video path · follow the exact model variant"):
        st.write("Use the video template's own VAE, latent preparation and decoder. An IMAGE batch of decoded frames still needs timing and video assembly. These pixels do not become an editable 3D scene just by decoding them.")
        st.table({"Official Wan2.2 example": ["5B", "14B"], "VAE specified by that example": ["wan2.2_vae.safetensors", "wan_2.1_vae.safetensors"]})
        st.caption("This example shows why even a shared model-family name is insufficient. Preserve the exact template's requirements; these filenames are not recommendations for every video workflow.")
        st.markdown(f"[Official Wan2.2 workflows and required files]({_VIDEO})")
    st.download_button("Download this VAE wiring path", reference_markdown(source, purpose),
                       file_name=f"comfyui-vae-{source}-{purpose}.md", mime="text/markdown", key=key_prefix + "_download")
    st.caption("Practice next: 07 / Workflow lab → Practice path → Diagnose the boundary between latent data and pixels. Record the VAE source/file, observed error or output, and your next change. The CFA worked example also includes a real graph with a separate VAE loader.")
    st.markdown(f"[VAE Decode inputs and output]({_DECODE})")
