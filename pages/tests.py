from django.test import TestCase, SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_about_page_status_code(self):
        resp = self.client.get('/about/')
        self.assertEqual(resp.status_code, 200)