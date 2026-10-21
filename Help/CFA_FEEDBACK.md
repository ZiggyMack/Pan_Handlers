# Nova → Pathfinder

## Pathfinder to CFA - Gemini clip-scoped notebook context adopted, October 20, 2026

CFA's October 14 intake (`pathfinder_handoff/gemini_clip_context_20261014/TEACHING_RETURN.txt`, registered in [CFA_TUTORIAL_LEDGER.md](CFA_TUTORIAL_LEDGER.md) under "October 14 intake: Gemini video context and clip-specific source scope") asked for one short attributed lesson: notebook source context contributed to a Gemini video in the Bellglass test, and Ziggy's immediate refinement is to scope active sources to the exact clip. Adopted by Claude, Pan_Handlers Master Repo steward, on Ziggy's go in the October 20 session (in substance: the note about what we learned flowing back into Pan Handlers is to be done too). The dated facts come from CFA's `HUMAN_REVIEW_20261014.json`, `RESULT.json` and `technical_review/TECHNICAL_REVIEW.json` for run `472f240d`; the operating rule is CFA's `notebook_workflow/GEMINI_CLIP_SOURCES.txt`, taught by link. Nyquist keeps the general notebook method; CFA keeps its project application; Pan adds no second copy.

### Pages and lessons adopted

| In Pathfinder | Change and owner |
| --- | --- |
| **Collaborators > 02 / Preserve or explore** | New dated lesson in [content/collaborators.py](content/collaborators.py): *Notebook context can reach the clip; scope it to the clip* (October 14 intake, adopted October 20). It states the finding with its caveat (no guaranteed inclusion of every source, no persistent raw visual-media ingestion, no known renderer internals, no tested reliability); Ziggy's refinement (load only what is pertinent to the exact clip, not the whole scene) kept separate from CFA's operating decision drawn from it (full story kept separately; clip pack = approved excerpt plus necessary continuity, actor direction, lighting, camera and background; verify which sources are actually active; repeat critical requirements in the prompt; a fresh chat is no proof of source isolation); and cross-references the existing reference-scope lesson *Bind side, hand and occlusion to each reference* and the prompt and video lessons under 03 / Continue a lesson. Its evidence link is CFA's operating note `notebook_workflow/GEMINI_CLIP_SOURCES.txt`. |
| **Collaborators > 01 / Role & handoff** (Gemini) | Step 7 is a one-sentence pointer to the lesson (no second copy of CFA's operating steps). The boundaries paragraph gains one dated sentence: the October 14 Bellglass clip is a text source contributing to a video result, distinct from the unverified raw visual-media ingestion recorded on October 8 and 9. Three evidence links added under Source records: the operating note, the clip-pack template `source_packet/CLIP_SOURCE_PACK.template.txt` (not uploaded or executed) and `HUMAN_REVIEW_20261014.json`. The snapshot line `REVIEWED` and the module docstring now name the October 14 intake adopted October 20. |
| **Workflow lab > Video & audio** (the same shared video handoff is shown inside Collaborators > 03 / Continue a lesson and Video workshop) | [guides/video_handoff.py](guides/video_handoff.py): one sentence appended to the dialogue caption cross-referencing the new lesson: scope a provider notebook's active sources to the exact clip and judge picture, motion and audible sound separately. No new stage row. |
| [CFA_TUTORIAL_LEDGER.md](CFA_TUTORIAL_LEDGER.md) | The October 14 section's Status line now reads adopted with the lesson link; the section's earlier text is unchanged. |

### Corrections preserved

- Dated states stay dated. One 10-second 1280 × 720, 24 fps, 240-frame H.264/AAC clip from one submission, no retries, no regeneration. The prompt omitted dog, collar and bark; those cues lived only in one verified copied-text source (readback matched before submission). Ziggy confirmed the dog and a quick bark-like head motion and called the unmoving mouth a minor defect; the vivid blue/cyan collar is visible in CFA's six sampled frames (RESULT.json) and is not part of his recorded review. Audible barking is not separately confirmed: the audio stream decodes but no listening was performed. Which source details get used, and whether the renderer reads sources directly or through prompt assembly, remain unknown or unexposed.
- The older Gemini caveats stand: text and chat context are distinct from raw visual-media ingestion; usable selected image sources remained zero as of October 9; nothing here upgrades that.
- Source-bleed prevention is Ziggy's operating direction, not a measured comparison; the lesson says so. Lyrics guide meaning and cuts; unassigned singing or mouthing is not required.
- Ownership as agreed October 10: CFA owns production inputs, notebooks, account operations, runs, receipts and acceptance; Nyquist owns the notebook, round and routing method; Pan teaches by link with one maintained general source and attributed dated examples. No Nyquist methodology, CFA media, production approval state or notebook-account operation was copied into Pathfinder.

### Verification and remaining ownership

`python -B -m unittest discover -s tests -q` from `D:\Documents\Pan_Handlers`: 70 tests passed (OK in 98.5 s; 69 before the change plus one new) (one new check in `tests/test_collaborators.py` asserts that the lesson is present exactly once and that its evidence path is CFA's `notebook_workflow/GEMINI_CLIP_SOURCES.txt`). `py_compile` passed for `content/collaborators.py`, `guides/video_handoff.py` and the test file. The three new evidence paths exist in the adjacent CFA checkout; the app still never reads them at runtime. No schema, page or state file changed; no media copied; no provider job, upload, notebook or account operation; no commit, push or deployment.

Learner-facing adoption claims nothing about CFA production state: CFA's technical review records acceptance as not inferred and Ziggy's accepted scope is the notebook-context finding, not the clip as a take; the missing mouth articulation is a recorded defect, not a regeneration order (automatic regeneration not authorized); the clip-pack template is unfilled and unexecuted; the next clip's source selection, prompt, run and human listen remain CFA's work. The same adoption summary was returned to CFA's handoff map (`pathfinder_handoff/README.md`) as one dated paragraph appended under a SHA-256 guard on its prior bytes; `evidence.json` there is the September pump manifest and was not touched.

## Pathfinder to CFA - Briefing #002 synchronization adopted, October 10, 2026

CFA Nova's disposition of Briefing #002 (mailbox message `0a6263b2`; full text in CFA `pathfinder_handoff/pan_cfa_sync_20261010/NOVA_REPLY_002.txt`) accepted the Pan/CFA split with two qualifications, said yes to all seven ownership proposals with concise CFA-local fallbacks, corrected the CFA-side stale spots herself, triaged the seventeen open follow-ups (1–5 L, 6 H, 7–15 L, 16 L pending matched service takes, 17 L; 13 L for the learning loop and P for courier operations) and agreed the cadence. This return records the Pan side of that agreement; the dated status table lives in [CFA_TUTORIAL_LEDGER.md](CFA_TUTORIAL_LEDGER.md) under "October 10 synchronization with CFA Nova".

### Pages and lessons adopted

| In Pathfinder | Change and owner |
| --- | --- |
| **Collaborators > 02 / Preserve or explore** | Three new dated lessons in [content/collaborators.py](content/collaborators.py): *One component preference becomes an explicit brief* (item 5), *A missing ID is a bookkeeping gap, not a missing picture* (items 7 and the filename-map half of 8) and *Bind side, hand and occlusion to each reference* (item 14). The counts lesson gains pixels-versus-CSV and long-path wording (item 11); the scene-card lesson gains the 4:30-versus-3:54.960 worked case (item 10). |
| **Collaborators > 01 / Role & handoff** | Gemini step 2 binds references by stable ID, exact filename and batch-bound picture number with the cast map linked (item 9); Gemini step 6 teaches the result → lesson-mining → master-package → follow-up loop by link to Nyquist's method home and CFA's `notebook_workflow/START_HERE.txt` (item 13, link only). The evidence-state table now cites CFA `templates/workflow_intake.md`, section Evidence states, reviewed October 10, as the canonical definitions and calls Pan's rows a learner-facing summary (3f); *Accepted for a scope* distinguishes a reference target from an author-authorized tolerance (item 15). The Grok boundary names the October 10 opening actor reference `lf_full` (HD-RETURN-6c8900223ee9) and that date's mouth rule, with LOCK-FACE and the October 4 component directions as history. |
| **Workflow lab > Video & audio**; **Rewrite a scene > Understand the target** | [guides/video_handoff.py](guides/video_handoff.py): fourth stage row for the October 8 mouth-continuity plan, not executed (item 12); the inspect-the-streams lesson from the October 4 media intake (item 4); two dated research rows for LTX-2.5 audio-to-video and Dub-It plus Sync's bounce-versus-cut_off note, with the production plan linked (item 2); a frame-rate-is-not-motion sentence on the timing desk (item 7); a cross-reference to the Lil Vader case (item 17). |
| **Workflow anatomy > Save & load** | [guides/workflow_files.py](guides/workflow_files.py) now carries the consolidated readback lesson: the October 4 stale named-widget incident and the October 7 dropped-prompt conversion repair, in the expander and the downloadable checklist (item 8 and 3c). |
| **Controlled experiment** operating steps | [guides/workflow_decision.py](guides/workflow_decision.py) caption cross-references the observed-versus-inferred lesson (item 17). |
| **Video workshop** | [content/video_routes.py](content/video_routes.py): production plan in SOURCES, Wan Mix SAM2/pose and export-FPS trap as dated research (item 2), four finishing kinds and the H3 Regenerate-to-2K order in FINISHING (item 3). [content/h3_candidate.py](content/h3_candidate.py): the empty-input starter of October 4, the October 9 deferred native I2V lane distinguished from this R2V recipe, and the 2K step (items 2 and 3). [pages/video_workshop.py](pages/video_workshop.py) 03 / Preview & compare cites the October 4 image-to-video take as the worked review example (item 1). |
| [CFA_TUTORIAL_LEDGER.md](CFA_TUTORIAL_LEDGER.md) | Creative Studio locator corrected to `algaib` in the October 8 paragraph with the date preserved; new follow-up status table (open / adopted / closed) for the seventeen items. Item 6 closed as historical; item 16 open until matched service takes exist. |

### Corrections preserved

- The split: CFA owns production inputs, graphs, runs, receipts, acceptance and the evidence definitions; Pan owns general route selection, teaching and navigation; one maintained general source plus concise CFA-local fallbacks and attributed dated examples, no runtime dependency either way.
- Nyquist owns the notebook, round and routing method; CFA its project application; Pan teaches by link. Recorded in CFA's handoff map as one paragraph inside the existing October 10 section.
- Dated states stay dated: nothing adopted here claims a run, upload, acceptance or current availability that the sources do not record. Current Studio availability was not rechecked.

### Verification and remaining ownership

`python -B -m unittest discover -s tests -q`: **69 tests passed** after the change, the same count as before. All nine changed modules compile; the soundtrack, handoff and save/load Markdown exporters render. A read-only reviewer compared every adopted sentence with the ledger, the delta, CFA's benchmark files and Nova's triage; it confirmed all seventeen placements and the four corrections and caught two wording slips, both fixed (a transcription error CFA had corrected to Jabba, and a wrong host pointer in the status table). No schema, state or test file changed; no media copied; no commit, push or deployment.

Deferred maintenance, agreed as bounded follow-ups: pointing the five other Pan mentions of the stale-widget incident at Save & load; replacing the connector version in `guides/cloud_access.py` with a dated CFA pointer; thinning count prose in `README.md` and `CFA_HANDOFF.md` to pointers at `cfa_learning`. CFA's operational work named in the disposition stays CFA's.

## Pathfinder to CFA - October 9 teaching delta adopted, October 10, 2026

Read the [October 9 delta](../../CFA/docs/notes/explorable_world/pathfinder_handoff/claude_return_20261010/POST_014508_DELTA.txt) (35,999 bytes, SHA-256 `def32c638ac5c548097f22188bde74103a82138d7b2e30fe0543862f4cb1e05a`), which CFA Nova posted to Pan's REPO-SYNC inbox and which is dispositioned at `REPO-SYNC/SYNC_IN/processed/2026-10-10_nova_cfa_teaching_delta.md`. Adopted by Claude, Pan_Handlers Master Repo steward, with Ziggy's go in the active session. CFA retains receipts, media, graphs, provider operations and acceptance. The delta's dated production states are source material, not current facts; later production progress needs a new dated evidence return.

### Pages and lessons adopted

| In Pathfinder | Change and owner |
| --- | --- |
| **Collaborators > 02 / Preserve or explore** | Nine dated October 9 lessons in [content/collaborators.py](content/collaborators.py): received versus verified versus reviewed counts; outfit parents and prop states; prop cue versus favorite versus requested working reference versus approved character; workspace, mode and model as three fields; first-frame versus reference-image conditioning; static pose sheets versus supported conditioning; scene cards naming what exists and who executes next; observed scene versus inferred method; editing versus extension and starting frame versus character master. The Preserve list gains the October 9 mouth rule; the Explore list records that the ten first-round boss proofs are verified received and await selection. |
| **Collaborators > 01 / Role & handoff** | ComfyUI gains a conditioning step and the Seedance evidence link; Grok boundaries record the October 9 verified local receipts and two new evidence links; Gemini gains the scene-card development step, the native-source test and storyboard packets; Flow records product, mode and model as separate fields. The evidence-state table gains **Requested / reported**. |
| **Start here**, **Video workshop > Where we actually stand**, **Sources & roadmap** and tutorial evidence | [content/cfa_learning.py](content/cfa_learning.py) adds five dated status rows (verified Grok returns, Seedance first-frame candidate, opening-shot benchmark, head library and mouth standard, all October 9; and the October 8 mouth-continuity plan carried in the delta), updates the *Finishing and video* row, and adds three lessons: first-frame versus reference conditioning; a verified archive as a review candidate; ten turns as one base plus verified extensions. |
| [FILE_MAP.md](FILE_MAP.md) | Collaborators and cfa_learning descriptions name the October 10 adoption. |

### Corrections preserved

- **Grok:** the Lisan 500 pack, the five-archive Hon return (115 unique files, 86 images) and the benchmark and mouth kits (117 unique files) are verified received locally as of October 9; the October 8 provider-visible-only wording is historical. All remain review candidates. The 130-slot head library, the provider's 150/170 proposals and the 50 reported mouth macros are provider reports; Grok's approval claims are attributed reports.
- **Gemini:** one more native copied-text source succeeded and one more native JPEG upload failed; usable selected image sources remain zero. T02 is still a scene working reference.
- **Flow:** no upload, generation, cost or acceptance through October 9. Flow is the workspace; Nano Banana is an image-model family; Veo is a video model.
- **Comfy:** the Seedance 2.5 first-frame recipe is saved and reviewed but unexecuted and deferred; the opening-shot benchmark is prepared with zero video turns and no accepted starting frame; no new run, master or acceptance exists.
- **Hon mouth rule:** four upper gold caps (laterals plus short canines), white central incisors, lower silver grill; external-off base, iced external grill optional; the two-canines wording is historical.

### Verification and remaining ownership

`python -B -m unittest discover -s tests -q`: **69 tests passed** after the change, the same as the baseline run before it. Both modules compile. All new evidence paths (thirteen distinct, fourteen new references in collaborators.py) exist in the adjacent CFA checkout. No schema, page or test file changed; the Collaborators page and its download render the new entries through their existing loops. No production media copied, graph edited, provider task executed, commit, push or deployment.

CFA's next operational checks remain the nine FLAG images and 75 hero candidates in the Lisan pack, selection from the first boss round, the Seedance Cloud preflight, the opening-benchmark starting still and first service takes, the mouth-continuity proofs and the head-library receipt. This return documents adopted teaching, not those tasks. The same adoption summary was inserted into [CFA's handoff map](../../CFA/docs/notes/explorable_world/pathfinder_handoff/README.md) under a SHA-256 guard on its prior bytes.

### Same-day addendum: route cards now carry CFA evidence

A read-only comparison of both checkouts (three lenses: unadopted follow-ups, duplicated method prose, route-status drift) found that the route cards learners see first still showed October 2 research labels although CFA had since executed, preflighted or prepared several of them. Fixed in [content/video_routes.py](content/video_routes.py): every route has an `evidence` string (what CFA actually did, by record name; empty where CFA has not touched the route); the image-to-video card is labelled executed once on October 4 with acceptance pending and its caveat carries the measured defects; the Union Control card records the negative October 4 Cloud preflight and the LTX-2.3 IC-LoRA sibling that actually ran on October 7 and failed preservation; the dialogue card records the Sync editor prepared on October 7; hosted Seedance 2.5 first-frame is an image-to-video alternative. [pages/video_workshop.py](pages/video_workshop.py) renders that evidence beside the kind with the `cfa_learning` review date and labels the October 2 date as the documentation check; its woman-and-wolf preset now points at the CFA receipt instead of carrying the clip hash. [pages/start_here.py](pages/start_here.py) renders the snapshot's review date and first sentence instead of a hard-coded October 8 caption. [content/collaborators.py](content/collaborators.py) adds Flow's `delivery_status.json` (blocked before upload, October 8) and the still-lane gate for the opening benchmark. **69 tests passed** after these changes. The comparison's remaining findings (seventeen open follow-ups from CFA's October 4–9 returns, seven duplicated passages with proposed owners, two CFA-side stale spots) are in `REPO-SYNC/MASTER_REPO_SYNC_OUT.md`, Briefing #002, awaiting CFA Nova's triage.

## Pathfinder to CFA - Collaborators debrief adopted, October 8, 2026

Read the [October 8 return](../../CFA/docs/notes/explorable_world/comfy/projects/collaborators/panhandler_return_20261008.txt), including **CURRENT DEBRIEF, October 9 01:45:08 UTC** (October 8 locally). That append supersedes earlier preparation-only Grok states and qualifies Gemini source intake. Adopted the bounded teaching work below; CFA retains actual receipts, media, graphs, provider operations and acceptance. Later provider arrivals will need a new evidence return rather than automatic changes to this static snapshot.

### Pages and lessons adopted

| In Pathfinder | Change and owner |
| --- | --- |
| **Collaborators** in the sidebar / embedded dashboard | New [page](pages/collaborators.py) and [teaching data](content/collaborators.py), with ComfyUI first, then Grok, Gemini and Google Flow. This is the explanatory counterpart to CFA's operational Collaborators workspace. |
| **01 / Role & handoff** | Practical steps, sources and evidence states for the selected collaborator. Separate available/prepared, uploaded, usable source context, validated, provider-complete, received, verified, inspected and accepted. Local evidence paths are labels; the app does not read CFA. |
| **02 / Preserve or explore** | Prime preservation versus creative discovery; separate Hon/Lisan projects; limited reference roles; favorites and approval scope; exact crops versus generated reconstruction; honest artwork lineage; finite boss rounds; newer explicit source choice over historical stars; selection metadata versus actual media; durable review exports. |
| **03 / Continue a lesson** | Reuses the existing image/reference, controlled-comparison, prompt-composition, save/open-workflow and video/audio lessons. Buttons return to Video workshop and Field journal. Provider/lane/lesson choices survive navigation without changing saved schemas. |
| **Video & audio**, including Collaborators; **Rewrite a scene > Understand the target** | [video_handoff.py](guides/video_handoff.py) now supplies a shared dated soundtrack case to both screens and their Markdown guides: local stream copy, Cloud decoded-frame assembly and lip-sync have separate effects and evidence. |
| **Start here**, **Video workshop > Where we actually stand**, CFA tutorial evidence and Sources & roadmap | [cfa_learning.py](content/cfa_learning.py) now records executed image-to-video and depth/Canny tests, their defects/review limits, the measured local audio swap and unexecuted Cloud/lip-sync paths. Older still-workflow examples retain their October 4 scope. |

### Corrections preserved

- **Production progress:** video experiments have executed. The native motion candidate remains unaccepted; depth/Canny relights failed the strict lighting-only preservation brief. Matching timestamps and successful decoding do not establish unchanged identity, mouth motion or fine details. For lighting-only work, grading/compositing is a candidate worth evaluating before another full generative reinterpretation.
- **Sound:** the local ten-second soundtrack proof preserved compressed picture packets and all 240 decoded frame hashes/timestamps. Cloud version 2 is saved/server-converted, not executed; its frame-assembly route re-encodes. Lip-sync is a separate unexecuted candidate. Whole-track replacement also removes ambience; changing the recording requires timing review even when the written words match.
- **Grok:** LAG500 parts 01-08, boss round 01 and Hon v001/v002 are provider-visible in the latest receipt; local receipt, archive/file verification and acceptance are not established there. Earlier "not generated" boss wording is historical. The discovery plan still uses reviewed rounds before a winner turnaround. New tattoos require the four-option standalone companion sheet in the same delivery, with the matching body-proof option identified. No blanket stencil-first approval gate was added; existing Prime detail preservation remains separate.
- **Gemini:** configured notebooks, TXT sources, selected chat context and successful chat attachments do not establish persistent raw visual-media ingestion. The receipt's Lisan notebook has 11 entries but only five usable selected text/chat sources; six failed image entries are not usable visual evidence. YouTube transcript import is not raw-video ingestion. Cross-project digests, rules and winner promotion remain manual.
- **Flow:** the proposed lighting experiment uses the retained 41-second GEM-5A115C59 source, frames 244-387, 144 frames / six seconds / 1280 x 720 / 24 fps, re-encoded and silent. Upload, run, provider cost and acceptance remain unclaimed. Explicit retained-source corrections supersede older stars without deleting historical bytes or declaring different files pixel-identical.
- **Source roles:** thirteen stencil-named helpers are opaque crops/placement sheets, not verified transparent originals. Exact Luke/Leia/Han crops preserve source pixels and remain likeness inputs; they do not redefine Hon's tattoo/identity anchor. A liked outfit, a detail reference and an accepted complete character have different scope. Multiverse Dolo stays outside Prime packages by default.

### Verification and remaining ownership

**69 tests passed** with `python -m unittest discover -s tests -q`. The new interaction check visits all collaborators and reused lessons, restores selected provider/lane/prompt after navigation, and confirms the existing journey and video plan are unchanged. The existing suite now visits Collaborators in both themes and the embedded dashboard. Independent review checked the latest debrief state and audio/export boundaries. Module compilation and local provenance/document link checks supplement those tests.

Journal v1 and video-plan v1 are unchanged. The new Markdown download is teaching notes and source references only: not a media ZIP, selection list or CFA review-state export. No production media was copied, no provider jobs/uploads were performed, and no CFA graph or acceptance decision changed. The app remains usable without CFA or credentials. Changes are local; no commit, push or deployment was performed.

CFA's next operational checks remain receipt/verification of returned packages, honest handling of failed visual Sources, selection of a bounded Flow/Comfy experiment and explicit review of actual outputs. This response documents adopted teaching rather than claiming those tasks completed. The [ledger](CFA_TUTORIAL_LEDGER.md), [README](README.md) and [file map](FILE_MAP.md) now identify the new page; the same adoption summary was returned to [CFA's handoff map](../../CFA/docs/notes/explorable_world/pathfinder_handoff/README.md) with a SHA-256 guard. Verification confirmed all earlier map bytes were preserved.

## Pathfinder to CFA - PH TUT 01-06 implementation, October 4, 2026

Nova's eight-resource handoff now feeds Pathfinder's teaching screens and comparison exercises. The folder reorganization is retained: `Help/app.py` remains the deployment entry, `pages/` owns sidebar screens, and shared lessons/content/state stay in their respective directories. [FILE_MAP.md](FILE_MAP.md) is the current navigation-to-code map; [CFA_TUTORIAL_LEDGER.md](CFA_TUTORIAL_LEDGER.md) records dated done/deferred results.

### Find the integrated lessons

| Learner destination | What is implemented | Main files |
| --- | --- | --- |
| ComfyUI guide > 03 / Workflow anatomy > Tutorial notes | Eleven guide choices, including episodes 5-8, H3 and video comparison; 25 new timestamp annotations. The eight-resource register exports archive paths, SHA-256, byte counts, source URL/basis and review date. Episode 3/4 annotations are reused. | [tutorial_notes.py](guides/tutorial_notes.py), [tutorial_register.py](content/tutorial_register.py), [tutorial_followups.py](content/tutorial_followups.py), [episode_three.py](content/episode_three.py), [episode_four.py](content/episode_four.py) |
| Workflow anatomy > Node map > Beyond two prompts; Node Atlas > Recipes > Compose and inspect prompt text | Shared raw words with separate encoders, STRING concatenation versus ConditioningConcat, model-specific negative behavior, optional style off by default, exact text preview/download. The atlas now has 24 curated node types and six recipes, not a census of installed nodes. | [prompt_wiring.py](guides/prompt_wiring.py), [node_atlas.py](guides/node_atlas.py) |
| Workflow anatomy > Controlled experiment > A/B/C plan; Workflow lab > Image to image > Compare edits | Existing planners now carry optional problem/source/rationale/success fields, actual compiled settings and evidence state, output/error/result and next decision. Planned tables remain distinct from self-reported outcomes. | [workflow_decision.py](guides/workflow_decision.py), [sampling_lab.py](guides/sampling_lab.py), [image_edit_lab.py](guides/image_edit_lab.py) |
| Workflow lab > Control guide; Workflow anatomy > Save & load / Controlled experiment > Shared controls | Copy a complete sampler/decode/save branch, preserve shared versus changed controls, use distinct prefixes, mute unwanted terminal outputs, distinguish input previews from generated pixels and save actions, inspect compiled values, reopen actual editor JSON. | [workflow_controls.py](guides/workflow_controls.py), [workflow_files.py](guides/workflow_files.py), [shared_controls.py](guides/shared_controls.py) |
| Video workshop > 01 / Choose the route > Where we actually stand; Tutorial notes > Spanish creator / NKD > CFA evidence | Paired Civitai comparison v4 and SDXL refinement v2 with exact Cloud/reconstruction links and limits. Stale named-widget metadata is now an explicit compiled-input lesson. | [cfa_learning.py](content/cfa_learning.py), [creative_control_guide.py](content/creative_control_guide.py) |
| Video workshop > 01 / Choose the route > Additional candidate - MiniMax H3 reference roles; Workflow lab > Video & audio | Optional native R2V research checklist, exact documented dependencies, appearance/performance/audio roles, audio reuse versus reference, current-workspace checks. Downloadable checklist; no automatic route selection or readiness claim. | [h3_candidate.py](content/h3_candidate.py), [video_workshop.py](pages/video_workshop.py), [video_handoff.py](guides/video_handoff.py) |
| Video workshop > 03 / Preview & compare and 05 / Relevant lessons | Connect the creator model-comparison lesson to the existing take-review notebook. New quick entries open the tutorial register at Episode 8 or prompt-composition practice. Keep each take's own recipe and settings rather than equalizing incompatible model controls. | [video_workshop.py](pages/video_workshop.py) |

### Evidence and unresolved work

- All eight archived transcript hashes/byte counts were checked against CFA's manifest. Episode 3's existing URL was corroborated by indexed primary YouTube title/channel and transcript topics; [Episode 8's URL](https://www.youtube.com/watch?v=ImWHS5Ux36E) was recovered from Pixaroma metadata and matching chapters. Neither claim represents independent playback. H3 and comparison creator URLs remain unresolved; return a source receipt when available. CFA's original manifest remains unchanged.
- Paired comparison v4 and SDXL refinement v2 remain **validated, not rendered**. Earlier separate stills remain **unaccepted**. Main v6 control checks, the input-only executed graph and original rendered v2 remain distinct. Shared-catalog LoRA execution still does not verify a new authenticated Civitai import.
- H3 is **untested** here. The [official native recipe](https://docs.comfy.org/tutorials/video/minimax/minimax-h3-native) and [reference-role guide](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md) inform the checklist; a catalog title does not establish its exact graph, node schemas, accessible weights, output fidelity or cost. Native and hosted/API recipes remain distinct. CFA must verify its actual workspace, save/inspect the graph and compiled inputs, and validate before a bounded preview. No automatic H3 route or video-plan schema migration was added.
- Production remains CFA's responsibility: review the existing clean identity candidate before decorating it; choose and document one purposeful comparison when ready. For the first source-video test, inspect and trim the source, select the exact supported workflow, resolve remote dependencies and inspect effective settings, then record the bounded run and matched-timecode preservation review. H3 is one possible alternate candidate, not a prerequisite or a proven improvement.

### Validation and handoff

`python -m unittest discover -s tests -q`: **68 tests passed**. Checks cover standalone and embedded navigation, journal/video-plan round trips, scoped source selectors, style opt-in and literal prompt exports, typed connections, comparison decision/outcome exports and persistence, and the new Video workshop lesson entries without mutating the plan or journal. An independent code review caught fixed Markdown fences around pasted prompts; exports now choose a longer fence so literal backticks remain text.

The app stays offline-capable and credential-free; source archive paths are provenance labels, not runtime reads. New prompt and comparison notes survive navigation in the current session and have separate downloads; they are not silently added to journal v1 or video-plan v1. Existing exports and examples remain compatible. No Comfy jobs, account operations, model downloads or production graph edits occurred. Changes are local; this work does not commit, push or deploy either repository.

PH TUT 06 is complete: feedback, ledger and the [CFA handoff map](../../CFA/docs/notes/explorable_world/pathfinder_handoff/README.md) now record the same navigation and remaining work. The map update was prepared locally and guarded by its original SHA-256 before writing; its existing content is preserved. Python compilation, local documentation targets and whitespace checks also passed. The earlier CFA/September entries below are retained as historical records.

## Tutorial return October 4 2026

At Ziggy's request, CFA Nova returned the current tutorial learning to [CFA_TUTORIAL_LEDGER.md](CFA_TUTORIAL_LEDGER.md), with links from [README.md](README.md) and [CFA_HANDOFF.md](CFA_HANDOFF.md). It covers episodes 3–8, MiniMax H3 and the video-model comparison resource, links canonical transcript hashes and production recipes, and assigns six scoped follow-ups to Panhandler Nova. General learning remains in Panhandlers; production assets and records remain in CFA.

This contribution adds documentation and a standing manual handoff process. It changes no Python module, app route, journal schema, Comfy workflow, model or generation job. Existing episode 3/4 teaching was reviewed and reused by reference. Episodes 5–8 integration, prompt composition, H3 candidate teaching and the newer production snapshot remain open tasks. The paired comparison v4 and SDXL refinement v2 are validated but not rendered; previous reference-edit candidates remain unaccepted.

Validation for this transfer: target-file hashes checked before replacement, local source and module links checked, and documentation diff/whitespace reviewed. The application test suite was not run because no application code changed. A future functional integration should run the relevant existing tests and report the new learner navigation back to CFA. The September response below is preserved as historical evidence.

> **File-location note — October 4, 2026:** this response preserves the September evidence and filenames. Pathfinder has since moved page renderers into `Help/pages/`, lessons into `Help/guides/`, teaching data into `Help/content/`, plan/journal logic into `Help/state/`, and presentation into `Help/ui/`. See [FILE_MAP.md](FILE_MAP.md) for current locations. The app still launches from `Help/app.py`; example assets retain their paths.

September 12, 2026 · for Ziggy and future learners

I reviewed Pathfinder against **`D:\Documents\CFA`, branch `main`**, at HEAD
`710360d322e2d9725087fb3d501449272150f4b3`, including ongoing uncommitted work.
That commit alone does not contain the experiment. I preserved the existing
Pan Handlers edits and kept production execution in CFA.

## What CFA adds

Pathfinder already provides a useful map of the four paths and a practical scene
worksheet. The missing teaching bridge was **an actual result someone can inspect
beside its recipe and the decisions it caused**. A connected account, available
model, completed generation and acceptable result each answer a different question.

The handoff's opening refers to actual video animation work. Our evidence is more
limited: CFA has completed **one pump concept still** and separately built an
authored Godot chapter. We have no source-video/dialogue rewrite, generated speech,
lip-sync result or improved second generated image to present as a success.

The [CFA evidence index](../../CFA/docs/notes/explorable_world/pathfinder_handoff/README.md)
and its [hash manifest](../../CFA/docs/notes/explorable_world/pathfinder_handoff/evidence.json)
identify the canonical artifacts. The [portable sample](examples/cfa_pump_v001/README.md)
includes the actual [PNG](examples/cfa_pump_v001/pump_concept_v001.png), prompt,
editor/API graphs and run record, so future readers do not need this machine.

The image communicated its palette and service panel, but was too pristine and
slender to express the intended history of repair. CFA subsequently authored
repair details in Godot. The observed OAuth failure recovered after a fresh login
and a successful read-only check; replacing the Civitai key was not the remedy.
Actual GPU runtime and attributable credits remain unknown. Saved template
versions are distinguished from unknown deployed versions and model revisions.

## Focused changes

- **A worked example:** ComfyUI guide → **06 / Worked example** shows brief,
  output, critique and reproducible settings, with separate editor/API downloads
  and an evidence ZIP. It points out the saved graph's randomized seed control:
  explicitly restore seed 42 and fixed control for a controlled comparison.
- **A concrete scene rehearsal:** Rewrite a scene now offers a proposed
  eight-second Observatory script, source/rewrite beats and preservation/rejection
  criteria. It separates script, voice, lip sync, editing and sound. The downloaded
  guide retains this material, execution alternatives and failure recovery.
- **Better timing and handoffs:** timing compares the entire replacement WAV,
  including silence, and fixes a floating-point error at the 0.1-second boundary.
  Cloud instructions check existing models first, reuse saved access, and prepare
  one timely browser-import request with an exact file and completion signal.
  CFA's first authenticated Civitai import is still untested.

Changed guide files: `console.py`, `cloud_access.py`, `scene_content.py`,
`scene_lab.py`, `README.md`; added `worked_example.py`, the seven files in
`examples/cfa_pump_v001/`, and this response. Changed
`tests/test_help_console.py` only to match the clarified warning; added
`tests/test_scene_rehearsal.py` and `tests/test_worked_example.py`.

AUTOMATIC1111, Forge, Invoke/InvokeAI and ComfyUI remain visible. The SDXL +
Checkpoint + SafeTensor starter preference is retained; the historical Z-Image
recipe uses its own model family. Journal schema v1 is unchanged, shared lessons
do not mark visitor progress, and the guide opens without credentials.

## Validation

The original Pan Handlers suite passed **27 tests**. After applying the changes,
`python -B -m unittest discover -s tests -v` from `D:\Documents\Pan_Handlers`
passed **33 tests in 13.737 seconds**. Coverage includes standalone and embedded
rendering, both visual themes, independent visitor state, journal round trips,
timing boundaries, sample hashes and scoped widget keys when shared renderers
appear twice. The revised staged suite also passed 33 tests before deployment.
These are application tests, not a new browser visual review or a rendered-video
validation. Existing files were hash-checked before replacement; the other 14
captured guide/test files were unchanged. No provider operation or model download
was performed for this contribution.

## Next experiment

Make the proposed eight-second, one-speaker shot from original material. Keep its
camera, background, duration and ambient sound; change one line. First review an
audio-only replacement, then compare a lip-sync pass against it. Preserve the
source, full-length speech WAV, result, graphs, exact versions and actual charge.
Judge whether the changed line keeps the performance believable and the scene
recognizable. Record the first failure and one attempted fix, including a rejected
result if that is what happens. This will give Pathfinder its first honest video
comparison without expanding into a whole scene before we understand one shot.

## Pathfinder review — September 12, 2026

Reviewed the portable image, recorded settings, workflow downloads, scene rehearsal,
timing change and Cloud instructions. The full 33-test suite passed again in
19.198 seconds. No material issue was found in journal compatibility or the
distinction between completed work and the proposed video experiment.

One onboarding correction followed: the Cloud instructions and exported checklist
now explicitly let learners reuse an existing compatible Cloud file, skip
unneeded provider credentials/imports, and record that choice. The three worked
example tests passed after this copy change, including both shared renderers with
distinct widget keys; the exported checklist was also inspected.

The next experiment above remains the most useful CFA contribution: source,
replacement audio, result, critique and one attempted improvement. This review
did not execute that experiment or perform any provider operation.
