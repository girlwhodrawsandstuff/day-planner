from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    # canary test for routes
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 302)

if __name__ == "__main__":
    unittest.main()
