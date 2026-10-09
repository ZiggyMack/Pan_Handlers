"""Decision notes remain optional, scoped and separate from recorded project state."""

from copy import deepcopy
from pathlib import Path
import sys
import unittest

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.guides.workflow_decision import decision_markdown
from Help.guides.sampling_lab import build_cases, plan_markdown as sampling_markdown
from Help.guides.image_edit_lab import build_trials, plan_markdown as image_markdown


class WorkflowDecisionTests(unittest.TestCase):
    def test_optional_exports_preserve_plan_and_actual_report_independently(self):
        notes = {"problem": "Retain face while changing texture", "lesson": "Episode 4 / 2026-10-04",
                 "rationale": "Single original, denoise comparison", "success": "Earring remains visible",
                 "evidence_state": "executed", "effective": "run-v2: denoise 0.35; seed 9007199254740993",
                 "record": "output-B.png / run-v2.json", "result": "Earring drifted <img src=x> ![x](bad)",
                 "next": "Decline this take; compare a lower denoise"}
        before = deepcopy(notes)
        sampling = {"seed": "9007199254740993", "steps": 30, "cfg": 7.0, "variable": "cfg",
                    "recipe": "baseline-v1.editor.json", "sampler": "dpmpp_2m", "scheduler": "karras"}
        cases = build_cases("cfg", sampling, "5, 6")
        old = sampling_markdown(sampling, cases)
        self.assertNotIn("## Decision and actual observations", old)
        augmented = sampling_markdown(sampling, cases, notes)
        self.assertTrue(augmented.startswith(old))
        image = {"recipe": "sdxl-v2", "input_image": "original.png", "seed": "9007199254740993",
                 "lora_enabled": False, "variable": "denoise", "denoise": 0.5, "denoise_values": "0.3, 0.6"}
        exported = image_markdown(image, build_trials(image), notes)
        self.assertIn(r"0\.35", exported)  # actual settings aren't replaced by proposed 0.5/0.3/0.6
        self.assertIn("9007199254740993", exported)
        self.assertIn("Generation reported; acceptance not established", exported)
        self.assertIn("output", exported)
        self.assertNotIn("<img", exported)
        self.assertNotIn("![x]", exported)
        self.assertEqual(notes, before)

    def test_missing_or_unknown_status_does_not_infer_execution(self):
        for notes in (None, {}, {"evidence_state": "accepted", "result": "nice image"}):
            with self.subTest(notes=notes):
                text = decision_markdown(notes)
                self.assertIn("Evidence state: Planned / no execution reported", text)
                self.assertNotIn("Evidence state: accepted", text)

    def test_navigation_keeps_each_exercises_notes_without_changing_journal(self):
        script = '''
import streamlit as st
from Help.state.journey import new_journey
from Help.guides.sampling_lab import render as sampling
from Help.guides.image_edit_lab import render as image_edit
if 'help_journey' not in st.session_state:
    st.session_state['help_journey'] = new_journey()
if 'help_video_plan' not in st.session_state:
    st.session_state['help_video_plan'] = {'schema_version': 1, 'source': 'retain-this', 'takes': []}
page = st.radio('Page', ['Sampling', 'Image edit', 'Away'], key='test_page')
if page == 'Sampling':
    sampling()
elif page == 'Image edit':
    image_edit()
'''
        app = AppTest.from_string(script, default_timeout=30).run()
        self.assertFalse(app.exception)
        journal = deepcopy(app.session_state["help_journey"])
        video = deepcopy(app.session_state["help_video_plan"])
        app.text_area(key="help_sampling_decision_problem").set_value("Reduce highlights").run()
        app.text_area(key="help_sampling_decision_success").set_value("Keep face detail").run()
        app.selectbox(key="help_sampling_decision_evidence_state").select("validated").run()
        app.text_area(key="help_sampling_decision_result").set_value("Dry-run only; nothing generated").run()
        app.radio(key="test_page").set_value("Image edit").run()
        self.assertFalse(app.exception)
        self.assertEqual(app.text_area(key="help_image_edit_decision_problem").value, "")
        app.text_area(key="help_image_edit_decision_problem").set_value("Preserve face").run()
        app.radio(key="test_page").set_value("Away").run()
        app.radio(key="test_page").set_value("Sampling").run()
        self.assertFalse(app.exception)
        self.assertEqual(app.text_area(key="help_sampling_decision_problem").value, "Reduce highlights")
        self.assertEqual(app.selectbox(key="help_sampling_decision_evidence_state").value, "validated")
        self.assertEqual(app.session_state["help_image_edit_decision_draft"]["problem"], "Preserve face")
        self.assertEqual(app.session_state["help_journey"], journal)
        self.assertEqual(app.session_state["help_video_plan"], video)
        fresh = AppTest.from_string(script, default_timeout=30).run()
        self.assertEqual(fresh.text_area(key="help_sampling_decision_problem").value, "")
        self.assertEqual(fresh.selectbox(key="help_sampling_decision_evidence_state").value, "not_run")


if __name__ == "__main__":
    unittest.main()
