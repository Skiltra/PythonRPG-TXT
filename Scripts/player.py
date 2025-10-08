###########################################// TESTING \\#############################################
from market import markets # for sell buy


class locations:
    def __init__(self):
        self.POS = [8,8]
        self.year = 0
        self.day = 0
        self.hour = 0
        self.minutes = 0.0

    def dates(self):
        print(f"Y: {self.year}, D: {self.day} Time: {self.hour}:{self.minutes}")

class Inventory:
    def __init__(self):
        self.items = []
    
    def inventory(self, item):  
        if self.item in self.items:
            self.inventory.remove(item)
        else:
            self.inventory.append(item)


class Player(Inventory, locations):
    def __init__(self):
        self.inventory = Inventory()
        locations.__init__(self)
        self.element = None
        self.health = 100
        self.morality = 5.0
        self.score = 0
        self.conditions = []