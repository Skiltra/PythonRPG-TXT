###########################################// TESTING: \\#############################################
########################### SUPPOSE TO REPLACE Scenes or supplement it! ##############################
import random
import json
from time import sleep



class eventSystem:
    def __init__(self):
        self.varUse = None
        print("instance event initialized")

    def randomEvent(self):
        number = random.randint(1,7)
        print("was in plannign for original never implementede")
    
    def mapMode(self):
       print("movement without dialogue loop or input wait")


class dialogueManager():
    def __init__(self):
      self.scene = sceneLoader
      self.id = ["active",0,1]
      self.text = []
      self.actionNotify = None

    def getDialogue(self,jsonheading=sceneLoader, jsonIncrement=0):
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

    def getJSON(self, menu, tarid):
        self.scene = menu
        print(f">getJSON DEBUG: ID{self.id}, ACT:{self.actionNotify}")
        with open("scenes.json", "r", encoding='utf-8') as file:
          data = json.load(file) 
          self.text = data[menu]
          for content in self.text:
              self.action = content.get("conditions")
              if tarid == self.id:
                  return content["text"]
              elif isinstance(self.id[2], str):
                  global sceneLoader
                  print(">Switching JSON Array")
                  self.id[2] = 0
                  self.scene = self.id[2]
              else:
                 print("all json conditions failed")


# EXPERIMENTING HERE, UNRELATED TO GOALS
class actions:
    def __init__(self):
        self.actionsSet = {
            "passive": {
                "talk"
                "insult"

            },
            "active": {
                "gift": [0,0,0]

            },
            "special": {

            }
        }
    
    def barter():
        print("from companion inventory or player exchange items")