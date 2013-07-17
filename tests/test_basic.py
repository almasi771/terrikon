# -*- coding: utf-8 -*-

from .context import terrikon, render_email
import os
import unittest
import tempfile



class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def setUp(self):
        self.app = terrikon.app.test_client()
    def test_index(self):
        rv = self.app.get('/')
        assert("render" in rv.data)

class RenderEmailSuite(unittest.TestCase):
    def test_render_template_for_email(self):
        rendered_email = render_email.render('sample_email.html', FirstName = "AFirstName")
        print(rendered_email)
        assert("sample email generated for" in rendered_email)
        assert("AFirstName" in rendered_email)


if __name__ == '__main__':
    unittest.main()
