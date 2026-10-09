"""The evidence sample travels intact and never becomes a visitor's progress."""

from copy import deepcopy
from hashlib import sha256
from io import BytesIO
import json
import unittest
from zipfile import ZipFile

from streamlit.testing.v1 import AppTest

from Help.state.journey import dumps_journey, loads_journey
from Help.guides.worked_example import CASE_FILES, case_bundle


class WorkedExampleTests(unittest.TestCase):
    def test_download_is_self_contained_and_matches_the_recorded_output(self):
        with ZipFile(BytesIO(case_bundle())) as archive:
            self.assertEqual(set(archive.namelist()), {"cfa_pump_v001/" + name for name in CASE_FILES})
            self.assertLess(sum(item.file_size for item in archive.infolist()), 2_000_000)
            manifest = json.loads(archive.read("cfa_pump_v001/manifest.json"))
            self.assertTrue(manifest["completed_still"])
            self.assertFalse(manifest["dialogue_rewrite_executed"])
            self.assertFalse(manifest["improved_second_generated_image"])
            self.assertIsNone(manifest["actual_runtime_seconds"])
            self.assertIsNone(manifest["actual_credits"])
            for artifact in manifest["files"]:
                content = archive.read("cfa_pump_v001/" + artifact["filename"])
                self.assertEqual(len(content), artifact["bytes"])
                self.assertEqual(sha256(content).hexdigest(), artifact["sha256"])
            record = json.loads(archive.read("cfa_pump_v001/pump_concept_v001.record.json"))
            png = archive.read("cfa_pump_v001/pump_concept_v001.png")
            self.assertEqual(sha256(png).hexdigest(), record["outputs"][0]["sha256"])
            editor = json.loads(archive.read("cfa_pump_v001/pump_concept_v001.editor.json"))
            api = json.loads(archive.read("cfa_pump_v001/pump_concept_v001.api.json"))
            self.assertIsInstance(editor["nodes"], list)
            self.assertNotIn("nodes", api)
            sampler = next(node for node in api.values() if node["class_type"] == "KSampler")
            self.assertEqual(sampler["inputs"]["seed"], record["inputs"]["seed"])
            self.assertEqual(sampler["inputs"]["steps"], record["inputs"]["resolved_parameters"]["steps"])

    def test_embedded_guide_preserves_choice_and_v1_progress_while_showing_case(self):
        app = AppTest.from_string(
            "from Help.console import render\n"
            "import streamlit as st\n"
            "from Help.state.journey import new_journey\n"
            "if 'help_journey' not in st.session_state:\n"
            "    journal = new_journey()\n"
            "    journal['chosen_path'] = 'forge'\n"
            "    journal['goal'] = 'My own scene experiment'\n"
            "    journal['completed_steps'] = ['brief']\n"
            "    st.session_state['help_journey'] = journal\n"
            "render(standalone=False)\n", default_timeout=25,
        ).run()
        self.assertFalse(list(app.exception))
        before = deepcopy(app.session_state["help_journey"])
        app.radio(key="help_section").set_value("ComfyUI guide").run()
        self.assertFalse(list(app.exception), [item.message for item in app.exception])
        self.assertTrue(any("Worked example" in item.label for item in app.tabs))
        self.assertEqual(app.session_state["help_journey"], before)
        self.assertEqual(loads_journey(dumps_journey(before)), before)
        app.radio(key="help_section").set_value("Field journal").run()
        self.assertEqual(app.session_state["help_journey"], before)

    def test_shared_renderers_can_appear_twice_with_distinct_keys(self):
        app = AppTest.from_string(
            "from Help.guides.cloud_access import render as cloud\n"
            "from Help.guides.worked_example import render as example\n"
            "cloud('first_cloud')\ncloud('second_cloud')\n"
            "example('first_example')\nexample('second_example')\n", default_timeout=25,
        ).run()
        self.assertFalse(list(app.exception), [item.message for item in app.exception])


if __name__ == "__main__":
    unittest.main()
