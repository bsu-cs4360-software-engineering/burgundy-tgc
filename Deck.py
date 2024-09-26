import json
import random
from DBController import DBController

class Deck:
    def __init__(self):
        self.deck = []
        self.db = DBController("info.json")

    def clear(self):
        self.deck = []

    def populate(self):
        data = self.db.read_database()
        for card in data['cards']:
            self.deck.append(card)
    
    def deal(self):
        if len(self.deck) == 0:
            return 0
        else:
            return self.deck.pop()
    
    def shuffle(self):
        random.shuffle(self.deck)