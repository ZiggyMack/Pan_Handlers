"""Portable video experiment plans and explicit, context-bound take reviews.

This module records human decisions. It does not inspect media, verify a cloud
installation, render a workflow, or certify that a review is correct.
"""

from __future__ import annotations

from datetime import datetime, timezone
import html
import json
import re
from typing import Any


MATERIALS = {
    "video": "Existing video (.mp4 / .mov)",
    "still": "Still image",
    "scene": "Editable 3D scene (.blend)",
    "mesh": "3D mesh (.glb / .fbx / .obj)",
    "idea": "Idea / no source yet",
}
CHANGES = {
    "look": "Lighting, atmosphere or visual style",
    "setting": "Setting or background",
    "character": "Character or appearance",
    "dialogue": "Spoken dialogue",
    "new_motion": "Generate a new motion or shot",
}
PRESERVE = {
    "motion": "Original motion and performance",
    "camera": "Camera movement and framing",
    "identity": "Character identity",
    "background": "Original background",
    "contact": "Contact between people, animals and objects",
    "audio": "Original audio",
}
REVIEW_CHECKS = {
    "performance": "Motion, performance and requested preserved details hold up",
    "appearance": "The intended visual or dialogue change is convincing",
    "temporal": "Faces, hands, contact and texture remain stable across frames",
    "timing": "Duration, frame rate, cuts and sound are correct",
}
MAX_IMPORT_BYTES = 1_048_576
MAX_TAKES = 30
_TEXT_FIELDS = (
    "source", "reference", "brief", "clip_notes", "workflow_revision",
    "environment_notes", "settings", "estimate",
)
_CONTEXT_FIELDS = {"material", "change", "preserve", *_TEXT_FIELDS} - {"estimate"}
_FIELDS = {"schema_version", *_CONTEXT_FIELDS, "estimate", "takes", "accepted_id"}
_TAKE_FIELDS = {"id", "result", "observations", "checks", "context", "route_id"}
_LABELS = {
    "source": "Source file or asset",
    "reference": "Reference image / audio / control asset",
    "brief": "Requested change",
    "clip_notes": "Clip preparation and preservation notes",
    "workflow_revision": "Exact workflow / model revision",
    "environment_notes": "Cloud environment and dependency checks",
    "settings": "Generation settings / seed",
    "estimate": "Expected runtime / cost (unverified until measured)",
}


def new_plan() -> dict[str, Any]:
    """Return an independent, unfinished plan for a small visual change."""
    return {
        "schema_version": 1,
        "material": "video",
        "change": "look",
        "preserve": ["motion", "camera", "identity", "contact"],
        "source": "",
        "reference": "",
        "brief": "Change only the lighting and atmosphere; preserve the original motion, performance, identity and contact.",
        "clip_notes": "",
        "workflow_revision": "",
        "environment_notes": "",
        "settings": "",
        "estimate": "",
        "takes": [],
        "accepted_id": "",
    }


def _fields(value: Any, expected: set[str], label: str) -> None:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object.")
    missing, extra = expected - set(value), set(value) - expected
    if missing or extra:
        details = []
        if missing:
            details.append("missing " + ", ".join(sorted(missing)))
        if extra:
            details.append("unknown fields " + ", ".join(sorted(map(str, extra))))
        raise ValueError(f"{label}: {'; '.join(details)}.")


def _text(value: Any, label: str, limit: int = 2000, required: bool = False) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{label} must be text.")
    if len(value) > limit:
        raise ValueError(f"{label} must be at most {limit:,} characters.")
    try:
        value.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"{label} must contain valid Unicode text.") from exc
    if required and not value.strip():
        raise ValueError(f"{label} is required; record the actual result and review observations.")
    return value


def _choice(value: Any, choices: dict[str, str], label: str) -> str:
    if not isinstance(value, str) or value not in choices:
        raise ValueError(f"{label} must be one of: {', '.join(choices)}.")
    return value


def _context(data: dict[str, Any]) -> dict[str, Any]:
    """Normalize the details whose changes require a fresh take review."""
    result = {
        "material": _choice(data["material"], MATERIALS, "Starting material"),
        "change": _choice(data["change"], CHANGES, "Requested change"),
    }
    preserve = data["preserve"]
    if not isinstance(preserve, list) or len(preserve) > len(PRESERVE):
        raise ValueError("Preservation choices must be a list of known, unique choices.")
    for item in preserve:
        _choice(item, PRESERVE, "Preservation choice")
    if len(preserve) != len(set(preserve)):
        raise ValueError("Preservation choices must not contain duplicates.")
    result["preserve"] = [item for item in PRESERVE if item in preserve]
    for field in _TEXT_FIELDS:
        if field != "estimate":
            result[field] = _text(data[field], _LABELS[field], 1000 if field == "brief" else 2000)
    return result


def _route(context: dict[str, Any]) -> str:
    material, change = context["material"], context["change"]
    if material in ("scene", "mesh"):
        return "render_first"
    if material == "idea":
        return "brief_first"
    if material == "still" or change == "new_motion":
        return "image_to_video"
    if change == "dialogue":
        return "dialogue"
    if change == "character":
        return "wan_mix" if "background" in context["preserve"] else "wan_animate"
    return "ltx_union"


def route_for(plan: Any) -> str:
    """Choose the next suitable candidate route, not a compatibility guarantee."""
    return _route(_context(validate_plan(plan)))


def contradictions(plan: Any) -> list[str]:
    """Surface choices that need a narrower brief before a paid experiment."""
    plan = validate_plan(plan)
    items = []
    if plan["change"] == "character" and "identity" in plan["preserve"]:
        items.append("Changing the character conflicts with preserving identity. Specify an appearance-only edit, or allow identity to change.")
    if plan["change"] == "setting" and "background" in plan["preserve"]:
        items.append("Changing the setting conflicts with keeping the original background. Specify which background elements may change.")
    if plan["material"] != "video" and "motion" in plan["preserve"]:
        items.append("Motion preservation needs a driving video or a rendered animation. A still image or mesh alone does not supply a performance to preserve.")
    if plan["change"] == "new_motion" and "motion" in plan["preserve"]:
        items.append("A new motion is a new performance. Remove motion preservation or choose a transformation of the existing video.")
    if plan["change"] == "dialogue" and "audio" in plan["preserve"]:
        items.append("Replacing dialogue changes the soundtrack. Specify whether music, ambience or other speakers should remain.")
    return items


def _checks(value: Any) -> dict[str, bool]:
    _fields(value, set(REVIEW_CHECKS), "Review checks")
    if any(type(value[key]) is not bool for key in REVIEW_CHECKS):
        raise ValueError("Every review check must be true or false.")
    return {key: value[key] for key in REVIEW_CHECKS}


def _acceptance_evidence(context: dict[str, Any]) -> None:
    """Acceptance needs a traceable source, request and recipe, even if a
    failure or an early draft was recorded before these details were known.
    """
    missing = [label for field, label in (
        ("source", "source clip / asset reference"),
        ("brief", "requested change"),
        ("workflow_revision", "workflow copy and exact revision"),
    ) if not context[field].strip()]
    if missing:
        raise ValueError("Before accepting a take, record its " + ", ".join(missing) +
                         ". Complete the current plan, then record and review a take with that context.")


def _json(plan: dict[str, Any]) -> str:
    return json.dumps(plan, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def validate_plan(data: Any) -> dict[str, Any]:
    """Validate the complete v1 schema, returning detached nested containers."""
    _fields(data, _FIELDS, "Video plan")
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise ValueError("schema_version must be the integer 1.")
    result = {"schema_version": 1, **_context(data)}
    result["estimate"] = _text(data["estimate"], _LABELS["estimate"])
    if not isinstance(data["takes"], list) or len(data["takes"]) > MAX_TAKES:
        raise ValueError(f"Takes must be a list of at most {MAX_TAKES} records.")
    result["takes"] = []
    ids = set()
    for take in data["takes"]:
        _fields(take, _TAKE_FIELDS, "Take")
        take_id = _text(take["id"], "Take ID", 20)
        if not re.fullmatch(r"take-[0-9]{3,6}", take_id) or int(take_id[5:]) < 1:
            raise ValueError("Take ID must have the form take-001 with a positive number.")
        if take_id in ids:
            raise ValueError("Take IDs must be unique.")
        ids.add(take_id)
        _fields(take["context"], _CONTEXT_FIELDS, "Take context")
        context = _context(take["context"])
        if take["route_id"] != _route(context):
            raise ValueError("Take route must match its recorded context.")
        result["takes"].append({
            "id": take_id,
            "result": _text(take["result"], "Result file / link", required=True),
            "observations": _text(take["observations"], "Review observations", 1000, required=True),
            "checks": _checks(take["checks"]),
            "context": context,
            "route_id": take["route_id"],
        })
    accepted_id = _text(data["accepted_id"], "Accepted take ID", 20)
    if accepted_id:
        accepted = next((take for take in result["takes"] if take["id"] == accepted_id), None)
        if accepted is None:
            raise ValueError("Accepted take ID must refer to a recorded take.")
        if not all(accepted["checks"].values()):
            raise ValueError("An accepted take must have every review check confirmed.")
        _acceptance_evidence(accepted["context"])
    result["accepted_id"] = accepted_id
    if len(_json(result).encode("utf-8")) > MAX_IMPORT_BYTES:
        raise ValueError("Video plan exceeds the 1 MiB portable file limit; archive some takes or shorten notes.")
    return result


def add_take(plan: Any, result: str, observations: str, checks: dict[str, bool]) -> dict[str, Any]:
    """Record an observed result with its exact current context; do not accept it."""
    updated = validate_plan(plan)
    if len(updated["takes"]) >= MAX_TAKES:
        raise ValueError(f"A plan can contain at most {MAX_TAKES} takes.")
    number = max((int(take["id"][5:]) for take in updated["takes"]), default=0) + 1
    context = _context(updated)
    updated["takes"].append({
        "id": f"take-{number:03d}", "result": result,
        "observations": observations, "checks": checks,
        "context": context, "route_id": _route(context),
    })
    return validate_plan(updated)


def accept_take(plan: Any, take_id: str) -> dict[str, Any]:
    """Explicitly accept a reviewed take only for the current experiment context."""
    updated = validate_plan(plan)
    selected = next((take for take in updated["takes"] if take["id"] == take_id), None)
    if selected is None:
        raise ValueError("Choose a recorded take to accept.")
    if not all(selected["checks"].values()):
        raise ValueError("Confirm every review check before accepting a take.")
    if selected["context"] != _context(updated):
        raise ValueError("This take belongs to an earlier plan. Record and review a take for the current source, brief, workflow, environment and settings.")
    _acceptance_evidence(selected["context"])
    updated["accepted_id"] = take_id
    return validate_plan(updated)


def current_accepted(plan: Any) -> dict[str, Any] | None:
    """Return a detached accepted take, or None when absent or stale."""
    normalized = validate_plan(plan)
    context = _context(normalized)
    return next((take for take in normalized["takes"]
                 if take["id"] == normalized["accepted_id"] and take["context"] == context), None)


def dumps_plan(plan: Any) -> str:
    """Export a complete editable plan, including historical take contexts."""
    return _json(validate_plan(plan))


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON field: {key}.")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"Invalid JSON number: {value}.")


def loads_plan(raw: str | bytes) -> dict[str, Any]:
    """Import UTF-8 JSON, rejecting duplicate fields and incompatible schemas."""
    if not isinstance(raw, (str, bytes)):
        raise ValueError("Video plan must be JSON text or UTF-8 bytes.")
    try:
        size = len(raw) if isinstance(raw, bytes) else len(raw.encode("utf-8"))
        if size > MAX_IMPORT_BYTES:
            raise ValueError("Video plan file must be at most 1 MiB.")
        decoded = raw.decode("utf-8-sig") if isinstance(raw, bytes) else raw.lstrip("\ufeff")
        data = json.loads(decoded, object_pairs_hook=_unique_object, parse_constant=_reject_constant)
    except UnicodeError as exc:
        raise ValueError("Video plan must contain valid UTF-8 text.") from exc
    except (json.JSONDecodeError, RecursionError) as exc:
        raise ValueError("Video plan must be valid, reasonably nested JSON.") from exc
    return validate_plan(data)


def _plain(value: str) -> str:
    value = html.escape(value, quote=False)
    return re.sub(r"([\\`*_{}\[\]()#+.!|~>-])", r"\\\1", value)


def _context_lines(context: dict[str, Any], escape: bool) -> list[str]:
    text = _plain if escape else str
    lines = [
        f"Material: {MATERIALS[context['material']]}",
        f"Change: {CHANGES[context['change']]}",
        "Preserve: " + (", ".join(PRESERVE[key] for key in context["preserve"]) or "No constraints recorded"),
    ]
    for field in _TEXT_FIELDS:
        if field in context:
            lines.extend(["", f"{_LABELS[field]}: {text(context[field]) or 'Not recorded'}"])
    return lines


def _report(plan: dict[str, Any], escape: bool) -> str:
    text = _plain if escape else str
    accepted = current_accepted(plan)
    status = (f"Accepted for this plan: {plan['accepted_id']} (human review)" if accepted
              else f"Earlier acceptance is stale: {plan['accepted_id']}; review a current take before finishing."
              if plan["accepted_id"] else "No accepted take. Preview and review are still required.")
    lines = ["# Video experiment plan", "", "Planning and self-reported evidence; this guide does not render or inspect media.", "",
             f"Schema version: {plan['schema_version']}", f"Candidate route: {_route(plan)}", "", status, "",
             *_context_lines(plan, escape), "", "## Recorded takes", ""]
    if not plan["takes"]:
        lines.append("No result recorded.")
    for take in plan["takes"]:
        lines.extend([f"### {take['id']}", "", f"Candidate route: {take['route_id']}", "",
                      f"Result: {text(take['result'])}", "", f"Observations: {text(take['observations'])}", ""])
        for key, label in REVIEW_CHECKS.items():
            lines.append(f"- [{'x' if take['checks'][key] else ' '}] {label}")
        lines.extend(["", "Recorded context:", "", *_context_lines(take["context"], escape), ""])
    lines.extend(["", "## Next handoff", "", _next_step(plan), "",
                  "The JSON plan restores editable fields and take history. A field-journal entry is a readable snapshot only.", ""])
    return "\n".join(lines)


def _next_step(plan: dict[str, Any]) -> str:
    if current_accepted(plan):
        return "Use the accepted take as the finishing source. Make and inspect an HD master, then a separately reviewed 4K derivative; do not treat upscaling as new captured detail."
    if plan["accepted_id"]:
        return "The plan changed after acceptance. Record and review a take under the current source, brief, workflow, environment and settings before finishing."
    return "Verify the candidate workflow and cloud dependencies, run one bounded preview, record its actual result and compare it against the original before accepting a take."


def plan_markdown(plan: Any) -> str:
    """Readable complete report with inert user-authored text and every snapshot."""
    return _report(validate_plan(plan), escape=True)


def plan_entry(plan: Any) -> dict[str, str]:
    """Create a bounded journal-v1 snapshot without claiming editable restoration."""
    plan = validate_plan(plan)
    observation = _report(plan, escape=False)
    if len(observation) > 20_000:
        # Full history can legitimately exceed a journal entry's limit. Preserve
        # the current brief and review status, identify every result, and state
        # exactly which details require the downloadable JSON/Markdown plan.
        accepted = current_accepted(plan)
        status = (f"Accepted for current context: {plan['accepted_id']} (human review)." if accepted
                  else f"Acceptance stale: {plan['accepted_id']}." if plan["accepted_id"]
                  else "No accepted take.")
        lines = ["Video experiment plan — bounded journal summary", "",
                 "Full take contexts and full observations are in the separately downloaded JSON / Markdown plan. This summary cannot restore editable fields.", "",
                 f"Candidate route: {_route(plan)}", status, "", *_context_lines(plan, False), "", "Take summary:"]
        for take in plan["takes"]:
            result = take["result"][:100] + ("… [truncated]" if len(take["result"]) > 100 else "")
            note = take["observations"][:60] + ("… [truncated]" if len(take["observations"]) > 60 else "")
            lines.append(f"{take['id']} | {take['route_id']} | {sum(take['checks'].values())}/4 checks | {result} | {note}")
        observation = "\n".join(lines)
        # The current context is bounded to 15,000 characters; 30 summaries can
        # still exceed the journal ceiling. Explicitly truncate this summary.
        if len(observation) > 20_000:
            observation = observation[:19_850] + "\n[Summary shortened to fit the journal; download the complete JSON / Markdown plan.]"
    return {
        "date": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "title": "Video experiment: " + CHANGES[plan["change"]],
        "observation": observation,
        "next_step": _next_step(plan),
        "resource": "",
    }
