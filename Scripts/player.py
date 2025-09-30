###########################################// TESTING \\#############################################

class Inventory:
    def __init__(self):
        self.items = []
    
    def inventory(self, item):  
        if self.item in self.items:
            self.inventory.remove(item)
        else:
            self.inventory.append(item)

class Player():
    def __init__(self):
        self.inventory = Inventory()
        self.element = None
        self.health = 100
        self.morality = 5.0
        self.score = 0
        self.conditions = []

class locations:
    def __init__(self):
        self.xPOS = 8
        self.yPOS = 8

    def dates():
        print("either new class or sub component of locations")
    def randomEvent():
        print("TODO: passive encounters")
        print("TODO: aggressive encounters")