"""Dated CFA findings for teaching; no account calls or sibling-repo reads.

This static snapshot reflects local CFA records reviewed on October 4, 2026.
It does not verify the learner's current account or installed node catalog.
Evidence paths are relative to Help and are references, not runtime inputs.
"""

REVIEWED = "October 4, 2026"
SOURCE_PATH = "D:/Documents/CFA/docs/notes/explorable_world/comfy/workflows/README.md"
SUMMARY = (
    "CFA records include the historical pump still and two completed Hon Dolo "
    "reference-edit candidates awaiting user acceptance. Input-only checks and "
    "exposed controls were validated October 4; tattoo/grill finishing and video "
    "remain pending. This is a review of saved records, not a new account check."
)

STATUS_ROWS = [
    {
        "Evidence": "Historical pump still",
        "Status": "Completed September example, packaged under Worked example; a starting direction, not an accepted game asset.",
    },
    {
        "Evidence": "Hon Dolo clean likeness and style comparison",
        "Status": "Two 1360 × 768 stills completed in Cloud; both await user acceptance. The Candid Film 0.5 comparison established no quality improvement.",
    },
    {
        "Evidence": "Prompt and reference check",
        "Status": "Independent input-only workflow completed with no model or sampler nodes. Browser text-widget display was not inspected; Cloud runtime may still accrue.",
    },
    {
        "Evidence": "Reference editor version 6",
        "Status": "Connected sampling controls exposed; dry run and prior execution-graph equivalence passed. No additional render for this controls change.",
    },
    {
        "Evidence": "Connection and model access",
        "Status": "Saved records show restored Comfy access and a successful shared Civitai-origin LoRA run. Authenticated Civitai import remains unverified.",
    },
    {
        "Evidence": "Woman-and-wolf capability test",
        "Status": "Source clip and official graph inspection preserved; source playback, trim, dependencies and execution remain pending. Separate from the music-video production.",
    },
    {
        "Evidence": "Finishing and video",
        "Status": "No accepted decorated identity master, CFA video transformation, rap lip-sync result or accepted HD/4K video master is recorded. H3 template discovery does not establish execution.",
    },
]

LESSONS = (
    {
        "title": "Name each reference and inspect its crop",
        "observation": "CFA used image 1 for the Grok design and image 2 for likeness, cropping the intended person from a multi-person source. The whole-image result retained recognizable shirt, chain and framing, but the smile and earring drifted.",
        "apply": "Record input order and role, preview the visible crop, and reset it when changing sources. Review everything that must remain: reference conditioning does not guarantee likeness or lock pixels outside the intended edit.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_reference_edit_v001.record.json",
    },
    {
        "title": "Check inputs before diffusion",
        "observation": "The separate prompt/reference check completed image loading, cropping, style/text composition and previews with zero model or sampler nodes. It is an independent copy; its changes do not synchronize to the main editor. Browser text-widget display remains uninspected.",
        "apply": "Inspect the effective prompt and crop, then explicitly transfer chosen settings into the render workflow. Input-only runs produce no generated character, and Cloud runtime may still accrue.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_prompt_reference_check_v001.record.json",
    },
    {
        "title": "Expose the controls that actually drive this graph",
        "observation": "Version 6 exposes the connected KSamplerSelect, seed, steps and CFG around SamplerCustomAdvanced. Defaults remain seed 42, four steps, Euler and CFG 1. The controls update passed a dry run and graph-equivalence check without another render; the negative field remains inactive notes.",
        "apply": "Trace each control to the active model and sampler. Do not copy an SDXL negative branch into this CFG 1 Klein baseline or invent an ordinary img2img denoise control. Start with no style and compare one change at a fixed seed.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/README.md",
    },
    {
        "title": "Review the clean identity before finishing",
        "observation": "The clean candidate removed tattoos and grill while changing face and hair toward the supplied reference. Its broader smile, missing earring, skin/eyes and background still require user review. Both recorded still candidates remain unaccepted.",
        "apply": "Preserve the clean image, references, graph and settings; accept the face before localized tattoo/grill finishing. Check lettering, placement and facial structure separately. Only an accepted decorated still becomes the identity master; performance testing follows.",
        "evidence": "../../CFA/docs/notes/explorable_world/comfy/workflows/hon_dolo_reference_edit_v001.record.json",
    },
)
