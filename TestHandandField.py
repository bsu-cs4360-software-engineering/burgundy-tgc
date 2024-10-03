import unittest
from Hand import Hand
from Field import Field
from Card import Card

class TestHand(unittest.TestCase):
    def generate_test_hand(self):
        # generates hand with 5 cards (max is 4)
        self.hand = Hand(max_cards=4)
        self.card1 = Card(name="Card1", attack=10)
        self.card2 = Card(name="Card2", attack=20)
        self.card3 = Card(name="Card3", attack=30)
        self.card4 = Card(name="Card4", attack=40)
        self.card5 = Card(name="Card5", attack=50)

    def test_add_card(self):
        # tests adding a card to the hand
        self.hand.add_card(self.card1)
        self.hand.add_card(self.card2)
        self.hand.add_card(self.card3)
        self.hand.add_card(self.card4)
        self.assertEqual(len(self.hand.cards_in_hand), 4)
        self.hand.add_card(self.card5)  # should not work since max is 4
        self.assertEqual(len(self.hand.cards_in_hand), 4)

    def test_add_invalid_card(self):
        with self.assertRaises(ValueError):
            self.hand.add_card("InvalidCard")  # Not a Card object

    def test_play_card(self):
        self.hand.add_card(self.card1)
        self.hand.add_card(self.card2)
        played_card = self.hand.play_card(0)
        self.assertEqual(played_card, self.card1)
        self.assertEqual(len(self.hand.cards_in_hand), 1)

    def test_play_invalid_card(self):
        self.hand.add_card(self.card1)
        played_card = self.hand.play_card(5)  # should not work (cards are 0-4 index)
        self.assertEqual(played_card, 0)

    def test_show_hand(self):
        self.hand.add_card(self.card1)
        self.hand.add_card(self.card2)
        self.hand.show_hand()

class TestField(unittest.TestCase):
    def setUpField(self):
        # tests setting up the field (boss health)
        self.field = Field()
        self.card = Card(name="AttackCard", attack=20)

    def test_apply_card(self):
        self.field.apply_card(self.card)
        self.assertEqual(self.field.boss_health, 80)

    def test_boss_defeated(self):
        # tests boss running out of health
        self.card.attack = 100  # depletes all 100 of boss health
        self.field.apply_card(self.card)
        self.assertEqual(self.field.boss_health, 0)

    def test_apply_invalid_card(self):
        # tests applying a card that isn't valid
        result = self.field.apply_card(0)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
