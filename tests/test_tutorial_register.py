"""Portable exports and independent tutorial selectors for the CFA intake."""

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.content.tutorial_register import SOURCES
from Help.guides.tutorial_notes import notes_markdown


class TutorialRegisterTests(unittest.TestCase):
    def test_exports_work_without_archived_files_or_credentials(self):
        # The source checkout is useful evidence, never an app dependency.
        with patch("builtins.open", side_effect=AssertionError("Unexpected file read")):
            exports = {key: notes_markdown(key) for key in SOURCES}
        for key, exported in exports.items():
            with self.subTest(source=key):
                source = SOURCES[key]
                self.assertIn(source["sha256"], exported)
                self.assertIn(source["archive_path"], exported)
                self.assertIn(source["reviewed"], exported)
                self.assertNotIn("(None", exported)
                if source["url"]:
                    self.assertIn(source["url"] + "&t=", exported)
                else:
                    self.assertIn("Video URL unresolved", exported)
                    self.assertIn("video URL not verified", exported)

    def test_existing_default_export_is_still_episode_one(self):
        self.assertEqual(notes_markdown(), notes_markdown("ep1"))
        self.assertIn("# Episode 1", notes_markdown())

    def test_new_sources_render_with_scoped_selectors_and_preserve_notes(self):
        app = AppTest.from_string('''
import streamlit as st
from Help.guides.tutorial_notes import render
st.session_state.setdefault("help_journey", {"schema_version": 1, "goal": "Keep this goal", "entries": []})
st.session_state.setdefault("help_video_plan", {"schema_version": 1, "brief": "Keep the performance", "takes": []})
render("left", initial_episode="ep5")
render("right", initial_episode="ep8")
''', default_timeout=20).run()
        before_journal = dict(app.session_state["help_journey"])
        before_video = dict(app.session_state["help_video_plan"])
        for key in SOURCES:
            with self.subTest(source=key):
                app.selectbox(key="left_episode").set_value(key).run()
                self.assertFalse(list(app.exception), [item.message for item in app.exception])
                self.assertEqual(app.selectbox(key="right_episode").value, "ep8")
                self.assertEqual(app.session_state["help_journey"], before_journal)
                self.assertEqual(app.session_state["help_video_plan"], before_video)


if __name__ == "__main__":
    unittest.main()
