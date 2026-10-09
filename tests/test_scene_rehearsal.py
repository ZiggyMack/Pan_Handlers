"""The proposed scene exercise stays separate from learner evidence and drafts."""

from copy import deepcopy
from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest

from Help.state.journey import dumps_journey, loads_journey
from Help.pages.rewrite_scene import _guide_markdown


APP = Path(__file__).resolve().parents[1] / "Help" / "app.py"


class SceneRehearsalTests(unittest.TestCase):
    def scene_app(self):
        app = AppTest.from_file(str(APP), default_timeout=20).run()
        app.button(key="help_nav_Rewrite a scene").click().run()
        self.assertFalse(list(app.exception))
        return app

    def test_timing_tolerance_handles_decimal_boundary_in_both_directions(self):
        app = self.scene_app()
        for shot, wav, aligned in ((8.2, 8.3, True), (8.3, 8.2, True),
                                   (8.2, 8.4, False), (8.4, 8.2, False)):
            with self.subTest(shot=shot, wav=wav):
                app.number_input(key="help_scene_widget_duration_seconds").set_value(shot).run()
                app.number_input(key="help_scene_widget_audio_seconds").set_value(wav).run()
                self.assertFalse(list(app.exception))
                warnings = [item.value for item in app.warning if "The exported replacement WAV is" in item.value]
                self.assertEqual(bool(warnings), not aligned)
                self.assertEqual(any("durations align within 0.1" in item.value for item in app.info), aligned)
                if warnings:
                    self.assertIn("0.2 seconds", warnings[0])
                    self.assertIn("including silence", warnings[0])

    def test_rehearsal_and_guide_preserve_learner_draft_and_v1_journal(self):
        app = self.scene_app()
        app.text_input(key="help_scene_widget_source").set_value("my-own-source.mp4").run()
        app.text_area(key="help_scene_widget_replacement_line").set_value("My own line and pauses.").run()
        app.button(key="help_scene_save").click().run()
        draft = deepcopy(app.session_state["help_scene_draft"])
        journal = deepcopy(app.session_state["help_journey"])
        app.selectbox(key="help_scene_step").select("save_recipe").run()
        self.assertFalse(list(app.exception))
        self.assertTrue(any("Proposed rehearsal only" in item.value for item in app.info))
        guide = _guide_markdown()
        self.assertIn("No source footage, replacement WAV or rendered result exists", guide)
        self.assertIn("Runtime, credits and visual quality remain unknown", guide)
        self.assertEqual(app.session_state["help_scene_draft"], draft)
        self.assertEqual(app.session_state["help_journey"], journal)
        self.assertEqual(loads_journey(dumps_journey(journal)), journal)
        self.assertEqual(len(journal["entries"]), 1)
        self.assertNotIn("The crowd can wait.", journal["entries"][0]["observation"])

    def test_download_retains_comparison_stages_alternatives_and_recovery(self):
        guide = _guide_markdown()
        for expected in ("Planned source performance", "Proposed rewrite", "00:07–00:08",
                         "Must stay", "May change", "Reject if", "including its silent beats",
                         "**Script:**", "**Voice performance:**", "**Lip sync:**",
                         "**Editing:**", "**Sound:**", "Replace the soundtrack",
                         "Sync Studio", "LatentSync", "Inspect failures before changing settings",
                         "The old voice is still audible", "Possible cause:", "Next test:"):
            with self.subTest(expected=expected):
                self.assertIn(expected, guide)


if __name__ == "__main__":
    unittest.main()
