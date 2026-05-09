###########################################// TESTING \\#############################################
"""market is supposed to be buying/sell and market mechanics, economy is the self-explanatory"""
from market import Markets
from events import RollSystem as roller# for npc behaviour determination

# TODO: handle persistent and non persistent NPC

class Behaviour(roller):
    stateFocus = "live" # Handles what is available by instances and stops processes if needed
    def __init__(self, type, health=100):
        self.name = type
        self.health = health
        self.strength = 0
        self.alive = True
        
        self.stateNPC = "passive" #primary condition for behavior
        self.flags = 0 # behavior switching TODO: make max 100.0

    def determineAI(self):
        if self.alive == "dead":
            print("delete this somehow")
    
    def attack(self):
        value = roller.basic()
        if value > 2:
            self.flags += 1 # TODO: make relative addition instead of static

class PlayFeatures:
    def __init__(self):
        return

    def Inventory(self):
        return
    def Location(self): # dating and location
        return

# TODO: Implement npc and player relation system

###################################LIVING OBJECTS###################################
class Player(Inventory, locations):
    def __init__(self):
        self.inventory = Inventory()
        self.element = None
        self.health = 100
        self.morality = 5.0
        self.score = 0
        self.conditions = []



class npcs(Behaviour, hasInventory=False, companion=False): # TODO: loot/enemy toggle
    def __init__(self):
        Behaviour.__init__()
        self.inventory = Inventory() if hasInventory else None # TODO: Test this works
        
