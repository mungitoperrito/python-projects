# To run tests:
#
# # # All tests
# python test_hello_flask.py
#
# # Specific test
# python -m unittest test_hello_flask.FlaskAppTestCase
#
# # Specific test method
# python -m unittest test_hello_flask.FlaskAppTestCase.test_hello_name_endpoint

import unittest
from hello_flask import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        """Test the root endpoint."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_hello_name_endpoint(self):
        """Test the /hello/<n> endpoint with a specific name."""
        response = self.app.get('/hello/Alice')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Alice!', response.data)
        self.assertIn(b'Nice to meet you!', response.data)

    def test_hello_name_different_names(self):
        """Test the /hello/<n> endpoint with different names."""
        test_names = ['Bob', 'Charlie', 'Diana']

        for name in test_names:
            with self.subTest(name=name):
                response = self.app.get(f'/hello/{name}')
                self.assertEqual(response.status_code, 200)
                self.assertIn(f'Hello, {name}!'.encode(), response.data)

    def test_hello_name_special_characters(self):
        """Test the /hello/<n> endpoint with special characters."""
        response = self.app.get('/hello/José')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, Jos', response.data)

if __name__ == '__main__':
    unittest.main()