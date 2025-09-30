#########################################// Testing \\###############################################
import random #TBD; used for some behaviours 
from player import inventory

# TODO: use npc.json
class behaviour:
    def __init__(self, type, health=100):
        self.name = type
        self.health = health
        self.strength = 0
        self.alive = True
        self.state = "passive" #primary condition for behavior

    def determineAI(self):
        if self.alive == "dead":
            print("delete this somehow")
    def moveLogic(self):
        print("figuring out coordinates")
    
    def AIattack(self):
        random.randint(1,5)

class companion(behaviour, inventory):
    def __init__(self):
        behaviour.__init__(self)
        inventory.__init__(self)

class persistantNPC(behaviour, inventory):
    def __init__(self):
        self.relation
        self.prefernces = {"talk": 0, "trade": 0}

class enemy(behaviour):
    def __init__(self):
        self.loot = None