# Pathfinder file map

Use the name you see in the website to find the file that builds it. **Launch the whole app with `Help/app.py`; the files under `pages/` are parts of that app.** Opening a Python file in an editor shows its code, not the live page.

From `D:\Documents\Pan_Handlers`:

```powershell
python -m streamlit run Help/app.py --server.port 8506
```

The Streamlit Cloud entry point remains **`Help/app.py`**. The operations dashboard still embeds the same console through `dashboard/pages/pathfinder.py`.

## Match the sidebar to a file

| In Pathfinder | Page file | Supporting material |
| --- | --- | --- |
| **Start here** | [pages/start_here.py](pages/start_here.py) | The material/change/preserve questions reuse [pages/video_workshop.py](pages/video_workshop.py); candidate descriptions live in [content/video_routes.py](content/video_routes.py). |
| **Compare paths** | [pages/compare_paths.py](pages/compare_paths.py) | The four applications and their tradeoffs live in [content/catalog.py](content/catalog.py). |
| **Video workshop** | [pages/video_workshop.py](pages/video_workshop.py) | Route recommendations: [content/video_routes.py](content/video_routes.py); optional H3 candidate: [content/h3_candidate.py](content/h3_candidate.py). Editable plans, take reviews and exports: [state/video_plan.py](state/video_plan.py). Relevant lessons also opens the tutorial register and prompt-composition practice. |
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

**Collaborators** has three nested tabs: **01 / Role & handoff**, **02 / Preserve or explore**, and **03 / Continue a lesson**. ComfyUI is first; Grok, Gemini and Flow explain their current project roles. The October 8 receipt includes its October 9 01:45:08 UTC appendix: provider completion is distinct from verified local receipt, and text/chat sources are distinct from raw visual-media ingestion. The provider, lane and lesson selections survive page navigation without changing journal or video-plan schemas. Its Markdown download contains teaching and provenance only, not media or CFA review state.

**Rewrite a scene > Understand the target** and **Workflow lab > Video & audio** share the dated soundtrack case in [guides/video_handoff.py](guides/video_handoff.py): measured local stream-copy picture preservation, saved/unexecuted Cloud assembly, and separate unexecuted lip-sync. [content/cfa_learning.py](content/cfa_learning.py) now distinguishes executed but unaccepted motion/relighting tests from the older October 4 still examples.

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
├── README.md           Running, coverage and maintenance instructions
├── FILE_MAP.md         This map
├── CFA_HANDOFF.md      Current coordination and historical handoffs
└── CFA_FEEDBACK.md     Dated feedback and production evidence
```

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

Give the supporting workflow, run record or tutorial when available, and say whether the result was tried, completed or accepted. That keeps new guidance tied to evidence. CFA findings reach this guide through the [manual handoff](CFA_HANDOFF.md); reorganizing these files does not synchronize the repositories.

## Finding an older filename

The October 4, 2026 reorganization retained most basenames. Old `Help/video_workshop.py` is now `Help/pages/video_workshop.py`; old `Help/scene_lab.py` is now `Help/pages/rewrite_scene.py`. Old lesson files such as `Help/node_atlas.py` moved into `Help/guides/`; researched content such as `Help/catalog.py` moved into `Help/content/`; plan/journal modules moved into `Help/state/`; and `Help/theme.py` moved into `Help/ui/`. Dated feedback may still mention the historical locations.
