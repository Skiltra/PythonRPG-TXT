from random import randint
from time import sleep
import json

gameState = True
enablin = True

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
      if type(self.nextID) is str: 
            self.activeScene = self.nextID
            self.text = self.getJSON(self.activeScene, self.nextID)
      while self.activeScene:
          if self.text != None and type(self.nextID) is int:
            print(f"{self.text}") #TODO: fix printing of entire JSON file
            sleep(5)
            if self.nextID > self.id:
              self.text = self.getJSON(self.activeScene, self.nextID)
              print(f">Assigning New Text {self.nextID}")
          else:
             print(f"DEBUG FALLBACK; text{self.text} id {self.id} nextID {self.nextID}")
             self.getJSON(self.activeScene, self.nextID)

    def getJSON(self, menu, tarid):
        print(f">ID Set at {self.id} nextIs {self.nextID}, activeScene: {self.activeScene}")
        with open("scenes.json", "r", encoding='utf-8' ) as file:
          data = json.load(file) 
          self.text = data[menu] 
          for content in self.text:
              self.nextID = content.get("nextID")
              if tarid == content["id"]: # tarid can be boht str and int
                return content["text"]
              if isinstance(self.nextID, str):
                print(">Switching JSON Array")
                self.nextID = 0
                self.activeScene = self.nextID

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
    if enablin:
      scenes = dialogueManager()
      player = Player()
      input = inputSystem()
      enablin = False
    Main_Menu()
    scenes.getDialogue("ship")