"""Exercise task routing, evidence records and navigation in the real app."""

from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest

from Help.state.journey import dumps_journey, loads_journey
from Help.state.video_plan import current_accepted, dumps_plan, loads_plan, route_for


APP = Path(__file__).resolve().parents[1] / "Help" / "app.py"


class VideoWorkshopTests(unittest.TestCase):
    def app(self):
        return AppTest.from_file(str(APP), default_timeout=25).run()

    def check(self, app):
        self.assertFalse(list(app.exception), [error.message for error in app.exception])

    def nav(self, app, section):
        app.button(key="help_nav_" + section).click().run()
        self.check(app)

    @staticmethod
    def label(elements, label):
        return next(element for element in elements if element.label == label)

    def test_entry_and_workshop_share_intent_without_changing_the_old_journey(self):
        app = self.app()
        app.text_input(key="help_widget_goal").set_value("Keep my larger project brief").run()
        before = loads_journey(dumps_journey(app.session_state["help_journey"]))
        app.selectbox(key="help_video_home_change").select("character").run()
        app.multiselect(key="help_video_home_preserve").set_value(["motion", "background"]).run()
        self.assertEqual(route_for(app.session_state["help_video_plan"]), "wan_mix")
        app.button(key="help_video_home_open").click().run()
        self.check(app)
        self.assertEqual(app.session_state["help_section"], "Video workshop")
        self.assertEqual(app.selectbox(key="help_video_work_change").value, "character")
        app.text_input(key="help_video_work_source").set_value("D:/Footage/scene.mp4").run()
        app.selectbox(key="help_video_work_material").select("mesh").run()
        self.assertEqual(route_for(app.session_state["help_video_plan"]), "render_first")
        self.nav(app, "Start here")
        self.assertEqual(app.selectbox(key="help_video_home_material").value, "mesh")
        self.nav(app, "Video workshop")
        self.assertEqual(app.text_input(key="help_video_work_source").value, "D:/Footage/scene.mp4")
        self.assertEqual(app.session_state["help_journey"], before)
        fresh = self.app()
        self.assertEqual(fresh.session_state["help_video_plan"]["source"], "")

    def test_record_review_accept_and_invalidate_after_a_new_brief(self):
        app = self.app()
        self.nav(app, "Video workshop")
        app.button(key="help_video_guardian").click().run()
        app.text_area(key="help_video_work_workflow_revision").set_value("union-depth-pinned.json / fixed revision").run()
        app.text_area(key="help_video_work_environment_notes").set_value("Operator recorded actual Cloud compatibility").run()
        app.text_area(key="help_video_work_settings").set_value("seed 42 / matched timing / recorded dimensions").run()
        app.text_area(key="help_video_take_observations").set_value("Keep these notes if a required field is missing.")
        self.label(app.button, "Record this take").click().run()
        self.assertTrue(app.error)
        self.assertIn("Keep these notes", app.text_area(key="help_video_take_observations").value)
        result = self.label(app.text_input, "Result file / remote asset reference")
        observation = self.label(app.text_area, "What happened? Include timecodes and the next change.")
        result.set_value("D:/Footage/preview001.mp4")
        observation.set_value("00:02 paw contact drifts; reduce the requested visual change.")
        self.label(app.button, "Record this take").click().run()
        self.check(app)
        app.button(key="help_video_accept").click().run()
        self.assertTrue(app.error)
        self.assertIsNone(current_accepted(app.session_state["help_video_plan"]))
        result = self.label(app.text_input, "Result file / remote asset reference")
        observation = self.label(app.text_area, "What happened? Include timecodes and the next change.")
        result.set_value("D:/Footage/preview002.mp4")
        observation.set_value("Compared motion, contact and sound throughout; this take meets the brief.")
        for key in ("performance", "appearance", "temporal", "timing"):
            app.checkbox(key="help_video_check_" + key).check()
        self.label(app.button, "Record this take").click().run()
        for key in ("performance", "appearance", "temporal", "timing"):
            self.assertFalse(app.checkbox(key="help_video_check_" + key).value)
        app.selectbox(key="help_video_take_choice").select("take-002").run()
        app.button(key="help_video_accept").click().run()
        self.check(app)
        accepted = current_accepted(app.session_state["help_video_plan"])
        self.assertEqual(accepted["id"], "take-002")
        self.assertEqual(len(app.session_state["help_video_plan"]["takes"]), 2)

        exported = dumps_plan(app.session_state["help_video_plan"])
        self.assertEqual(current_accepted(loads_plan(exported))["id"], "take-002")
        app.text_area(key="help_video_work_brief").set_value("Now change the setting too.").run()
        self.assertIsNone(current_accepted(app.session_state["help_video_plan"]))
        app.button(key="help_video_journal").click().run()
        self.check(app)
        journal = loads_journey(dumps_journey(app.session_state["help_journey"]))
        self.assertEqual(len(journal["entries"]), 1)
        self.assertEqual(journal["completed_steps"], [])
        self.assertIn("preview001.mp4", journal["entries"][0]["observation"])
        self.assertIn("preview002.mp4", journal["entries"][0]["observation"])
        self.nav(app, "Field journal")
        self.nav(app, "Video workshop")
        self.assertEqual(len(app.session_state["help_video_plan"]["takes"]), 2)

    def test_new_lessons_and_candidate_leave_plan_and_journal_unchanged(self):
        app = self.app()
        self.nav(app, "Video workshop")
        before_plan = dumps_plan(app.session_state["help_video_plan"])
        before_journal = dumps_journey(app.session_state["help_journey"])
        self.assertTrue(any("MiniMax H3" in expander.label for expander in app.expander))
        app.selectbox(key="help_video_lesson").select("tutorials").run()
        self.check(app)
        self.assertEqual(app.selectbox(key="help_video_source_notes_episode").value, "ep8")
        app.selectbox(key="help_video_source_notes_episode").select("comparison").run()
        self.check(app)
        app.selectbox(key="help_video_lesson").select("prompts").run()
        app.text_area(key="help_video_prompt_composition_instruction").set_value("Keep the performance.").run()
        self.nav(app, "Field journal")
        self.nav(app, "Video workshop")
        app.selectbox(key="help_video_lesson").select("prompts").run()
        self.check(app)
        self.assertEqual(app.text_area(key="help_video_prompt_composition_instruction").value, "Keep the performance.")
        self.assertEqual(dumps_plan(app.session_state["help_video_plan"]), before_plan)
        self.assertEqual(dumps_journey(app.session_state["help_journey"]), before_journal)

if __name__ == "__main__":
    unittest.main()
