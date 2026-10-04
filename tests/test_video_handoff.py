"""Verify timing semantics and the learner's video handoff explorer."""

from pathlib import Path
import sys
import unittest

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.video_handoff import handoff_markdown, timing


class VideoHandoffTests(unittest.TestCase):
    def test_playback_duration_and_rate_changes_are_distinct_from_generation(self):
        self.assertEqual(timing(81, 24, 24), {
            "source_seconds": 3.375, "export_seconds": 3.375, "speed_ratio": 1.0,
        })
        fast = timing(81, 24, 48)
        self.assertEqual(fast["source_seconds"], 3.375)
        self.assertEqual(fast["export_seconds"], 1.6875)
        self.assertEqual(fast["speed_ratio"], 2.0)
        self.assertAlmostEqual(timing(30000, 30000 / 1001, 30)["source_seconds"], 1001.0)
        for frames, source, output in (
            (0, 24, 24), (1.5, 24, 24), (True, 24, 24),
            (81, 0, 24), (81, 24, -1), (81, float("nan"), 24),
            (81, 24, float("inf")), (81, True, 24),
        ):
            with self.subTest(frames=frames, source=source, output=output):
                with self.assertRaises(ValueError):
                    timing(frames, source, output)

    def test_explorer_switches_handoffs_and_warns_only_for_changed_playback_rate(self):
        script = """
import streamlit as st
from Help.journey import new_journey
from Help.video_handoff import render
if 'help_journey' not in st.session_state:
    st.session_state['help_journey'] = new_journey()
render()
"""
        app = AppTest.from_string(script, default_timeout=20).run()
        self.assertFalse(app.exception)
        original = app.session_state["help_journey"].copy()
        for route, node in (("video_native", "Save Video"),
                            ("frames_native", "Create Video"),
                            ("video_vhs", "Get Video Components")):
            app.selectbox(key="help_video_handoff_route").select(route).run()
            self.assertFalse(app.exception)
            self.assertIn(node, app.code[0].value)
        self.assertFalse(app.warning)
        app.number_input(key="help_video_handoff_export_fps").set_value(48.0).run()
        self.assertFalse(app.exception)
        self.assertTrue(any("does not create intermediate frames" in item.value for item in app.warning))
        self.assertEqual([metric.value for metric in app.metric], ["3.375 s", "1.688 s", "2.000\u00d7"])
        plan = handoff_markdown(app.selectbox(key="help_video_handoff_route").value,
                                app.number_input(key="help_video_handoff_frames").value,
                                app.number_input(key="help_video_handoff_source_fps").value,
                                app.number_input(key="help_video_handoff_export_fps").value)
        self.assertIn("Get Video Components", plan)
        self.assertIn("1.687500 seconds", plan)
        self.assertIn("not an executable ComfyUI workflow", plan)
        app.number_input(key="help_video_handoff_export_fps").set_value(24.0).run()
        self.assertFalse(app.exception)
        self.assertFalse(app.warning)
        self.assertEqual(app.session_state["help_journey"], original)


if __name__ == "__main__":
    unittest.main()
