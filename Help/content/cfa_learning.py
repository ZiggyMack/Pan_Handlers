"""Dated CFA findings for teaching; no account calls or sibling-repo reads.

This static snapshot reflects local CFA records reviewed on October 8, 2026.
The October 4 still-workflow lessons remain dated historical examples.
It does not verify the learner's current account or installed node catalog.
Evidence paths are relative to Help and are references, not runtime inputs.
"""

REVIEWED = "October 8, 2026"
SOURCE_PATH = "D:/Documents/CFA/docs/notes/explorable_world/comfy/workflows/README.md"
COLLABORATOR_RECORD = "../../CFA/docs/notes/explorable_world/comfy/projects/collaborators/comfy_workflows.json"
SUMMARY = (
    "CFA has executed a short Hon Dolo image-to-video test and two source-video relighting "
    "tests. The motion candidate remains unaccepted; the depth and Canny comparisons failed "
    "strict preservation of the source details. A separate local soundtrack swap preserved "
    "all 240 picture frames and their timestamps; its Cloud assembly graph is saved and "
    "server-converted but unexecuted. Lip-sync is a separate unexecuted candidate. "
    "Earlier still-workflow lessons remain below with their October 4 scope. "
    "This is a review of saved records, not a new account check or fresh media inspection."
)

STATUS_ROWS = [
    {
        "Evidence": "Historical pump still",
        "Status": "Completed September example, packaged under Worked example; a starting direction, not an accepted game asset.",
    },
    {
        "Evidence": "October 4 · Hon Dolo clean likeness and style comparison",
        "Status": "Two 1360 × 768 stills completed in Cloud; both await user acceptance. The Candid Film 0.5 comparison established no quality improvement.",
    },
    {
        "Evidence": "October 4 · Prompt and reference check",
        "Status": "Independent input-only workflow completed with no model or sampler nodes. Browser text-widget display was not inspected; Cloud runtime may still accrue.",
    },
    {
        "Evidence": "October 4 · Reference editor version 6",
        "Status": "Connected sampling controls exposed; dry run and prior execution-graph equivalence passed. No additional render for this controls change.",
    },
    {
        "Evidence": "October 4 · Civitai Film Comparison version 4",
        "Status": "Paired A baseline / B Candid Film 0.5 passed conversion, dry run and branch-equivalence checks. Paired render not submitted; earlier separate stills are not results from this layout. Base-trained adapter on distilled Klein remains experimental.",
    },
    {
        "Evidence": "October 4 · Image Refinement SDXL version 2",
        "Status": "Saved single-image Juggernaut XL v9 graph passed conversion, resolved-input checks and dry run. Not rendered. Denoise 0.30 is a starting experiment, not tested quality or a preservation percentage.",
    },
    {
        "Evidence": "October 4 · Connection and model access",
        "Status": "Saved records show restored Comfy access and a successful shared Civitai-origin LoRA run. Authenticated Civitai import remains unverified.",
    },
    {
        "Evidence": "October 4 · Woman-and-wolf capability test",
        "Status": "Source clip and official graph inspection preserved; source playback, trim, dependencies and execution remain pending. Separate from the music-video production.",
    },
    {
        "Evidence": "October 4 · Hon Dolo motion test",
        "Status": "Native LTX-2.5 image-to-video executed: 97 frames at 24 fps, 960 × 512. Twelve sampled frames show long eye closures and smile drift. Full playback/audio review and acceptance remain pending. New motion from a still, not preservation of source-video performance.",
    },
    {
        "Evidence": "October 7 · Depth and Canny relighting comparisons",
        "Status": "Both LTX-2.3 source-video tests executed: 57 frames at 24 fps, 1024 × 576. Matched timestamps and full decode passed, but sampled mouth, grill, piercings, lettering and background drift failed strict lighting-only preservation. Canny showed no material fidelity gain. Neither is accepted.",
    },
    {
        "Evidence": "October 7 · Local soundtrack replacement",
        "Status": "Ten-second FFmpeg stream-copy proof completed locally without AI generation: compressed picture packets and all 240 decoded frame hashes/timestamps match the source. Replacement audio was encoded separately. Listening, normal-speed review and acceptance remain pending; no mouth movement was changed.",
    },
    {
        "Evidence": "October 7 · Cloud soundtrack assembly version 2",
        "Status": "Saved with uploaded inputs and server conversion/readback; 38 schema/routing/media checks passed. Not executed. This frame-assembly graph re-encodes picture, so the local preview's stream-preservation result does not establish the Cloud export's quality.",
    },
    {
        "Evidence": "October 7 · Lip-sync candidate",
        "Status": "Separate Sync editor prepared for a provisional 2.375-second source/vocal interval. Not executed or accepted; exact lyric selection, suitable vocal signal, live compatibility and an account quote remain to be checked. Soundtrack replacement is not lip-sync.",
    },
    {
        "Evidence": "Finishing and video",
        "Status": "Executed motion and relighting tests now exist, with the review limits above. No accepted Comfy decorated identity master, rap lip-sync result or accepted HD/4K video master is established by these records. H3 template discovery does not establish execution.",
    },
]

LESSONS = (
    {
        "title": "A successful video job can fail the preservation brief",
        "observation": "October 7: the depth and Canny LTX-2.3 tests both produced 57-frame, 24 fps videos with matching source timestamps and clean full decode. Matched samples nevertheless changed mouth shape, lower grill, lip rings, eye/know lettering and background geometry. Canny did not materially improve continuity. Recorded review covered matched samples and decode, not normal-speed playback or listening.",
        "apply": "Compare the same source timecodes and the details named in the brief. A correctly timed file is not proof of matching performance or identity. Keep both failed results as evidence; do not promote their altered details into working references. For a lighting-only change, evaluate non-generative grading or compositing before another generative reinterpretation. Saved graphs: [depth](https://cloud.comfy.org/#a63aca02-3ec8-45fe-a830-5baf40bd9eeb) and [Canny](https://cloud.comfy.org/#fa384c55-d9d5-4afe-9f41-d0bbe30b15d1). Exact run records: [depth record](../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_gemini_relight_v001.record.json) and [Canny record](../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_gemini_relight_v002.record.json).",
        "evidence": COLLABORATOR_RECORD,
    },
    {
        "title": "Keep new motion separate from preserving a recorded performance",
        "observation": "October 4: the clean Hon Dolo still drove a completed native LTX-2.5 image-to-video trial. Its 97 frames decoded; twelve samples broadly retained the face, hair, shirt, chain and setting, but showed prolonged eye closure and a changing smile. The source still was a candidate, not an accepted identity master. Full playback and audio were not reviewed.",
        "apply": "Use [the recorded motion workflow](https://cloud.comfy.org/#bfe78175-2366-4a28-bb76-518c89bef525) as an image-to-video example. A still supplies appearance and an opening frame; it supplies no original motion to preserve. Record actual output dimensions and frame count instead of inferring them from a selector label. Acceptance needs a full-speed review against the shot brief, not only a successful job or contact sheet.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_motion_v001.record.json",
    },
    {
        "title": "Attach preservation evidence to the exact export method",
        "observation": "October 7: a local FFmpeg soundtrack proof copied the original compressed picture and replaced all original audio with song time 0:00–0:10. The saved record measures matching compressed video packets and all 240 decoded frame hashes/timestamps. The separate Cloud version 2 was saved, server-converted and inspected with uploaded inputs; it has not executed. Its native image-frame assembly re-encodes the picture.",
        "apply": "Open [Replace Video Soundtrack](https://cloud.comfy.org/#2c490a37-6110-4c7b-b073-a3354493645b) to study Load Video → Get Video Components → Create Video → Save Video, with source FPS and a separately trimmed audio input. Keep the original audio disconnected for a whole-track replacement. The local stream-copy result does not prove the quality of a future Cloud export. Audition the intended phrase, then measure and review that actual export. The [Cloud preflight](../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_audio_replace_v001.cloud_preflight.json) supersedes the older local record's authentication status; neither is a live account check here.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_audio_replace_v001.README.md",
    },
    {
        "title": "Replacing a soundtrack does not synchronize the mouth",
        "observation": "The completed local swap changes sound while retaining the same picture. A separate Sync lip-sync candidate has only a prepared editor and preflight record. Its provisional 2.375-second song interval has not been accepted as the intended lyric, and no generated mouth/grill fidelity result exists.",
        "apply": "Choose a continuous shot and exact replacement vocal interval before a mouth-sync test. Preserve the baseline picture and song timecodes; review fast syllables, pauses, grill, piercings and nearby lettering after an actual run. A whole-track swap also removes source ambience, music and dialogue together; preserving selected ambience needs stems or a deliberate new mix. Keep the candidate's live compatibility and quoted cost checks separate from the already measured local swap.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_lipsync_v001.preflight.json",
    },
    {
        "title": "Name each reference and inspect its crop",
        "observation": "October 4 snapshot: CFA used image 1 for the Grok design and image 2 for likeness, cropping the intended person from a multi-person source. The whole-image result retained recognizable shirt, chain and framing, but the smile and earring drifted.",
        "apply": "Record input order and role, preview the visible crop, and reset it when changing sources. Review everything that must remain: reference conditioning does not guarantee likeness or lock pixels outside the intended edit.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_reference_edit_v001.record.json",
    },
    {
        "title": "Check inputs before diffusion",
        "observation": "October 4 snapshot: The separate prompt/reference check completed image loading, cropping, style/text composition and previews with zero model or sampler nodes. It is an independent copy; its changes do not synchronize to the main editor. Browser text-widget display remains uninspected.",
        "apply": "Inspect the effective prompt and crop, then explicitly transfer chosen settings into the render workflow. Input-only runs produce no generated character, and Cloud runtime may still accrue.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_prompt_reference_check_v001.record.json",
    },
    {
        "title": "Expose the controls that actually drive this graph",
        "observation": "October 4 snapshot: Version 6 exposes the connected KSamplerSelect, seed, steps and CFG around SamplerCustomAdvanced. Defaults remain seed 42, four steps, Euler and CFG 1. The controls update passed a dry run and graph-equivalence check without another render; the negative field remains inactive notes.",
        "apply": "Trace each control to the active model and sampler. Do not copy an SDXL negative branch into this CFG 1 Klein baseline or invent an ordinary img2img denoise control. Start with no style and compare one change at a fixed seed.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/README.md",
    },
    {
        "title": "Compare a complete baseline with one changed adapter",
        "observation": "October 4 snapshot: Civitai Film Comparison v4 has two complete generation/decode/save branches. Both share original references, crop, assembled prompt, Euler sampler, four steps, CFG 1 and seed 42. A bypasses the LoRA; B enables Candid Film at 0.5. The compiled graph confirmed A matches main v6, and B matches A after bypassing its sole LoRA. Conversion and dry run passed; no paired render was submitted. The earlier separate stills remain unaccepted.",
        "apply": "Open [Civitai Film Comparison](https://cloud.comfy.org/#1ee8615b-5586-42fd-bf3d-3d202b2377eb) and check the revision. Preserve the shared inputs and distinct A_baseline / B_candid_film save prefixes. Run evaluates two generation branches unless the unwanted output is muted. The creator's Candid Film examples target Klein 9B base; CFA uses distilled 9B, so successful loading does not establish recommended compatibility or improved quality. This independent graph does not synchronize with the main editor. Reconstruction files: hon_dolo_civitai_comparison_v001.editor.json and hon_dolo_civitai_comparison_v001.preflight.api.json in the linked CFA workflow directory.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_reference_edit_v001.record.json",
    },
    {
        "title": "Choose single-image refinement for its actual scope",
        "observation": "October 4 snapshot: Image Refinement SDXL v2 loads the original Grok design, resizes it with Lanczos and VAE-encodes those pixels into KSampler's starting latent. Its Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors checkpoint supplies matching encode/decode VAE and both CLIP text encoders. Defaults are seed 42 fixed, 30 steps, CFG 5, dpmpp_2m / karras, denoise 0.30 and approximately 1 MP aligned to 8 pixels. Positive and negative branches are active; negative starts empty. Validation passed, but it has no generated output yet.",
        "apply": "Open [Image Refinement SDXL](https://cloud.comfy.org/#2a60a23f-f68a-4a66-92c6-0e30aa0d5e03), currently recorded as v2. For a denoise comparison, keep the same original image, prompt, seed and remaining settings. This whole-image recipe has no second likeness input, mask, ControlNet, video control or active LoRA. Low denoise can still change faces, lettering, teeth and jewelry; resizing is interpolation, not learned upscaling. Keep SDXL adapters separate from Klein adapters. Reconstruction files: hon_dolo_img2img_sdxl_v001.editor.json and hon_dolo_img2img_sdxl_v001.preflight.api.json in the linked CFA workflow directory.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_img2img_sdxl_v001.record.json",
    },
    {
        "title": "Inspect compiled inputs before trusting the canvas",
        "observation": "October 4 snapshot: The recovered SDXL source template carried stale widgets_values_named fields that overrode edited positional widget values during conversion. CFA caught the mismatch in v1 and corrected it in v2 before any render. Final compiled-input checks confirmed the intended model, text, source, seed, sampler, denoise, VAE and output prefix.",
        "apply": "After adapting or reopening a graph, compare the converted execution graph with the settings you intended. A visible value, a successful import or a structural dry run alone does not prove that the submitted prompt/model/settings are correct. Record the resolved values and graph revision, then distinguish validation from an executed result. Preserve the original JSON when repairing a recovered template.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_img2img_sdxl_v001.record.json",
    },
    {
        "title": "Review the clean identity before finishing",
        "observation": "October 4 snapshot: The clean candidate removed tattoos and grill while changing face and hair toward the supplied reference. Its broader smile, missing earring, skin/eyes and background still require user review. Both recorded still candidates remain unaccepted.",
        "apply": "Preserve the clean image, references, graph and settings; accept the face before localized tattoo/grill finishing. Check lettering, placement and facial structure separately. Only an accepted decorated still becomes the identity master; performance testing follows.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_reference_edit_v001.record.json",
    },
)
