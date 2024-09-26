class Field:
    def __init__(self):
        self.boss_health = 100

    def apply_card(self, card):
        # for now, just damages a single boss, but we can add more effects later on
        self.boss_health -= card.damage
        print(f"The boss took {card.damage} damage. The boss health is now {self.boss_health}/100.")

        if self.boss_health <= 0:
            print("The boss has been defeated.")
