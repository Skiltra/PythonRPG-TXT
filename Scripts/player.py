###########################################// TESTING \\#############################################
from market import markets # for sell buy
from events import rollSystem as roller# for npc behaviour determination



class behaviour(roller):
    stateFocus = "live" # Handles what is available by instances and stops processes if needed
    def __init__(self, type, health=100):
        self.name = type
        self.health = health
        self.strength = 0
        self.alive = True
        
        self.stateNPC = "passive" #primary condition for behavior
        self.flags = 0 # tbehavioru switching TODO: make max 100.0

    def determineAI(self):
        if self.alive == "dead":
            print("delete this somehow")
    
    def AIattack(self):
        value = roller.basic()
        if value > 2:
            self.flags += 1 # TODO: make relative addition instead of static

class Inventory:
    def __init__(self):
        self.items = []
    
    def inventory(self, item):  
        if self.item in self.items:
            self.inventory.remove(item)
        else:
            self.inventory.append(item)

class locations:
    location = {}
    grid = 15 * 15

    def __init__(self):
        self.POS = [8,8]
        self.year = 0
        self.day = 0
        self.hour = 0
        self.minutes = 0.0

    def dates(self):
        print(f"Y: {self.year}, D: {self.day} Time: {self.hour}:{self.minutes}")

    @classmethod
    def loadLocationData(cls,source):
        cls.locations = json.load(source) # BUG: work with main.py to get json

# TODO: Implement npc and player relation system

###################################LIVING OBJECTS###################################
class Player(Inventory, locations):
    def __init__(self):
        self.inventory = Inventory()
        locations.__init__(self)
        self.element = None
        self.health = 100
        self.morality = 5.0
        self.score = 0
        self.conditions = []



class npcs(behaviour, hasInventory=False, companion=False): # TODO: loot/enemy toggle
    def __init__(self):
        behaviour.__init__()
        self.inventory = Inventory() if hasInventory else None # TODO: Test this works
        

# class persistantNPC(behaviour, inventory):
#     def __init__(self):
#         behaviour.__init__(self)
#         inventory.__init__(self)
#         self.relation
#         self.prefernces = {"talk": 0, "trade": 0}
