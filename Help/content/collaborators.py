"""Portable teaching snapshot of CFA's October 8 collaborator handoff.

Includes the appended receipt dated 2026-10-09 01:45:08 UTC (October 8 local).
All evidence paths are relative to Help. Nothing reads CFA or calls a provider.
Provider roles describe this project's division of work, not a quality ranking.
"""

REVIEWED = "October 8, 2026 · receipt through October 9, 01:45:08 UTC"
_CFA = "../../CFA/docs/notes/explorable_world/comfy/"
_PROJECTS = _CFA + "projects/"
_COLLAB = _PROJECTS + "collaborators/"
_HON = _PROJECTS + "hon_dolo_strictly_business/"
_RETURN = _COLLAB + "panhandler_return_20261008.txt"

PROVIDERS = {
    "comfyui": {
        "name": "ComfyUI",
        "purpose": "Make a bounded, inspectable edit and compare the result with its actual source.",
        "how": (
            "Choose the job first: animate a still, change a video's appearance, replace its soundtrack, or match mouth motion. Each has different inputs and success checks.",
            "Carry an exact source ID, its allowed role, a saved workflow revision and the settings into a short Cloud test. Keep the original and a distinct output branch.",
            "Review matching moments and normal-speed playback. Record drift in face, tattoos, jewelry, motion and timing before promoting a take.",
            "Use the existing video handoff lesson for frame/FPS/audio assembly. CFA's local soundtrack preview preserved all 240 picture frames and timestamps; its Cloud graph was converted but not executed. A soundtrack swap does not change lip motion.",
        ),
        "boundaries": "CFA's native LTX motion test ran; sampled frames showed long blinks and smile drift, with acceptance pending. Both depth and Canny relight tests ran and failed detail preservation. The separate lip-sync candidate has not run. These measured limitations should shape the next test.",
        "sources": (),
        "evidence": (
            ("Comfy run states and observed defects", _COLLAB + "comfy_workflows.json"),
            ("Measured soundtrack replacement", _CFA + "workflows/hon_dolo_audio_replace_v001.README.md"),
        ),
    },
    "grok": {
        "name": "Grok",
        "purpose": "Explore character designs, wardrobe, tattoo art and scene ideas through finite review rounds.",
        "how": (
            "Name the project and lane: Prime preservation, a scoped correction, or new discovery. Give each attachment one explicit job such as identity, outfit, setting or motif.",
            "For discovery, invent freely within the brief. Every new tattoo comes with a four-option standalone design sheet in the same delivery; mark which option matches the body proof. No approval-first gate is needed for each invention.",
            "For the boss search, compare the slug, hippo and gecko-frog directions in five reviewed rounds of ten single proofs. Review each round before the next; only the selected winner receives a front/back/left/right set.",
            "Request actual files, a contact sheet and a manifest with roles and honest lineage. After receipt, verify the archive and extracted files before visual review and scoped acceptance.",
        ),
        "boundaries": "The latest receipt reports provider-visible LAG500 parts 01–08, boss round 01 and Hon Dolo returns v001/v002. None is yet verified received locally in that receipt. Preserve the eight-part completeness check; a visible download packet is not verified intake or an accepted cast.",
        "sources": (),
        "evidence": (
            ("Current creative and companion-art rules", _COLLAB + "grok_design_instructions.txt"),
            ("Boss discovery plan", _HON + "feedback/boss_discovery_20261008.txt"),
            ("Provider-visible returns and intake boundary", _RETURN),
        ),
    },
    "gemini": {
        "name": "Gemini",
        "purpose": "Develop the story and shot ideas while keeping reusable project context and actual visual inputs distinguishable.",
        "how": (
            "Keep the shared CFA/Comfy methods notebook separate from the Hon Dolo and Lisan Al Gaib project notebooks. Their identities, tattoos, music and source roles remain separate.",
            "Record the effective model and actual attachments for every result. A chat attachment, a selected notebook text source and a successfully ingested visual-media source are different records.",
            "Inspect the source itself: does it open as usable text, image or video? Check failed entries separately from selected usable sources; do not use a model's acknowledgement as proof that it saw raw video frames.",
            "Return reusable findings through the project handoff. Shared-rule changes, cross-project digests and winner promotion remain manual decisions in this setup.",
        ),
        "boundaries": "The receipt verifies three notebooks, processed TXT imports, synced chat context and some chat attachments. Direct native MP4 Sources attempts and a JPEG retry failed. Lisan had 11 entries but only five usable selected sources: two TXT and three chats; six image entries failed. Persistent raw visual-media readiness remains unverified. T02 remains a scene working reference, not an identity standard.",
        "sources": (
            ("Google: notebook and chat context", "https://support.google.com/gemininotebook/answer/17003757?hl=en"),
            ("Google: source types and YouTube transcript import", "https://support.google.com/gemininotebook/answer/16215270?hl=en"),
        ),
        "evidence": (
            ("Notebook setup and failed-source receipt", _COLLAB + "gemini_notebooks_20261008/setup_status.json"),
            ("Latest context-versus-media finding", _RETURN),
        ),
    },
    "flow": {
        "name": "Google Flow",
        "purpose": "Prepare a small character or video proof with explicit reference roles, then judge preservation against the baseline.",
        "how": (
            "Finish sorting before upload. Keep Hon and Lisan in separate projects; distinguish identity references from outfit, setting and composition references. A local Characters folder does not automatically create a Flow character.",
            "Unzip the chosen package locally and attach its actual media. Bind the real uploaded filename and asset ID to its source hash and allowed role; an exported selection list is not the media itself.",
            "Inspect the account's actual model, mode, output count and displayed cost. The prepared character proof starts with one identity image. The separate video test starts with one six-second excerpt and changes only lighting.",
            "Compare the result with matching baseline moments and playback; check duration, FPS, framing, motion, contact and audible content. Record defects and acceptance separately from a pleasing appearance.",
        ),
        "boundaries": "Experiment 002 is prepared from retained GEM-5A115C59, the 41-second source: frames 244–387, 144 frames, six seconds, 1280 × 720 at 24 fps. The H.264 excerpt is re-encoded and silent; exact pixel preservation is not established. No Flow upload, generation, provider cost or acceptance is recorded. A longer montage is not evidence of better quality.",
        "sources": (
            ("Google: create video and assign references", "https://support.google.com/flow/answer/16353334?co=GENIE.Platform%3DDesktop&hl=en"),
            ("Google: projects and character assets", "https://support.google.com/flow/answer/16935308"),
        ),
        "evidence": (
            ("Where brief, files and prompt go", _COLLAB + "flow_start_here.txt"),
            ("Identity versus outfit/scene intake", _COLLAB + "flow_intake_20261008.txt"),
            ("Retained-source lighting experiment", _HON + "flow/second_video_experiment_20261008.txt"),
            ("Excerpt preparation measurements", _HON + "flow/video_test_002/manifest.json"),
        ),
    },
}

COMMON_LESSONS = (
    {
        "title": "A favorite has an approval scope",
        "meaning": "A star shortlists an image. A working-reference decision must say which details may guide later work; the independent export basket selects the actual handoff package.",
        "example": "A liked coat or saloon setting may still need tattoo and grill repairs. Keep/needs-fixes/removal choices and shot destinations do not approve the whole character or delete an original.",
        "evidence": _HON + "feedback/review_sweep_20261008.json",
    },
    {
        "title": "Describe the artwork you actually have",
        "meaning": "Filename, appearance, transparency and lineage answer different questions. Preserve the source ID/hash and label original, derived crop, reconstruction or missing original honestly.",
        "example": "Thirteen stencil-named helpers were opaque photo crops or placement sheets, not verified transparent originals. Some dice-named files showed retired details; two ship drawings disagreed in geometry.",
        "evidence": _RETURN,
    },
    {
        "title": "An exact crop is a different kind of evidence",
        "meaning": "A pixel crop retains part of an existing image and can record parent hash and bounds. A generated recreation or later tracing adds interpretation and needs its own lineage.",
        "example": "Luke, Leia and Han likeness crops preserve pixels from the group photo. They are separate possible Comfy inputs and do not redefine Hon Dolo's tattoos or current identity anchor.",
        "evidence": _CFA + "casting/likeness_crops/manifest.json",
    },
    {
        "title": "Export review decisions and media deliberately",
        "meaning": "A selection JSON/list describes assets; a media ZIP contains files. Browser/session choices need the chosen review file or export/import to become durable CFA state.",
        "example": "Mission Control can prepare a sweep or package without invoking another agent, sending to a provider or deleting originals. CFA keeps one master media record visible through both project and collaborator views.",
        "evidence": _RETURN,
    },
    {
        "title": "A newer explicit choice overrides an older star",
        "meaning": "Keep the decision history and bytes while updating the working source. Selection precedence does not mean two files have identical content.",
        "example": "Retain GEM-5A115C59 (41 seconds), archive GEM-97D0B65E (40 seconds) from the working library; retain GEM-D6940AFC (20-second Leather Jacket Turnaround), archive GEM-3CA92958 (10 seconds).",
        "evidence": _RETURN,
    },
    {
        "title": "Completion at the provider is only one stage",
        "meaning": "Record provider completion, local receipt, verified extraction, visual inspection and acceptance independently. Check all parts of a multipart delivery before cleanup or promotion.",
        "example": "The latest debrief sees LAG500's eight provider packets, a boss round and Hon returns. It does not verify local receipt, archive CRC, extracted hashes, image decode, manifest reconciliation or acceptance.",
        "evidence": _RETURN,
    },
    {
        "title": "Text context does not establish visual ingestion",
        "meaning": "A synced chat can preserve useful conversation text without proving that its raw attached video became a persistent visual source. Count usable selected sources separately from failed entries.",
        "example": "Lisan's five usable selected sources were text and chats, despite 11 entries. Google's documented YouTube source imports the transcript; a YouTube link alone would not meet the raw visual-video objective.",
        "evidence": _COLLAB + "gemini_notebooks_20261008/setup_status.json",
    },
    {
        "title": "Test the requested preservation, not just attractiveness",
        "meaning": "Use a short continuous shot, keep other changes fixed and inspect the precise features that must survive. A successful render can fail its purpose.",
        "example": "Depth and Canny relights drifted in mouth, grill and tattoo details. The separate Flow lighting proposal therefore compares one subtle change against a known excerpt; its future result is still unknown.",
        "evidence": _COLLAB + "comfy_workflows.json",
    },
)

EVIDENCE_STATES = (
    {"Stage": "Available / prepared", "Meaning": "An identified local source, recipe or brief exists; no upload or run follows from that."},
    {"Stage": "Uploaded / bound", "Meaning": "The provider's actual attachment is linked to its source ID, hash and allowed role."},
    {"Stage": "Usable source context", "Meaning": "The intended source opens and is selectable. Text context and raw visual ingestion are distinct checks."},
    {"Stage": "Validated", "Meaning": "A graph or request passes specified checks; generation and quality remain unproven."},
    {"Stage": "Executed / provider complete", "Meaning": "A job or return is visible at the provider. That does not prove a local download."},
    {"Stage": "Received locally", "Meaning": "Actual expected files/parts arrived; names alone do not establish integrity or completeness."},
    {"Stage": "Verified extraction", "Meaning": "Archive integrity, file hashes, decode and manifest completeness are checked and recorded."},
    {"Stage": "Visually inspected", "Meaning": "Record sampled frames versus full playback, observed defects and what was not inspected."},
    {"Stage": "Accepted for a scope", "Meaning": "The user accepts a stated role or take. A favorite or technical pass is not this decision."},
)

DISCOVERY = (
    "Name the project and exploratory lane. Hon Dolo / Strictly Business and Lisan Al Gaib / Meta Mirror retain separate identities and sources.",
    "Invent coherent tattoos, piercings, missing limbs, prosthetics or other features within the discovery brief; do not require approval before each idea.",
    "Deliver each new tattoo's body proof with a FOUR-OPTION standalone design sheet, label A–D, and identify the matching option. Supply its matching art separately when available; identify later reconstruction honestly.",
    "Expand a motif to 10–12 only on request. For the boss search, use five reviewed rounds of ten single proofs, followed by four views of the selected winner. The latest round-01 provider return still awaits verified local intake.",
    "Return actual files and a manifest. Proposed, received, inspected and accepted designs stay distinct; discovery does not silently establish a project-wide identity lock.",
)

PRESERVATION = (
    "Choose the current source and exact permitted change. Protect established details in Prime work; keep Multiverse Dolo variants labelled and excluded from Prime collaborator packages by default.",
    "Assign limited roles: identity, tattoo/detail, outfit, setting, composition, motion and audio. A wardrobe favorite cannot silently replace the face or revive a retired tattoo era.",
    "Keep missing source artwork explicit. Recovering an original, extracting an exact crop and inventing a replacement are separate tasks with separate provenance.",
    "Use the latest explicit selection, retain historical bytes and plan one comparison. For Flow 002, use the prepared silent six-second excerpt, not the full montage or an extra likeness reference.",
    "Compare matching moments and playback; record failures without promoting the take. Export the scoped decision for CFA to persist. Soundtrack replacement and lip-sync require separate checks.",
)
