from DBController import DBController
from Card import Card

import random
import unittest
from unittest.mock import Mock, patch

class Deck:
    def __init__(self, database: DBController):
        self.deck = []
        if not isinstance(database, DBController):
            raise TypeError
        else:
            self.db = database

    def clear(self):
        self.deck = []

    def populate(self):
        data = self.db.read_database()
        for obj in data['cards']:
            self.deck.append(Card(obj['health_points'], obj["attack"], obj["defense"], obj["name"]))
    
    def draw(self):
        if len(self.deck) == 0:
            return 0
        else:
            return self.deck.pop()
    
    def shuffle(self):
        random.shuffle(self.deck)


class DeckUnitTest(unittest.TestCase):
    def setUp(self):
        self.mock_db = Mock(spec=DBController)
        self.test_deck = Deck(self.mock_db)

    def test_deck_init_valid(self):
        self.assertEqual(self.test_deck.db, self.mock_db)
        
    def test_deck_init_invalid(self):
        with self.assertRaises(TypeError):
            Deck("invalid_db")

    def test_deck_populate(self):
        mock_data = {
            "cards": [
                {
                    "name": "Barbarian",
                    "health_points": 90,
                    "defense": 15,
                    "attack": 20
                },
                {
                    "name": "Monk",
                    "health_points": 50,
                    "defense": 15,
                    "attack": 30
                }
            ]
        }
        self.mock_db.read_database.return_value = mock_data

        self.test_deck.populate()

        expected_length       = 2
        expected_instance     = True
        expected_name_index_0 = "Barbarian"

        actual_length         = len(self.test_deck.deck)
        actaul_instance       = isinstance(self.test_deck.deck[0], Card)
        actual_name_index_0   = self.test_deck.deck[0].name

        self.assertEqual(actual_length, expected_length)
        self.assertEqual(actaul_instance, expected_instance)
        self.assertEqual(actual_name_index_0, expected_name_index_0)

    def test_empty_deck_draw(self):
        self.assertEqual(self.test_deck.draw(), 0)

    def test_populated_deck_draw(self):
        mock_card = Mock(Card)
        self.test_deck.deck.append(mock_card)

        expected_value = self.test_deck.deck[0]
        expected_length = 0

        actual_value = self.test_deck.draw()
        actual_length = len(self.test_deck.deck)

        self.assertEqual(actual_value, expected_value)
        self.assertEqual(actual_length, expected_length)

    @patch('random.shuffle')
    def test_deck_shuffle(self, mock_shuffle):
        self.test_deck.deck = [Mock(Card), Mock(Card)]

        self.test_deck.shuffle()

        mock_shuffle.assert_called_once_with(self.test_deck.deck)

    def test_deck_clear(self):
        self.test_deck.deck = [Mock(Card), Mock(Card)]

        expected = []

        self.test_deck.clear()
        actual = self.test_deck.deck

        self.assertEqual(actual, expected)