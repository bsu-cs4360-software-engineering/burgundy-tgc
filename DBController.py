import json

class DBController:
    def __init__(self, filename):
        self.filename = filename

    def read_database(self):    
        with open(self.filename, 'r') as data:
            return json.load(data)
        
    def add_card_to_db(self, newData):
        with open(self.filename, 'w') as data:
            json.dump(newData, data, indent=4)