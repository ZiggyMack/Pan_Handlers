"""Scene-rewrite learning content, primary sources reviewed on 2026-09-12.

The first-shot plan and effort labels are editorial guidance. Source review is
not installation or render validation. This module performs no network calls.
"""

INSPIRATION = {
    "url": "https://x.com/Innerstand/status/2097309066489921821?s=20",
    "description": (
        "The spark: a user-described Denzel Washington film scene whose familiar "
        "visual setting and performance were retained while the dialogue was rewritten."
    ),
    "access_note": (
        "We could not inspect the linked video. This description comes from the user; "
        "the creator's production stack and exact editing method remain unverified."
    ),
}

EDITING_APPROACHES = [
    {
        "id": "dub",
        "name": "Replace the soundtrack",
        "preserves": "Original pictures, camera movement, faces and cuts.",
        "changes": "The spoken line and final sound mix.",
        "effort": "Lowest setup effort; useful first baseline.",
        "limit": "The original mouth movements remain. Timing the audio alone cannot redraw them.",
    },
    {
        "id": "lipsync",
        "name": "Rewrite dialogue + match the mouth",
        "preserves": "Uses the existing shot as the visual foundation.",
        "changes": "Replacement speech drives generated mouth movements.",
        "effort": "A bounded first experiment with one clear speaker; more review as shots get complex.",
        "limit": "Face detail and timing still need comparison with the source. A new line may not fit the original acting.",
    },
    {
        "id": "regenerate",
        "name": "Reimagine the whole scene",
        "preserves": "Reference material can guide the new scene's look and composition.",
        "changes": "Can extend to action, expressions, environment and camera behavior.",
        "effort": "A later creative branch with more continuity and shot matching work.",
        "limit": "Reference guidance does not guarantee the original frames, identity or performance will survive unchanged.",
    },
]

REHEARSAL = {
    "title": "The Observatory: water before the crossing",
    "status": "Proposed rehearsal only. No source footage, replacement WAV or rendered result exists for this example.",
    "shot": "Plan an eight-second locked shot of one clearly visible speaker beside a village water pump. Keep the face unobstructed and the camera still; record or create the source shot before testing the rewrite.",
    "beats": (
        ("00:00–00:01", "Silent look toward the crossing.", "Keep the silent look."),
        ("00:01–00:03", "The bridge can wait.", "The crowd can wait."),
        ("00:03–00:04", "Pause; hold the speaker's expression.", "Keep the pause and expression."),
        ("00:04–00:07", "First, we fix the pump.", "First, we bring them water."),
        ("00:07–00:08", "Silent reaction beat.", "Keep the silent reaction."),
    ),
    "timing_note": "These are proposed acting beats, not measured takes. Read both lines aloud and adjust the writing to the source performance. Export the clean replacement WAV for the full eight seconds, including its silent beats; do not stretch the spoken words simply to fill the shot.",
    "criteria": (
        ("Must stay", "Speaker identity, framing, camera position, pump and background, shot length, and silent reaction beats."),
        ("May change", "The spoken words and voice performance; a lip-sync candidate may also change the mouth region. The audio baseline keeps the original picture."),
        ("Reject if", "The face or background drifts, the new line overruns its beat, a silent reaction starts speaking, or the old dialogue is still audible."),
    ),
    "stages": (
        ("Script", "The timed replacement line and a note about what must remain recognizable."),
        ("Voice performance", "A recorded take fitted to the beats; a clean speech WAV with silence, separate from music and ambience."),
        ("Lip sync", "One candidate driven by the source shot and replacement WAV; compare it against the untouched shot and audio baseline."),
        ("Editing", "Keep the accepted picture on the original timeline; retain the start, end and reaction beats."),
        ("Sound", "Mix replacement dialogue with preserved or rebuilt ambience and effects; listen for doubled original speech."),
    ),
    "review_note": "Keep source, audio baseline and lip-sync candidate as three separate files. Record observations at the same timecodes, including one rejected candidate if a run fails. Runtime, credits and visual quality remain unknown until the experiment is performed.",
}

FAST_STEPS = [
    {
        "id": "choose_shot",
        "title": "Choose one shot to prove the idea",
        "actions": [
            "Start with a 5–10-second shot: one visible speaker, a clear face and no cuts. This is our proposed experiment size, not a tool limit.",
            "Use your own or permitted footage and a recorded voice or licensed/consented synthetic voice.",
            "Write down what must stay recognizable: camera, background, expression, timing and speaker.",
        ],
        "evidence": "A source clip, its duration and frame rate, and one sentence defining a successful rewrite.",
    },
    {
        "id": "rewrite_line",
        "title": "Write to the performance already on screen",
        "actions": [
            "Mark the start and end of the spoken line, pauses and reaction beats.",
            "Write a replacement that fits those beats; read it aloud against the clip.",
            "If it needs substantially more time or a different emotional performance, simplify the line or choose another shot.",
        ],
        "evidence": "Original timing notes and the replacement script, including intentional pauses.",
    },
    {
        "id": "prepare_audio",
        "title": "Make the replacement audio",
        "actions": [
            "Record the line or generate your selected voice, then export a clean speech WAV.",
            "Align the performance to the shot in an editor. Export the full replacement WAV including leading, internal and trailing silence; preserve reaction beats rather than stretching speech to fill them.",
            "Listen without the picture: check intelligibility, delivery and clipped words before spending a lip-sync run.",
        ],
        "evidence": "A clean replacement WAV and its full exported duration, including silence, compared with the source shot; record the spoken beats separately.",
    },
    {
        "id": "build_baseline",
        "title": "Hear the new scene before changing its face",
        "actions": [
            "Place the replacement dialogue under the untouched shot in the editor.",
            "Remove the old dialogue. Use separate ambience/effects tracks when available; otherwise separate or rebuild that background and listen for damaged sound.",
            "Export an audio-only replacement baseline. Keep its clean speech file separate from the final mix.",
        ],
        "evidence": "A baseline clip that proves the writing, pacing and sound work; original mouth mismatch is expected here.",
    },
    {
        "id": "sync_shot",
        "title": "Run one lip-sync experiment",
        "actions": [
            "Choose a documented execution route below and record its version or model before running.",
            "Supply the source video and clean replacement speech. Keep music, ambience and overlapping voices out of this speech input.",
            "Check duration handling explicitly, then generate one result before changing settings or adding more shots.",
        ],
        "evidence": "One output clip, the route/settings used, and actual run time and spend if the service reports them.",
    },
    {
        "id": "review_mix",
        "title": "Inspect the face, then finish the sound",
        "actions": [
            "Compare source and result at normal playback and around difficult frames: lip closures, teeth, beard edges and head turns.",
            "Check background, camera motion, shot length and speech ending; listen for any remaining original dialogue.",
            "Return the accepted shot to the editor, mix the replacement speech with ambience/effects, and label the shared result as an edited scene.",
        ],
        "evidence": "A final mixed clip plus specific observations about what matched, drifted or needs another pass.",
    },
    {
        "id": "save_recipe",
        "title": "Leave a trail the next person can follow",
        "actions": [
            "Save the source clip, script, speech WAV, editor project, workflow/settings and accepted output together.",
            "Record versions, model, asset locations, actual time/cost and the fix for each failure you encountered.",
            "Attempt a second shot only after this one works. Add cuts and additional speakers as separate learning milestones.",
        ],
        "evidence": "A restorable experiment package and a short explanation of what has actually been verified.",
    },
]

COMFY_RECIPE = [
    "This is a documented connection recipe, not an installation-tested workflow file. Use the setup guide first if ComfyUI is not running yet.",
    "Check your installed version for sync.so Lip Sync (SyncLipSyncNode) under partner/video/sync.so. It exists in current official source; stable releases may lag. Record the version that provides it.",
    "For this native partner route, sign in to your Comfy account, check Comfy credits and network access, and inspect the displayed charge before execution. Media is uploaded for hosted processing.",
    "Add Load Video (LoadVideo) for the trimmed source shot and Load Audio (LoadAudio) for the replacement WAV. Connect their VIDEO and AUDIO outputs to sync.so Lip Sync, then its VIDEO output to Save Video (SaveVideo).",
    "Select the available model; the reviewed native node offers sync-3. Compare input durations before execution: its default bounce mode can reverse playback when the audio outlasts the shot. Fit the audio to the shot and inspect the chosen mode.",
    "Save the output and the workflow; compare the result in the editor. The node's seed is a rerun control, not a guarantee of identical generated output.",
    "If the node is absent, check the official release/update guidance. Sync Studio is a separate hosted fallback using a Sync account and its own billing; it is not the same login or credit balance.",
    "Local LatentSync uses a community integration plus downloaded models and GPU inference. Treat that as a separate setup route; do not combine its install instructions with this partner-node recipe.",
]

EXECUTION_ROUTES = [
    {
        "name": "ComfyUI · native sync.so partner node",
        "setup": "A ComfyUI version containing the node, Comfy sign-in and available credits.",
        "compute": "Hosted lip-sync processing; ComfyUI is the workflow interface.",
        "tradeoff": "Our suggested first Comfy experiment. Requires an upload and per-run credits; installation and generation are not yet verified here.",
        "url": "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_api_nodes/nodes_sync_so.py",
    },
    {
        "name": "Sync Studio · direct hosted fallback",
        "setup": "A separate Sync account; upload the same video and replacement speech in Studio.",
        "compute": "Hosted generation through Sync's interface; API is optional.",
        "tradeoff": "Useful if the Comfy node is unavailable. Keeps the experiment moving, but uses separate billing and does not teach the Comfy graph.",
        "url": "https://sync.so/docs/quickstart",
    },
    {
        "name": "ComfyUI · local LatentSync candidate",
        "setup": "Working ComfyUI, a compatible community wrapper, FFmpeg and matching model downloads.",
        "compute": "Local GPU inference. Upstream lists 8 GB VRAM for 1.5 and 18 GB for 1.6; wrapper overhead and compatibility need separate validation.",
        "tradeoff": "More local control and setup work. Candidate only: no installation or render has been tested here. Check code, model and dependency licenses separately.",
        "url": "https://github.com/bytedance/LatentSync",
    },
]

FAILURES = [
    {
        "symptom": "The line ends late, or the video loops, reverses or changes speed.",
        "cause": "Audio and shot durations differ; the selected sync mode determines how the mismatch is handled.",
        "fix": "Retime or rerecord the replacement line, match input duration and review the mode before another run.",
    },
    {
        "symptom": "The mouth moves for the wrong person or around a cut.",
        "cause": "Speaker ambiguity or a scene boundary makes a single input harder to control.",
        "fix": "Split at cuts, use one speaker per test, then examine the selected route's speaker controls for later multi-person shots.",
    },
    {
        "symptom": "Teeth, lips or beard edges change unnaturally.",
        "cause": "Generated facial detail or a difficult viewing angle may fail to match the source.",
        "fix": "Compare the exact failing frames. Start with a larger, clear frontal face; keep a failure note before trying a setting or another model.",
    },
    {
        "symptom": "A hand or object across the mouth looks wrong.",
        "cause": "The mouth is partly hidden; obstruction handling differs by model.",
        "fix": "Use an unobstructed first shot. For the later shot, inspect every obstructed section and compare another route if needed.",
    },
    {
        "symptom": "The old voice is still audible or the background sounds hollow.",
        "cause": "The source mix still contains dialogue, or separation damaged ambience and effects.",
        "fix": "Solo the editor tracks, remove the original dialogue path, and use clean background stems or rebuild the damaged background.",
    },
    {
        "symptom": "Lip timing is weak although the soundtrack sounds finished.",
        "cause": "Music, noise or overlapping speakers may be reaching the lip-sync input.",
        "fix": "Send the isolated replacement speech to lip sync; add the finished soundtrack afterwards in the editor.",
    },
    {
        "symptom": "The Comfy partner node is missing or asks for sign-in again.",
        "cause": "Installed-version availability, authentication, credits or connection environment may differ.",
        "fix": "Check the partner-node FAQ and account state. Keep direct Sync and Comfy account credentials separate.",
    },
    {
        "symptom": "Local inference runs out of GPU memory.",
        "cause": "The selected model and wrapper exceed available memory; general ComfyUI system requirements do not establish this workload's fit.",
        "fix": "Check the exact model version and wrapper requirements. Use an appropriate hosted route while documenting the local setup gap.",
    },
]

TOPIC_NOTES = [
    "Changing the script, creating a voice performance and synchronizing a face are separate decisions. Rewriting text does not automatically recreate an actor's exact voice.",
    "This target can begin with existing video. Reconstructing an editable 3D set, camera or character is a separate branch to explore when a shot actually requires it.",
    "A convincing result depends on writing, acting rhythm, face quality and sound together. A lip-sync pass cannot guarantee that new words fit the emotion already on screen.",
    "Our fast path proves one shot and records real effort before estimating a whole scene. Difficulty labels are planning judgments, not measured benchmarks.",
]

SCENE_SOURCES = [
    {
        "title": "Official ComfyUI · sync.so partner node",
        "url": "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_api_nodes/nodes_sync_so.py",
        "note": "Reviewed upstream implementation for the native video-and-audio node. Source availability does not confirm an installed version.",
    },
    {
        "title": "Official ComfyUI · video load/save nodes",
        "url": "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_video.py",
        "note": "Confirms LoadVideo and SaveVideo names and VIDEO connections used in the recipe.",
    },
    {
        "title": "Official ComfyUI · audio loader",
        "url": "https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_audio.py",
        "note": "Confirms LoadAudio and its AUDIO output.",
    },
    {
        "title": "Sync · prepare video and clean speech",
        "url": "https://sync.so/docs/compatibility-and-tips/media-content-tips",
        "note": "Input advice for face visibility, speaking motion and isolated speech.",
    },
    {
        "title": "Sync · duration mismatch modes",
        "url": "https://sync.so/docs/developer-guides/sync-mode",
        "note": "Explains trimming, looping, reversing, padding and retiming when video and audio lengths differ.",
    },
    {
        "title": "Sync · models and caveats",
        "url": "https://sync.so/docs/models/lipsync",
        "note": "Provider-described capabilities, speaker handling and common quality limitations; not our own output evaluation.",
    },
    {
        "title": "Sync · direct hosted entry point",
        "url": "https://sync.so/docs/quickstart",
        "note": "Direct API and Studio entry points, independent of the native Comfy partner integration.",
    },
    {
        "title": "Comfy · partner-node credits",
        "url": "https://support.comfy.org/articles/1982697177-partner-nodes-pricing",
        "note": "Comfy credits are consumed when partner nodes execute. Check live pricing in the chosen route.",
    },
    {
        "title": "Comfy · partner-node troubleshooting",
        "url": "https://docs.comfy.org/tutorials/partner-nodes/faq",
        "note": "Node availability, release differences, login, connectivity and credit checks.",
    },
    {
        "title": "ByteDance · LatentSync upstream",
        "url": "https://github.com/bytedance/LatentSync",
        "note": "Local inference requirements and model versions; distinguish inference VRAM from training figures.",
    },
    {
        "title": "Community · LatentSync Comfy wrapper candidate",
        "url": "https://github.com/ShmuelRonen/ComfyUI-LatentSyncWrapper",
        "note": "Unofficial integration with examples. Its setup claims need checking against upstream before selecting an installation.",
    },
    {
        "title": "ByteDance · LatentSync 1.6 model card",
        "url": "https://huggingface.co/ByteDance/LatentSync-1.6/blob/main/README.md",
        "note": "The weight card lists OpenRAIL++; this differs from the code repository's Apache-2.0 license.",
    },
    {
        "title": "Blackmagic Design · Fairlight audio workflow",
        "url": "https://www.blackmagicdesign.com/products/davinciresolve/fairlight/",
        "note": "Recording, dialogue replacement, editing and mixing for the baseline and final soundtrack.",
    },
    {
        "title": "FFmpeg · stream selection and copying",
        "url": "https://ffmpeg.org/ffmpeg.html",
        "note": "Technical reference for retaining encoded video while selecting replacement audio; it does not generate mouth movements.",
    },
]
