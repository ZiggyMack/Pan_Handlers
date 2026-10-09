"""Portable, validated progress for the help console; never writes to disk.

Schema version 1 requires every field emitted by :func:`new_journey`.
Unknown fields are rejected so an import cannot silently discard future data.
The returned data is always a fresh dictionary with fresh nested containers.
"""

from __future__ import annotations

import html
import json
import re
from typing import Any
from urllib.parse import urlsplit


PATH_IDS = ("automatic1111", "forge", "invoke", "comfyui")
STEP_IDS = (
    "brief", "setup", "first_image", "workflow", "first_video", "bridge_3d", "publish"
)
OUTPUT_KINDS = ("AI video", "Editable 3D + AI", "Exploring")
ENVIRONMENTS = ("Undecided", "Desktop", "Portable", "Manual", "Cloud")
MAX_IMPORT_BYTES = 1_048_576
MAX_ENTRIES = 300

_FIELDS = {
    "schema_version", "goal", "output_kind", "chosen_path", "environment",
    "decision_reason", "completed_steps", "step_notes", "entries",
}
_ENTRY_FIELDS = {"date", "title", "observation", "next_step", "resource"}
_STEP_LABELS = {
    "brief": "Define the shot",
    "setup": "Choose and prepare an environment",
    "first_image": "Generate a first image",
    "workflow": "Understand and save a workflow",
    "first_video": "Generate a first video",
    "bridge_3d": "Connect an editable 3D scene",
    "publish": "Package and share the result",
}
_PATH_LABELS = {
    "automatic1111": "AUTOMATIC1111",
    "forge": "Forge UI",
    "invoke": "Invoke",
    "comfyui": "ComfyUI",
}


def new_journey() -> dict[str, Any]:
    """Return an independent, empty version 1 journey."""
    return {
        "schema_version": 1,
        "goal": "",
        "output_kind": "Exploring",
        "chosen_path": "comfyui",
        "environment": "Undecided",
        "decision_reason": "",
        "completed_steps": [],
        "step_notes": {},
        "entries": [],
    }


def _check_fields(data: Any, expected: set[str], context: str) -> None:
    if not isinstance(data, dict):
        raise ValueError(f"{context} must be an object.")
    if set(data) != expected:
        missing = expected - set(data)
        extra = set(data) - expected
        details = []
        if missing:
            details.append("missing " + ", ".join(sorted(missing)))
        if extra:
            details.append("unknown fields " + ", ".join(sorted(map(str, extra))))
        raise ValueError(f"{context}: {'; '.join(details)}.")


def _string(value: Any, context: str, limit: int) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{context} must be text.")
    if len(value) > limit:
        raise ValueError(f"{context} must be at most {limit:,} characters.")
    # JSON permits escaped surrogate code points that cannot be exported as UTF-8.
    try:
        value.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"{context} must contain valid Unicode text.") from exc
    return value


def _choice(value: Any, choices: tuple[str, ...], context: str) -> str:
    if not isinstance(value, str) or value not in choices:
        raise ValueError(f"{context} must be one of: {', '.join(choices)}.")
    return value


def _resource(value: Any, context: str) -> str:
    value = _string(value, context, 2_048)
    if not value:
        return value
    if any(char.isspace() or ord(char) < 32 for char in value) or "\\" in value:
        raise ValueError(f"{context} must be a complete HTTP or HTTPS URL without spaces.")
    try:
        parts = urlsplit(value)
        valid = parts.scheme in ("http", "https") and bool(parts.hostname)
        # Accessing port also validates its syntax and numeric range.
        parts.port
    except ValueError:
        valid = False
    if not valid:
        raise ValueError(f"{context} must be blank or a complete HTTP or HTTPS URL.")
    return value


def _json(journey: dict[str, Any]) -> str:
    return json.dumps(journey, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def validate_journey(data: Any) -> dict[str, Any]:
    """Validate all version 1 fields and return a detached, normalized copy.

    No fields are silently defaulted on import. A notes dictionary may contain
    any subset of the known steps, and dates are bounded text for human notes.
    Validation includes the total export size, so every accepted journey can
    be downloaded and subsequently imported under the same size limit.
    """
    _check_fields(data, _FIELDS, "Journey")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValueError("schema_version must be the integer 1.")
    normalized = new_journey()
    normalized["goal"] = _string(data["goal"], "Goal", 4_000)
    normalized["output_kind"] = _choice(data["output_kind"], OUTPUT_KINDS, "Output kind")
    normalized["chosen_path"] = _choice(data["chosen_path"], PATH_IDS, "Chosen path")
    normalized["environment"] = _choice(data["environment"], ENVIRONMENTS, "Environment")
    normalized["decision_reason"] = _string(data["decision_reason"], "Decision reason", 10_000)

    steps = data["completed_steps"]
    if not isinstance(steps, list) or len(steps) > len(STEP_IDS):
        raise ValueError("Completed steps must be a list of known, unique steps.")
    for step in steps:
        _choice(step, STEP_IDS, "Completed step")
    if len(steps) != len(set(steps)):
        raise ValueError("Completed steps must not contain duplicates.")
    normalized["completed_steps"] = [step for step in STEP_IDS if step in steps]

    notes = data["step_notes"]
    if not isinstance(notes, dict):
        raise ValueError("Step notes must be an object keyed by step ID.")
    for step, note in notes.items():
        _choice(step, STEP_IDS, "Step notes key")
        normalized["step_notes"][step] = _string(note, f"Notes for {step}", 20_000)

    entries = data["entries"]
    if not isinstance(entries, list) or len(entries) > MAX_ENTRIES:
        raise ValueError(f"Entries must be a list of at most {MAX_ENTRIES} observations.")
    for index, entry in enumerate(entries, start=1):
        context = f"Entry {index}"
        _check_fields(entry, _ENTRY_FIELDS, context)
        normalized["entries"].append({
            "date": _string(entry["date"], f"{context} date", 40),
            "title": _string(entry["title"], f"{context} title", 300),
            "observation": _string(entry["observation"], f"{context} observation", 20_000),
            "next_step": _string(entry["next_step"], f"{context} next step", 10_000),
            "resource": _resource(entry["resource"], f"{context} resource"),
        })
    if len(_json(normalized).encode("utf-8")) > MAX_IMPORT_BYTES:
        raise ValueError("Journey exceeds the 1 MiB portable file limit; shorten or archive some notes.")
    return normalized


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON field: {key}.")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"Invalid JSON number: {value}.")


def loads_journey(raw: str | bytes) -> dict[str, Any]:
    """Import UTF-8 JSON with a 1 MiB limit and strict duplicate-key checks."""
    if not isinstance(raw, (str, bytes)):
        raise ValueError("Journey file must be JSON text or UTF-8 bytes.")
    try:
        size = len(raw) if isinstance(raw, bytes) else len(raw.encode("utf-8"))
        if size > MAX_IMPORT_BYTES:
            raise ValueError("Journey file must be at most 1 MiB.")
        decoded = raw.decode("utf-8-sig") if isinstance(raw, bytes) else raw.lstrip("\ufeff")
        data = json.loads(decoded, object_pairs_hook=_unique_object, parse_constant=_reject_constant)
    except UnicodeError as exc:
        raise ValueError("Journey file must contain valid UTF-8 text.") from exc
    except (json.JSONDecodeError, RecursionError) as exc:
        raise ValueError("Journey file is not valid, reasonably nested JSON.") from exc
    return validate_journey(data)


def dumps_journey(journey: Any) -> str:
    """Export a validated journey as readable UTF-8-compatible JSON."""
    return _json(validate_journey(journey))


def _markdown_text(value: str) -> str:
    """Preserve personal notes as text instead of executable HTML or images."""
    value = html.escape(value, quote=False)
    return re.sub(r"([\\`*_{}\[\]()#+.!|~>-])", r"\\\1", value)


def journey_markdown(journey: Any) -> str:
    """Export a readable learning journal, escaping all user-authored text."""
    journey = validate_journey(journey)
    plain = _markdown_text
    lines = [
        "# My AI-assisted 3D and video journey",
        "",
        f"**Goal:** {plain(journey['goal']) or 'Not recorded'}",
        "",
        f"**Output:** {plain(journey['output_kind'])}",
        "",
        f"**Chosen path:** {_PATH_LABELS[journey['chosen_path']]}",
        "",
        f"**Environment:** {journey['environment']}",
        "",
        f"**Why this path:** {plain(journey['decision_reason']) or 'Not recorded'}",
        "",
        "## Progress",
        "",
    ]
    for step in STEP_IDS:
        checked = "x" if step in journey["completed_steps"] else " "
        lines.append(f"- [{checked}] {_STEP_LABELS[step]}")
    for step in STEP_IDS:
        note = journey["step_notes"].get(step, "")
        if note:
            lines.extend(["", f"### {_STEP_LABELS[step]}", "", plain(note)])
    lines.extend(["", "## Field notes", ""])
    if not journey["entries"]:
        lines.append("No observations recorded yet.")
    for index, entry in enumerate(journey["entries"], start=1):
        lines.extend([
            f"### Observation {index}", "",
            f"**Date:** {plain(entry['date']) or 'Not recorded'}", "",
            f"**Title:** {plain(entry['title']) or 'Untitled'}", "",
            plain(entry["observation"]) or "No observation recorded.", "",
            f"**Next step:** {plain(entry['next_step']) or 'Not recorded'}", "",
        ])
        if entry["resource"]:
            lines.extend([f"**Resource:** {plain(entry['resource'])}", ""])
    lines.extend([
        "", "## Routes to revisit", "",
        "AUTOMATIC1111, Forge UI, Invoke, and ComfyUI remain available choices.",
        "This console currently develops the ComfyUI learning path.", "",
    ])
    return "\n".join(lines)
