"""Exercise the learner's navigation, durable notes, and session isolation.

Run with: python -m unittest discover -s tests -p test_help_console.py -v
AppTest executes the real Streamlit entry point without a browser or server.
"""

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from streamlit.testing.v1 import AppTest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.state.journey import dumps_journey, loads_journey

APP = ROOT / "Help" / "app.py"
SECTIONS = (
    "Start here", "Video workshop", "Collaborators", "Rewrite a scene", "Compare paths", "ComfyUI guide", "Field journal", "Sources & roadmap"
)


class HelpConsoleTests(unittest.TestCase):
    def new_app(self):
        app = AppTest.from_file(str(APP), default_timeout=20).run()
        self.assert_no_exception(app)
        return app

    def assert_no_exception(self, app):
        self.assertFalse(list(app.exception), [error.message for error in app.exception])

    def navigate(self, app, section):
        app.button(key="help_nav_" + section).click().run()
        self.assert_no_exception(app)
        self.assertEqual(app.session_state["help_section"], section)

    @staticmethod
    def by_label(elements, label):
        return next(element for element in elements if element.label == label)

    def test_all_pages_render_in_both_themes(self):
        app = self.new_app()
        for matrix in (False, True):
            if app.toggle(key="help_matrix").value != matrix:
                app.toggle(key="help_matrix").set_value(matrix).run()
            for section in SECTIONS:
                with self.subTest(matrix=matrix, section=section):
                    self.navigate(app, section)
                    self.assertEqual(app.toggle(key="help_matrix").value, matrix)
                    rendered = "\n".join(element.value for element in app.markdown)
                    theme = "matrix" if matrix else "ledger"
                    self.assertIn(f'data-help-theme="{theme}"', rendered)
                    self.assertIn("help-hero", rendered)

    def test_embedded_dashboard_keeps_navigation_and_journal_across_pages(self):
        # Match the script-directory path supplied by `streamlit run dashboard/app.py`.
        dashboard_path = patch.object(sys, "path", [str(ROOT / "dashboard"), *sys.path])
        dashboard_path.start()
        self.addCleanup(dashboard_path.stop)
        app = AppTest.from_file(str(ROOT / "dashboard" / "app.py"), default_timeout=20)
        app.session_state["current_page"] = "🧭 Pathfinder"
        app.session_state["matrix_mode"] = True
        app.run()
        self.assert_no_exception(app)
        app.text_input(key="help_widget_goal").set_value("Keep this embedded project brief").run()
        before = loads_journey(dumps_journey(app.session_state["help_journey"]))
        for section in SECTIONS:
            with self.subTest(section=section):
                app.radio(key="help_section").set_value(section).run()
                self.assert_no_exception(app)
                self.assertEqual(app.session_state["help_journey"], before)
                self.assertFalse(any(button.key == "help_nav_" + section for button in app.button))
                self.assertTrue(any('data-help-theme="matrix"' in element.value for element in app.markdown))
        app.radio(key="help_section").set_value("Start here").run()
        self.assertEqual(app.text_input(key="help_widget_goal").value, before["goal"])

    def test_shot_and_output_choice_survive_leaving_the_page(self):
        app = self.new_app()
        shot = "A ten-second orbit around a ceramic robot on a desk."
        app.text_input(key="help_widget_goal").set_value(shot).run()
        app.radio(key="help_widget_output_kind").set_value("Editable 3D + AI").run()
        self.navigate(app, "ComfyUI guide")
        self.navigate(app, "Field journal")
        self.navigate(app, "Start here")
        self.assertEqual(app.text_input(key="help_widget_goal").value, shot)
        self.assertEqual(app.radio(key="help_widget_output_kind").value, "Editable 3D + AI")
        self.assertEqual(app.session_state["help_journey"]["goal"], shot)

    def test_browsing_comfyui_preserves_the_users_forge_decision(self):
        app = self.new_app()
        self.navigate(app, "Compare paths")
        app.selectbox(key="help_widget_chosen_path").select("forge").run()
        reason = "I want familiar image controls while comparing the node approach."
        app.text_area(key="help_widget_decision_reason").set_value(reason).run()
        self.navigate(app, "ComfyUI guide")
        self.assertEqual(app.session_state["help_journey"]["chosen_path"], "forge")
        self.assertTrue(any("Forge" in caption.value for caption in app.caption))
        self.navigate(app, "Compare paths")
        self.assertEqual(app.selectbox(key="help_widget_chosen_path").value, "forge")
        self.assertEqual(app.text_area(key="help_widget_decision_reason").value, reason)

    def test_checkpoint_notes_and_completion_survive_step_and_page_changes(self):
        app = self.new_app()
        self.navigate(app, "ComfyUI guide")
        brief_note = "One subject, a ten-second orbit, and an editable Blender scene."
        setup_note = "Record Desktop version and model filename before testing."
        app.text_area(key="help_widget_note_brief").set_value(brief_note).run()
        app.checkbox(key="help_widget_done_brief").check().run()
        app.selectbox(key="help_step_select").select("setup").run()
        app.text_area(key="help_widget_note_setup").set_value(setup_note).run()
        app.checkbox(key="help_widget_done_setup").check().run()
        app.selectbox(key="help_widget_environment").select("Desktop").run()
        self.navigate(app, "Field journal")
        self.assertTrue(any(brief_note == element.value for element in app.text))
        self.assertTrue(any(setup_note == element.value for element in app.text))
        self.navigate(app, "ComfyUI guide")
        for step, expected_note in (("brief", brief_note), ("setup", setup_note)):
            with self.subTest(step=step):
                app.selectbox(key="help_step_select").select(step).run()
                self.assert_no_exception(app)
                self.assertEqual(app.text_area(key="help_widget_note_" + step).value, expected_note)
                self.assertTrue(app.checkbox(key="help_widget_done_" + step).value)
        self.assertEqual(app.selectbox(key="help_widget_environment").value, "Desktop")
        app.checkbox(key="help_widget_done_setup").uncheck().run()
        self.assertEqual(app.session_state["help_journey"]["completed_steps"], ["brief"])

    def fill_entry(self, app, resource="https://docs.comfy.org/get_started/first_generation"):
        self.by_label(app.text_input, "Entry title").set_value("First still saved")
        self.by_label(app.text_area, "What did you try, and what happened?").set_value(
            "Fixed the seed and changed one prompt detail. The image and workflow are saved."
        )
        self.by_label(app.text_area, "What should the next person do?").set_value(
            "Restore the baseline prompt before changing the seed."
        )
        self.by_label(app.text_input, "Reference or result URL (optional)").set_value(resource)
        self.by_label(app.button, "Add to field journal").click().run()
        self.assert_no_exception(app)

    def test_submitted_experiment_is_visible_and_survives_navigation(self):
        app = self.new_app()
        self.navigate(app, "Field journal")
        self.fill_entry(app)
        entries = app.session_state["help_journey"]["entries"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["title"], "First still saved")
        self.assertIn("Fixed the seed", entries[0]["observation"])
        self.assertTrue(entries[0]["date"])
        self.navigate(app, "Start here")
        self.navigate(app, "Field journal")
        self.assertEqual(len(app.session_state["help_journey"]["entries"]), 1)
        self.assertTrue(any("First still saved" in element.value for element in app.text))
        self.assertTrue(any("Restore the baseline" in element.value for element in app.text))

    def test_invalid_resource_does_not_enter_the_journal(self):
        app = self.new_app()
        self.navigate(app, "Field journal")
        self.fill_entry(app, resource="javascript:alert(1)")
        self.assertEqual(app.session_state["help_journey"]["entries"], [])
        self.assertTrue(app.error)

    def test_different_visitors_do_not_share_goals_or_journals(self):
        first = self.new_app()
        first.text_input(key="help_widget_goal").set_value("First visitor's private shot").run()
        self.navigate(first, "Field journal")
        self.fill_entry(first)
        second = self.new_app()
        self.assertEqual(second.text_input(key="help_widget_goal").value, "")
        self.assertEqual(second.session_state["help_journey"]["entries"], [])
        second.text_input(key="help_widget_goal").set_value("Second visitor's shot").run()
        self.navigate(first, "Start here")
        self.assertEqual(first.text_input(key="help_widget_goal").value, "First visitor's private shot")
        self.assertEqual(len(first.session_state["help_journey"]["entries"]), 1)
        self.assertEqual(second.session_state["help_journey"]["goal"], "Second visitor's shot")

    def test_scene_draft_and_saved_snapshot_preserve_the_existing_journey(self):
        app = self.new_app()
        goal = "Keep my original animation experiment alongside the dialogue study."
        app.text_input(key="help_widget_goal").set_value(goal).run()
        self.navigate(app, "Compare paths")
        app.selectbox(key="help_widget_chosen_path").select("forge").run()
        self.navigate(app, "ComfyUI guide")
        app.checkbox(key="help_widget_done_brief").check().run()
        before_scene = loads_journey(dumps_journey(app.session_state["help_journey"]))
        original = {
            field: before_scene[field]
            for field in ("goal", "chosen_path", "completed_steps")
        }
        self.navigate(app, "Rewrite a scene")
        source = r"D:\Footage\cafe-closeup.mp4"
        dialogue = "00:00–00:04 | The coffee is ready.\n00:04–00:08 | Shall we begin?"
        app.text_input(key="help_scene_widget_source").set_value(source).run()
        app.text_area(key="help_scene_widget_replacement_line").set_value(dialogue).run()
        app.selectbox(key="help_scene_widget_status").select("Audio baseline saved").run()
        self.navigate(app, "Field journal")
        self.assertEqual(app.session_state["help_journey"]["entries"], [])
        self.navigate(app, "Rewrite a scene")
        self.assertEqual(app.text_input(key="help_scene_widget_source").value, source)
        self.assertEqual(app.text_area(key="help_scene_widget_replacement_line").value, dialogue)
        self.assertEqual(app.selectbox(key="help_scene_widget_status").value, "Audio baseline saved")

        app.button(key="help_scene_save").click().run()
        self.assert_no_exception(app)
        journal = app.session_state["help_journey"]
        self.assertEqual({field: journal[field] for field in original}, original)
        self.assertEqual(len(journal["entries"]), 1)
        observation = journal["entries"][0]["observation"]
        for expected in (source, dialogue, "Status (self-reported)", "Audio baseline saved"):
            self.assertIn(expected, observation)
        self.assertEqual(loads_journey(dumps_journey(journal))["entries"], journal["entries"])
        self.navigate(app, "Field journal")
        self.assertTrue(any(dialogue in element.value for element in app.text))
        self.navigate(app, "Rewrite a scene")
        self.assertEqual(app.text_area(key="help_scene_widget_replacement_line").value, dialogue)
        self.assertEqual(len(app.session_state["help_journey"]["entries"]), 1)

    def test_scene_save_requires_source_and_dialogue_without_marking_foundations(self):
        app = self.new_app()
        self.navigate(app, "Rewrite a scene")
        self.assertTrue(app.button(key="help_scene_save").disabled)
        app.text_input(key="help_scene_widget_source").set_value("clip.mp4").run()
        self.assertTrue(app.button(key="help_scene_save").disabled)
        app.text_input(key="help_scene_widget_source").set_value("   ").run()
        app.text_area(key="help_scene_widget_replacement_line").set_value("I brought the coffee.").run()
        self.assertTrue(app.button(key="help_scene_save").disabled)
        app.text_input(key="help_scene_widget_source").set_value("clip.mp4").run()
        self.assertFalse(app.button(key="help_scene_save").disabled)
        app.button(key="help_scene_save").click().run()
        self.assert_no_exception(app)
        journal = app.session_state["help_journey"]
        self.assertEqual(journal["completed_steps"], [])
        self.assertEqual(journal["goal"], "")
        self.assertEqual(journal["chosen_path"], "comfyui")
        self.assertEqual(len(journal["entries"]), 1)
        self.assertIn("Status (self-reported):\nPlanning", journal["entries"][0]["observation"])

    def test_scene_timing_feedback_distinguishes_unmeasured_aligned_and_mismatched_audio(self):
        app = self.new_app()
        self.navigate(app, "Rewrite a scene")

        def timing_warnings():
            return [warning.value for warning in app.warning if "The exported replacement WAV is" in warning.value]

        self.assertEqual(timing_warnings(), [])
        app.number_input(key="help_scene_widget_audio_seconds").set_value(8.0).run()
        self.assertEqual(timing_warnings(), [])
        self.assertTrue(any("durations align" in info.value for info in app.info))
        for seconds, wording in ((10.0, "2.0 seconds longer"), (6.0, "2.0 seconds shorter")):
            with self.subTest(seconds=seconds):
                app.number_input(key="help_scene_widget_audio_seconds").set_value(seconds).run()
                self.assert_no_exception(app)
                self.assertEqual(len(timing_warnings()), 1)
                self.assertIn(wording, timing_warnings()[0])
        app.number_input(key="help_scene_widget_audio_seconds").set_value(0.0).run()
        self.assertEqual(timing_warnings(), [])
        self.assertFalse(any("durations align" in info.value for info in app.info))


if __name__ == "__main__":
    unittest.main()
