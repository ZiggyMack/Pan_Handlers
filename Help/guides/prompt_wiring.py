"""A small interactive wiring lesson, shared without changing journal progress."""

import re

import streamlit as st

from Help.content.catalog import TUTORIAL_URL


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


_COMPOSITION_PATTERNS = {
    "Share words across models": (
        "Raw prompt [STRING]\n  -> Model A encoder.text -> A conditioning -> A sampler\n"
        "  -> Model B encoder.text -> B conditioning -> B sampler",
        "Fan out the same words, then encode separately for each model. Matching text and a numeric seed does not make different architectures use identical noise or produce a controlled quality ranking.",
    ),
    "Join text before encoding": (
        "Core instruction [STRING] + optional style [STRING]\n"
        "  -> String concatenation [STRING] -> inspect effective text\n"
        "  -> this model's encoder -> CONDITIONING -> its sampler",
        "Join ordinary text before tokenization/encoding. Leave style off for the baseline; inspect the complete instruction before a run. A style text preset is not a trained LoRA.",
    ),
    "Join encoded conditioning": (
        "Compatible instruction encoder -> CONDITIONING -> conditioning_to\n"
        "Compatible style encoder       -> CONDITIONING -> conditioning_from\n"
        "ConditioningConcat -> CONDITIONING -> compatible sampling branch",
        "Episode 6 combines already encoded conditioning. This is not a text join or a weighted average. Both inputs must suit the same model/encoder recipe; matching socket types alone do not make SDXL and FLUX embeddings interchangeable.",
    ),
}
_COMPOSITION_SOURCES = (
    ("Ep05 shared prompts", "https://www.youtube.com/watch?v=q9ufjcMofI0"),
    ("Ep06 conditioning", "https://www.youtube.com/watch?v=cmikc-Jo1gk"),
    ("Ep07 text styles", "https://www.youtube.com/watch?v=Xsx-u0OMezw"),
    ("Core text encoding and conditioning", "https://github.com/Comfy-Org/ComfyUI/blob/master/nodes.py"),
    ("Current core string nodes", "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_string.py"),
)


def compose_text(instruction, style="", enabled=False, separator=", "):
    """Prepare ordinary text only; do not encode it or emulate a Comfy graph."""
    if not enabled or not style.strip():
        return instruction
    return separator.join((instruction, style))


def composition_markdown(instruction, style="", enabled=False, separator=", "):
    effective = compose_text(instruction, style, enabled, separator)
    fence = "`" * max(3, 1 + max((len(run) for run in re.findall(r"`+", instruction + style + effective)), default=0))
    lines = ["# Prompt composition practice", "", "Reviewed October 4, 2026. This prepares text, not conditioning or a generated output.", "",
             "## Entered instruction", "", fence + "text", instruction, fence, "",
             "## Optional style", "", "Enabled: " + str(enabled), "", fence + "text", style, fence, "",
             "Separator: " + repr(separator), "", "## Prepared effective text", "", fence + "text",
             effective, fence, ""]
    for name, (diagram, explanation) in _COMPOSITION_PATTERNS.items():
        lines.extend(["## " + name, "", "```text", diagram, "```", "", explanation, ""])
    lines.extend([
        "## Verify in the real recipe", "",
        "Record the model/variant, actual encoder and reachable sampling inputs. For SDXL, trace separate positive and negative conditioning. CFA's distilled Klein CFG-1 baseline keeps its negative field as inactive notes; do not assume the SDXL branch applies there.", "",
        "In Cloud, check supported node schemas. CFA's WAS style selector exposed only None; its embedded ImpactStringSelector library uses blank index 0 and multiline off. Copying a local CSV does not provision Cloud.", "",
        "Preview the actual assembled text and inspect the converted execution graph. A displayed widget may differ from a compiled value; CFA caught stale widgets_values_named overriding positional edits. This Pathfinder preview cannot inspect that graph.", "",
        "Keep the original instruction, optional style, effective prompt, resolved settings, output and review together. Input previews, generation and file saving are separate stages.", "",
        "References: " + " · ".join(f"[{label}]({url})" for label, url in _COMPOSITION_SOURCES), "",
        "CFA evidence: docs/notes/explorable_world/comfy/workflows/README.md (October 4 snapshot); archived transcripts and hashes are listed in Help/CFA_TUTORIAL_LEDGER.md.",
    ])
    return "\n".join(lines)


def _remember_composition(draft_key, field, widget_key):
    st.session_state[draft_key][field] = st.session_state[widget_key]


def render_composition(key_prefix):
    st.markdown("#### Prompt composition · words, encoders and optional styles")
    st.caption("Episodes 5–7 / CFA return · October 4, 2026. Source register and annotated timestamps are in Tutorial notes.")
    pattern = st.selectbox("Which connection are you designing?", list(_COMPOSITION_PATTERNS), key=key_prefix + "_pattern")
    diagram, explanation = _COMPOSITION_PATTERNS[pattern]
    st.code(diagram, language="text")
    st.write(explanation)
    st.table([
        {"Carries": "STRING", "Meaning": "Words before encoding", "Where it goes": "A text encoder's text input; expose its widget as a socket if needed."},
        {"Carries": "CLIP", "Meaning": "The compatible text-encoder object", "Where it goes": "The encoder node's clip input, not the text socket."},
        {"Carries": "CONDITIONING", "Meaning": "Encoded guidance", "Where it goes": "Compatible conditioning operations and sampler inputs, not a string join."},
    ])
    st.info("SDXL has active positive/negative branches in the CFA refinement recipe. The distilled Klein CFG-1 reference recipe has an inactive negative-notes field. Follow the actual graph and variant.")
    with st.expander("Compose and inspect the effective text", expanded=True):
        draft_key = key_prefix + "_draft"
        draft = st.session_state.setdefault(draft_key, {"instruction": "", "style": "", "enabled": False, "separator": ", "})
        for field, value in draft.items():
            st.session_state.setdefault(key_prefix + "_" + field, value)
        def widget(kind, label, field, **kwargs):
            widget_key = key_prefix + "_" + field
            return kind(label, key=widget_key, on_change=_remember_composition,
                        args=(draft_key, field, widget_key), **kwargs)
        instruction = widget(st.text_area, "Core instruction", "instruction", max_chars=6000)
        enabled = widget(st.toggle, "Include an optional style", "enabled")
        style = widget(st.text_area, "Style text", "style", max_chars=3000, disabled=not enabled)
        separator = widget(st.selectbox, "Text separator", "separator", options=[", ", "\n", " "],
                           format_func=lambda value: {", ": "Comma and space", "\n": "New line", " ": "Space"}[value])
        st.markdown("**Prepared text · before encoding**")
        st.code(compose_text(instruction, style, enabled, separator), language="text")
        st.caption("This text preview is calculated here. Check the effective text and compiled inputs in Comfy before rendering; it does not simulate embeddings or inspect your Cloud workflow. Style starts off and empty.")
        st.download_button("Download prompt composition notes", composition_markdown(instruction, style, enabled, separator),
                           "pathfinder-prompt-composition.md", "text/markdown", key=key_prefix + "_download")
    st.write("CFA's Cloud WAS selector offered only None. Its working alternative embeds the style library in ImpactStringSelector: index 0 blank, multiline off. Keep optional styles out of the baseline and verify the selected node is supported in your workspace.")
    st.caption("The draft survives page navigation in this session. Download it separately; it is not added to journey JSON and does not mark a checkpoint complete.")
    st.markdown(" · ".join(f"[{label}]({url})" for label, url in _COMPOSITION_SOURCES))


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
    with st.expander("Beyond two prompts · composition and styles"):
        render_composition(key_prefix + "_composition")
