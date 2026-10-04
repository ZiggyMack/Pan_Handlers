"""Scene worksheets remain safe, complete, and portable through v1 journals."""

import copy
import unittest

from Help.journey import dumps_journey, journey_markdown, loads_journey, new_journey, validate_journey
from Help.scene_plan import (
    CHALLENGES, INSPIRATION_URL, new_plan, plan_markdown, plan_to_entry, validate_plan,
)


def filled_plan(**changes):
    plan = new_plan()
    plan.update({
        "title": "Cafe close-up",
        "source": r"D:\Footage\scene.mp4",
        "approach": "lipsync",
        "start_seconds": 12.5,
        "duration_seconds": 8,
        "speaker": "Speaker A",
        "replacement_line": "00:00–00:04 | I already brought the coffee.\n00:04–00:08 | What happens next?",
        "voice_source": "Recorded performance",
        "preserve": "Keep the framing and cafe background.",
        "challenges": ["Fast motion", "Cuts"],
        "audio_seconds": 7.25,
        "status": "Audio baseline saved",
        "result_notes": "Checked the dub; lips do not match yet.",
        "next_step": "Test one mouth edit and compare the unedited frames.",
    })
    plan.update(changes)
    return plan


class ScenePlanTests(unittest.TestCase):
    def test_incomplete_draft_is_valid_but_cannot_be_saved_as_a_recipe(self):
        plan = new_plan()
        self.assertEqual(validate_plan(plan), plan)
        self.assertIn("Not recorded", plan_markdown(plan))
        for changes in ({}, {"source": "clip.mp4"}, {"replacement_line": "Hello"},
                        {"source": " \n", "replacement_line": "Hello"}):
            with self.subTest(changes=changes), self.assertRaisesRegex(ValueError, "source clip"):
                plan_to_entry(dict(plan, **changes))

    def test_each_session_and_validated_plan_own_their_lists(self):
        original = new_plan()
        original["challenges"].append("Cuts")
        self.assertEqual(new_plan()["challenges"], [])
        validated = validate_plan(original)
        validated["challenges"].append("Fast motion")
        self.assertEqual(original["challenges"], ["Cuts"])
        normalized = validate_plan(filled_plan())
        self.assertEqual(normalized["challenges"], ["Cuts", "Fast motion"])
        self.assertIs(type(normalized["duration_seconds"]), float)

    def test_all_plan_fields_survive_existing_journal_export_and_restore(self):
        plan = filled_plan()
        before = copy.deepcopy(plan)
        entry = plan_to_entry(plan)
        journal = new_journey()
        journal["entries"].append(entry)
        restored = loads_journey(dumps_journey(journal).encode("utf-8"))
        self.assertEqual(restored, validate_journey(journal))
        self.assertEqual(restored["completed_steps"], [])
        self.assertEqual(restored["entries"][0], entry)
        self.assertEqual(entry["resource"], INSPIRATION_URL)
        self.assertIn("Scene rewrite plan", journey_markdown(restored))
        for field, value in plan.items():
            values = value if isinstance(value, list) else [value]
            for expected in values:
                with self.subTest(field=field):
                    self.assertIn(str(expected), entry["observation"])
        self.assertIn("Status (self-reported)", entry["observation"])
        self.assertIn("does not generate or edit media", entry["observation"])
        self.assertEqual(plan, before)

    def test_fractional_clip_timings_are_not_rounded_in_the_recipe(self):
        plan = filled_plan(start_seconds=12345.678901, duration_seconds=8.123456789,
                           audio_seconds=7.987654321)
        entry = plan_to_entry(plan)
        markdown = plan_markdown(plan)
        for field in ("start_seconds", "duration_seconds", "audio_seconds"):
            with self.subTest(field=field):
                self.assertIn(str(plan[field]), entry["observation"])
                self.assertIn(str(plan[field]).replace(".", "\\."), markdown)

    def test_field_shapes_enums_and_unknown_data_are_rejected(self):
        invalid = [None, [], {**new_plan(), "future": "do not lose me"}]
        missing = new_plan()
        del missing["source"]
        invalid.append(missing)
        for field, value in (
            ("title", []), ("approach", "automatic"), ("approach", {}),
            ("voice_source", "Unknown"), ("status", "Generated"),
            ("challenges", "Cuts"), ("challenges", ["Cuts", "Cuts"]),
            ("challenges", ["Unlisted"]), ("challenges", [{}]),
        ):
            invalid.append(dict(new_plan(), **{field: value}))
        for candidate in invalid:
            with self.subTest(candidate=candidate), self.assertRaises(ValueError):
                validate_plan(candidate)

    def test_timing_rejects_nonfinite_boolean_and_out_of_range_values(self):
        for field in ("start_seconds", "duration_seconds", "audio_seconds"):
            for value in (True, False, None, "8", float("nan"), float("inf"), float("-inf"), -0.1, 10 ** 400):
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    validate_plan(dict(new_plan(), **{field: value}))
        for field, value in (("duration_seconds", 0), ("start_seconds", 86400.1),
                             ("duration_seconds", 600.1), ("audio_seconds", 600.1)):
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                validate_plan(dict(new_plan(), **{field: value}))
        self.assertEqual(validate_plan(filled_plan(start_seconds=86400, duration_seconds=600, audio_seconds=600))["audio_seconds"], 600)

    def test_character_limits_keep_the_largest_plan_within_journal_limits(self):
        limits = {"title": 200, "source": 2000, "speaker": 200, "replacement_line": 5000,
                  "preserve": 2000, "result_notes": 3000, "next_step": 1000}
        for field, limit in limits.items():
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_plan(filled_plan(**{field: "x" * (limit + 1)}))
        longest = filled_plan(**{field: "界" * limit for field, limit in limits.items()})
        longest["challenges"] = list(CHALLENGES)
        entry = plan_to_entry(longest)
        self.assertLessEqual(len(entry["observation"]), 20_000)
        self.assertLessEqual(len(entry["title"]), 300)
        journal = dict(new_journey(), entries=[entry])
        self.assertEqual(loads_journey(dumps_journey(journal)), journal)
        with self.assertRaisesRegex(ValueError, "Unicode"):
            validate_plan(filled_plan(source="\ud800"))

    def test_markdown_keeps_user_markup_and_source_paths_inert(self):
        attack = '<img src="https://tracker.test/pixel">\n![leak](https://tracker.test/x)\n# injected'
        plan = filled_plan(source=attack, replacement_line=attack, title="<script>test</script>")
        before = copy.deepcopy(plan)
        markdown = plan_markdown(plan)
        self.assertNotIn("<img", markdown)
        self.assertNotIn("<script>", markdown)
        self.assertNotIn("![leak]", markdown)
        self.assertNotIn("\n# injected", markdown)
        self.assertIn("&lt;img", markdown)
        self.assertIn(f"[Inspiration reference]({INSPIRATION_URL})", markdown)
        entry = plan_to_entry(plan)
        self.assertEqual(entry["resource"], INSPIRATION_URL)
        self.assertIn(attack, entry["observation"])
        self.assertEqual(plan, before)


if __name__ == "__main__":
    unittest.main()
