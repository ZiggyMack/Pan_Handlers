# CFA worked example: first Observatory pump concept

Field evidence from `D:/Documents/CFA`, branch `main`, September 12, 2026.
Production execution and canonical artifacts remain in CFA. This small copy lets
Pathfinder readers inspect the evidence without that checkout, credentials, or
model downloads. `manifest.json` records source paths and artifact hashes.

## What happened

A written brief requested a compact, lake-green communal pump with brass fittings,
a pale stone footing, a readable service panel, a repair patch, a replaced coupling,
and a lever socket. There was no source image or video. Comfy Cloud completed one
1024 × 1024 Z-Image-Turbo generation. The original PNG is included.

The palette, service panel, and silhouette read clearly. The housing was too tall
and pristine; visible repairs and a distinct lever socket did not read as intended.
Ziggy found it a promising starting direction. Completion and acceptable design
quality were different judgments. No improved second generated image exists.
The next production choice was to author repair details in the separate Godot
prototype and prioritize a playable experience.

## Open or run the recipe

1. `pump_concept_v001.editor.json` is an **editor-save graph** with a `nodes`
   array. Open/drag this file into the ComfyUI editor. Inspect models and available
   nodes in the environment where you intend to run it.
2. The baseline uses separate Z-Image loaders: `z_image_turbo_bf16.safetensors`,
   `qwen_3_4b.safetensors` (encoder type `lumina2`), and `ae.safetensors`.
   A new SDXL checkpoint recipe is a separate compatible graph; SDXL remains
   Pathfinder's starter search preference.
3. Restore seed **42**, size **1024 × 1024**, batch **1**, steps **8**, CFG **1**,
   sampler **res_multistep**, scheduler **simple**, denoise **1**, and shift **3**.
   The editor retains a randomize seed control: choose fixed control and explicitly
   set 42 for a controlled comparison. A fixed seed is not a promise of identical
   pixels across changed software or models.
4. `pump_concept_v001.api.json` is the **API submission graph** (node-ID keys,
   `class_type` and `inputs`). Use it with a compatible submission API, not as the
   draggable editor file. Both graphs were extracted from the completed PNG;
   they were not hand-converted.
5. Confirm current model/node availability and compute charges before running.
   Pathfinder only supplies the files; it executes no generation.

## Completion, failure, and unknowns

- Completed job: `cb835f1e-3b10-4972-860c-fb83fb0517c0`.
- Submitted: `2026-09-12 14:08:59 UTC`; completion observed:
  `2026-09-12T14:12:05+00:00`. This interval includes waiting/observation delay;
  it is not measured GPU runtime.
- A preceding OAuth refresh failed with `invalid_grant: refresh token reuse detected`.
  The first browser callback timed out; a fresh login for the existing Comfy
  connection succeeded, and a read-only server-info call confirmed access.
  The recurring rejection's cause is unknown. The Civitai provider key is a
  separate credential and was not replaced to fix Comfy OAuth.
- MCP server version observed: **0.57.0**, **41 tools**. Embedded template
  metadata reports comfy-core **0.3.64/0.3.73** and frontend **1.42.15**; these
  are not verified versions of the deployed engine. Immutable model revisions
  and weight hashes are unknown.
- Actual GPU runtime, attributable credits and balances are **unknown**. The
  zero paid-API-node estimate excluded GPU time, and the queried usage window
  ended before this job. Neither establishes a free run.
- No video rewrite, speech generation, lip-sync result, or generated mesh import
  is demonstrated. Model import, completed generation, accepted quality, and
  independently retrieved backup each require their own evidence. The first
  authenticated Civitai import and independent Drive retrieval remain unverified
  at this checkpoint.

The most easily missed step: save the correct graph format **and** the actual
seed/settings before changing anything. A completed result with its recipe is a
stronger starting point than a screenshot of a canvas alone.
