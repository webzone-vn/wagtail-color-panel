from django.core.exceptions import ValidationError
from django.test import TestCase
from wagtail.tests.utils import WagtailTestUtils

from wagtail_color_panel.blocks import ColorBlock


class PanelTest(TestCase, WagtailTestUtils):
    def test_color_block_render(self):
        block = ColorBlock()
        html = block.render("#333333")

        self.assertEqual("#333333", html)

    def test_form_uses_proper_input_type(self):
        block = ColorBlock()
        html = block.render_form("#333333")

        self.assertIn('type="color"', html)

    def test_that_hex_colors_are_validated(self):
        block = ColorBlock()
        with self.assertRaises(ValidationError) as ctx:
            block.clean("Invalid")

        self.assertTrue('Enter a valid color hash' in str(ctx.exception))
