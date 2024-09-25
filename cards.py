import json

class cards:

    def __init__(self):
        with open('info.json', 'r') as f:
            self.data = json.load(f)

    def GetHealth(self, name):
        for card in self.data['cards']:
            if card['name'].lower() == name.lower():
                return card['health_points']
        return None

    def GetDefense(self, name):
        for card in self.data['cards']:
            if card['name'].lower() == name.lower():
                return card['defense']
        return None
    
    def GetAttack(self, name):
        for card in self.data['cards']:
            if card['name'].lower() == name.lower():
                return card['attack']
        return None
    
    def GetName(self, name):
        for card in self.data['cards']:
            if card['name'].lower() == name.lower():
                return card['name']
        return None
    
    # Update Functions

    def UpdateHealth(self, name, new_attack):
        for card in self.data['cards']:
            if card['name'].lower() == name.lower():
                card['health'] = new_attack
                self._save_to_file()
                return True
        return False
        
    def UpdateDefense(self, name, new_attack):
        for card in self.data['cards']:
            if card['name'].lower() == name.lower():
                card['defense'] = new_attack
                self._save_to_file()
                return True
        return False

    def UpdateAttack(self, name, new_attack):
        for card in self.data['cards']:
            if card['name'].lower() == name.lower():
                card['attack'] = new_attack
                self._save_to_file()
                return True
        return False

    def _save_to_file(self):
        with open('info.json', 'w') as f:
            json.dump(self.data, f, indent=4)