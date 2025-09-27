

class inventory:
    def __init__(self):
        self.items = []
    
    def inventory(self, item):  
        if self.item in self.inventory:
            self.inventory.remove(item)
        else:
            self.inventory.append(item)

class Player:
    def __init__(self):
        self.inventory = inventory()
        self.element = None
        self.health = 100
        self.morality = 5.0
        self.score = 0
        self.conditions = []
