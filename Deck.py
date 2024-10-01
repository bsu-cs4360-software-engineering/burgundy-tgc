import unittest
import random
from DBController import DBController
from Card import Card

class Deck:
    def __init__(self, database: DBController):
        self.deck = []
        if database is not DBController:
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


class DeckUnitTaest(unittest.TestCase):
    def setUp(self):
        self.test_deck = Deck(DBController('info.json'))

    def test_deck_populate(self):
        self.assertEqual(self.test_deck, False)

        self.test_deck.populate()

        self.assertEqual(self.test_deck, True)

    def test_deck_draw(self):
        drawed_card = self.test_deck.draw()

        self.assertEqual(drawed_card, True)

    def test_deck_shuffle(self):
        unshuffled_deck = self.test_deck

        self.test_deck.shuffle()
        
        self.assertEqual(unshuffled_deck == self.test_deck, False)

    def test_deck_clear(self):
        self.test_deck_clear()

        self.assertEqual(self.test_deck, [])
        
unittest.main()