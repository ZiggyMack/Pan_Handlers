"""Check exact seeds and controlled comparisons without claiming generated results."""

from copy import deepcopy
from pathlib import Path
import sys
import unittest

from streamlit.testing.v1 import AppTest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.sampling_lab import build_cases, plan_markdown


class SamplingLabTests(unittest.TestCase):
    def test_comparisons_preserve_exact_seeds_and_change_only_the_selected_setting(self):
        baseline = {"seed": "18446744073709551615", "steps": 30, "cfg": 7.0}
        original = deepcopy(baseline)
        for variable, values in (("cfg", "6, 6.5"), ("cfg", "6.1234561, 6.1234562"), ("steps", "32, 36"),
                                 ("seed", "9007199254740993, 18446744073709551614")):
            with self.subTest(variable=variable):
                cases = build_cases(variable, baseline, values)
                self.assertEqual({key: cases[0][key] for key in baseline}, baseline)
                for case in cases[1:]:
                    self.assertEqual([key for key in baseline if case[key] != baseline[key]], [variable])
                draft = {**baseline, "variable": variable, "recipe": '<img src="x"> ![x](https://example.com)',
                         "sampler": "dpmpp_2m", "scheduler": "karras"}
                exported = plan_markdown(draft, cases)
                self.assertIn("18446744073709551615", exported)
                self.assertNotIn("<img", exported)
                self.assertNotIn("![x]", exported)
                self.assertIn("Planned only", exported)
                if "6.1234561" in values:
                    self.assertIn("6.1234561", exported)
                    self.assertIn("6.1234562", exported)
        self.assertEqual(baseline, original)
        for variable, values in (("seed", "18446744073709551616, 42"), ("seed", "1.5, 2"),
                                 ("steps", "0, 30"), ("cfg", "NaN, 7"), ("cfg", "inf, 7"),
                                 ("cfg", "-1, 7"), ("steps", "30")):
            with self.subTest(variable=variable, invalid=values):
                with self.assertRaises(ValueError):
                    build_cases(variable, baseline, values)

    def test_draft_navigation_and_invalid_input_preserve_plan_and_journal(self):
        script = '''
import streamlit as st
from Help.journey import new_journey
from Help.sampling_lab import render
if 'help_journey' not in st.session_state:
    st.session_state['help_journey'] = new_journey()
if st.radio('Page', ['Sampling', 'Away'], key='page') == 'Sampling':
    render()
'''
        app = AppTest.from_string(script, default_timeout=20).run()
        self.assertFalse(app.exception)
        original = deepcopy(app.session_state["help_journey"])
        exact_seed = "9007199254740993"
        app.text_input(key="help_sampling_widget_seed").set_value(exact_seed).run()
        app.text_input(key="help_sampling_widget_cfg_values").set_value("5, 6").run()
        app.selectbox(key="help_sampling_widget_variable").select("steps").run()
        app.text_input(key="help_sampling_widget_steps_values").set_value("32, 38").run()
        app.radio(key="page").set_value("Away").run()
        app.radio(key="page").set_value("Sampling").run()
        self.assertFalse(app.exception)
        self.assertEqual(app.selectbox(key="help_sampling_widget_variable").value, "steps")
        self.assertEqual(app.text_input(key="help_sampling_widget_seed").value, exact_seed)
        self.assertEqual(app.text_input(key="help_sampling_widget_steps_values").value, "32, 38")
        app.selectbox(key="help_sampling_widget_variable").select("cfg").run()
        self.assertEqual(app.text_input(key="help_sampling_widget_cfg_values").value, "5, 6")
        app.text_input(key="help_sampling_widget_cfg_values").set_value("nan, 7").run()
        self.assertFalse(app.exception)
        self.assertTrue(app.error)
        self.assertEqual(app.session_state["help_sampling_draft"]["seed"], exact_seed)
        app.text_input(key="help_sampling_widget_cfg_values").set_value("5, 6").run()
        self.assertFalse(app.error)
        self.assertEqual(app.session_state["help_journey"], original)
        fresh = AppTest.from_string(script, default_timeout=20).run()
        self.assertEqual(fresh.text_input(key="help_sampling_widget_seed").value, "42")


if __name__ == "__main__":
    unittest.main()
