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
    
    # Defesne
    def get_defense(self):
        return self.defense
    def update_defesne(self, new_defense):
        self.defense = new_defense
        return True
    
    #Name
    def get_name(self):
        return self.name
