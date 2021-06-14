from werkzeug.wrappers import response
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

    # register route should return OK
    def test_registration(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # profile route should return FOUND
    def test_profile(self):
        tester = app.test_client(self)
        response = tester.get('/profile', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    # tasks route should return FOUND
    def test_tasks(self):
        tester = app.test_client(self)
        response = tester.get('/tasks', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    # calendar route should return FOUND
    def test_calendar(self):
        tester = app.test_client(self)
        response = tester.get('/calendar', content_type='html/text')
        self.assertEqual(response.status_code, 302)
    
    # notes route should return FOUND
    def test_notes(self):
        tester = app.test_client(self)
        response = tester.get('/notes', content_type='html/text')
        self.assertEqual(response.status_code, 302)

if __name__ == "__main__":
    unittest.main()
