"""A reusable lesson for coordinated parameter inputs across sampler branches."""

import streamlit as st


_PRIMITIVE = "https://github.com/Comfy-Org/ComfyUI_frontend/blob/main/src/extensions/core/widgetInputs.ts"
_TOPICS = {
    "cfg": {"label": "CFG", "type": "FLOAT", "example": "7.0", "meaning": "Keep guidance coordinated while other branch settings remain independently editable."},
    "steps": {"label": "Steps", "type": "INT", "example": "30", "meaning": "Set a common step count across compatible samplers, using the model's supported range."},
    "seed": {"label": "Seed", "type": "INT", "example": "42", "meaning": "Use the same starting seed across branches. Keep its update control fixed for a comparison and record actual submitted values."},
    "scheduler": {"label": "Scheduler", "type": "COMBO", "example": "karras", "meaning": "Choose a shared schedule when the connected samplers offer a compatible set of choices."},
}


def wiring(parameter, branches=2):
    topic = _TOPICS[parameter]
    lines = [f"Primitive / Shared {topic['label']} ({topic['type']}) = {topic['example']}"]
    lines.extend(f"  {'`' if index == branches - 1 else '|'}--> KSampler {chr(65 + index)}.{parameter}" for index in range(branches))
    return "\n".join(lines)


def reference_markdown():
    lines = ["# Shared controls for multiple KSamplers", "",
             "Recommended pattern when several branches should follow the same parameter value. This is a conceptual wiring reference, not an executable workflow.", "",
             "Use one Primitive per independently controlled parameter. A CFG Primitive feeds corresponding compatible CFG inputs; a different Primitive can control steps.", "",
             "## Set it up", "",
             "1. Save an expanded baseline. Identify sampler branches A and B and keep all required model, conditioning and latent inputs connected.",
             "2. Expose or connect the chosen parameter's input on each sampler. Older frontends call this Convert widget to input; newer frontends can show widgets and sockets together.",
             "3. Add a Primitive from a compatible parameter input and connect its output to the corresponding input on each other sampler. Check widget type, bounds and allowed choices.",
             "4. Hold the control fixed while verifying the connections. Changing the shared value should update the linked settings; unlinked controls retain their own values.",
             "5. Run a small test in ComfyUI, retain distinct output prefixes, and record the resolved settings. Export and reopen the graph to verify the shared connections survived.", ""]
    for key, topic in _TOPICS.items():
        lines.extend(["## " + topic["label"], "", "```text", wiring(key), "```", "", topic["meaning"], ""])
    lines.extend(["## Keep comparisons controlled", "",
                  "Share only what should move together. To compare CFG values across branches, keep their CFG controls separate while sharing settings intended to stay fixed. A shared seed alone does not guarantee identical images.",
                  "If several controls advance automatically, several experimental variables can change at once. Start fixed; vary one deliberately.",
                  "A Primitive adapts to compatible widget-backed inputs. It is not a universal source for MODEL, CLIP, LATENT or arbitrary socket types.", "",
                  f"[Primitive behavior and conversion changes]({_PRIMITIVE})", ""])
    return "\n".join(lines)


def render(key_prefix):
    st.subheader("Shared controls · one change, multiple samplers")
    st.success("Recommended pattern: when several KSamplers should follow the same setting, give that parameter one shared Primitive control.")
    st.write("Use one Primitive per independently controlled parameter. For example, a Shared CFG node can drive every linked CFG input, while Shared Steps drives their steps. Their other settings keep their own controls.")
    setting, count = st.columns([2, 1])
    with setting:
        parameter = st.selectbox("Trace a shared parameter", list(_TOPICS), format_func=lambda key: _TOPICS[key]["label"], key=key_prefix + "_parameter")
    with count:
        branches = st.selectbox("Linked samplers in the diagram", [2, 3, 4], key=key_prefix + "_branches")
    topic = _TOPICS[parameter]
    st.code(wiring(parameter, branches), language="text")
    st.write(topic["meaning"])
    st.caption("Illustrative values only. This explorer draws connections; it does not change a ComfyUI graph or validate your installed samplers' compatibility.")
    st.markdown("**Set it up in your working graph**")
    st.markdown(
        "1. Save a baseline and label the sampler branches A and B.\n"
        "2. Expose or connect the parameter input on each sampler. Older versions use **Convert widget to input**; newer interfaces may show widgets and sockets together.\n"
        "3. Create a **Primitive** from a compatible parameter input, then branch its output to the corresponding input on the other sampler. Check the type, permitted range and dropdown choices.\n"
        "4. Keep the shared value fixed for the first check. Verify every linked setting and the sampler inputs that still need separate connections.\n"
        "5. Test in ComfyUI, save distinct output files, and reopen the exported workflow to check that the connections survived."
    )
    st.info("Share what should move together. If you are comparing different CFG values, keep each branch's CFG independent and share the settings meant to stay fixed. Separate Primitives let you coordinate several parameters without forcing them to one value.")
    with st.expander("Avoid the common shared-control mistakes"):
        st.write("A Primitive adapts to a compatible widget-backed input; it cannot provide an arbitrary MODEL, CLIP or LATENT. Two inputs having a similar label is not sufficient: their widget configurations and allowed values must be compatible.")
        st.write("Keep automatic increment/randomize behavior deliberate. If both the seed and CFG advance, you have changed two variables. A fixed shared seed is useful evidence, but the model, prompts, sampler and environment still affect the result.")
        st.caption("Inspect the resolved value in the queued workflow or output metadata when available. A control displayed after generation may already show the next value.")
    st.markdown(f"[Current Primitive and parameter-input behavior]({_PRIMITIVE}) · [KSampler settings](https://docs.comfy.org/built-in-nodes/sampling/ksampler)")
    st.download_button("Download the shared-control pattern", reference_markdown(),
                       file_name="comfyui-shared-sampler-controls.md", mime="text/markdown", key=key_prefix + "_download")
