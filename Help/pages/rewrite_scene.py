"""The scene-dialogue mission: a sourced guide and a portable shot worksheet."""

from math import isclose

import streamlit as st

from Help.content.scene_content import (
    COMFY_RECIPE, EDITING_APPROACHES, EXECUTION_ROUTES, FAILURES,
    FAST_STEPS, INSPIRATION, REHEARSAL, SCENE_SOURCES,
)
from Help.state.scene_plan import new_plan, plan_markdown, plan_to_entry, validate_plan
from Help.guides.node_atlas import render_recipe_nodes
from Help.guides.video_handoff import render_soundtrack_case, soundtrack_case_markdown

from Help.state.session import append_journal_entry
from Help.ui.components import hero, route_strip


APPROACH_NAMES = {item["id"]: item["name"] for item in EDITING_APPROACHES}
CHALLENGES = ["Cuts", "Multiple speakers", "Profile or covered mouth", "Background dialogue or music", "Fast motion"]


def _draft():
    if "help_scene_draft" not in st.session_state:
        st.session_state["help_scene_draft"] = new_plan()
    return st.session_state["help_scene_draft"]


def _remember(field, key):
    _draft()[field] = st.session_state[key]


def _field(kind, label, name, options=None, **kwargs):
    key = "help_scene_widget_" + name
    if key not in st.session_state:
        st.session_state[key] = _draft()[name]
    kwargs.update(key=key, on_change=_remember, args=(name, key))
    if options is None:
        return kind(label, **kwargs)
    return kind(label, options=options, **kwargs)


def _guide_markdown():
    lines = ["# Rewrite a scene: first-shot field guide", "",
             "Goal: keep an existing shot recognizable while replacing its dialogue.", "",
             "This is a documented learning recipe. No render or installation is claimed as tested.", "",
             "Start with a proposed 5–10-second, single-speaker shot with a clear face and no cuts.", "",
             "## Choose the editing approach", ""]
    for approach in EDITING_APPROACHES:
        lines.extend([f'### {approach["name"]}', "",
                      f'- Preserves: {approach["preserves"]}',
                      f'- Changes: {approach["changes"]}',
                      f'- Effort: {approach["effort"]}',
                      f'- Limit: {approach["limit"]}', ""])
    lines.extend(["## Proposed Observatory rehearsal", "", REHEARSAL["title"], "",
                  REHEARSAL["status"], "", REHEARSAL["shot"], "",
                  "| Time in the shot | Planned source performance | Proposed rewrite |",
                  "| --- | --- | --- |"])
    lines.extend("| " + " | ".join(beat) + " |" for beat in REHEARSAL["beats"])
    lines.extend(["", REHEARSAL["timing_note"], ""])
    lines.extend(f'- **{label}:** {detail}' for label, detail in REHEARSAL["criteria"])
    lines.extend(["", "### Keep the production stages separate", ""])
    lines.extend(f'- **{stage}:** {handoff}' for stage, handoff in REHEARSAL["stages"])
    lines.extend(["", REHEARSAL["review_note"], "", "## First experiment", ""])
    for number, step in enumerate(FAST_STEPS, 1):
        lines.extend([f'### {number}. {step["title"]}', ""])
        lines.extend(f"- {action}" for action in step["actions"])
        lines.extend(["", f'**Evidence:** {step["evidence"]}', ""])
    lines.extend(["## ComfyUI partner-node recipe", ""])
    lines.extend(f"{number}. {item}" for number, item in enumerate(COMFY_RECIPE, 1))
    lines.extend(["", "## Execution routes and alternatives", ""])
    for route in EXECUTION_ROUTES:
        lines.extend([f'### {route["name"]}', "",
                      f'- Setup: {route["setup"]}',
                      f'- Compute: {route["compute"]}',
                      f'- Tradeoff: {route["tradeoff"]}',
                      f'- [Maintainer reference]({route["url"]})', ""])
    lines.extend(["## Inspect failures before changing settings", ""])
    for failure in FAILURES:
        lines.extend([f'### {failure["symptom"]}', "",
                      f'Possible cause: {failure["cause"]}', "",
                      f'Next test: {failure["fix"]}', ""])
    lines.extend(["", "## Sources", ""])
    lines.extend(f'- [{item["title"]}]({item["url"]}) — {item["note"]}' for item in SCENE_SOURCES)
    lines.extend(["", "## Inspiration", "", INSPIRATION["url"], "", INSPIRATION["access_note"], "", soundtrack_case_markdown()])
    return "\n".join(lines)


def _intent():
    st.subheader("Keep the scene. Change what is said.")
    st.write("The target is an existing shot with a new scripted performance: preserve its recognizable composition, camera, cast and setting while changing the dialogue. Lip sync can adapt the visible mouth to that audio; editing and sound work make the result feel like a scene.")
    st.info("Editable 3D geometry is a separate branch. You can begin this mission with a video clip and replacement speech.")
    render_soundtrack_case()
    fit, difficulty, reference = st.tabs(["What stays / what changes", "How hard is it?", "The inspiration"])
    with fit:
        st.table({
            "Editing approach": [route["name"] for route in EDITING_APPROACHES],
            "What stays": [route["preserves"] for route in EDITING_APPROACHES],
            "What changes": [route["changes"] for route in EDITING_APPROACHES],
            "The limit": [route["limit"] for route in EDITING_APPROACHES],
        })
        st.caption("These are editing approaches inside a project. AUTOMATIC1111, Forge, Invoke and ComfyUI remain the separate interface choices.")
        st.markdown("**Voice and dialogue are separate decisions.** Writing new words does not recreate the original actor's voice. Start with a recorded performance or a licensed or consented synthetic voice; treat any voice-matching work as an additional stage.")
    with difficulty:
        for route in EDITING_APPROACHES:
            st.markdown(f'**{route["name"]}:** {route["effort"]}')
        st.markdown("**What raises the difficulty:** multiple speakers, cuts, profile faces, covered mouths, fast action, background dialogue and changes to the original emotional performance.")
        st.markdown("**A useful first success:** one short shot whose new line is intelligible, fits the intended timing, follows the mouth acceptably, and preserves the parts of the frame you care about.")
        st.caption("Difficulty is an editorial planning assessment. Runtime, price and quality have not been measured for your footage or hardware.")
    with reference:
        st.markdown(f'[The example that started this mission]({INSPIRATION["url"]})')
        st.write(INSPIRATION["description"])
        st.caption(INSPIRATION["access_note"])
        st.write("We are documenting a credible route to the described effect. Keep the reference, the shot we actually test and its production notes together so later learners can compare intention with evidence.")


def _fast_path():
    st.subheader("First prove one shot")
    st.write("A proposed 5–10-second test, one speaker and no cut keeps the experiment small. Establish the replacement performance in an editor, then test lip sync on that same shot.")
    with st.expander("Try the proposed Observatory rehearsal"):
        st.markdown("**" + REHEARSAL["title"] + "**")
        st.info(REHEARSAL["status"])
        st.write(REHEARSAL["shot"])
        st.table({
            "Time in the shot": [beat[0] for beat in REHEARSAL["beats"]],
            "Planned source performance": [beat[1] for beat in REHEARSAL["beats"]],
            "Proposed rewrite": [beat[2] for beat in REHEARSAL["beats"]],
        })
        st.write(REHEARSAL["timing_note"])
        st.table({"Review": [row[0] for row in REHEARSAL["criteria"]],
                  "What to compare": [row[1] for row in REHEARSAL["criteria"]]})
        st.table({"Stage": [row[0] for row in REHEARSAL["stages"]],
                  "Hand off to the next stage": [row[1] for row in REHEARSAL["stages"]]})
        st.write(REHEARSAL["review_note"])
        st.caption("This read-only example is included in the first-shot guide download. Your worksheet and journal stay yours to fill in.")
    selected = st.selectbox("Open a scene step", [s["id"] for s in FAST_STEPS],
                            format_func=lambda value: next(f'{i:02d} / {s["title"]}' for i, s in enumerate(FAST_STEPS, 1) if s["id"] == value),
                            key="help_scene_step")
    step = next(s for s in FAST_STEPS if s["id"] == selected)
    instructions, evidence = st.tabs(["Do the work", "Keep the evidence"])
    with instructions:
        st.subheader(step["title"])
        for number, action in enumerate(step["actions"], 1):
            st.markdown(f"{number}. {action}")
    with evidence:
        st.write(step["evidence"])
        st.caption("Record the observed result in the shot worksheet or field journal. Opening a step or saving a plan does not complete a render.")
    st.download_button("Download the first-shot guide", _guide_markdown(),
                       file_name="scene-rewrite-first-shot.md", mime="text/markdown", key="help_scene_guide_download")


def _recipe():
    st.subheader("Where ComfyUI fits in the scene")
    native, routes, outside = st.tabs(["ComfyUI partner recipe", "Other execution routes", "Before and after the graph"])
    with native:
        st.caption("Documented from current upstream code; availability must be checked in your installed version. This recipe has not yet been run on our reference footage.")
        st.code("Load Video ── VIDEO ──┐\n                     ├─ sync.so Lip Sync ── VIDEO ── Save Video\nLoad Audio ── AUDIO ──┘", language="text")
        st.write("The graph expresses the core handoff: existing shot + replacement speech → a lip-synced video to inspect and finish in an editor.")
        for number, action in enumerate(COMFY_RECIPE, 1):
            st.markdown(f"{number}. {action}")
        st.warning("Check duration handling before running. The current upstream node defaults to bounce, which can play footage forward and backward to fill longer audio. Fit the line to the shot and deliberately choose how mismatched durations are handled.")
        st.caption("The lip-sync computation in this partner route runs remotely. ComfyUI still loads and uploads the media, and execution uses the relevant account and credits.")
        with st.expander("Inspect the four nodes"):
            st.caption("See each node's job, inputs, outputs and caveats without leaving this recipe.")
            render_recipe_nodes("scene_lipsync", key_prefix="help_scene_atlas")
    with routes:
        for route in EXECUTION_ROUTES:
            with st.expander(route["name"], expanded=True):
                st.markdown("**Setup:** " + route["setup"])
                st.markdown("**Where it runs:** " + route["compute"])
                st.markdown("**Tradeoff:** " + route["tradeoff"])
                st.markdown(f'[Official or maintainer reference]({route["url"]})')
    with outside:
        st.markdown("**Before the graph:** choose and trim the shot, write the replacement line, record or generate its performance, and fit its pauses and duration. Keep the clean speech separate from the music and ambience.")
        st.markdown("**After the graph:** compare faces and timing, assemble the shots, rebuild or restore room tone and sound effects, mix the dialogue, and label a shared creative rewrite clearly.")
        st.markdown("**For a full scene:** work shot by shot. Maintain a speaker/voice map, consistent audio settings, shot identifiers and a matching timeline. Preserve reaction shots where useful; inspect every cut and handoff between speakers.")
        st.write("Lip sync does not automatically write the script, recreate the actor's voice, remove all original dialogue, preserve every pixel or finish the sound mix.")


def _worksheet(save_entry):
    st.subheader("Plan and record one replacement performance")
    st.caption("This draft stays in the session across navigation. Save a snapshot to Field journal to include it in your JSON/Markdown exports. A restored journal contains readable snapshots; it does not refill this worksheet automatically.")
    left, right = st.columns(2)
    with left:
        _field(st.text_input, "Shot name", "title", max_chars=200)
        _field(st.text_input, "Source clip or file location", "source", max_chars=2000,
               placeholder="Your clip filename or reference URL")
        _field(st.selectbox, "Editing approach", "approach", options=list(APPROACH_NAMES), format_func=APPROACH_NAMES.get)
        _field(st.number_input, "Shot start in the source (seconds)", "start_seconds", min_value=0.0, max_value=86400.0, step=0.1)
        _field(st.number_input, "Shot duration (seconds)", "duration_seconds", min_value=0.1, max_value=600.0, step=0.1)
        _field(st.text_input, "Speaker or character label", "speaker", max_chars=200)
    with right:
        _field(st.selectbox, "Replacement voice source", "voice_source",
               options=["Recorded performance", "Licensed or consented synthetic voice", "Undecided"])
        _field(st.text_area, "Replacement line and pauses", "replacement_line", max_chars=5000,
               placeholder="Write one new line. Mark the pauses and delivery you want.")
        _field(st.number_input, "Full exported replacement WAV duration, including silence (seconds; 0 = not measured)", "audio_seconds", min_value=0.0, max_value=600.0, step=0.1)
        st.caption("Measure the whole WAV file. Keep spoken words, intentional pauses and silent reaction beats on the source timeline; a shorter line may need silence around it, not slower speech.")
        _field(st.text_area, "What must remain recognizable?", "preserve", max_chars=2000)
    _field(st.multiselect, "Difficult conditions in this shot", "challenges", options=CHALLENGES)
    draft = _draft()
    if draft["audio_seconds"]:
        difference = draft["audio_seconds"] - draft["duration_seconds"]
        # Decimal tenths can fall just above the boundary in binary floats.
        if abs(difference) > 0.1 and not isclose(abs(difference), 0.1, rel_tol=0.0, abs_tol=1e-9):
            st.warning(f'The exported replacement WAV is {abs(difference):.1f} seconds {"longer" if difference > 0 else "shorter"} than the shot, including silence. Preserve pauses and reaction beats; check the WAV export and chosen lip-sync duration mode.')
        else:
            st.info("The entered durations align within 0.1 seconds. Review actual speech beats and the exported clip; these numbers do not verify mouth synchronization.")
    else:
        st.caption("Timing will become clearer once you have a recorded line. The worksheet does not estimate your voice speed or inspect media files.")
    if draft["challenges"]:
        st.caption("For the first experiment, consider a cleaner subsection of the scene. Keep these difficulties in your result notes if they are essential to the shot.")
    _field(st.selectbox, "Experiment status (self-reported)", "status",
           options=["Planning", "Audio baseline saved", "Lip-sync test reviewed", "Final edit reviewed"])
    _field(st.text_area, "Observed result, files, settings, time or cost", "result_notes", max_chars=3000)
    _field(st.text_area, "Next experiment", "next_step", max_chars=1000)
    ready = bool(draft["source"].strip() and draft["replacement_line"].strip())
    if st.button("Save shot snapshot to Field journal", disabled=not ready, type="primary", key="help_scene_save"):
        try:
            save_entry(plan_to_entry(draft))
        except ValueError as error:
            st.error(str(error))
        else:
            st.session_state["help_scene_saved"] = True
            st.rerun()
    if st.session_state.pop("help_scene_saved", False):
        st.success("Shot snapshot added to Field journal. Download the journey JSON to keep it between visits.")
    if not ready:
        st.caption("Add a source location and replacement line to save a useful shot snapshot.")
    st.download_button("Download this shot worksheet", plan_markdown(validate_plan(draft)),
                       file_name="scene-rewrite-shot.md", mime="text/markdown", key="help_scene_plan_download")


def _failure_lab():
    st.subheader("Inspect the shot, then change one thing")
    for item in FAILURES:
        with st.expander(item["symptom"]):
            st.markdown("**Possible cause:** " + item["cause"])
            st.markdown("**Next test:** " + item["fix"])
    with st.expander("A/B review before calling it finished", expanded=True):
        st.write("Watch source and result at normal speed, then inspect the mouth and face around difficult frames. Check which person speaks, the teeth and jaw, identity and lighting changes, frame timing, audio onset, lingering original dialogue and room tone. Keep the rejected outputs and the reason you rejected them.")
    with st.expander("Sourcebook"):
        for source in SCENE_SOURCES:
            st.markdown(f'**[{source["title"]}]({source["url"]})**')
            st.write(source["note"])


def _render_lab(save_entry):
    tabs = st.tabs(["01 / Understand the target", "02 / Fast path", "03 / ComfyUI recipe", "04 / Shot worksheet", "05 / Failure lab"])
    for tab, renderer in zip(tabs, (_intent, _fast_path, _recipe, lambda: _worksheet(save_entry), _failure_lab)):
        with tab:
            renderer()


def render():
    hero("RELATED BRANCH / SCENE DIALOGUE REWRITE", "Same scene. New dialogue.",
          "Understand what to preserve, what to replace, and how to turn one short experiment into a recipe someone else can follow.")
    route_strip()
    st.caption("Start with the editing approach; choose tools for its individual stages. The ComfyUI foundations remain available alongside this dedicated mission.")
    _render_lab(append_journal_entry)
