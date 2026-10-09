"""Explore video/audio handoffs without loading media or executing a workflow."""

import math

import streamlit as st

from Help.content.h3_candidate import H3_CANDIDATE


_NATIVE = "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_video.py"
_VHS = "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite#video-combine"
_VHS_SOURCE = "https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite/blob/main/videohelpersuite/nodes.py"
_SUBGRAPH = "https://docs.comfy.org/interface/features/subgraph"
_LTX = "https://docs.comfy.org/tutorials/video/ltx/ltx-2-3"
_AUDIO_EVIDENCE = "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_audio_replace_v001.record.json"
_AUDIO_GUIDE = "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_audio_replace_v001.README.md"
_AUDIO_STAGES = (
    {"Stage": "Replace the soundtrack locally", "CFA evidence": "Completed ten-second FFmpeg preview: compressed picture packets and all 240 decoded frame hashes/timestamps match the source.", "Limit": "Technical picture preservation; normal-speed listening, lyric alignment and creative acceptance were not established by those checks."},
    {"Stage": "Assemble frames and replacement audio in Cloud", "CFA evidence": "Native graph saved and server-converted; live schemas and uploaded inputs checked. Not executed.", "Limit": "Create Video assembles decoded frames and audio; saving this route re-encodes picture. Local stream-copy measurements do not apply to its eventual output."},
    {"Stage": "Change visible mouth motion", "CFA evidence": "Separate lip-sync candidate prepared; unexecuted.", "Limit": "Prepared speech/vocals are required. A soundtrack swap has no generative mouth stage; lip sync needs its own detail, timing and acceptance review."},
)


def soundtrack_case_markdown():
    lines = ["## CFA case: soundtrack replacement is separate from lip sync", "",
             "October 8, 2026 review of saved CFA records; no new render or media inspection by this guide.", ""]
    for row in _AUDIO_STAGES:
        lines.extend(["### " + row["Stage"], "", row["CFA evidence"], "", row["Limit"], ""])
    lines.extend([
        "The whole-track replacement removes original dialogue, music and ambience. Preserve ambience with separate stems or a deliberate new mix; do not infer selective voice replacement from a soundtrack swap.", "",
        "Prepare the exact replacement recording before choosing mouth timing. Identical written lyrics do not give a new recording identical timing. The first ten seconds are a technical excerpt, not an approved lyric-to-shot edit.", "",
        "Keep source-picture ID/hash, exact audio recording and trim, output route, measured frame/FPS/audio checks, listening notes and acceptance scope together. Stream copy avoids picture decoding/re-encoding; assembling decoded frames uses an encoding path.", "",
        f"[Measured local record]({_AUDIO_EVIDENCE}) · [Cloud and lip-sync handoff]({_AUDIO_GUIDE})", "",
        "Local CFA paths are provenance only; the hosted guide does not read the sibling checkout or include its media.", "",
        f"[FFmpeg stream copy](https://ffmpeg.org/ffmpeg.html#Streamcopy) · [Native Comfy video nodes]({_NATIVE})", "",
    ])
    return "\n".join(lines)


def render_soundtrack_case():
    with st.expander("CFA worked distinction · soundtrack swap, assembly and lip sync"):
        st.caption("October 8 review of saved records. The measured proof was local video editing; Comfy processing remains a Cloud task.")
        st.table(_AUDIO_STAGES)
        st.code("Source picture + replacement recording -> soundtrack swap\nSource frames + FPS + trimmed audio -> Create Video -> Save Video\nSource picture + prepared speech/vocals -> separate lip-sync candidate", language="text")
        st.write("Replacing the complete soundtrack also removes ambience. Use separate stems or a deliberate new mix when ambience must survive. A new recording requires rechecking lyric timings even when the words stay the same.")
        st.write("The ten-second preview is a technical proof, not an approved lyric edit. Listen to the chosen recording, then review mouth motion and preserved details separately.")
        st.markdown("[FFmpeg stream-copy behavior](https://ffmpeg.org/ffmpeg.html#Streamcopy) · [Native Comfy video nodes](" + _NATIVE + ")")
        st.caption("Canonical local CFA evidence (requires its checkout):")
        st.code("D:/Documents/CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_audio_replace_v001.record.json", language="text")

ROUTES = {
    "video_native": {
        "label": "I already have VIDEO → save with native nodes",
        "diagram": "Generator / subgraph.VIDEO [VIDEO]\n  → Save Video.video [VIDEO]\n  → saved video file",
        "meaning": "Use this when the template already assembles its frames and audio into VIDEO. Open the exported file to check picture, sound and duration.",
        "check": "A VIDEO object is not proof of a saved file. Save Video writes the file; keep the workflow JSON separately.",
        "source": _NATIVE,
    },
    "frames_native": {
        "label": "I have frames + audio → assemble with native nodes",
        "diagram": "Decoded frames [IMAGE] → Create Video.images\nOptional sound [AUDIO] → Create Video.audio\nOriginal frame rate   → Create Video.fps\nCreate Video.VIDEO    → Save Video.video",
        "meaning": "Create Video assembles an IMAGE batch, optional AUDIO and a frame rate. Save Video writes the resulting VIDEO to disk. Native nodes are enough for this handoff.",
        "check": "Use the rate that belongs to these frames. Missing audio does not appear just because a video is assembled. When rebuilding HDR video, preserve the source bit depth and color space with supported node/codec settings.",
        "source": _NATIVE,
    },
    "video_vhs": {
        "label": "I have VIDEO → use the optional VHS frame exporter",
        "diagram": "Existing VIDEO → Get Video Components.video\n  images [IMAGE] → Video Combine.images\n  audio  [AUDIO] → Video Combine.audio (if present)\n  fps    [FLOAT] → Video Combine.frame_rate\nVideo Combine → encoded file(s); output type VHS_FILENAMES",
        "meaning": "VideoHelperSuite's Video Combine takes frames on this route. Get Video Components exposes them from VIDEO, so you can keep the generator's subgraph intact.",
        "check": "VIDEO cannot connect straight to its images input. The current VHS socket also supports LATENT with a compatible VAE; this lesson uses decoded IMAGE frames. VHS_FILENAMES cannot feed Save Video.video.",
        "source": _VHS_SOURCE,
    },
}


def timing(frames, source_fps, export_fps):
    """Nominal constant-rate picture durations; no model-validity or sync claim."""
    if isinstance(frames, bool) or not isinstance(frames, int) or frames < 1:
        raise ValueError("Frame count must be a positive whole number.")
    for rate in (source_fps, export_fps):
        if isinstance(rate, bool) or not isinstance(rate, (int, float)) or not math.isfinite(rate) or rate <= 0:
            raise ValueError("Frame rates must be finite, positive numbers.")
    source_seconds = frames / source_fps
    export_seconds = frames / export_fps
    return {"source_seconds": source_seconds, "export_seconds": export_seconds,
            "speed_ratio": export_fps / source_fps}


def handoff_markdown(route_id, frames, source_fps, export_fps):
    route = ROUTES[route_id]
    result = timing(frames, source_fps, export_fps)
    return "\n".join([
        "# Video & audio handoff plan", "", route["label"], "",
        "Conceptual wiring only. This is not an executable ComfyUI workflow or a measured render result.", "",
        "```text", route["diagram"], "```", "", route["meaning"], "", route["check"], "",
        f"- Frames: {frames}", f"- Source/generation FPS: {source_fps}", f"- Export FPS: {export_fps}",
        f"- Nominal source picture duration: {result['source_seconds']:.6f} seconds",
        f"- Nominal exported picture duration: {result['export_seconds']:.6f} seconds",
        f"- Playback speed relative to source: {result['speed_ratio']:.6f}x", "",
        "Frames / FPS describes constant-rate picture duration. It does not validate a model's frame-count rules, account for trimming, or measure an audio track.",
        "Changing only export FPS does not generate intermediate frames or retime speech.", "",
        "## Assign the reference roles", "",
        "- Appearance image and its intended identity / costume / setting:",
        "- Performance video, exact trim and movement / camera to preserve:",
        "- Audio asset and whether to reuse the same signal or reference its voice / rhythm:",
        "- Ordered reference labels and effective prompt inspected in the actual graph:", "",
        "A video input does not automatically enable its soundtrack as an audio reference. Review the actual output; a reuse instruction is not proof of preserved audio or lip sync.", "",
        "## Keep the evidence", "",
        "- Exact model variant, template revision, companion files and custom-node versions:",
        "- Saved baseline workflow and input media:",
        "- Requested dialogue, resolved enhanced prompt (if used) and words actually heard:",
        "- Output filename, codec, frame count, FPS and measured audio/video durations:",
        "- Mouth timing, subject/scene drift, flicker and next change:",
        "- Runtime and attributable usage cost (unknown until measured):", "",
        "Reopen the exported file outside the canvas. Save JSON and media together. Record actual observations in My workbook or Field journal.", "",
        f"[Node reference]({route['source']}) · [Native video nodes]({_NATIVE}) · [Subgraph ports]({_SUBGRAPH})", "",
        soundtrack_case_markdown(),
    ])


def h3_markdown():
    candidate = H3_CANDIDATE
    lines = ["# " + candidate["title"], "", "Research reviewed " + candidate["reviewed"], "",
             candidate["status"], "", candidate["caveat"], "", "## Assign each input a job", ""]
    for role in candidate["roles"]:
        lines.extend(["### " + role["Input"], "", role["Job"], "", "Review: " + role["Review"], ""])
    lines.extend(["## Dependencies to verify in Cloud", ""])
    lines.extend("- " + item for item in candidate["dependencies"])
    lines.extend(["", "## From candidate to a bounded preview", ""])
    lines.extend(f"{index}. {item}" for index, item in enumerate(candidate["steps"], 1))
    lines.extend(["", "Record exact template/revision, reference roles, compiled settings and workspace evidence in the existing Video workshop plan fields. This checklist is not a Comfy workflow or a successful run record.", ""])
    lines.extend(f"- [{label}]({url})" for label, url in candidate["sources"])
    return "\n".join(lines) + "\n"


def render_h3_candidate(key_prefix):
    """Read-only research branch; opening it never selects a route or accepts a take."""
    candidate = H3_CANDIDATE
    with st.expander("Additional candidate · MiniMax H3 reference roles"):
        st.markdown("**" + candidate["title"] + "**")
        st.caption("Research reviewed " + candidate["reviewed"])
        st.info(candidate["status"])
        st.table(candidate["roles"])
        st.markdown("**Dependencies to check in the actual Cloud workspace**")
        for item in candidate["dependencies"]:
            st.markdown("- " + item)
        st.markdown("**From candidate to a bounded preview**")
        for index, item in enumerate(candidate["steps"], 1):
            st.markdown(f"{index}. {item}")
        st.write(candidate["caveat"])
        st.caption("If CFA chooses this alternate recipe, record its exact template in Workflow copy and exact revision, assign inputs in Reference image / replacement audio / control asset, and document compiled settings and Cloud compatibility evidence. This callout leaves the recommended route and saved takes unchanged; opening it does not select H3.")
        st.markdown(" · ".join(f"[{label}]({url})" for label, url in candidate["sources"]))
        st.download_button("Download H3 candidate checklist", h3_markdown(),
                           "pathfinder-h3-candidate.md", "text/markdown", key=key_prefix + "_download")


def _dialogue():
    st.markdown("### Keep control of the spoken line")
    st.write("A prompt enhancer is another author in the chain: inspect the text it produces before treating the final speech as a test of your original script.")
    st.markdown(
        "1. Begin with one speaker and one short line. Keep the exact requested wording.\n"
        "2. In a copy of the graph, inspect the enhancer's resolved text. Compare enabled versus direct-text routing only where the template supports it. Keep the required text encoder and conditioning stages.\n"
        "3. Listen to the output and write down the words actually spoken. Matching the prompt does not guarantee matching speech.\n"
        "4. If exact words and timing are essential, prepare and verify the replacement audio first, then choose a workflow that accepts that audio."
    )
    st.table([
        {"Goal": "Explore a new speaking shot", "Path": "LTX text-to-video or image-to-video with generated audio", "Check": "The line, pronunciation and scene are generated; review each take."},
        {"Goal": "Animate an image to prepared speech", "Path": "Documented LTX-2.3 image + audio-to-video template", "Check": "Uses supplied audio while generating motion; the result is a new clip."},
        {"Goal": "Rewrite dialogue within an existing scene", "Path": "Rewrite a scene → replacement audio / localized lip-sync route", "Check": "Start from the source footage and compare its camera, cuts, background and identity against the result."},
    ])
    st.caption("The new tutorial demonstrates generated shots. It does not establish the toolchain used in your movie-scene inspiration or prove that an existing scene will be preserved.")
    st.markdown(f"[Official LTX-2.3 task-specific templates]({_LTX})")


def _reference_and_detail():
    with st.expander("Use a simple 3D scene to control a reference"):
        st.write("The creator's low-poly scene plus style-reference demonstration suggests a useful practice branch for your original 3D goal.")
        st.markdown(
            "1. Build a simple Blender scene, set its camera and save the .blend file. Render one reference image.\n"
            "2. In a compatible image-editing template, label the first input as the structure reference and the second as the desired visual style. Keep the exact image order.\n"
            "3. Compare silhouettes, object placement and camera angle against the source render. Record the drift as well as the appealing detail.\n"
            "4. Change the camera in Blender for a second view and repeat. Consistency between generated views still needs checking."
        )
        st.info("The .blend file retains editable geometry. Generated image detail is pixels; it does not update the mesh, materials or animation rig.")
        st.markdown("[Official FLUX.2 Klein editing/reference workflows](https://docs.comfy.org/tutorials/flux/flux-2-klein) · [Blender rendering](https://docs.blender.org/manual/en/5.1/render/introduction.html)")
    with st.expander("Iterate first, upscale the selected take"):
        st.write("Review motion and dialogue at a supported working resolution, then spend the extra processing on a take worth keeping. Inspect edges, faces, text and flicker before and after upscaling; added detail can be invented or altered.")
        st.code("Decoded IMAGE frames → compatible image upscaler\n  → Create Video / optional Video Combine\nOriginal AUDIO and FPS → the same assembly stage", language="text")
        st.write("An image upscaler operates on pixels. LTX's latent spatial upscaler is a different model role used within its documented generation pipeline; keep its weights in the requested latent_upscale_models location. Neither changes frame count merely by increasing image dimensions.")
        st.caption("The tutorial's NVIDIA RTX extension is an optional hardware-specific route. Its package, SDK and Python environment must match the installation; Cloud support must be checked in the managed catalog. Installing it locally does not add it to Cloud.")
        st.markdown(f"[LTX component roles and folders]({_LTX}) · [Cloud environment](https://docs.comfy.org/get_started/cloud)")


def render(key_prefix="help_video_handoff"):
    st.subheader("Video & audio · make the handoff visible")
    st.write("Open a compact graph, identify what comes out, and carry its frames, sound and timing all the way to a playable file.")
    st.caption("Practice alongside the additional guide's annotations in Workflow anatomy → Tutorial notes. These diagrams explain connections; they do not run or inspect ComfyUI.")
    selected = st.selectbox("What are you handing off?", list(ROUTES),
                            format_func=lambda value: ROUTES[value]["label"], key=key_prefix + "_route")
    route = ROUTES[selected]
    st.code(route["diagram"], language="text")
    st.write(route["meaning"])
    st.info(route["check"])
    st.markdown(f"[Check this node's documented behavior]({route['source']})")
    with st.expander("Expose frames and audio from a subgraph"):
        st.markdown(
            "1. Save a copy, then open the subgraph and find its real output chain. A compact node can contain many internal nodes.\n"
            "2. Connect the decoded IMAGE output to a subgraph output slot. Expose an actual AUDIO output separately when present.\n"
            "3. Return to the parent graph and connect those matching ports to the assembly/export nodes. Keep the source FPS with them.\n"
            "4. If the subgraph already returns VIDEO, Get Video Components is an alternative that leaves its internals intact."
        )
        st.caption("A subgraph port exposes data; renaming a port or adding a reroute does not convert VIDEO to IMAGE. Use Node Atlas to inspect the individual sockets.")
        st.markdown(f"[Subgraph input/output editing]({_SUBGRAPH})")
    with st.expander("VHS format, preview and file retention"):
        st.write("VideoHelperSuite is optional. Confirm the package is available in your environment before choosing its route. Use an audio-capable format when keeping speech; its video/h264-mp4 preset supports audio, while a GIF does not.")
        st.write("Check save_output: True writes into the configured output directory; False still writes files, but into temp. A canvas preview or a temporary file is not a retained handoff. Download Cloud results and reopen the saved file.")
        st.markdown("[VHS save paths](" + _VHS_SOURCE + ") · [H.264/MP4 preset](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite/blob/main/video_formats/h264-mp4.json)")

    st.markdown("### Timing desk · same frames, different playback")
    frame_col, source_col, output_col = st.columns(3)
    frames = frame_col.number_input("Frame count", min_value=1, max_value=100000, value=81, step=1, key=key_prefix + "_frames")
    source_fps = source_col.number_input("Source / generation FPS", min_value=1.0, max_value=240.0, value=24.0, step=1.0, key=key_prefix + "_source_fps")
    export_fps = output_col.number_input("Export FPS", min_value=1.0, max_value=240.0, value=24.0, step=1.0, key=key_prefix + "_export_fps")
    result = timing(frames, source_fps, export_fps)
    before, after, speed = st.columns(3)
    before.metric("Source picture duration", f"{result['source_seconds']:.3f} s")
    after.metric("Exported picture duration", f"{result['export_seconds']:.3f} s")
    speed.metric("Playback speed", f"{result['speed_ratio']:.3f}×")
    if source_fps != export_fps:
        st.warning("Changing only export FPS changes picture speed and duration. It does not create intermediate frames or retime the audio. Recheck speech alignment before saving a final take.")
    st.caption("Nominal constant-rate duration = frames ÷ FPS. Trimming, looping or ping-pong change the result. These numbers do not validate a model's supported frame counts or measure audio. Keep the chosen template's generation settings for the first test.")
    st.markdown(f"[Video Combine frame-rate behavior]({_VHS})")
    _dialogue()
    render_soundtrack_case()
    render_h3_candidate(key_prefix + "_h3")
    _reference_and_detail()
    st.download_button("Download this video handoff plan", handoff_markdown(selected, frames, source_fps, export_fps),
                       file_name="comfyui-video-audio-handoff.md", mime="text/markdown", key=key_prefix + "_download")
    st.caption("Keep actual run observations in My workbook or Field journal. This explorer's settings are not included in a journey export; download the plan to retain them.")
