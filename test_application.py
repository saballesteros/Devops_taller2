import unittest
import application

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.app = application.application.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertGreater(len(data), 0)

    def test_heroe(self):
        response = self.app.get('/0')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data['name'], 'A-Bomb')

if __name__ == '__main__':
    unittest.main()