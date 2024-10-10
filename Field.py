from Hand import Hand
class Field:
    def __init__(self):
        self.boss_health = 100

    def apply_card(self, card):
        if card == 0:
            return False
        else:
            # for now, just damages a single boss, but we can add more effects later on
            self.boss_health -= card.attack
            print(f"The boss took {card.attack} damage. The boss health is now {self.boss_health}/100.")

            if self.boss_health <= 0:
                print("The boss has been defeated.")

    def get_boss_health(self):
        return self.boss_health