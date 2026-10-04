"""Exercise image-edit comparisons, exact seeds and optional LoRA state."""

from copy import deepcopy
from pathlib import Path
import sys
import unittest

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.image_edit_lab import build_trials, plan_markdown


def sample_plan():
    return {"recipe": "baseline.json / <model> [reference]", "input_image": "original.png",
            "seed": "18446744073709551615", "lora_enabled": True, "variable": "denoise",
            "denoise": 0.5, "strength_model": 0.9, "strength_clip": 1.0,
            "denoise_values": "0.35, 0.65", "strength_model_values": "0.5, 0.8",
            "strength_clip_values": "0.0, 0.8"}


class ImageEditTests(unittest.TestCase):
    def test_trials_change_only_one_active_control_and_keep_exact_seed(self):
        draft = sample_plan()
        for variable in ("denoise", "strength_model", "strength_clip"):
            draft["variable"] = variable
            original = deepcopy(draft)
            trials = build_trials(draft)
            for trial in trials:
                self.assertEqual(trial["seed"], draft["seed"])
                for field in {"denoise", "strength_model", "strength_clip"} - {variable}:
                    self.assertEqual(trial[field], draft[field])
            self.assertEqual(draft, original)
            trials[0]["denoise"] = 0.01
            self.assertEqual(draft, original)
        draft["variable"] = "denoise"
        draft["lora_enabled"] = False
        trials = build_trials(draft)
        self.assertNotIn("strength_model", trials[0])
        exported = plan_markdown(draft, trials)
        self.assertIn(draft["seed"], exported)
        self.assertNotIn("<model>", exported)
        self.assertIn("&lt;model&gt;", exported)
        for field, value in (("denoise_values", "nan, 0.5"), ("denoise_values", "1.1, 0.5"),
                             ("denoise_values", "0.5"), ("denoise", True),
                             ("seed", "18446744073709551616"), ("seed", "-1"),
                             ("variable", "strength_clip")):
            with self.subTest(field=field, value=value):
                with self.assertRaises(ValueError):
                    build_trials({**draft, field: value})

    def test_optional_lora_and_navigation_preserve_the_draft_and_journal(self):
        script = """
import streamlit as st
from Help.image_edit_lab import render
from Help.journey import new_journey
if 'help_journey' not in st.session_state:
    st.session_state['help_journey'] = new_journey()
if st.radio('Page', ['Lesson', 'Elsewhere'], key='test_page') == 'Lesson':
    render()
"""
        app = AppTest.from_string(script, default_timeout=20).run()
        self.assertFalse(app.exception)
        original = deepcopy(app.session_state["help_journey"])
        app.text_input(key="help_image_edit_widget_seed").set_value("18446744073709551615").run()
        app.text_input(key="help_image_edit_widget_input_image").set_value("original.png").run()
        app.checkbox(key="help_image_edit_widget_lora_enabled").check().run()
        app.selectbox(key="help_image_edit_widget_variable").select("strength_clip").run()
        app.text_input(key="help_image_edit_widget_strength_clip_values").set_value("0, 0.75").run()
        app.number_input(key="help_image_edit_widget_strength_model").set_value(0.8).run()
        app.radio(key="test_page").set_value("Elsewhere").run()
        app.radio(key="test_page").set_value("Lesson").run()
        self.assertFalse(app.exception)
        self.assertEqual(app.selectbox(key="help_image_edit_widget_variable").value, "strength_clip")
        self.assertEqual(app.text_input(key="help_image_edit_widget_seed").value, "18446744073709551615")
        app.checkbox(key="help_image_edit_widget_lora_enabled").uncheck().run()
        self.assertFalse(app.exception)
        self.assertEqual(app.selectbox(key="help_image_edit_widget_variable").value, "denoise")
        self.assertNotIn("strength_model", build_trials(app.session_state["help_image_edit_draft"])[0])
        app.checkbox(key="help_image_edit_widget_lora_enabled").check().run()
        app.selectbox(key="help_image_edit_widget_variable").select("strength_clip").run()
        self.assertEqual(app.number_input(key="help_image_edit_widget_strength_model").value, 0.8)
        self.assertEqual(app.text_input(key="help_image_edit_widget_strength_clip_values").value, "0, 0.75")
        app.text_input(key="help_image_edit_widget_strength_clip_values").set_value("inf, 0.75").run()
        self.assertFalse(app.exception)
        self.assertTrue(app.error)
        app.text_input(key="help_image_edit_widget_strength_clip_values").set_value("0, 0.75").run()
        self.assertFalse(app.error)
        self.assertEqual(app.session_state["help_journey"], original)
        fresh = AppTest.from_string(script, default_timeout=20).run()
        self.assertEqual(fresh.text_input(key="help_image_edit_widget_seed").value, "42")
        self.assertFalse(fresh.checkbox(key="help_image_edit_widget_lora_enabled").value)


if __name__ == "__main__":
    unittest.main()
