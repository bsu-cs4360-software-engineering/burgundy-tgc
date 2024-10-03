import random
import unittest

class Card:
    def __init__(self, hp, attack, defense, name):
        self.health_points = hp
        self.attack = attack
        self.defense = defense
        self.name = name

    # Health Point
    def get_hp(self):
        return self.health_points
    def update_hp(self, new_hp):
        self.health_points = new_hp
        return True
    
    # Attack
    def get_attack(self):
        return self.attack
    def update_attack(self, new_attack):
        self.attack = new_attack
        return True
    
    # Damage
    def take_damage(self, inflected):
        self.health_points -= inflected
        return True
    
    # Defense
    def get_defense(self):
        return self.defense
    def update_defense(self, new_defense):
        self.defense = new_defense
        return True
    
    # Name
    def get_name(self):
        return self.name

class TestCardMethods(unittest.TestCase):
    
    def setUp(self):
        self.card = Card(200, 124, 432, "Test Card")

    def test_get_hp(self):
        self.assertEqual(self.card.get_hp(), 200)

    def test_update_hp(self):
        new_hp = random.randint(1, 1000)
        self.card.update_hp(new_hp)
        self.assertEqual(self.card.get_hp(), new_hp)

    def test_get_attack(self):
        self.assertEqual(self.card.get_attack(), 124)

    def test_update_attack(self):
        new_attack = random.randint(1, 1000)
        self.card.update_attack(new_attack)
        self.assertEqual(self.card.get_attack(), new_attack)

    def test_take_damage(self):
        initial_hp = self.card.get_hp()
        damage = 50
        self.card.take_damage(damage)
        self.assertEqual(self.card.get_hp(), initial_hp - damage)

    def test_get_defense(self):
        self.assertEqual(self.card.get_defense(), 432)

    def test_update_defense(self):
        new_defense = random.randint(1, 1000)
        self.card.update_defense(new_defense)
        self.assertEqual(self.card.get_defense(), new_defense)

    def test_get_name(self):
        self.assertEqual(self.card.get_name(), "Test Card")

    def test_random_values(self):
        new_hp = random.randint(1, 1000)
        new_attack = random.randint(1, 1000)
        new_defense = random.randint(1, 1000)
        card_new = Card(new_hp, new_attack, new_defense, "Windows Sucks")
        
        self.assertEqual(card_new.get_hp(), new_hp)
        self.assertEqual(card_new.get_attack(), new_attack)
        self.assertEqual(card_new.get_defense(), new_defense)
        self.assertEqual(card_new.get_name(), "Windows Sucks")