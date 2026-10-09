"""Behavior checks for the portable journal and untrusted file boundary."""

import copy
import json
import unittest

from Help.state.journey import (
    MAX_IMPORT_BYTES,
    STEP_IDS,
    dumps_journey,
    journey_markdown,
    loads_journey,
    new_journey,
    validate_journey,
)


def observation(**changes):
    entry = {
        "date": "2026-09-12",
        "title": "A first workflow",
        "observation": "Fixed the seed; saved the workflow with the image.",
        "next_step": "Compare the next frame.",
        "resource": "https://docs.comfy.org/get_started/introduction",
    }
    entry.update(changes)
    return entry


class JourneyTests(unittest.TestCase):
    def test_personal_journal_survives_json_and_utf8_round_trip(self):
        journey = new_journey()
        journey.update({
            "goal": "Render a café fly-through ☕",
            "output_kind": "Editable 3D + AI",
            "decision_reason": "Repeatability and explicit workflows.",
            "environment": "Cloud",
            "completed_steps": ["first_image", "brief"],
            "step_notes": {"brief": "Keep an editable scene."},
            "entries": [observation()],
        })
        restored = loads_journey(dumps_journey(journey).encode("utf-8"))
        self.assertEqual(restored["goal"], journey["goal"])
        self.assertEqual(restored["entries"], journey["entries"])
        self.assertEqual(restored["completed_steps"], ["brief", "first_image"])
        self.assertEqual(restored, loads_journey(dumps_journey(restored)))

    def test_fresh_data_cannot_modify_original_or_another_session(self):
        original = new_journey()
        original["entries"].append(observation())
        original["step_notes"]["setup"] = "Use a cloud instance."
        validated = validate_journey(original)
        validated["entries"][0]["title"] = "Changed"
        validated["step_notes"]["setup"] = "Changed"
        validated["completed_steps"].append("setup")
        self.assertEqual(original["entries"][0]["title"], "A first workflow")
        self.assertEqual(original["step_notes"]["setup"], "Use a cloud instance.")
        self.assertEqual(original["completed_steps"], [])
        self.assertEqual(new_journey()["entries"], [])

    def test_missing_unknown_and_wrong_version_fields_are_rejected(self):
        for mutation in (
            lambda j: j.pop("goal"),
            lambda j: j.update({"future_field": "Do not silently discard me"}),
            lambda j: j.update({"schema_version": True}),
            lambda j: j.update({"schema_version": 1.0}),
            lambda j: j.update({"schema_version": 2}),
        ):
            journey = new_journey()
            mutation(journey)
            with self.subTest(journey=journey), self.assertRaises(ValueError):
                validate_journey(journey)

    def test_invalid_enums_steps_and_shapes_are_rejected(self):
        cases = [
            ("chosen_path", "unlisted"), ("output_kind", "video"),
            ("environment", "cloud"), ("goal", 12),
            ("completed_steps", ["setup", "setup"]),
            ("completed_steps", ["unlisted"]),
            ("completed_steps", [{}]), ("completed_steps", "setup"),
            ("step_notes", {"unlisted": "note"}),
            ("step_notes", {"setup": []}), ("step_notes", []),
            ("entries", {}), ("entries", [None]),
            ("entries", [dict(observation(), extra=True)]),
        ]
        for field, value in cases:
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                validate_journey(dict(new_journey(), **{field: value}))

    def test_resources_require_an_http_host_and_valid_url_syntax(self):
        for resource in (
            "javascript:alert(1)", "file:///private/photo", "https:///missing-host",
            "https://example.com\n![image](https://tracker.test/image)",
            "https://example.com:bad/path", "https://[broken", "https://example.com\\x",
        ):
            journey = new_journey()
            journey["entries"] = [observation(resource=resource)]
            with self.subTest(resource=resource), self.assertRaises(ValueError):
                validate_journey(journey)
        for resource in ("", "http://localhost:8188", "https://docs.comfy.org/?a=1#intro"):
            journey = new_journey()
            journey["entries"] = [observation(resource=resource)]
            self.assertEqual(validate_journey(journey)["entries"][0]["resource"], resource)

    def test_import_rejects_malformed_utf8_duplicate_fields_and_nonstandard_json(self):
        for raw in (
            b"\xff", "{", "[]", '{"schema_version": 1, "schema_version": 1}',
            '{"goal": NaN}', "[" * 2_000 + "]" * 2_000,
        ):
            with self.subTest(raw=repr(raw[:80])), self.assertRaises(ValueError):
                loads_journey(raw)
        nested_duplicate = dumps_journey(dict(new_journey(), entries=[observation()])).replace(
            '"title": "A first workflow",', '"title": "First", "title": "Second",'
        )
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            loads_journey(nested_duplicate)
        self.assertEqual(loads_journey(b"\xef\xbb\xbf" + dumps_journey(new_journey()).encode()), new_journey())

    def test_total_bytes_and_per_field_limits_apply_to_import_and_export(self):
        with self.assertRaisesRegex(ValueError, "1 MiB"):
            loads_journey(b" " * (MAX_IMPORT_BYTES + 1))
        # UTF-8 byte count is larger than the Python character count.
        with self.assertRaisesRegex(ValueError, "1 MiB"):
            loads_journey("☕" * (MAX_IMPORT_BYTES // 3 + 1))
        for changes in (
            {"goal": "x" * 4_001},
            {"step_notes": {"setup": "x" * 20_001}},
            {"entries": [observation()] * 301},
            {"entries": [observation(observation="x" * 20_000)] * 60},
            {"goal": "\ud800"},
        ):
            with self.subTest(fields=list(changes)), self.assertRaises(ValueError):
                dumps_journey(dict(new_journey(), **changes))

    def test_markdown_export_includes_progress_and_escapes_user_markup(self):
        attack = '<img src="https://tracker.test/pixel">\n![leak](https://tracker.test/x)\n# injected'
        journey = new_journey()
        journey.update({
            "goal": attack,
            "completed_steps": ["brief", "setup"],
            "step_notes": {"setup": attack},
            "entries": [observation(title=attack, observation=attack)],
        })
        original = copy.deepcopy(journey)
        markdown = journey_markdown(journey)
        self.assertIn("- [x] Define the shot", markdown)
        self.assertIn("- [ ] Generate a first image", markdown)
        self.assertIn("AUTOMATIC1111, Forge UI, Invoke, and ComfyUI", markdown)
        self.assertNotIn("<img", markdown)
        self.assertNotIn("![leak]", markdown)
        self.assertNotIn("\n# injected", markdown)
        self.assertIn("&lt;img", markdown)
        self.assertEqual(journey, original)
        self.assertEqual(markdown.count("- ["), len(STEP_IDS))


if __name__ == "__main__":
    unittest.main()
