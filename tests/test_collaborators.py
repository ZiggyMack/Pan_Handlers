"""The collaborator teaching workspace preserves existing learner state."""

from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest

from Help.state.journey import dumps_journey
from Help.state.video_plan import dumps_plan


APP = Path(__file__).resolve().parents[1] / "Help" / "app.py"


class CollaboratorTests(unittest.TestCase):
    def test_provider_lessons_and_navigation_do_not_promote_or_replace_work(self):
        app = AppTest.from_file(str(APP), default_timeout=25).run()
        app.text_input(key="help_widget_goal").set_value("Keep my existing shot brief").run()
        before_journey = dumps_journey(app.session_state["help_journey"])
        before_video = dumps_plan(app.session_state["help_video_plan"])
        app.button(key="help_nav_Collaborators").click().run()
        self.assertFalse(app.exception)
        self.assertEqual(app.radio(key="help_collaborators_provider").value, "comfyui")
        for provider in ("grok", "gemini", "flow", "comfyui"):
            app.radio(key="help_collaborators_provider").set_value(provider).run()
            self.assertFalse(app.exception)
            self.assertEqual(dumps_journey(app.session_state["help_journey"]), before_journey)
            self.assertEqual(dumps_plan(app.session_state["help_video_plan"]), before_video)
        for lesson in ("reference", "comparison", "files", "audio", "prompts"):
            app.selectbox(key="help_collaborators_lesson").select(lesson).run()
            self.assertFalse(app.exception)
        app.radio(key="help_collaborators_provider").set_value("grok").run()
        app.radio(key="help_collaborators_lane").set_value("Explore a new design").run()
        app.text_area(key="help_collaborators_prompt_instruction").set_value("Explore one new costume.").run()
        app.button(key="help_collaborators_to_journal").click().run()
        app.button(key="help_nav_Collaborators").click().run()
        self.assertFalse(app.exception)
        self.assertEqual(app.radio(key="help_collaborators_provider").value, "grok")
        self.assertEqual(app.radio(key="help_collaborators_lane").value, "Explore a new design")
        self.assertEqual(app.selectbox(key="help_collaborators_lesson").value, "prompts")
        self.assertEqual(app.text_area(key="help_collaborators_prompt_instruction").value, "Explore one new costume.")
        self.assertEqual(dumps_journey(app.session_state["help_journey"]), before_journey)
        self.assertEqual(dumps_plan(app.session_state["help_video_plan"]), before_video)


if __name__ == "__main__":
    unittest.main()
