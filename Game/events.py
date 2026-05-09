###########################################// Events: \\#############################################
import random
import json
import Scripts.player as play
from Scripts.player import Behaviour
from time import sleep
from market import Economy


class Eventsystem:
    def __init__(self):
        self.varUse = None
        print("instance event initialized")

    def randomEvent(self):
        number = random.randint(1,7)
        print("was in plannign for original never implemented")
    
    def mapMode(self):
       print("movement without dialogue loop or input wait")
       print(DialogueManager())


class DialogueManager():
    def __init__(self, scene):
      self.scene = scene
      self.id = ["active",0,1]
      self.text = []
      self.actionNotify = None

    def getDialogue(self,jsonheading=None, jsonIncrement=0):
      jsonheading = self.scene
      print(f"{self.scene}")
      if self.id[1] < self.id[2]:
          self.scene = self.getJSON(jsonheading, jsonIncrement)
      while self.scene:
          print(f"text {self.text}")
          if self.text != None and type(self.id[2]) is int: # BUG: ENDLESS LOOP HERE
            print(f"{self.text} dataDEBUG: ID{self.id}, ACT{self.action}")
            sleep(5)
          if type(self.id[2]) is str:
            global sceneLoader
            self.scene = self.id[2]
            sceneLoader = self.getJSON(self.scene, self.id[2])      

# TODO: Replace with mgrNumbers
## READ: factor1 + factor2 / 2 = combined then combined < roll = True (flag made)
class RollSystem:
    def __init__(self, max=100):
        self.chance = 0.5
        self.flags = 0 # determine long term behavior even for successful actions or repetitious behavior
        self.maxFlags = max # if higher set to 100

    def outcome(self):
       number = random.random()
       if self.chance < number:
          return True
       else:
          return False

    def changeAction(self):
       print(f"{self.flags}")

    @staticmethod
    def basic():
       return random.random()

