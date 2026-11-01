# Pathfinder file map

Use the name you see in the website to find the file that builds it. **Launch the whole app with `Help/app.py`; the files under `pages/` are parts of that app.** Opening a Python file in an editor shows its code, not the live page.

## Run Pathfinder

From `D:\Documents\Pan_Handlers`:

```powershell
python -m pip install -r Help/requirements.txt
python -m streamlit run Help/app.py --server.port 8506
```

This block is the canonical run command for Pathfinder since 2026-10-31 (Python 3.10 or newer, Streamlit >=1.36,<2): [README.md](README.md) points here instead of repeating it, and any other copy should do the same. The root README.md and dashboard/README.md still carry their own copies; they were outside the 2026-10-31 pass.

The Streamlit Cloud entry point remains **`Help/app.py`**. The operations dashboard still embeds the same console through `dashboard/pages/pathfinder.py`.

Deploy source of record, recorded 2026-10-31: by Ziggy's decision of that date the hosted apps deploy from the Hall at the root `pages/` package. Its launcher is not tracked in this repository, so the hosted main file is configured on the host and is not in the repo. `Help/app.py` is the local standalone entry; the Streamlit Cloud sentence above is the earlier record.

## Match the sidebar to a file

| In Pathfinder | Page file | Supporting material |
| --- | --- | --- |
| **Start here** | [pages/start_here.py](pages/start_here.py) | The material/change/preserve questions reuse [pages/video_workshop.py](pages/video_workshop.py); candidate descriptions live in [content/video_routes.py](content/video_routes.py). |
| **Compare paths** | [pages/compare_paths.py](pages/compare_paths.py) | The four applications and their tradeoffs live in [content/catalog.py](content/catalog.py). |
| **Video workshop** | [pages/video_workshop.py](pages/video_workshop.py) | Route recommendations: [content/video_routes.py](content/video_routes.py), where each route's `evidence` string names what CFA has actually done with it (executed, preflighted, prepared or nothing) and the card shows it beside the kind with the `cfa_learning` review date; optional H3 candidate: [content/h3_candidate.py](content/h3_candidate.py). Editable plans, take reviews and exports: [state/video_plan.py](state/video_plan.py). Relevant lessons also opens the tutorial register and prompt-composition practice. |
| **Collaborators** | [pages/collaborators.py](pages/collaborators.py) | ComfyUI, Grok, Gemini and Flow roles, reference scope, discovery/preservation and evidence states: [content/collaborators.py](content/collaborators.py). Reuses the existing reference, comparison, prompt, file and video/audio lessons. |
| **Rewrite a scene** | [pages/rewrite_scene.py](pages/rewrite_scene.py) | Dialogue approaches and rehearsal: [content/scene_content.py](content/scene_content.py). Worksheet rules: [state/scene_plan.py](state/scene_plan.py). |
| **ComfyUI guide** | [pages/comfyui_guide.py](pages/comfyui_guide.py) | Nested lessons in `guides/`; steps, setup instructions and glossary in [content/catalog.py](content/catalog.py). See the tab map below. |
| **Field journal** | [pages/field_journal.py](pages/field_journal.py) | Journal validation and portable JSON/Markdown: [state/journey.py](state/journey.py). |
| **Sources & roadmap** | [pages/sources_roadmap.py](pages/sources_roadmap.py) | Sources and expansion plans in `content/catalog.py`, `content/video_routes.py` and `content/scene_content.py`; reviewed CFA status in [content/cfa_learning.py](content/cfa_learning.py). |

## Find a nested ComfyUI lesson

The outer tabs are assembled in [pages/comfyui_guide.py](pages/comfyui_guide.py). Shared lessons can also appear in Video workshop when relevant to the selected task.

| ComfyUI guide tab | Where to make the change |
| --- | --- |
| **00 / Fit & tradeoffs** | Page layout in `pages/comfyui_guide.py`; benefits, costs and alternatives in `content/catalog.py`. |
| **01 / Follow the steps** | Page layout in `pages/comfyui_guide.py`; foundation steps in `content/catalog.py`; journal rules in `state/journey.py`. |
| **02 / Setup routes** | Environment instructions in `content/catalog.py`; [guides/cloud_access.py](guides/cloud_access.py), [guides/model_library.py](guides/model_library.py) and [guides/model_filters.py](guides/model_filters.py) cover access, files and Civitai filtering. |
| **03 / Workflow anatomy** | Node map and glossary in the page/catalog; individual lessons listed below. |
| **04 / Troubleshooting** | Troubleshooting entries and their links in `pages/comfyui_guide.py`. |
| **05 / Node Atlas** | [guides/node_atlas.py](guides/node_atlas.py): 24 curated node types and six recipes, including prompt composition. |
| **06 / Worked example** | [guides/worked_example.py](guides/worked_example.py), with the packaged evidence under [examples/cfa_pump_v001/](examples/cfa_pump_v001/). |
| **07 / Workflow lab** | [guides/workflow_lab.py](guides/workflow_lab.py); practice milestones in [content/workflow_lessons.py](content/workflow_lessons.py). |

**Workflow anatomy** has these smaller lessons:

- First prompt connections and **Beyond two prompts · composition and styles**: [guides/prompt_wiring.py](guides/prompt_wiring.py). The composition practice also appears in Node Atlas's composition recipe and Video workshop → Relevant lessons.
- VAE paths: [guides/vae_paths.py](guides/vae_paths.py).
- Size & sampler: [guides/generation_settings.py](guides/generation_settings.py).
- Save & load: [guides/workflow_files.py](guides/workflow_files.py).
- Controlled experiment: [guides/sampling_lab.py](guides/sampling_lab.py), with [guides/shared_controls.py](guides/shared_controls.py) for one control feeding multiple samplers. [guides/workflow_decision.py](guides/workflow_decision.py) supplies the optional decision/outcome fields and copy → inspect inputs → compare → reopen exercise shared with image-to-image comparisons.
- Tutorial notes: [guides/tutorial_notes.py](guides/tutorial_notes.py) renders eleven selector entries and their exports. Episode 1's notes are there; earlier guides remain in [content/episode_three.py](content/episode_three.py), [content/episode_four.py](content/episode_four.py), [content/additional_guide.py](content/additional_guide.py) and [content/creative_control_guide.py](content/creative_control_guide.py). [content/tutorial_followups.py](content/tutorial_followups.py) adds episode 5–8 annotations, H3 media roles and video-comparison review questions. [content/tutorial_register.py](content/tutorial_register.py) preserves eight source records, archive hashes, review dates and URL evidence; it never opens CFA files at runtime. CFA's dated learning snapshot is [content/cfa_learning.py](content/cfa_learning.py).

**Workflow lab** also draws on [guides/workflow_controls.py](guides/workflow_controls.py) for the control reference, [guides/image_edit_lab.py](guides/image_edit_lab.py) for image-to-image comparisons, and [guides/video_handoff.py](guides/video_handoff.py) for frames, sound, export timing and the optional H3 callout. Episode 2's practice, repair exercises and workbook are assembled by `guides/workflow_lab.py`.

**Video workshop → 05 / Relevant lessons → Tutorial source register** opens the same notes renderer with Episode 8 selected initially; **Compose prompt text and inspect optional styles** opens `guides/prompt_wiring.py`. **01 / Choose the route → Additional candidate · MiniMax H3 reference roles** reuses `guides/video_handoff.py` and [content/h3_candidate.py](content/h3_candidate.py). This callout does not select a new route or migrate the video-plan schema.

The October 4, 2026 teaching additions keep prompt drafts and comparison decision notes in scoped session state. Prompt-note downloads and the existing A/B/C sampling/image-edit Markdown exports preserve those notes; journal v1 and video-plan JSON do not automatically include them. Source-register JSON is a portable evidence index, not a transcript bundle or journal backup.

**Collaborators** has three nested tabs: **01 / Role & handoff**, **02 / Preserve or explore**, and **03 / Continue a lesson**. ComfyUI is first; Grok, Gemini and Flow explain their current project roles. The October 8 receipt includes its October 9 01:45:08 UTC appendix: provider completion is distinct from verified local receipt, and text/chat sources are distinct from raw visual-media ingestion. The October 10 adoption of CFA's October 9 teaching delta adds nine dated lessons under **02 / Preserve or explore** (received versus verified versus reviewed counts, outfit parents and prop states, prop cue versus approved character, workspace versus mode versus model, first-frame versus reference conditioning, static pose sheets, scene cards, observed scene versus inferred method, editing versus extension), a **Requested / reported** evidence stage, the October 9 mouth rule under Preserve, and updated provider boundaries in [content/collaborators.py](content/collaborators.py). The provider, lane and lesson selections survive page navigation without changing journal or video-plan schemas. Its Markdown download contains teaching and provenance only, not media or CFA review state.

**Rewrite a scene > Understand the target** and **Workflow lab > Video & audio** share the dated soundtrack case in [guides/video_handoff.py](guides/video_handoff.py): measured local stream-copy picture preservation, saved/unexecuted Cloud assembly, and separate unexecuted lip-sync. [content/cfa_learning.py](content/cfa_learning.py) now distinguishes executed but unaccepted motion/relighting tests from the older October 4 still examples, and its new dated rows record verified Grok returns, the saved-but-unexecuted Seedance first-frame candidate, the prepared opening-shot benchmark and the head-library standard (October 9) and the mouth-continuity plan (October 8) as dated states.

## Shared pieces and folders

```text
Help/
├── app.py              Start the standalone Streamlit app
├── console.py          Shared shell: navigation and page dispatch
├── pages/              One file per sidebar page
├── guides/             Reusable lessons and interactive learning tools
├── content/            Sourced teaching material, route data and tutorial notes
├── state/              Session helpers, validation and portable exports
├── ui/                 Theme and shared presentation components
├── examples/           Small portable evidence and workflow samples
├── README.md           Orientation, coverage and maintenance instructions
├── FILE_MAP.md         This map, the canonical run command and the handbook index below
├── CFA_HANDOFF.md      The direction letter through October 8, 2026
├── CFA_FEEDBACK.md     Pan's dated adoption returns to CFA, newest first
└── CFA_TUTORIAL_LEDGER.md  CFA intakes and Pan adoption status, dated per section
```

### The five maintainer documents (handbook index, 2026-10-31)

| Document | Role | Who writes it | Who reads it | Cadence |
| --- | --- | --- | --- | --- |
| [README.md](README.md) | Orientation, what the app covers, how to maintain it; the dated production state below its orientation block is history | Pan's steward (Claude since 2026-10-10) | learners, maintainers, CFA agents | at each adoption that changes coverage |
| [FILE_MAP.md](FILE_MAP.md) | Page and tab names to files; the canonical run command; this index | Pan's steward | anyone requesting or making a change | at each adoption that adds or moves a file |
| [CFA_HANDOFF.md](CFA_HANDOFF.md) | The direction letter to CFA, September 12 through October 8, 2026; later adoptions live in CFA_FEEDBACK.md and the ledger | Pan's side, in dated layers (the September letter was drafted for Ziggy to pass to CFA) | CFA Nova | not extended after October 8; a dated note under its title, 2026-10-31 |
| [CFA_FEEDBACK.md](CFA_FEEDBACK.md) | Pan's dated adoption returns to CFA (October 4 to 20) above CFA Nova's September 12 review | Pan's steward for the adoption returns; CFA Nova wrote the September review | CFA Nova, Ziggy | one dated section per adopted delta |
| [CFA_TUTORIAL_LEDGER.md](CFA_TUTORIAL_LEDGER.md) | CFA's intakes (sources, recipes, evidence, bounded follow-ups) and Pan's adoption status, dated per section | CFA Nova for intake sections, Claude for adoption sections (byline convention of 2026-10-31) | both | one intake per CFA return; one status update per adoption |

- [console.py](console.py) owns the shared navigation shell; edit a page file for a page-specific change.
- [ui/theme.py](ui/theme.py) owns visual styling and Matrix mode. [ui/components.py](ui/components.py) contains reusable presentation helpers.
- [state/session.py](state/session.py) provides shared session access; `state/journey.py`, `state/scene_plan.py` and `state/video_plan.py` own the relevant validation and export rules. Moving the files does not change the saved journal or video-plan format.
- `examples/` retains its existing paths. Large production media, weights and canonical run records still belong in CFA/cloud storage according to the project handoff.

The standalone launcher uses explicit, hidden Streamlit navigation so `pages/` does not create a second sidebar menu. Our existing custom sidebar remains the way to move around Pathfinder. This needs **Streamlit >=1.36,<2**; [Streamlit documents how explicit navigation disables automatic `pages/` discovery](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation).

## How to request an update

Tell us the **page → tab → desired change**. You do not need to know a Python filename. For example:

> Video workshop → Relevant lessons: add Nova's source/result comparison and explain which control fixed the flicker.

Or, when you know the file:

> ComfyUI guide → Workflow anatomy → VAE paths (`Help/guides/vae_paths.py`): make the Cloud setup steps easier to follow.

Give the supporting workflow, run record or tutorial when available, and say whether the result was tried, completed or accepted. That keeps new guidance tied to evidence. CFA findings reach this guide through the [manual handoff](CFA_HANDOFF.md) (the letter through October 8; since October 10 the working channel is the protocol in [REPO-SYNC/README.md](../REPO-SYNC/README.md), noted 2026-10-31); reorganizing these files does not synchronize the repositories.

## Finding an older filename

The October 4, 2026 reorganization retained most basenames. Old `Help/video_workshop.py` is now `Help/pages/video_workshop.py`; old `Help/scene_lab.py` is now `Help/pages/rewrite_scene.py`. Old lesson files such as `Help/node_atlas.py` moved into `Help/guides/`; researched content such as `Help/catalog.py` moved into `Help/content/`; plan/journal modules moved into `Help/state/`; and `Help/theme.py` moved into `Help/ui/`. Dated feedback may still mention the historical locations.
