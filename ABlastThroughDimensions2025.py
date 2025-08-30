from random import randint
from time import sleep
import json

gameState = True

class dialogueManager:
    def __init__(self):
      self.activeScene = None # assigning strings
      self.id = None
      self.nextID = 1
      self.text = []
      self.action = None

    def getDialogue(self,jsonheading, jsonIncrement=0):
      self.activeScene = jsonheading
      self.id = jsonIncrement
      self.text = self.getJSON(jsonheading, self.id) 
      while self.activeScene:
          if self.text != None:
            print(f"{self.text}")
            sleep(5)
          if self.nextID > self.id:
            self.text = self.getJSON(self.activeScene, self.nextID)
            print(f">displaying test and adjusting IDs")
          elif isinstance(self.nextID, str): # TODO: DOES NOT WORK STILL implement scenes via text
             self.activeScene = self.nextID
          else:
             print(f"SCENE FALLBACK; function couldnt adjust ID's or text already is something; id {self.id} nextID {self.nextID}")

    def getJSON(self, menu, tarid):
        print(f">ID Set at {self.id} nextIs {self.nextID}, activeScene: {self.activeScene}")
        if self.text == None: # A method to end loop and reintialize
           self.activeScene = False
        with open("scenes.json", "r") as file:
          data = json.load(file) 
          self.text = data[menu] # Filters JSON by array contents
          for content in self.text:
              purpose = content.get("nextID")
              if tarid == content["id"]:
                return content["text"]
              if isinstance(purpose, str):
                 self.activeScene = purpose

class inputSystem:
    def _init_(self):
      self.options = [] # Used for storing options
      self.variable = None # Used for checking previous options
      self.userInput = None # used for comparing user data
  
    def listen(self, var):
       if var == "attack":
          player.rollCombat()

    def inputHandler(self, option, list=None):
        print("pause getDialogue through activeScene")
        if option == "choices":
          if list:
            self.option = list
            input()
          else: 
            self.option = self.variable 
        if option == "determine":
           print("using conditions, also passes to getDialogue class variables")
           player.conditions # as in this has to check conditions to determine which ID is needed on conditions attribute in json
        if option == "type":
           print("pause getDialogue;player types to varibale, options are assigned to self.option, self. variable is compared against self.options continue getDialogue chain")
           if self.userInput in input.advancedType():
              scenes.getDialogue("continue, and unpause getDialogue")

class Player:
  def __init__(self):
     self.inventory = []
     self.element = None
     self.health = 100
     self.morality = 5.0
     self.score = 0
     self.conditions = []
  def movePos(self, value):
      player.xpos += value
      player.ypos +- value
  def combatRoll(self, value):
     yes = randint(1)
     print("attribute base * random modifier outcome")

  def inventory(self, item):
     if self.item in self.inventory:
        self.inventory.remove(item)
     else:
        self.inventory.append(item)

def Main_Menu():
  print("""

    _      ____  _           _     _____ _                           _     
   / \    | __ )| | __ _ ___| |_  |_   _| |__  _ __ ___  _   _  __ _| |__  
  / _ \   |  _ \| |/ _` / __| __|   | | | '_ \| '__/ _ \| | | |/ _` | '_ \ 
 / ___ \  | |_) | | (_| \__ \ |_    | | | | | | | | (_) | |_| | (_| | | | |
/_/__ \_\ |____/|_|\__,_|___/\__| _ |_| |_| |_|_|  \___/ \__,_|\__, |_| |_|
|  _ \(_)_ __ ___   ___ _ __  ___(_) ___  _ __  ___            |___/       
| | | | | '_ ` _ \ / _ \ '_ \/ __| |/ _ \| '_ \/ __|                       
| |_| | | | | | | |  __/ | | \__ \ | (_) | | | \__ \                       
|____/|_|_| |_| |_|\___|_| |_|___/_|\___/|_| |_|___/                       

        """)

############################ Loop and Exit Functions ############################
def gameend():
  with open("scorelog.txt", "w") as file:
      file.write(str(player.score))
  if player.health >= 1:
    print("""
  ____                            ___                 _ 
 / ___| __ _ _ __ ___   ___      / _ \__   _____ _ __| |
| |  _ / _` | '_ ` _ \ / _ \    | | | \ \ / / _ \ '__| |
| |_| | (_| | | | | | |  __/    | |_| |\ V /  __/ |  |_|
 \____|\__,_|_| |_| |_|\___|     \___/  \_/ \___|_|  (_)

  """)
    Main_Menu ()
  else:
    Game_Exit ()

def Game_Exit ():
  choice = input('Press Q to Quit')
  if choice == 'q':
    gameState = False

if __name__ == "__main__":
  while gameState:
    print(" \n Initialized Game States")
    scenes = dialogueManager()
    player = Player()
    input = inputSystem()
    Main_Menu()
    scenes.getDialogue("mysteryMan")