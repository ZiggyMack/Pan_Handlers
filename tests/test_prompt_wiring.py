"""The shared lesson changes its illustration without touching learner progress."""

from pathlib import Path
import sys
import unittest

from streamlit.testing.v1 import AppTest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Help.journey import dumps_journey, loads_journey


class PromptWiringTests(unittest.TestCase):
    def test_shared_lessons_keep_independent_controls_and_preserve_journal(self):
        app = AppTest.from_string("""
import streamlit as st
from Help.journey import new_journey
from Help.prompt_wiring import render
from Help.generation_settings import render as render_settings
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
