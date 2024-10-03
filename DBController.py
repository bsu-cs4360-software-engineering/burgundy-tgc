import json
import unittest
from unittest.mock import mock_open, patch

class DBController:
    def __init__(self, filename):
        self.filename = filename

    def read_database(self):    
        with open(self.filename, 'r') as data:
            return json.load(data)
        
class DBControllerUnitTest(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test.json"
        self.test_db = DBController(self.test_filename)

    @patch('builtins.open', new_callable = mock_open, read_data='{"cards": [{"name": "Barbarian", "attack": 20, "defense": 15, "health_points": 90}]}')
    def test_read_database(self, mock_file):
    
        expected = {
            "cards": [
                {
                "name": "Barbarian",
                "health_points": 90,
                "defense": 15,
                "attack": 20
                }
            ]
        }

        actual = self.test_db.read_database()

        self.assertEqual(actual, expected)