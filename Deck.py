import random
from DBController import DBController
from Card import Card

class Deck:
    def __init__(self):
        self.deck = []
        self.db = DBController("info.json")

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