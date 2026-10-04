"""Verify practice evidence survives navigation and stays portable in journal v1."""

from copy import deepcopy
from pathlib import Path
import sys
import unittest

from streamlit.testing.v1 import AppTest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.journey import MAX_ENTRIES, dumps_journey, loads_journey, new_journey
from Help.workflow_lab import new_workbook, workbook_entry, workbook_markdown
from Help.workflow_lessons import LESSONS


class WorkflowLabTests(unittest.TestCase):
    def new_app(self):
        app = AppTest.from_file(str(ROOT / "Help" / "app.py"), default_timeout=25).run()
        self.navigate(app, "ComfyUI guide")
        return app

    def navigate(self, app, section):
        app.button(key="help_nav_" + section).click().run()
        self.assertFalse(app.exception)

    def test_evidence_and_place_survive_navigation_and_export_without_changing_foundations(self):
        app = self.new_app()
        app.checkbox(key="help_widget_done_brief").check().run()
        self.navigate(app, "Compare paths")
        app.selectbox(key="help_widget_chosen_path").select("forge").run()
        self.navigate(app, "ComfyUI guide")
        original = deepcopy(app.session_state["help_journey"])
        app.text_area(key="help_workbook_widget_orient_evidence").set_value("Saved the learning copy; moving a box kept its links.").run()
        app.selectbox(key="help_workbook_widget_orient_status").select("Evidence recorded").run()
        app.selectbox(key="help_workbook_lesson").select("decode").run()
        note = "Decoder reported a missing vae input. Connected the matching VAE; preview appeared."
        app.text_area(key="help_workbook_widget_decode_evidence").set_value(note).run()
        app.selectbox(key="help_workbook_widget_decode_status").select("Practicing").run()
        app.text_input(key="help_workbook_widget_workflow").set_value("decoder-practice-v02.json").run()
        app.text_area(key="help_workbook_widget_next_step").set_value("Reopen the exported copy.").run()
        self.navigate(app, "Field journal")
        self.assertEqual(app.session_state["help_journey"], original)
        self.navigate(app, "ComfyUI guide")
        self.assertEqual(app.selectbox(key="help_workbook_lesson").value, "decode")
        self.assertEqual(app.text_area(key="help_workbook_widget_decode_evidence").value, note)
        self.assertEqual(app.text_input(key="help_workbook_widget_workflow").value, "decoder-practice-v02.json")
        app.selectbox(key="help_workbook_lesson").select("orient").run()
        self.assertEqual(app.selectbox(key="help_workbook_widget_orient_status").value, "Evidence recorded")
        self.assertIn("moving a box", app.text_area(key="help_workbook_widget_orient_evidence").value)
        app.button(key="help_workbook_save").click().run()
        self.assertFalse(app.exception)
        journal = app.session_state["help_journey"]
        self.assertEqual(len(journal["entries"]), 1)
        self.assertIn(note, journal["entries"][0]["observation"])
        self.assertEqual({key: value for key, value in journal.items() if key != "entries"},
                         {key: value for key, value in original.items() if key != "entries"})
        self.assertEqual(loads_journey(dumps_journey(journal)), journal)
        self.navigate(app, "Field journal")
        self.assertTrue(any(note in item.value for item in app.text))
        fresh = self.new_app()
        self.assertEqual(fresh.text_area(key="help_workbook_widget_orient_evidence").value, "")
        self.assertEqual(fresh.session_state["help_journey"]["entries"], [])

    def test_save_rejects_empty_evidence_and_full_journal_without_losing_draft(self):
        app = self.new_app()
        app.button(key="help_workbook_save").click().run()
        self.assertTrue(app.error)
        self.assertEqual(app.session_state["help_journey"]["entries"], [])
        note = "The exported graph reopened; a required model is still missing."
        app.text_area(key="help_workbook_widget_orient_evidence").set_value(note).run()
        original = deepcopy(app.session_state["help_journey"])
        old_entry = {"date": "2026-09-12", "title": "Earlier practice", "observation": "Saved.",
                     "next_step": "", "resource": ""}
        original["entries"] = [deepcopy(old_entry) for _ in range(MAX_ENTRIES)]
        app.session_state["help_journey"] = deepcopy(original)
        app.button(key="help_workbook_save").click().run()
        self.assertFalse(app.exception)
        self.assertTrue(any("300" in error.value for error in app.error))
        self.assertEqual(app.session_state["help_journey"], original)
        self.assertEqual(app.text_area(key="help_workbook_widget_orient_evidence").value, note)
        app.session_state["help_journey"] = {**original, "entries": original["entries"][:-1]}
        app.button(key="help_workbook_save").click().run()
        self.assertFalse(app.exception)
        self.assertEqual(len(app.session_state["help_journey"]["entries"]), MAX_ENTRIES)
        self.assertIn(note, app.session_state["help_journey"]["entries"][-1]["observation"])

    def test_exploring_skills_and_repair_feedback_does_not_claim_execution(self):
        app = self.new_app()
        original = deepcopy(app.session_state["help_journey"])
        for lesson in LESSONS:
            app.selectbox(key="help_workbook_lesson").select(lesson["id"]).run()
            self.assertFalse(app.exception)
            self.assertEqual(app.text_area(key=f"help_workbook_widget_{lesson['id']}_evidence").value, "")
        app.radio(key="help_workbook_answer_encode_prompt").set_value("Rename the CLIP output to positive").run()
        self.assertTrue(any("does not address" in item.value for item in app.info))
        app.radio(key="help_workbook_answer_encode_prompt").set_value("Insert CLIP Text Encode and enter a prompt").run()
        self.assertTrue(any("addresses this example" in item.value for item in app.success))
        app.selectbox(key="help_workbook_drill").select("family_match").run()
        app.radio(key="help_workbook_answer_family_match").set_value("Use an SDXL-compatible ControlNet and its documented control map").run()
        self.assertFalse(app.exception)
        self.assertTrue(any("structural check" in item.value for item in app.markdown))
        self.assertEqual(app.session_state["help_journey"], original)
        self.assertTrue(all(item["status"] == "Not started" for item in app.session_state["help_workflow_lab_draft"]["lessons"].values()))

    def test_largest_workbook_fits_v1_and_markdown_treats_notes_as_text(self):
        workbook = new_workbook()
        with self.assertRaises(ValueError):
            workbook_entry(workbook)
        workbook["lessons"]["trace"]["evidence"] = "Observed a connection error."
        workbook["lessons"]["build"]["status"] = "Evidence recorded"
        with self.assertRaises(ValueError):
            workbook_entry(workbook)
        for item in workbook["lessons"].values():
            item.update(status="Evidence recorded", evidence="界" * 1200)
        workbook["workflow"] = "w" * 1000
        workbook["next_step"] = "n" * 2000
        journal = new_journey()
        journal["entries"] = [workbook_entry(workbook)]
        self.assertEqual(loads_journey(dumps_journey(journal)), journal)
        workbook["lessons"]["orient"]["evidence"] = '<img src="https://example.com/pixel"> ![image](https://example.com/pixel)'
        exported = workbook_markdown(workbook)
        self.assertNotIn("<img", exported)
        self.assertNotIn("![image]", exported)
        self.assertIn("https://www.youtube.com/watch?v=JE5eykLuTXI", exported)


if __name__ == "__main__":
    unittest.main()
