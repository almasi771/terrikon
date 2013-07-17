 # -*- coding: utf-8 -*-

from .context import terrikon, render
import os
import unittest



class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""
    def setUp(self):
        self.app = terrikon.app.test_client()
    def test_index(self):
        rv = self.app.get('/')
        assert("render" in rv.data)

class RenderEmailSuite(unittest.TestCase):
    
    def test_sample_email(self):
        context = {"FirstName": "Test",
            "LastName": "Registrant",
            "Program": "Test Program",
            "ProgramYear": "2013",
            "ProgramName": "Test Program Academic Year Exchange",
            "DocumentDeadlineDate": "January 1st, 1985",
            "Finalist":True}
        rendered = render.render_html('sample_email.html', context)
        assert("January" in rendered)

if __name__ == '__main__':
    unittest.main()
