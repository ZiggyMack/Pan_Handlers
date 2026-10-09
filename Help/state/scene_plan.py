"""A portable scene-rewrite worksheet, stored as an ordinary v1 journal entry.

This module only validates and formats learner-authored plans. It does not load
source media, run a model, or infer that a render has been completed.
"""

from __future__ import annotations

from datetime import date
import html
import math
import re
from typing import Any


INSPIRATION_URL = "https://x.com/Innerstand/status/2097309066489921821?s=20"
APPROACHES = ("dub", "lipsync", "regenerate")
APPROACH_LABELS = {
    "dub": "Audio-only dub",
    "lipsync": "Localized lip-sync edit",
    "regenerate": "Regenerate the scene",
}
VOICE_SOURCES = (
    "Recorded performance", "Licensed or consented synthetic voice", "Undecided",
)
CHALLENGES = (
    "Cuts", "Multiple speakers", "Profile or covered mouth",
    "Background dialogue or music", "Fast motion",
)
STATUSES = (
    "Planning", "Audio baseline saved", "Lip-sync test reviewed", "Final edit reviewed",
)
_TEXT_LIMITS = {
    "title": 200,
    "source": 2_000,
    "speaker": 200,
    "replacement_line": 5_000,
    "preserve": 2_000,
    "result_notes": 3_000,
    "next_step": 1_000,
}


def new_plan() -> dict[str, Any]:
    """Return an independent blank worksheet with an eight-second experiment."""
    return {
        "title": "First dialogue rewrite",
        "source": "",
        "approach": "lipsync",
        "start_seconds": 0.0,
        "duration_seconds": 8.0,
        "speaker": "",
        "replacement_line": "",
        "voice_source": "Undecided",
        "preserve": "Keep the shot composition, camera movement, identity and scene timing; allow mouth-region changes.",
        "challenges": [],
        "audio_seconds": 0.0,
        "status": "Planning",
        "result_notes": "",
        "next_step": "Cut one clean shot and record one replacement line.",
    }


def _text(value: Any, field: str, limit: int) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be text.")
    if len(value) > limit:
        raise ValueError(f"{field} must be at most {limit:,} characters.")
    try:
        value.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"{field} must contain valid Unicode text.") from exc
    return value


def _choice(value: Any, options: tuple[str, ...], field: str) -> str:
    if not isinstance(value, str) or value not in options:
        raise ValueError(f"{field} must be one of: {', '.join(options)}.")
    return value


def _seconds(value: Any, field: str, maximum: int, *, positive: bool = False) -> float:
    if type(value) not in (int, float) or (type(value) is float and not math.isfinite(value)):
        raise ValueError(f"{field} must be a finite number of seconds, not a boolean.")
    if value < 0 or value > maximum or (positive and value == 0):
        lower = "greater than 0" if positive else "at least 0"
        raise ValueError(f"{field} must be {lower} and at most {maximum:,} seconds.")
    return float(value)


def validate_plan(data: Any) -> dict[str, Any]:
    """Validate every field and return a detached copy; incomplete drafts are valid."""
    if not isinstance(data, dict):
        raise ValueError("Scene plan must be an object.")
    normalized = new_plan()
    expected = set(normalized)
    if set(data) != expected:
        details = []
        if expected - set(data):
            details.append("missing " + ", ".join(sorted(expected - set(data))))
        if set(data) - expected:
            details.append("unknown fields " + ", ".join(sorted(map(str, set(data) - expected))))
        raise ValueError("Scene plan: " + "; ".join(details) + ".")
    for field, limit in _TEXT_LIMITS.items():
        normalized[field] = _text(data[field], field, limit)
    for field, options in (
        ("approach", APPROACHES), ("voice_source", VOICE_SOURCES), ("status", STATUSES),
    ):
        normalized[field] = _choice(data[field], options, field)
    normalized["start_seconds"] = _seconds(data["start_seconds"], "start_seconds", 86_400)
    normalized["duration_seconds"] = _seconds(data["duration_seconds"], "duration_seconds", 600, positive=True)
    normalized["audio_seconds"] = _seconds(data["audio_seconds"], "audio_seconds", 600)
    challenges = data["challenges"]
    if not isinstance(challenges, list) or len(challenges) > len(CHALLENGES):
        raise ValueError("challenges must be a list of known, unique shot conditions.")
    for challenge in challenges:
        _choice(challenge, CHALLENGES, "challenges")
    if len(challenges) != len(set(challenges)):
        raise ValueError("challenges must not contain duplicates.")
    normalized["challenges"] = [challenge for challenge in CHALLENGES if challenge in challenges]
    return normalized


def _plan_rows(plan: dict[str, Any]) -> list[tuple[str, str]]:
    """Keep every worksheet field in the readable snapshot."""
    return [
        ("Plan title", plan["title"] or "Not recorded"),
        ("Source clip or locator", plan["source"] or "Not recorded"),
        ("Approach", APPROACH_LABELS[plan["approach"]] + " (" + plan["approach"] + ")"),
        ("Clip start", f'{plan["start_seconds"]} seconds'),
        ("Clip duration", f'{plan["duration_seconds"]} seconds'),
        ("Speaker", plan["speaker"] or "Not recorded"),
        ("Replacement dialogue / timed beats", plan["replacement_line"] or "Not recorded"),
        ("Voice source", plan["voice_source"]),
        ("What to preserve", plan["preserve"] or "Not recorded"),
        ("Shot conditions", ", ".join(plan["challenges"]) or "None recorded"),
        ("Measured replacement audio", f'{plan["audio_seconds"]} seconds' if plan["audio_seconds"] else "Not measured (0 seconds recorded)"),
        ("Status (self-reported)", plan["status"]),
        ("Result / review notes", plan["result_notes"] or "No result recorded"),
        ("Next experiment", plan["next_step"] or "Not recorded"),
    ]


def plan_to_entry(plan: Any) -> dict[str, str]:
    """Make a v1 journal entry after a source and replacement line are recorded.

    Source locators are plain text in the observation; the resource field uses
    only the fixed inspiration URL. No user-authored path is turned into a link.
    """
    plan = validate_plan(plan)
    if not plan["source"].strip() or not plan["replacement_line"].strip():
        raise ValueError("Add a source clip or locator and replacement dialogue before saving the plan to your journal.")
    observation = "\n\n".join(label + ":\n" + value for label, value in _plan_rows(plan))
    observation += "\n\nStatus is self-reported. Saving this worksheet does not generate or edit media, or verify a completed result."
    return {
        "date": date.today().isoformat(),
        "title": "Scene rewrite plan · " + (plan["title"] or "Untitled shot"),
        "observation": observation,
        "next_step": plan["next_step"],
        "resource": INSPIRATION_URL,
    }


def _markdown_text(value: str) -> str:
    value = html.escape(value, quote=False)
    return re.sub(r"([\\`*_{}\[\]()#+.!|~>-])", r"\\\1", value)


def plan_markdown(plan: Any) -> str:
    """Export a readable worksheet, including incomplete drafts, as inert text."""
    plan = validate_plan(plan)
    lines = [
        "# Scene rewrite worksheet", "",
        "Status is self-reported. This worksheet does not generate or edit media, or verify a completed result.",
        "",
    ]
    for label, value in _plan_rows(plan):
        lines.extend([f"**{label}:**", "", _markdown_text(value), ""])
    lines.extend([f"[Inspiration reference]({INSPIRATION_URL})", ""])
    return "\n".join(lines)
