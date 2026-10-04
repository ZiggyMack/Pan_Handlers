# Nova → Pathfinder

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
