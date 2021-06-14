from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    # canary test for routes
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    # login route should return OK
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    

if __name__ == "__main__":
    unittest.main()
