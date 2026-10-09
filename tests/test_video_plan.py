"""Route selection, reviewed evidence and portable video experiment state."""

import copy
import json
import unittest

from Help.state.journey import dumps_journey, loads_journey, new_journey
from Help.state.video_plan import (
    MATERIALS, MAX_IMPORT_BYTES, REVIEW_CHECKS, accept_take, add_take,
    contradictions, current_accepted, dumps_plan, loads_plan, new_plan,
    plan_entry, plan_markdown, route_for, validate_plan,
)


def reviewed_plan():
    plan = new_plan()
    plan.update({
        "source": r"D:\Footage\woman-and-wolf.mp4",
        "reference": r"D:\Footage\lighting-reference.png",
        "clip_notes": "A two-second continuous excerpt; preserve paw and hand contact.",
        "workflow_revision": "Candidate template revision recorded before execution",
        "environment_notes": "Cloud session; exact dependencies checked by operator",
        "settings": "Seed 18446744073709551615; FPS and duration match the source",
    })
    return add_take(plan, "D:/Renders/preview-001.mp4", "Motion and contact checked against the source; lighting changed as requested.",
                    dict.fromkeys(REVIEW_CHECKS, True))


class VideoPlanTests(unittest.TestCase):
    def test_routes_prioritize_available_material_and_preservation(self):
        cases = [
            ({}, "ltx_union"),
            ({"change": "setting"}, "ltx_union"),
            ({"change": "character", "preserve": ["motion", "background"]}, "wan_mix"),
            ({"change": "character", "preserve": ["motion"]}, "wan_animate"),
            ({"change": "dialogue"}, "dialogue"),
            ({"change": "new_motion"}, "image_to_video"),
        ]
        for material, route in (("still", "image_to_video"), ("scene", "render_first"),
                                ("mesh", "render_first"), ("idea", "brief_first")):
            for change in ("look", "dialogue", "character", "new_motion"):
                cases.append(({"material": material, "change": change}, route))
        for changes, expected in cases:
            with self.subTest(changes=changes):
                self.assertEqual(route_for(dict(new_plan(), **changes)), expected)

    def test_conflicting_intent_is_visible_without_blocking_saved_drafts(self):
        self.assertEqual(contradictions(new_plan()), [])
        for changes, phrase in (
            ({"change": "character"}, "identity"),
            ({"change": "setting", "preserve": ["background"]}, "background"),
            ({"material": "still"}, "driving video"),
            ({"change": "new_motion"}, "new performance"),
            ({"change": "dialogue", "preserve": ["audio"]}, "soundtrack"),
        ):
            with self.subTest(changes=changes):
                plan = dict(new_plan(), **changes)
                self.assertIn(phrase, " ".join(contradictions(plan)))
                self.assertEqual(loads_plan(dumps_plan(plan)), validate_plan(plan))

    def test_take_evidence_and_every_boolean_review_are_required(self):
        all_checks = dict.fromkeys(REVIEW_CHECKS, True)
        for result, notes in (("", "reviewed"), ("clip.mp4", " \n")):
            with self.subTest(result=result), self.assertRaisesRegex(ValueError, "required"):
                add_take(new_plan(), result, notes, all_checks)
        for invalid in ({}, {**all_checks, "extra": True}, {**all_checks, "timing": 1}):
            with self.subTest(checks=invalid), self.assertRaises(ValueError):
                add_take(new_plan(), "clip.mp4", "Observed the actual clip.", invalid)
        incomplete = add_take(new_plan(), "clip.mp4", "Timing still needs review.", {**all_checks, "timing": False})
        self.assertIsNone(current_accepted(incomplete))
        with self.assertRaisesRegex(ValueError, "every review"):
            accept_take(incomplete, "take-001")
        with self.assertRaisesRegex(ValueError, "every review"):
            validate_plan(dict(incomplete, accepted_id="take-001"))
        with self.assertRaises(ValueError):
            accept_take(incomplete, "take-999")

    def test_acceptance_is_explicit_and_invalidated_by_relevant_changes(self):
        pending = reviewed_plan()
        self.assertIsNone(current_accepted(pending))
        accepted = accept_take(pending, "take-001")
        self.assertEqual(current_accepted(accepted)["id"], "take-001")
        self.assertEqual(pending["accepted_id"], "")
        edits = {
            "source": "another.mp4", "reference": "another.png", "brief": "Different lighting",
            "clip_notes": "Use the last two seconds", "workflow_revision": "A newer template",
            "environment_notes": "Different cloud runtime", "settings": "Seed 99",
            "material": "still", "change": "setting", "preserve": ["motion"],
        }
        for key, value in edits.items():
            with self.subTest(key=key):
                stale = dict(accepted, **{key: value})
                self.assertIsNone(current_accepted(stale))
                self.assertEqual(loads_plan(dumps_plan(stale))["accepted_id"], "take-001")
                with self.assertRaisesRegex(ValueError, "earlier plan"):
                    accept_take(stale, "take-001")
                self.assertIn("stale", plan_markdown(stale))
                self.assertIn("plan changed", plan_entry(stale)["next_step"])
        # Updating a price estimate or changing the order of identical choices
        # does not change the recipe represented by an already reviewed result.
        cost_update = dict(accepted, estimate="Measured cloud charge recorded later")
        self.assertIsNotNone(current_accepted(cost_update))
        reordered = dict(accepted, preserve=list(reversed(accepted["preserve"])))
        self.assertIsNotNone(current_accepted(reordered))

    def test_acceptance_needs_traceable_context_but_failure_records_stay_flexible(self):
        all_checks = dict.fromkeys(REVIEW_CHECKS, True)
        for field in ("source", "brief", "workflow_revision"):
            with self.subTest(field=field):
                plan = reviewed_plan()
                plan["takes"] = []
                plan[field] = " \n"
                # Drafts and observed failures need not already be reproducible.
                plan = add_take(plan, "preview.mp4", "The operator inspected this result.", all_checks)
                self.assertEqual(loads_plan(dumps_plan(plan)), plan)
                with self.assertRaisesRegex(ValueError, "Before accepting"):
                    accept_take(plan, "take-001")
                # Importing a manually fabricated approval cannot bypass the
                # same requirements enforced by the UI's accept operation.
                plan["accepted_id"] = "take-001"
                with self.assertRaisesRegex(ValueError, "Before accepting"):
                    loads_plan(json.dumps(plan))
        accepted = accept_take(reviewed_plan(), "take-001")
        # Clearing a working field invalidates current approval without making
        # the old, complete evidence impossible to save or restore.
        accepted["source"] = ""
        self.assertIsNone(current_accepted(loads_plan(dumps_plan(accepted))))

    def test_new_takes_snapshot_each_context_without_mutating_prior_state(self):
        first = reviewed_plan()
        frozen = copy.deepcopy(first)
        second = add_take(dict(first, settings="Seed 43"), "second.mp4", "Contact slips in the final frame.",
                          dict.fromkeys(REVIEW_CHECKS, False))
        self.assertEqual([take["id"] for take in second["takes"]], ["take-001", "take-002"])
        self.assertNotEqual(second["takes"][0]["context"]["settings"], second["takes"][1]["context"]["settings"])
        second["takes"][0]["context"]["preserve"].clear()
        self.assertEqual(first, frozen)
        self.assertEqual(new_plan()["takes"], [])
        detached = current_accepted(accept_take(first, "take-001"))
        detached["context"]["preserve"].clear()
        self.assertEqual(first, frozen)

    def test_complete_editable_history_roundtrips_through_json(self):
        plan = accept_take(reviewed_plan(), "take-001")
        plan["source"] += " — 雨"
        before = copy.deepcopy(plan)
        encoded = dumps_plan(plan)
        restored = loads_plan(encoded.encode("utf-8"))
        self.assertEqual(restored, validate_plan(plan))
        self.assertIsNone(current_accepted(restored))
        self.assertEqual(plan, before)
        self.assertIn("18446744073709551615", encoded)
        self.assertEqual(loads_plan(b"\xef\xbb\xbf" + encoded.encode("utf-8")), restored)
        entry = plan_entry(plan)
        journey = dict(new_journey(), entries=[entry])
        self.assertEqual(loads_journey(dumps_journey(journey)), journey)
        self.assertEqual(journey["completed_steps"], [])

    def test_strict_imports_reject_unknown_duplicate_nonfinite_and_invalid_text(self):
        base = dumps_plan(new_plan())
        invalid_json = [
            base.replace('"schema_version": 1', '"schema_version": 1, "schema_version": 1'),
            base.replace('"estimate": ""', '"estimate": NaN'),
            base.replace('"estimate": ""', '"estimate": Infinity'),
            b"\xff", "[", "[" * 1100 + "]" * 1100,
            " " * (MAX_IMPORT_BYTES + 1),
        ]
        for candidate in invalid_json:
            with self.subTest(candidate=str(candidate)[:80]), self.assertRaises(ValueError):
                loads_plan(candidate)
        invalid = [None, [], {**new_plan(), "extra": 1}, {**new_plan(), "schema_version": True}]
        missing = new_plan()
        del missing["estimate"]
        invalid.append(missing)
        for changes in (
            {"material": {}}, {"change": "magic"}, {"preserve": "motion"},
            {"preserve": ["motion", "motion"]}, {"preserve": [{}]},
            {"brief": "x" * 1001}, {"source": "x" * 2001}, {"source": "\ud800"},
            {"takes": {}}, {"accepted_id": "take-001"},
        ):
            invalid.append(dict(new_plan(), **changes))
        for candidate in invalid:
            with self.subTest(candidate=str(candidate)[:80]), self.assertRaises(ValueError):
                validate_plan(candidate)
        valid_take = reviewed_plan()
        for mutation in ("route", "context", "duplicate", "missing", "observations"):
            bad = copy.deepcopy(valid_take)
            if mutation == "route":
                bad["takes"][0]["route_id"] = "wan_animate"
            elif mutation == "context":
                bad["takes"][0]["context"]["extra"] = "future data"
            elif mutation == "duplicate":
                bad["takes"].append(copy.deepcopy(bad["takes"][0]))
            elif mutation == "missing":
                del bad["takes"][0]["result"]
            else:
                bad["takes"][0]["observations"] = "x" * 1001
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                loads_plan(json.dumps(bad))

    def test_large_history_has_bounded_journal_summary_and_complete_download(self):
        plan = new_plan()
        plan["source"] = "界" * 2000
        plan["workflow_revision"] = "Recorded template revision and pinned model files"
        for index in range(30):
            plan = add_take(plan, f"clip-{index}.mp4", "Observed " + "界" * 990,
                            dict.fromkeys(REVIEW_CHECKS, True))
        with self.assertRaisesRegex(ValueError, "at most 30"):
            add_take(plan, "overflow.mp4", "Observed", dict.fromkeys(REVIEW_CHECKS, True))
        plan = accept_take(plan, "take-030")
        entry = plan_entry(plan)
        self.assertLessEqual(len(entry["observation"]), 20_000)
        self.assertIn("bounded journal summary", entry["observation"])
        self.assertIn("separately downloaded", entry["observation"])
        self.assertIn("take-030", entry["observation"])
        self.assertIn("HD master", entry["next_step"])
        self.assertEqual(loads_plan(dumps_plan(plan)), plan)
        self.assertGreater(len(plan_markdown(plan)), 20_000)
        journey = dict(new_journey(), entries=[entry])
        self.assertEqual(loads_journey(dumps_journey(journey)), journey)

    def test_markdown_keeps_all_user_markup_inert_including_historical_context(self):
        attack = '<img src="https://tracker.test/pixel">\n![leak](https://tracker.test/x)\n# injected'
        plan = new_plan()
        for key in ("source", "reference", "brief", "clip_notes", "workflow_revision", "environment_notes", "settings", "estimate"):
            plan[key] = attack
        plan = add_take(plan, attack, attack, dict.fromkeys(REVIEW_CHECKS, True))
        plan["source"] = "new.mp4"
        report = plan_markdown(plan)
        self.assertNotIn("<img", report)
        self.assertNotIn("![leak]", report)
        self.assertNotIn("\n# injected", report)
        self.assertIn("&lt;img", report)
        self.assertIn("new\\.mp4", report)
        self.assertIn("Recorded context", report)


if __name__ == "__main__":
    unittest.main()
