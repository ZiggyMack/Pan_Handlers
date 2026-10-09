"""Portable, dated source records for the CFA eight-transcript intake.

Hashes/byte counts were verified against archived files on October 4, 2026.
Archive paths are provenance labels only: no sibling files or accounts are read
at import or render time, and transcripts are not copied into the app.
"""

REVIEWED = "October 4, 2026"
MANIFEST_PATH = "D:/Documents/CFA/docs/notes/explorable_world/comfy/references/user_transcripts_20261003.provenance.json"
REVIEW_PATH = "D:/Documents/CFA/docs/notes/explorable_world/comfy/REFERENCE_DRIVEN_WORKFLOWS.md"

SOURCES = {'ep3': {'id': 'comfy_episode_03_sampling_canvas',
         'archive_path': 'D:/Documents/CFA/docs/notes/explorable_world/comfy/references/comfy_episode03_sampling_canvas_20261004.user_transcript.txt',
         'bytes': 21557,
         'sha256': 'dacb137f3931805b25e5c1bb34bc28f4c255fcc0eede5030a029f61b990f299f',
         'url': 'https://www.youtube.com/watch?v=g8UlYE_HM2M',
         'url_basis': 'Existing Pathfinder URL corroborated by the indexed primary YouTube page title, '
                      'ComfyUI Tutorial Series: Ep03 - TXT2IMG Basics, and Pixaroma channel. Supplied '
                      'transcript topics align with the existing annotations. Video playback was not '
                      'independently reviewed.',
         'reviewed': 'October 4, 2026',
         'video_watch_verified': False,
         'role': 'Episode 03 SDXL seed/steps/CFG, promoted shared inputs, batching versus queued jobs, '
                 'grouping/bypass and connected branch duplication'},
 'ep4': {'id': 'comfy_episode_04_img2img_lora',
         'archive_path': 'D:/Documents/CFA/docs/notes/explorable_world/comfy/references/comfy_episode04_img2img_lora_20261004.user_transcript.txt',
         'bytes': 18021,
         'sha256': '888309d77ef3e99127566a556253727c00aaaacead3f81b72be644dd5f672a17',
         'url': 'https://www.youtube.com/watch?v=xedwjtaPVzw',
         'url_basis': 'supplied_by_user',
         'reviewed': 'October 4, 2026',
         'video_watch_verified': False,
         'role': 'Episode 04 SDXL single-image img2img, denoise and resizing, compatible LoRA model/CLIP '
                 'routing and fixed-seed comparisons; no two-reference face mapping'},
 'ep5': {'id': 'comfy_episode_05_sd3_comparison',
         'archive_path': 'D:/Documents/CFA/docs/notes/explorable_world/comfy/references/comfy_episode05_sd3_comparison_20261004.user_transcript.txt',
         'bytes': 19323,
         'sha256': '532ded1d7a08499a3d2c93e07f4a3614e9c59d6e8758505e712316cecc99dd9a',
         'url': 'https://www.youtube.com/watch?v=q9ufjcMofI0',
         'url_basis': 'supplied_by_user',
         'reviewed': 'October 4, 2026',
         'video_watch_verified': False,
         'role': 'Episode 05 SD3 Medium text-encoder-package comparison followed by SDXL Juggernaut X; '
                 'shared prompt strings and seed, separate model branches and output prefixes'},
 'ep6': {'id': 'comfy_episode_06_styles_sampling',
         'archive_path': 'D:/Documents/CFA/docs/notes/explorable_world/comfy/references/comfy_episode06_styles_sampling_20261004.user_transcript.txt',
         'bytes': 18418,
         'sha256': '8cb827eda20a524a9696be08d62599a03eb56809682e99e3f04cd024efb3082e',
         'url': 'https://www.youtube.com/watch?v=cmikc-Jo1gk',
         'url_basis': 'supplied_by_user',
         'reviewed': 'October 4, 2026',
         'video_watch_verified': False,
         'role': 'Episode 06 SDXL styles CSV, encoded-conditioning concatenation and grouped interface '
                 'tutorial; sampling controls require model-specific adaptation'},
 'ep7': {'id': 'comfy_episode_07_prompt_styles',
         'archive_path': 'D:/Documents/CFA/docs/notes/explorable_world/comfy/references/comfy_episode07_prompt_styles_20261004.user_transcript.txt',
         'bytes': 13506,
         'sha256': '7766ac23ddc78db75a939d32108144c3f9ab81acab224ea9e447237a9833f535',
         'url': 'https://www.youtube.com/watch?v=Xsx-u0OMezw',
         'url_basis': 'supplied_by_user',
         'reviewed': 'October 4, 2026',
         'video_watch_verified': False,
         'role': 'Episode 07 prompt-string concatenation, optional style mixing, and compact SDXL workflow '
                 'tutorial'},
 'ep8': {'id': 'flux_episode_08',
         'archive_path': 'D:/Documents/CFA/docs/notes/explorable_world/comfy/references/flux_episode08_20261003.user_transcript.txt',
         'bytes': 33622,
         'sha256': '3c1c00fd08cea88823fbf9bb5a75b220f7dc7159c0e92ea243cada298a9ea7d6',
         'url': 'https://www.youtube.com/watch?v=ImWHS5Ux36E',
         'url_basis': 'Recovered from indexed Pixaroma YouTube metadata describing Episode 8, FLUX '
                      'Dev/Schnell and FP8. Description chapter markers 02:14 (installation) and 08:14 (art '
                      'styles) align with the supplied transcript. This supports the source association; '
                      'playback was not independently reviewed.',
         'reviewed': 'October 4, 2026',
         'video_watch_verified': False,
         'role': 'FLUX.1 text-to-image workflow and controlled-comparison tutorial'},
 'h3': {'id': 'minimax_h3',
        'archive_path': 'D:/Documents/CFA/docs/notes/explorable_world/comfy/references/minimax_h3_20261003.user_transcript.txt',
        'bytes': 10778,
        'sha256': 'd265a1b2e87651956b027014c2a3a154fdf3669a9c2a743ba67e24f51801be3e',
        'url': None,
        'url_basis': 'Unresolved; no canonical video URL in the supplied intake.',
        'reviewed': 'October 4, 2026',
        'video_watch_verified': False,
        'role': 'Creator tutorial describing text/image/reference-to-video examples'},
 'comparison': {'id': 'video_model_comparison',
                'archive_path': 'D:/Documents/CFA/docs/notes/explorable_world/comfy/references/video_model_comparison_20261003.user_transcript.txt',
                'bytes': 27758,
                'sha256': 'ed5894fe0321fd6eeb478b83ed57f1d922122f826a7aec8a41bd5afbf4dccd97',
                'url': None,
                'url_basis': 'Unresolved; no canonical video URL in the supplied intake.',
                'reviewed': 'October 4, 2026',
                'video_watch_verified': False,
                'role': 'Creator opinions and examples, not a controlled benchmark or current price source'}}


def source_markdown(key):
    """Carry provenance into the portable lesson export without reading CFA."""
    source = SOURCES[key]
    video = f"[Source video]({source['url']})" if source["url"] else "Video URL unresolved."
    return "\n".join((
        "## Source record", "", video, "", source["url_basis"], "",
        "Transcript reviewed: " + source["reviewed"] + "; video not independently watched.", "",
        "Archive path (reference only; requires the adjacent local CFA checkout):", "",
        "`" + source["archive_path"] + "`", "",
        "SHA-256: `" + source["sha256"] + "`", "",
        f"Bytes: {source['bytes']} (archive bytes and hash verified at review).", "",
        "Provenance manifest: `" + MANIFEST_PATH + "`", "",
        "CFA lesson review: `" + REVIEW_PATH + "`", "",
        "These notes include the source identifiers, not the original transcript. The deployed guide does not read sibling repositories or require credentials.", "",
    ))


def register_rows():
    return [dict(Resource=key, Method=value["role"],
                 Source="Video linked; transcript reviewed" if value["url"] else "Transcript reviewed; video URL unresolved",
                 Reviewed=value["reviewed"])
            for key, value in SOURCES.items()]
