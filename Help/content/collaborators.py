"""Portable teaching snapshot of CFA's October 8 collaborator handoff.

Includes the appended receipt dated 2026-10-09 01:45:08 UTC (October 8 local)
and the later October 9 teaching delta (CFA's POST_014508_DELTA.txt), adopted
on October 10, 2026. All evidence paths are relative to Help. Nothing reads
CFA or calls a provider. Provider roles describe this project's division of
work, not a quality ranking. Dated production states are source material,
not current operating facts.
"""

REVIEWED = "October 8, 2026 · receipt through October 9, 01:45:08 UTC · October 9 delta adopted October 10"
_CFA = "../../CFA/docs/notes/explorable_world/comfy/"
_PROJECTS = _CFA + "projects/"
_COLLAB = _PROJECTS + "collaborators/"
_HON = _PROJECTS + "hon_dolo_strictly_business/"
_LISAN = _PROJECTS + "lisan_al_gaib/"
_RETURN = _COLLAB + "panhandler_return_20261008.txt"
_DELTA = "../../CFA/docs/notes/explorable_world/pathfinder_handoff/claude_return_20261010/POST_014508_DELTA.txt"
_CASTING = _CFA + "casting/"

# CFA's canonical evidence vocabulary. The table below is Pan's learner-facing
# summary with attributed states; the definitions are owned and maintained there.
EVIDENCE_SOURCE = (
    "CFA templates/workflow_intake.md, section Evidence states (reviewed October 10, 2026)",
    _CFA + "templates/workflow_intake.md",
)

PROVIDERS = {
    "comfyui": {
        "name": "ComfyUI",
        "purpose": "Make a bounded, inspectable edit and compare the result with its actual source.",
        "how": (
            "Choose the job first: animate a still, change a video's appearance, replace its soundtrack, or match mouth motion. Each has different inputs and success checks.",
            "Carry an exact source ID, its allowed role, a saved workflow revision and the settings into a short Cloud test. Keep the original and a distinct output branch.",
            "Review matching moments and normal-speed playback. Record drift in face, tattoos, jewelry, motion and timing before promoting a take.",
            "Use the existing video handoff lesson for frame/FPS/audio assembly. CFA's local soundtrack preview preserved all 240 picture frames and timestamps; its Cloud graph was converted but not executed. A soundtrack swap does not change lip motion.",
            "Say which conditioning a recipe actually takes. The saved Seedance 2.5 candidate is first-frame only; the LTX-2.5 image-to-video graph starts from a still; a reference-image role is a different input. Decide whether the job is a new rendition, a targeted edit or an upscale before choosing the graph.",
        ),
        "boundaries": "CFA's native LTX motion test ran; sampled frames showed long blinks and smile drift, with acceptance pending. Both depth and Canny relight tests ran and failed detail preservation. The separate lip-sync candidate has not run. Through October 9, the Seedance 2.5 first-frame recipe is saved and reviewed but unexecuted, with Cloud availability, node schema and quote unverified, and the opening-shot benchmark has zero video turns. These measured limitations should shape the next test.",
        "sources": (),
        "evidence": (
            ("Comfy run states and observed defects", _COLLAB + "comfy_workflows.json"),
            ("Measured soundtrack replacement", _CFA + "workflows/hon_dolo_audio_replace_v001.README.md"),
            ("Seedance 2.5 first-frame candidate, saved and unexecuted", _CFA + "workflows/seedance_2_5_20261009.README.txt"),
            ("October 9 teaching delta, source of the dated lessons", _DELTA),
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
        "boundaries": "The October 8 receipt saw LAG500 parts 01–08, boss round 01 and Hon Dolo returns v001/v002 only at the provider. The October 9 delta then records verified local receipt: the Lisan 500 pack (500 unique sources, every hash and decode checked), the five-archive Hon return (115 unique files, 86 images) and the benchmark and mouth kits (117 unique files). All remain review candidates, not accepted masters. The 130-slot head library is the adopted standard with no full set yet received; the provider's later 150/170 counts and its report that all 50 mouth macros are complete are provider reports; Grok's approval claims are attributed reports, not local acceptance. For the opening-shot benchmark, as of October 10, the opening actor reference is lf_full (HD-RETURN-6c8900223ee9) with the mouth rule of that date: four gold upper caps on the lateral incisors and short canines, white central incisors, a lower silver/chrome grill and two plain lip hoops. LOCK-FACE (October 6 and 7) and the earlier component directions (October 4) are dated history, not inputs to replace.",
        "sources": (),
        "evidence": (
            ("Current creative and companion-art rules", _COLLAB + "grok_design_instructions.txt"),
            ("Boss discovery plan", _HON + "feedback/boss_discovery_20261008.txt"),
            ("Provider-visible returns and intake boundary", _RETURN),
            ("Verified October 9 Grok return", _HON + "grok_return_20261009/START_HERE.txt"),
            ("Reusable head standard and resolved grill", _COLLAB + "character_head_reference_standard.txt"),
            ("Current opening actor reference and scoped inputs", _HON + "handoffs/gemini_opening_continuation_20261009/START_HERE.txt"),
            ("October 4 component-based design review", _CASTING + "grok_intake_20261004/README.md"),
        ),
    },
    "gemini": {
        "name": "Gemini",
        "purpose": "Develop the story and shot ideas while keeping reusable project context and actual visual inputs distinguishable.",
        "how": (
            "Keep the shared CFA/Comfy methods notebook separate from the Hon Dolo and Lisan Al Gaib project notebooks. Their identities, tattoos, music and source roles remain separate.",
            "Record the effective model and actual attachments for every result. A chat attachment, a selected notebook text source and a successfully ingested visual-media source are different records. Bind each reference by stable ID plus exact filename; a picture number has meaning only inside the named upload batch that defined it, and local availability, actual attachment and approval stay separate.",
            "Inspect the source itself: does it open as usable text, image or video? Check failed entries separately from selected usable sources; do not use a model's acknowledgement as proof that it saw raw video frames.",
            "Return reusable findings through the project handoff. Shared-rule changes, cross-project digests and winner promotion remain manual decisions in this setup.",
            "Develop a preliminary panel into a proposed scene card: the narrative beat, action and camera, the scoped references by ID, start and end frame intent, a brief for any missing art, continuity notes and the execution prompt. Reuse existing footage before asking for more.",
            "Work the loop the method home defines: a primary creative result, a second pass that mines it for lessons, a reviewed master care package, then one relevant local follow-up. The general notebook, round and routing method lives in Nyquist (CFA's notebook_workflow/README.txt points to it); CFA's project application is notebook_workflow/START_HERE.txt; Pathfinder teaches it by link and adds no second copy of the machinery.",
        ),
        "boundaries": "The receipt verifies three notebooks, processed TXT imports, synced chat context and some chat attachments. Direct native MP4 Sources attempts and a JPEG retry failed. Lisan had 11 entries but only five usable selected sources: two TXT and three chats; six image entries failed. The October 9 delta adds one more native copied-text source success and one more native JPEG upload failure (\"This image content is not supported\"), leaving zero usable selected image sources. Persistent raw visual-media readiness remains unverified. T02 remains a scene working reference, not an identity standard.",
        "sources": (
            ("Google: notebook and chat context", "https://support.google.com/gemininotebook/answer/17003757?hl=en"),
            ("Google: source types and YouTube transcript import", "https://support.google.com/gemininotebook/answer/16215270?hl=en"),
        ),
        "evidence": (
            ("Notebook setup and failed-source receipt", _COLLAB + "gemini_notebooks_20261008/setup_status.json"),
            ("Latest context-versus-media finding", _RETURN),
            ("Native source test, October 8", _COLLAB + "gemini_notebooks_20261008/native_source_test_20261008.json"),
            ("Storyboard detail packets and workflow", _COLLAB + "storyboard_detail_20261009/START_HERE.txt"),
            ("Gemini cast attachment map (stable IDs, exact filenames, batch-bound picture numbers)", _CASTING + "gemini_cast_reference_map.txt"),
            ("Notebook workflow: CFA project application (method home is Nyquist)", _COLLAB + "notebook_workflow/START_HERE.txt"),
            ("Method-home breadcrumbs to Nyquist (HOLY_GRAIL.md, WORKFLOW_SPEC.md)", _COLLAB + "notebook_workflow/README.txt"),
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
        "boundaries": "Experiment 002 is prepared from retained GEM-5A115C59, the 41-second source: frames 244–387, 144 frames, six seconds, 1280 × 720 at 24 fps. The H.264 excerpt is re-encoded and silent; exact pixel preservation is not established. On October 8 a live attempt reached the Flow project's Agent, found an empty asset picker and stopped before upload, pending exact-payload approval; no Flow upload, generation, provider cost or acceptance is recorded through October 9. Record product, mode and model as separate fields: Flow is the workspace, Nano Banana an image-model family, Veo a video model. A longer montage is not evidence of better quality.",
        "sources": (
            ("Google: create video and assign references", "https://support.google.com/flow/answer/16353334?co=GENIE.Platform%3DDesktop&hl=en"),
            ("Google: projects and character assets", "https://support.google.com/flow/answer/16935308"),
        ),
        "evidence": (
            ("Where brief, files and prompt go", _COLLAB + "flow_start_here.txt"),
            ("Identity versus outfit/scene intake", _COLLAB + "flow_intake_20261008.txt"),
            ("Retained-source lighting experiment", _HON + "flow/second_video_experiment_20261008.txt"),
            ("Excerpt preparation measurements", _HON + "flow/video_test_002/manifest.json"),
            ("Delivery status: blocked before upload, October 8", _HON + "flow/video_test_002/delivery_status.json"),
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
    {
        "title": "Received, verified and reviewed are three different counts",
        "meaning": "October 9 delta. A package arrives as bytes; verification checks archive CRC, every hash and every decode; review looks at pictures with a scope. Provider QA notes travel with the files and are not a defect count. A CSV row or a chat acknowledgement is not pixels: deliver the selected files themselves. Long Windows paths are a tooling problem, not a naming problem: keep original names and provenance and use long-path-capable I/O rather than flattening or renaming.",
        "example": "The Lisan 500 pack: 50 nested ZIPs passed CRC, all 55 input hashes and 555 outputs verified, 551 images decoded, 500 unique sources. Grok reported 220 OK, 271 OK-note and 9 FLAG; 190 OK rows also carry comments. The nine FLAG images were the first review queue, not a removal list, and no identity lock changed.",
        "evidence": _LISAN + "grok_500_20261008/receipt_summary.txt",
    },
    {
        "title": "An outfit is a parent; a prop state is a variant",
        "meaning": "October 9 delta. Group gun and no-gun variants and angles under one outfit parent. Keep prop state (with, without, unspecified) separate from view and framing, and keep requested or reported states separate from visually verified ones.",
        "example": "Yellow keeps its existing album with known wardrobe source IDs; a hidden hip is unspecified, not without-gun. A media ID is reused only for exact SHA-256 duplicate bytes, with aliases and provenance kept; distinct takes keep their own IDs. Grouping deletes nothing and approves neither the old character nor the new hardware.",
        "evidence": _COLLAB + "grok_design_instructions.txt",
    },
    {
        "title": "A prop cue, a favorite, a requested working reference and an approved character differ",
        "meaning": "October 9 delta. A kept image can supply one transaction or object while its whole-look reference request stays REQUESTED. Carry the current identity anchor into the new brief; do not promote an old full character because one frame was liked.",
        "example": "The SB-03 pay-table still is marked keep for the luminous rectangular money Dolo handles. The planned money-handling brief uses the current Prime identity with that image only as prop evidence, preserving face, tattoos, grill and jewelry. A separate darts-and-bar idea in the same source item was preserved rather than overwritten.",
        "evidence": _HON + "feedback/review_decisions.json",
    },
    {
        "title": "Workspace, mode and model are three fields",
        "meaning": "October 9 delta. Name the product you are in, the mode it is set to and the model that actually ran. A provider's label for a model is a report until the runtime shows it.",
        "example": "Google Flow runs Nano Banana images and Veo video through separate modes. Comfy runs LTX and, as a saved candidate, Seedance. The image kit's ChatGPT Images 2.5 label was not verified for the available built-in route, so CFA preserves actual runtime labels instead.",
        "evidence": _COLLAB + "grok_image_benchmark_20261009/INTAKE_STATUS.json",
    },
    {
        "title": "First-frame conditioning is not reference-image conditioning",
        "meaning": "October 9 delta. A first-frame recipe fixes the opening picture and generates onward; a reference role conditions appearance without fixing a frame. Historical best-of-many image baselines are not matched one-shot model scores. New rendition, targeted edit and upscale are different requests.",
        "example": "Seedance 2.5 is saved as an unchanged official first-frame graph (five seconds, audio on) beside a local recipe for a future eight-second, audio-off comparison through Comfy Partner Nodes; its Cloud availability, live node schema, compiled inputs and quote remain unverified, so it is deferred and adds no run. An extension returns a new segment, not an automatically cumulative video.",
        "evidence": _CFA + "workflows/seedance_2_5_20261009.README.txt",
    },
    {
        "title": "A static pose sheet is not conditioning or training evidence",
        "meaning": "October 9 delta. Twelve mouth shapes on a contact sheet show what a provider drew; they prove nothing about temporal animation or a model's supported inputs. Hidden teeth stay unobserved rather than assumed.",
        "example": "The twelve mouth candidates and five rejected attempts were verified received. Independent review added two defects the provider had not reported: ball-ended rings on the AH shape and a lost lower silver grill on F/V. Open-mouth canine and cap geometry also differ between shapes. None is accepted.",
        "evidence": _COLLAB + "grok_image_benchmark_20261009/received/intake_receipt.json",
    },
    {
        "title": "A scene card says what exists and who executes next",
        "meaning": "October 9 delta. Separate concept art, production frames, missing art, available footage and the next execution owner on every card. Panel percentages are not song seconds until timing is aligned.",
        "example": "CFA prepared packets for the Hon and Lisan Gemini project notebooks covering Hon SB-01 to 04, S01A and S01B and Lisan LAG-SC-01 to 10, with scoped image bytes and per-scene planning prompts. Notebook 0 is meant to receive reviewed digests. Preparing a packet is not an upload: no upload, generation or stage promotion followed. The dated case for mapping before timing: Grok's 36-panel storyboard carried a 4:30 timing that conflicted with the 3:54.960 recording and reordered some lyric beats, so the panels were mapped semantically to the existing shot cards and no timing was overwritten; version-aware filenames keep that history (asset_review_20261007/README.md).",
        "evidence": _COLLAB + "storyboard_detail_20261009/START_HERE.txt",
    },
    {
        "title": "Observed scene versus inferred method",
        "meaning": "October 9 delta. A transcript or model breakdown of someone else's video records what was seen and what was guessed. The creator's toolchain, audio and exact cuts stay unverified unless the source says so.",
        "example": "The Lil Vader study captured a full AI Studio answer with 19 provisional sequence rows, six continuity rows and six limited spot-checks. The source page discloses AI but names no tool, and at 2:00 the picture is already end-screen cards, contradicting the model's final scene range. Three craft tests were proposed and none executed.",
        "evidence": _COLLAB + "video_studies/lil_vader_MwHocQFlw_c_20261009/START_HERE.txt",
    },
    {
        "title": "Editing is not extension; a starting frame is not a character master",
        "meaning": "October 9 delta. A ten-turn chain is one base plus up to nine verified native extensions, with no blind retries. A failed append or continuity check stops the chain, and only the longest passing cumulative take becomes the delivery master.",
        "example": "The opening continuation prototype prepares one Grok scene-frame request from three scoped references, then one short Gemini creation and dependent continuations. Multi-turn editing does not prove prefix-preserving extension. At the saved checkpoint there was no accepted starting frame and no video turn.",
        "evidence": _HON + "handoffs/gemini_opening_continuation_20261009/BENCHMARK.txt",
    },
    {
        "title": "One component preference becomes an explicit brief",
        "meaning": "October 4 review, adopted October 10. When the author likes one element of an image, write the brief that element implies: the component, its side in character terms (character-left or character-right, never inferred from another image), the exact source ID, what may change and what must stay. An archive of variants is not a render-batch request, and a reference role is assigned, not assumed.",
        "example": "CFA's October 4 Grok intake had 106 studies; Ziggy's screenshots selected a chest spacecraft, the Jabba tattoo and falcon bird (the first transcription's \"jaw\" was corrected to Jabba) and revised canine and grill details, not whole images. Those selections became preservation and change briefs with source IDs. The Chewie DJ studies used ape-like placeholder anatomy, a historical placeholder example rather than today's cast judgment.",
        "evidence": _CASTING + "grok_intake_20261004/README.md",
    },
    {
        "title": "A missing ID is a bookkeeping gap, not a missing picture",
        "meaning": "October 6 inventory, adopted October 10. Separate four things a filename cannot settle: a missing experiment ID versus a missing image; an exact duplicate versus a new option; a design anchor versus a pose or performance input; a higher frame rate versus coherent motion. A filename map is evidence of a mapping, not authority to select.",
        "example": "The October 6 drop held 297 images (268 unique) and 159 hash-named stills with no confirmed experiment ID; LOCK-FACE was the design anchor of that date, now history. Two silent clips at 12 and 24 fps were held stills and ghosted transitions, not a continuous walk. Recovering the ID-to-hash mapping stays CFA's bookkeeping.",
        "evidence": _CASTING + "grok_intake_20261006/README.md",
    },
    {
        "title": "Bind side, hand and occlusion to each reference",
        "meaning": "October 9 intake, adopted October 10. Every reference carries its visible hand, its character-side, the tattoo and jewelry it shows and what occludes them. A paper design sheet and an on-body layout are different artworks. Request a finite subset of props, angles and grill states, never the full product of all three.",
        "example": "Grok once assigned the hand tattoo to character-left by analogy to the holster; the recorded direction was character-right, and the correction asked for an explicit new source before any change. Matched head and mouth variants pair one state and view with external-off as the base and the iced external grill as an accessory.",
        "evidence": _COLLAB + "grok_coordination_20261009/002_delivery.json",
    },
)

EVIDENCE_STATES = (
    {"Stage": "Available / prepared", "Meaning": "An identified local source, recipe or brief exists; no upload or run follows from that."},
    {"Stage": "Requested / reported", "Meaning": "A feature was asked for, or a provider says it made or approved something. Neither establishes visibility, placement, receipt or acceptance."},
    {"Stage": "Uploaded / bound", "Meaning": "The provider's actual attachment is linked to its source ID, hash and allowed role."},
    {"Stage": "Usable source context", "Meaning": "The intended source opens and is selectable. Text context and raw visual ingestion are distinct checks."},
    {"Stage": "Validated", "Meaning": "A graph or request passes specified checks; generation and quality remain unproven."},
    {"Stage": "Executed / provider complete", "Meaning": "A job or return is visible at the provider. That does not prove a local download."},
    {"Stage": "Received locally", "Meaning": "Actual expected files/parts arrived; names alone do not establish integrity or completeness."},
    {"Stage": "Verified extraction", "Meaning": "Archive integrity, file hashes, decode and manifest completeness are checked and recorded."},
    {"Stage": "Visually inspected", "Meaning": "Record sampled frames versus full playback, observed defects and what was not inspected."},
    {"Stage": "Accepted for a scope", "Meaning": "The user accepts a stated role or take. A favorite or technical pass is not this decision. A reference target says what to aim at; an author-authorized tolerance says how much drift is kept without a reroll. Record both; a tolerance reopens no approvals and changes no feature count, material or scoped grill state."},
)

DISCOVERY = (
    "Name the project and exploratory lane. Hon Dolo / Strictly Business and Lisan Al Gaib / Meta Mirror retain separate identities and sources.",
    "Invent coherent tattoos, piercings, missing limbs, prosthetics or other features within the discovery brief; do not require approval before each idea.",
    "Deliver each new tattoo's body proof with a FOUR-OPTION standalone design sheet, label A–D, and identify the matching option. Supply its matching art separately when available; identify later reconstruction honestly.",
    "Expand a motif to 10–12 only on request. For the boss search, use five reviewed rounds of ten single proofs, followed by four views of the selected winner. The ten first-round boss proofs were verified received locally on October 9 and await selection; that is not completion of fifty characters.",
    "Return actual files and a manifest. Proposed, received, inspected and accepted designs stay distinct; discovery does not silently establish a project-wide identity lock.",
)

PRESERVATION = (
    "Choose the current source and exact permitted change. Protect established details in Prime work; keep Multiverse Dolo variants labelled and excluded from Prime collaborator packages by default.",
    "Assign limited roles: identity, tattoo/detail, outfit, setting, composition, motion and audio. A wardrobe favorite cannot silently replace the face or revive a retired tattoo era.",
    "Keep missing source artwork explicit. Recovering an original, extracting an exact crop and inventing a replacement are separate tasks with separate provenance.",
    "Use the latest explicit selection, retain historical bytes and plan one comparison. For Flow 002, use the prepared silent six-second excerpt, not the full montage or an extra likeness reference.",
    "Compare matching moments and playback; record failures without promoting the take. Export the scoped decision for CFA to persist. Soundtrack replacement and lip-sync require separate checks.",
    "Carry the current component rule, not the historical one. As of October 9, Hon's mouth is four upper gold caps (laterals plus short canines), white central incisors and a lower silver grill; external-off is the base state and the iced external grill an optional accessory. The old two-canines wording is history. A head library is a set of reusable views; its breadth is not conditioning capacity or temporal validation.",
)
