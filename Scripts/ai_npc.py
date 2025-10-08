#########################################// Testing \\###############################################
import random #TBD; used for some behaviours 
from events import rollSystem
from player import inventory

npcLoad = True
source = None

def callActions():
    if source:
        print("")
    else:
        print("no source cannot parse")

# TODO: use npc.json
class behaviour(rollSystem):
    def __init__(self, type, health=100):
        self.name = type
        self.health = health
        self.strength = 0
        self.alive = True
        self.state = "passive" #primary condition for behavior
        self.flags = 0 # trying to determine behaviour

    def determineAI(self):
        if self.alive == "dead":
            print("delete this somehow")
    
    def AIattack(self):
        value = random.randint(1,5)
        if value > 2:
            self.flags + 1 # TODO: make relative addition instead of static

class companion(behaviour, inventory):
    def __init__(self):
        behaviour.__init__(self)
        inventory.__init__(self)

class persistantNPC(behaviour, inventory):
    def __init__(self):
        behaviour.__init__(self)
        inventory.__init__(self)
        self.relation
        self.prefernces = {"talk": 0, "trade": 0}

class enemy(behaviour):
    def __init__(self):
        behaviour.__init__(self)
        self.loot = None

######### INITIALIZE
if npcLoad:
    callActions(source) # TODO: link either to events roll or figure out actions
    npcLoad = False