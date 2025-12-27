#########################################// Testing \\###############################################
import random #TBD; used for some behaviours, FIX: maybe could be rollSystem
from events import rollSystem
from player import inventory

npcLoad = True
source = None

# TODO: use npc.json
class behaviour(rollSystem):
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
        value = random.randint(1,5)
        if value > 2:
            self.flags + 1 # TODO: make relative addition instead of static
#  TODO: do somethign with this
class companion(behaviour, inventory):
    def __init__(self):
        behaviour.__init__(self)
        inventory.__init__(self)
# TODO: do later
class persistantNPC(behaviour, inventory):
    def __init__(self):
        behaviour.__init__(self)
        inventory.__init__(self)
        self.relation
        self.prefernces = {"talk": 0, "trade": 0}
# TODO: delay do later
class enemy(behaviour):
    def __init__(self):
        behaviour.__init__(self)
        self.loot = None
##### I DONT KNOW WHAT TO DO WITH THIS; why it needs to be a seperate class
class relations:
    def __init__(self):
        print("this relation")

######### INITIALIZE #########
if npcLoad:
    npcLoad = False
    rel = relations()
