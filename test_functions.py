import unittest
import funtions

class TestFunctions(unittest.TestCase):
    def test_load_file(self):
        data = funtions.load_file('./heroes.csv')
        self.assertIsInstance(data, dict)
        self.assertGreater(len(data), 0)
        # Check a specific hero
        self.assertIn('0', data)
        self.assertEqual(data['0']['name'], 'A-Bomb')

if __name__ == '__main__':
    unittest.main()