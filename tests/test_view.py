import unittest
from views import app


class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_page_by_default_url(self):
        status = self.app.get('/')
        self.assertEqual(status.status_code, 200)

    def test_home_page_by_home_page_url(self):
        status = self.app.get('/home_page')
        self.assertEqual(status.status_code, 200)