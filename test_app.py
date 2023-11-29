import unittest
from app import app

class FlaskForexConverterTests(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    def test_homepage(self):
        # Test the homepage response status code
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_converter_with_valid_data(self):
        # Test the forex converter with valid data
        response = self.app.post('/', data=dict(base_currency='USD', target_currency='EUR', amount=100))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'is equal to', response.data)

    def test_converter_with_invalid_data(self):
        # Test the forex converter with invalid data
        response = self.app.post('/', data=dict(base_currency='ABC', target_currency='XYZ', amount=100))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Error fetching exchange rate data', response.data)

if __name__ == '__main__':
    unittest.main()