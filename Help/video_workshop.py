"""Video-first routing and a review notebook; never submits Comfy jobs."""

from html import escape

import streamlit as st

from Help.video_plan import (
    MATERIALS, CHANGES, PRESERVE, REVIEW_CHECKS, new_plan, route_for,
    contradictions, add_take, accept_take, current_accepted, dumps_plan,
    loads_plan, plan_markdown, plan_entry,
)
from Help.video_routes import ROUTES, FINISHING
from Help import cfa_learning


STATE_KEY = "help_video_plan"
GUARDIAN = (
    "D:/Documents/CFA/docs/notes/explorable_world/comfy/outputs/references/"
    "preferred_10b936eb46c1e671b089bf26e0c551bb/10b936eb46c1e671b089bf26e0c551bb.mp4"
)


def _plan():
    if STATE_KEY not in st.session_state:
        st.session_state[STATE_KEY] = new_plan()
    return st.session_state[STATE_KEY]


def _remember(field, key):
    _plan()[field] = st.session_state[key]


def _field(kind, label, field, prefix="help_video_work", **kwargs):
    key = prefix + "_" + field
    # Home and workshop edit the same durable plan, with separate widget keys.
    st.session_state[key] = _plan()[field]
    return kind(label, key=key, on_change=_remember, args=(field, key), **kwargs)


def _guardian():
    # Keep earlier takes; changing the brief makes their acceptance stale.
    _plan().update(
        material="video", change="look", preserve=["motion", "camera", "identity", "contact"],
        source=GUARDIAN, reference="",
        brief="The same woman-and-wolf encounter in cool, overcast daylight. Keep both subjects, their scale, positions, gesture timing, contact and camera movement. Believable skin, fur and fabric. Change the atmosphere only.",
        clip_notes="CFA source receipt: 1088 x 1920; 193 frames at 24 fps; 8.042 s; audio track present. SHA256 3f2be3389bbf36c9e83927ac43b4f8181de836a6ddecefb629bac1756169678a (bytes rechecked October 2). Full playback and audio review still needed. Select one continuous 4–8-second gesture and record its exact in/out points before preparing inputs.",
        workflow_revision="", environment_notes="", settings="", estimate="",
    )


def _selector(prefix):
    left, right = st.columns(2)
    with left:
        _field(st.selectbox, "What material do you have?", "material", prefix,
               options=list(MATERIALS), format_func=MATERIALS.get)
    with right:
        _field(st.selectbox, "What do you want to change?", "change", prefix,
               options=list(CHANGES), format_func=CHANGES.get)
    _field(st.multiselect, "What must survive the change?", "preserve", prefix,
           options=list(PRESERVE), format_func=PRESERVE.get)
    for issue in contradictions(_plan()):
        st.warning(issue)
    if route_for(_plan()) == "wan_animate" and "camera" in _plan()["preserve"]:
        st.warning("Wan Animate 2 can change the camera and setting. If the original framing and camera path are strict requirements, evaluate the Mix or masked structural route before committing to this candidate.")


def _route_card():
    route = ROUTES[route_for(_plan())]
    st.markdown(
        '<div class="help-callout"><div class="help-kicker">YOUR STARTING CANDIDATE</div>'
        f'<h3>{escape(route["title"])}</h3><p>{escape(route["why"])}</p></div>',
        unsafe_allow_html=True,
    )
    st.caption(route["kind"] + " · Research checked October 2, 2026 · Your Cloud workspace is not checked by this guide.")
    st.write(route["caveat"])
    return route


def render_entry(go):
    st.subheader("Start with your material")
    _selector("help_video_home")
    _route_card()
    st.button("Build this video experiment →", type="primary", key="help_video_home_open",
              on_click=go, args=("Video workshop",))
    st.caption("A source-performance test needs a driving clip. A still or a mesh alone supplies no recorded performance to preserve.")


def _route_tab(go):
    _selector("help_video_work")
    route = _route_card()
    with st.expander("Why another route might fit better"):
        for alternative in route["alternatives"]:
            st.markdown("- " + alternative)
        st.write("Look, setting and character replacement are separate experiments. Change one major constraint at a time so the comparison explains what worked.")
    st.button("Use the CFA woman-and-wolf test brief", key="help_video_guardian", on_click=_guardian)
    st.caption("Optional lighting/motion capability test, separate from CFA's music-video production. It does not establish character replacement, rap lip-sync or tattoo consistency. This fills a brief and source reference; no media is loaded and earlier takes stay in the notebook.")
    _field(st.text_input, "Source clip / asset reference", "source", max_chars=2000)
    _field(st.text_input, "Reference image / replacement audio / control asset", "reference", max_chars=2000)
    _field(st.text_area, "Describe this one change", "brief", max_chars=1000)
    _field(st.text_area, "Source inspection and trim", "clip_notes", max_chars=2000,
           placeholder="In/out timecodes, cut boundaries, dimensions, FPS, frame count, sound, occlusions and source hash")
    with st.expander("Where we actually stand", expanded=False):
        st.caption("CFA records reviewed " + cfa_learning.REVIEWED + "; not a new account check.")
        st.table(cfa_learning.STATUS_ROWS)
        st.caption("The separate authored Godot prototype remains a future branch. The two recovered video graphs are reference recipes, not executed CFA videos.")
        st.write("The recovered wolf recipe starts from a missing gf_24_a.jpg. It is an image-to-video reference, so opening that graph does not turn the available MP4 into its input. Use a source-video control workflow for this test.")
        st.button("Inspect the completed still and foundations →", on_click=go,
                  args=("ComfyUI guide",), key="help_video_evidence_guide")


def _prepare_tab():
    route = ROUTES[route_for(_plan())]
    st.subheader("Open a real starting recipe")
    st.markdown(f'**{route["workflow_name"]}**')
    if route["workflow"]:
        st.link_button("Get the official workflow JSON", route["workflow"])
    st.markdown(f'[Workflow instructions and model links]({route["docs"]})')
    if route["workflow"]:
        st.caption("The JSON link goes to the maintainer's editor workflow. Save it on D: and use Comfy's Open command or drop the JSON onto the canvas. It is separate from the experiment-plan JSON exported here.")
    else:
        st.caption("This is a preparation or template-selection handoff. Follow its instructions to obtain the actual executable graph; the experiment-plan JSON exported here is a notebook, not a Comfy workflow.")
    if route_for(_plan()) == "image_to_video" and _plan()["material"] == "video":
        st.info("To make new motion from this clip, extract and choose a starting frame as the image input. This route does not preserve the full source performance. Choose a source-video transformation if preservation is the goal.")
    cols = st.columns(2)
    with cols[0]:
        st.markdown("**Inputs to prepare**")
        for item in route["inputs"]:
            st.markdown("- " + item)
    with cols[1]:
        st.markdown("**Dependencies to resolve in Cloud**")
        for item in route["dependencies"]:
            st.markdown("- " + item)
    st.markdown("**From source to first preview**")
    for index, item in enumerate(route["steps"], 1):
        st.markdown(f"{index}. {item}")
    st.info("Check the actual Cloud graph before a run: supported node versions, accessible model files, input sockets, timing rules and expected cost. A public workflow is not proof that your account can run it. Missing custom nodes need a supported Cloud alternative or a separately chosen cloud host; installing Manager on this PC does not add them to managed Cloud.")
    _field(st.text_area, "Workflow copy and exact revision", "workflow_revision", max_chars=2000,
           placeholder="Saved editor JSON, source URL/revision/hash, chosen task/adapter and model filenames")
    _field(st.text_area, "Cloud compatibility evidence", "environment_notes", max_chars=2000,
           placeholder="Date, workspace, missing/resolved nodes, model access, successful connection check and unresolved issues")
    _field(st.text_area, "Preview settings and effective prompt", "settings", max_chars=2000,
           placeholder="Fixed seed, control mode/strength, dimensions at each stage, frame count, input and output FPS, resampling, resolved prompt, sound plan")
    _field(st.text_area, "Run budget / observed usage", "estimate", max_chars=2000,
           placeholder="One bounded preview; estimated cost before execution; actual runtime and charge after execution, or unknown")
    st.caption("Keep weights and rendering in the cloud. Necessary source copies, JSON and review clips belong on D:. Keep full-resolution masters remote with a verified retrieval path; sanitized recipes and records belong in Git.")


def _record_take():
    checks = {key: st.session_state["help_video_check_" + key] for key in REVIEW_CHECKS}
    try:
        updated = add_take(_plan(), st.session_state["help_video_take_result"],
                           st.session_state["help_video_take_observations"], checks)
    except ValueError as error:
        st.session_state["help_video_take_notice"] = ("error", str(error))
    else:
        st.session_state[STATE_KEY] = updated
        st.session_state["help_video_take_notice"] = ("success", "Take recorded with its brief, workflow and settings. Acceptance is a separate decision below.")
        for key in REVIEW_CHECKS:
            st.session_state["help_video_check_" + key] = False
        st.session_state["help_video_take_result"] = ""
        st.session_state["help_video_take_observations"] = ""


def _review_tab():
    st.subheader("Judge the moving shot")
    st.write("Compare the source and candidate at matching timecodes and normal speed, then scrub the problem frames. These players have independent controls. Check contact, gesture, camera movement and timing before judging resolution.")
    with st.expander("Play a source / candidate comparison"):
        st.caption("Optional review copies only, up to 50 MB each. Uploading displays them in this Pathfinder session; it does not submit them to Comfy or save them in the plan. Keep the actual files on D: or in your cloud project.")
        for column, label, key in zip(st.columns(2), ("Source", "Candidate"), ("source", "candidate")):
            with column:
                upload = st.file_uploader(label + " review clip", type=["mp4", "mov", "webm"], key="help_video_review_" + key)
                if upload is not None:
                    if upload.size > 50 * 1024 * 1024:
                        st.error("Use a review copy under 50 MB.")
                    else:
                        st.video(upload.getvalue())
    st.write("Keep one fixed baseline. Record every attempted take, including failures; change one control or input for the next comparison. A beautiful frame with changed performance does not pass a motion-preservation brief.")
    st.caption("Acceptance requires a source reference, a change brief and an exact saved workflow revision, plus all four review checks. Failed takes can be recorded with incomplete preparation notes.")
    with st.form("help_video_take_form"):
        st.text_input("Result file / remote asset reference", max_chars=2000, key="help_video_take_result")
        st.text_area("What happened? Include timecodes and the next change.", max_chars=1000, key="help_video_take_observations")
        for key, label in REVIEW_CHECKS.items():
            st.checkbox(label, key="help_video_check_" + key)
        st.form_submit_button("Record this take", on_click=_record_take)
    notice = st.session_state.pop("help_video_take_notice", None)
    if notice:
        getattr(st, notice[0])(notice[1])
    plan = _plan()
    if not plan["takes"]:
        st.info("No takes recorded in this plan yet. This guide has not generated or inspected a video for you.")
        return
    st.table([{"Take": take["id"], "Result": take["result"],
               "Review checks": f'{sum(take["checks"].values())} / {len(REVIEW_CHECKS)}',
               "Observed": take["observations"]} for take in plan["takes"]])
    take_ids = [take["id"] for take in plan["takes"]]
    if st.session_state.get("help_video_take_choice") not in take_ids:
        st.session_state["help_video_take_choice"] = take_ids[0]
    take_id = st.selectbox("Take to inspect / accept", take_ids, key="help_video_take_choice")
    take = next(take for take in plan["takes"] if take["id"] == take_id)
    with st.expander("Recorded context for this take"):
        st.json(take["context"])
    if st.button("Accept this take for finishing", key="help_video_accept"):
        try:
            st.session_state[STATE_KEY] = accept_take(plan, take_id)
        except ValueError as error:
            st.error(str(error))
        else:
            st.success("Accepted against your recorded review checks. Keep the original output and its recipe.")


def _finish_tab(save_entry):
    plan = _plan()
    accepted = current_accepted(plan)
    st.subheader("A convincing take → an HD master → a reviewed 4K derivative")
    if accepted:
        st.success(f'Accepted for this brief: {accepted["id"]} · {accepted["result"]}')
    elif plan["accepted_id"]:
        st.warning("Your accepted take belongs to an earlier brief or configuration. Its record is retained; compare again under the current plan before finishing.")
    else:
        st.info("First record and accept a preview. The finishing path below is preparation; no HD or 4K result is implied.")
    st.table([
        {"Stage": "Convincing short clip", "Target": "One continuous 4–8-second shot at supported working dimensions", "Pass condition": "Performance, contact, intended change and temporal stability pass playback review."},
        {"Stage": "HD review master", "Target": "Portrait 1080 × 1920 / landscape 1920 × 1080", "Pass condition": "Compare again at full size; document any model-aligned padding and final crop or letterbox."},
        {"Stage": "4K derivative", "Target": "Portrait 2160 × 3840 / landscape 3840 × 2160", "Pass condition": "Accept only if detail helps without changing faces, fur, hands or temporal texture."},
    ])
    st.write("These are delivery dimensions, not promises of native generation quality. Preserve aspect ratio without stretching. Record source, generated, refined and exported dimensions separately. Upscaling can invent detail; retain the accepted unscaled take.")
    st.markdown(f'**Finishing candidate: {FINISHING["title"]}**')
    st.markdown(f'[Official finishing recipe]({FINISHING["docs"]})')
    if FINISHING["workflow"]:
        st.link_button("Get the finishing workflow JSON", FINISHING["workflow"])
    st.write(FINISHING["caveat"])
    with st.expander("Finishing dependencies"):
        for dependency in FINISHING["dependencies"]:
            st.markdown("- " + dependency)
    st.markdown(
        "1. Reopen the accepted take and its saved graph. Keep its exact motion and timing as the comparison.\n"
        "2. Test the selected finishing method on a difficult short interval before processing the whole take. Check its own node/model requirements and cost.\n"
        "3. Export HD, inspect at full size and normal speed, then compare one 4K derivative. Document crop/letterbox, codec and color space. Treat HDR and frame interpolation as separate experiments.\n"
        "4. Reopen the exported files. Check frame count, FPS, duration and sound. Changing FPS alone retimes the frames; it does not interpolate motion. Preserve or remux source audio only after confirming it still fits the picture.\n"
        "5. Keep the source, preview, accepted take, HD/4K comparison, rejected alternatives, exact recipes, model/node versions, settings and observed cost together. Verify you can retrieve the remote masters."
    )
    st.divider()
    st.subheader("Leave yourself a way back in")
    st.caption("The video-plan JSON restores this editable plan, take history and review decisions. The Field journal stores a readable snapshot. Media and models are never included in either export.")
    try:
        json_data = dumps_plan(plan)
        route = ROUTES[route_for(plan)]
        report = plan_markdown(plan) + "\n## Selected workflow guidance\n\n" + route["title"] + "\n\n"
        report += f'[Official instructions]({route["docs"]})\n\n'
        if route["workflow"]:
            report += f'[Editor workflow JSON]({route["workflow"]})\n\n'
        report += route["why"] + "\n\n" + route["caveat"] + "\n\n### Required inputs\n\n"
        report += "\n".join("- " + item for item in route["inputs"])
        report += "\n\n### Dependencies to check in Cloud\n\n" + "\n".join("- " + item for item in route["dependencies"])
        report += "\n\n### Opening and first-preview handoff\n\n" + "\n".join(f"{i}. {item}" for i, item in enumerate(route["steps"], 1))
        report += f'\n\nFinishing candidate after acceptance: [{FINISHING["name"]}]({FINISHING["workflow"]})\n\n{FINISHING["caveat"]}\n'
    except ValueError as error:
        st.error(str(error))
        return
    left, right = st.columns(2)
    left.download_button("Download video plan · JSON", json_data, "pathfinder-video-plan.json", "application/json", key="help_video_download_json")
    right.download_button("Download experiment record · Markdown", report, "pathfinder-video-experiment.md", "text/markdown", key="help_video_download_md")
    if st.button("Save video snapshot to Field journal", key="help_video_journal"):
        try:
            save_entry({**plan_entry(plan), "resource": ROUTES[route_for(plan)]["docs"]})
        except ValueError as error:
            st.error(str(error))
        else:
            st.success("Snapshot saved. Export your journey JSON too if you want to carry the journal to another session.")
    with st.expander("Restore a saved video plan"):
        uploaded = st.file_uploader("Video-plan JSON", type=["json"], key="help_video_plan_upload")
        st.caption("Restore replaces this session's video plan. Download the current plan first if you want to keep it. The ordinary Field journal stays unchanged.")
        if st.button("Restore this video plan", disabled=uploaded is None, key="help_video_restore"):
            try:
                restored = loads_plan(uploaded.getvalue())
            except ValueError as error:
                st.error(str(error))
            else:
                st.session_state[STATE_KEY] = restored
                st.rerun()


def _lessons_tab(go):
    st.subheader("Learn the part needed for this shot")
    lessons = {
        "open": "Open and inspect the borrowed workflow",
        "creative": "Direct the result · Spanish creator / NKD lessons",
        "access": "Resolve Cloud model imports and access",
        "controls": "Understand the menu, queue and canvas",
        "reference": "Prepare a character or look reference",
        "compare": "Change one parameter in a controlled comparison",
        "handoff": "Carry frames, sound and FPS into a saved clip",
        "nodes": "Inspect node inputs and outputs",
    }
    selected = st.selectbox("I need help with…", list(lessons), format_func=lessons.get, key="help_video_lesson")
    if selected == "open":
        from Help.workflow_files import render
        render("help_video_files")
    elif selected == "creative":
        from Help.tutorial_notes import render
        render("help_video_creative_notes", initial_episode="nkd")
    elif selected == "access":
        from Help.cloud_access import render
        render("help_video_access")
    elif selected == "controls":
        from Help.workflow_controls import render
        render("help_video_controls")
    elif selected == "reference":
        from Help.image_edit_lab import render
        render()
    elif selected == "compare":
        from Help.sampling_lab import render
        render()
    elif selected == "handoff":
        from Help.video_handoff import render
        render("help_video_handoff_workshop")
    else:
        from Help.node_atlas import render
        render()
    st.caption("The still-image lessons teach methods. Their SDXL defaults, sampler values and latent batch size are not video-model settings. Use the selected video's exact recipe and temporal constraints.")
    st.button("Open the complete lesson library →", on_click=go, args=("ComfyUI guide",), key="help_video_all_lessons")


def render(save_entry, go):
    st.markdown("**Source → workflow → preview → accepted take → HD → reviewed 4K**")
    st.caption("Plan and review here; run in your cloud Comfy workspace. This console does not connect to Comfy, inspect its catalog or submit jobs.")
    tabs = st.tabs(["01 / Choose the route", "02 / Prepare & open", "03 / Preview & compare", "04 / Finish & keep", "05 / Relevant lessons"])
    for tab, renderer in zip(tabs, (lambda: _route_tab(go), _prepare_tab, _review_tab,
                                    lambda: _finish_tab(save_entry), lambda: _lessons_tab(go))):
        with tab:
            renderer()
