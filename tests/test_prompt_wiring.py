"""The shared lesson changes its illustration without touching learner progress."""

from pathlib import Path
import sys
import unittest

from streamlit.testing.v1 import AppTest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.state.journey import dumps_journey, loads_journey
from Help.guides.prompt_wiring import compose_text, composition_markdown
from Help.guides.node_atlas import connection_types_match


class PromptWiringTests(unittest.TestCase):
    def test_style_opt_in_keeps_original_text_and_uses_chosen_separator(self):
        instruction = "Keep the face.\nChange the coat."
        self.assertEqual(compose_text(instruction, "film grain"), instruction)
        self.assertEqual(compose_text(instruction, "", True), instruction)
        self.assertEqual(compose_text(instruction, "film grain", True, "\n"), instruction + "\nfilm grain")
        exported = composition_markdown(instruction, "film grain", False, "\n")
        effective = exported.split("## Prepared effective text", 1)[1].split("## Share words", 1)[0]
        self.assertIn(instruction, effective)
        self.assertNotIn("film grain", effective)
        fenced = "Keep these literal instructions:\n```\n# Still prompt text\n````"
        exported = composition_markdown(fenced, "soft light", True)
        self.assertIn("`````text\n" + fenced + "\n`````", exported)
        self.assertIn("`````text\n" + fenced + ", soft light\n`````", exported)

    def test_prompt_types_distinguish_raw_strings_from_conditioning(self):
        self.assertTrue(connection_types_match("PrimitiveStringMultiline", "STRING", "StringConcatenate", "string_a"))
        self.assertTrue(connection_types_match("StringConcatenate", "STRING", "CLIPTextEncode", "text"))
        self.assertFalse(connection_types_match("StringConcatenate", "STRING", "ConditioningConcat", "conditioning_to"))
        self.assertTrue(connection_types_match("CLIPTextEncode", "CONDITIONING", "ConditioningConcat", "conditioning_to"))

    def test_composition_drafts_are_scoped_and_survive_leaving_the_lesson(self):
        app = AppTest.from_string('''
import streamlit as st
from Help.guides.prompt_wiring import render_composition
from Help.state.journey import new_journey
st.session_state.setdefault("help_journey", new_journey())
if st.toggle("Show lesson", value=True, key="show"):
    render_composition("first")
    render_composition("second")
''', default_timeout=20).run()
        before = loads_journey(dumps_journey(app.session_state['help_journey']))
        self.assertFalse(app.exception)
        self.assertFalse(app.toggle(key="first_enabled").value)
        app.text_area(key="first_instruction").set_value("Keep this design").run()
        app.toggle(key="first_enabled").set_value(True).run()
        app.text_area(key="first_style").set_value("soft daylight").run()
        self.assertTrue(any(code.value == "Keep this design, soft daylight" for code in app.code))
        self.assertFalse(app.toggle(key="second_enabled").value)
        self.assertEqual(app.text_area(key="second_instruction").value, "")
        app.toggle(key="first_enabled").set_value(False).run()
        self.assertTrue(any(code.value == "Keep this design" for code in app.code))
        app.toggle(key="show").set_value(False).run()
        app.toggle(key="show").set_value(True).run()
        self.assertEqual(app.text_area(key="first_style").value, "soft daylight")
        self.assertFalse(app.toggle(key="first_enabled").value)
        self.assertEqual(app.text_area(key="first_instruction").value, "Keep this design")
        self.assertEqual(app.session_state['help_journey'], before)
        self.assertFalse(app.exception)

    def test_shared_lessons_keep_independent_controls_and_preserve_journal(self):
        app = AppTest.from_string("""
import streamlit as st
from Help.state.journey import new_journey
from Help.guides.prompt_wiring import render
from Help.guides.generation_settings import render as render_settings
if 'help_journey' not in st.session_state:
    journey = new_journey()
    journey.update(chosen_path='forge', completed_steps=['brief'], goal='Keep my existing scene')
    st.session_state['help_journey'] = journey
render('anatomy')
render('atlas')
render_settings('anatomy_settings')
render_settings('model_settings')
""", default_timeout=20).run()
        self.assertFalse(app.exception)
        original = loads_journey(dumps_journey(app.session_state['help_journey']))
        app.radio(key='anatomy_stage').set_value('2 / Route the two prompts').run()
        self.assertFalse(app.exception)
        self.assertEqual(app.radio(key='atlas_stage').value, '1 / Supply both encoders')
        self.assertTrue(any('KSampler.positive' in code.value and 'KSampler.negative' in code.value for code in app.code))
        app.radio(key='atlas_stage').set_value('3 / Complete the image path').run()
        self.assertFalse(app.exception)
        self.assertEqual(app.radio(key='anatomy_stage').value, '2 / Route the two prompts')
        self.assertTrue(any('VAE Decode.IMAGE → Save Image.images' in code.value for code in app.code))
        app.selectbox(key='model_settings_size').select('SD 1.5 · tutorial portrait').run()
        self.assertFalse(app.exception)
        self.assertEqual(app.selectbox(key='anatomy_settings_size').value, 'SDXL · square starting point')
        self.assertEqual(app.radio(key='anatomy_stage').value, '2 / Route the two prompts')
        self.assertEqual(app.session_state['help_journey'], original)


if __name__ == '__main__':
    unittest.main()
