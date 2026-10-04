"""Exercise filter decisions as a portable plan separate from journal progress."""

from pathlib import Path
import sys
import unittest

from streamlit.testing.v1 import AppTest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.journey import dumps_journey, loads_journey
from Help.model_filters import _plan_markdown


_APP = """
import streamlit as st
from Help.journey import new_journey
from Help.model_filters import render

if 'help_journey' not in st.session_state:
    journey = new_journey()
    journey.update(goal='Keep an existing shot recognizable', chosen_path='forge', completed_steps=['brief'])
    st.session_state['help_journey'] = journey

page = st.radio('Test section', ['Filters', 'Elsewhere'], key='test_filter_section')
if page == 'Filters':
    render()
else:
    st.write('Another section')
"""


class ModelFilterTests(unittest.TestCase):
    def test_controlnet_plan_keeps_the_existing_model_family_and_file_role(self):
        app = AppTest.from_string(_APP, default_timeout=20).run()
        original_journey = loads_journey(dumps_journey(app.session_state["help_journey"]))
        app.selectbox(key="help_model_filter_widget_family").select("SD 1.5").run()
        app.selectbox(key="help_model_filter_widget_purpose").select("ControlNet for an existing image model").run()
        self.assertFalse(app.exception)
        decisions = app.table[0].value.set_index("Filter / decision")["Set it to"]
        self.assertEqual(decisions["Model type"], "ControlNet")
        self.assertEqual(decisions["Base model"], "SD 1.5")
        self.assertIn("/controlnet", decisions["Destination after choosing the file"])
        self.assertNotIn("/checkpoints", decisions["Destination after choosing the file"])
        self.assertIn("Not needed", decisions["Checkpoint type"])

        app.radio(key="test_filter_section").set_value("Elsewhere").run()
        app.radio(key="test_filter_section").set_value("Filters").run()
        self.assertFalse(app.exception)
        self.assertEqual(app.selectbox(key="help_model_filter_widget_family").value, "SD 1.5")
        markdown = _plan_markdown(dict(app.session_state["help_model_filter_draft"]))
        self.assertIn("ControlNet for an existing image model", markdown)
        self.assertIn("SD 1\\.5", markdown)
        self.assertIn("/controlnet", markdown)
        self.assertIn("control map", markdown)
        self.assertEqual(app.session_state["help_journey"], original_journey)

    def test_filter_choices_survive_navigation_and_export_without_changing_journey(self):
        app = AppTest.from_string(_APP, default_timeout=20).run()
        self.assertFalse(app.exception)
        original_journey = loads_journey(dumps_journey(app.session_state["help_journey"]))
        self.assertEqual(app.selectbox(key="help_model_filter_widget_family").value, "SDXL 1.0")
        self.assertEqual(app.selectbox(key="help_model_filter_widget_period").value, "Month")
        self.assertEqual(app.table[0].value.iloc[6]["Set it to"], "Confirm active time mode in Civitai")

        selections = {
            "purpose": "LoRA for an existing image model",
            "family": "SD 1.5",
            "sort": "Most Downloaded",
            "period": "Week",
            "period_basis": "Statistics",
        }
        for field, value in selections.items():
            app.selectbox(key="help_model_filter_widget_" + field).select(value).run()
        self.assertFalse(app.exception)
        self.assertEqual(app.table[0].value.iloc[0]["Set it to"], "LoRA")
        self.assertEqual(app.table[0].value.iloc[1]["Set it to"], "SD 1.5")
        self.assertIn("/loras", app.table[0].value.iloc[9]["Set it to"])

        app.radio(key="test_filter_section").set_value("Elsewhere").run()
        app.radio(key="test_filter_section").set_value("Filters").run()
        self.assertFalse(app.exception)
        for field, expected in selections.items():
            with self.subTest(field=field):
                self.assertEqual(app.selectbox(key="help_model_filter_widget_" + field).value, expected)
        markdown = _plan_markdown(dict(app.session_state["help_model_filter_draft"]))
        for expected in ("LoRA for an existing image model", "SD 1\\.5", "Most Downloaded", "Week", "Statistics"):
            self.assertIn(expected, markdown)
        self.assertIn("not live search results", markdown)
        self.assertEqual(len(app.get("download_button")), 1)

        app.selectbox(key="help_model_filter_widget_purpose").select("Follow an existing video or specialized workflow").run()
        self.assertFalse(app.exception)
        self.assertTrue(app.selectbox(key="help_model_filter_widget_family").disabled)
        self.assertIn("exact workflow", app.table[0].value.iloc[1]["Set it to"])
        self.assertIn("Follow each file", app.table[0].value.iloc[9]["Set it to"])
        self.assertNotIn("/checkpoints", app.table[0].value.iloc[9]["Set it to"])
        markdown = _plan_markdown(dict(app.session_state["help_model_filter_draft"]))
        self.assertIn("image-family preference is inactive", markdown)
        self.assertIn("project's model identifiers", markdown)
        self.assertEqual(app.session_state["help_journey"], original_journey)

        second = AppTest.from_string(_APP, default_timeout=20).run()
        self.assertFalse(second.exception)
        self.assertEqual(second.selectbox(key="help_model_filter_widget_family").value, "SDXL 1.0")
        self.assertEqual(second.selectbox(key="help_model_filter_widget_purpose").value, "Starter image checkpoint")
        self.assertEqual(app.session_state["help_model_filter_draft"]["family"], "SD 1.5")


if __name__ == "__main__":
    unittest.main()
