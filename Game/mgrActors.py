"""market is supposed to be buying/sell and market mechanics, economy is the self-explanatory"""
from Game.modRandom import RollSystem # for npc behaviour determination
from Game.modInventory import Inventory
from Game.modInventory import Location

# TODO: handle persistent and non persistent NPC

class Behaviour(RollSystem):
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
        value = RollSystem.basic()
        if value > 2:
            self.flags += 1 # TODO: make relative addition instead of static



# TODO: Implement npc and player relation system

###################################LIVING OBJECTS###################################
class Player(Inventory, Location):
    def __init__(self):
        self.element = None
        self.health = 100
        self.morality = 5.0
        self.score = 0
        self.conditions = []



class Npcs(Behaviour, companion=False): # TODO: loot/enemy toggle
    def __init__(self):
        Behaviour.__init__()

