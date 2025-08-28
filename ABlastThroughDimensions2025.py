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
            self.id = self.nextID
            self.nextID +=1
            print(f"ID {self.id} and next {self.nextID}")
          else:
             print("scene fallback")

    def getJSON(self, menu, tarid):
        print(f"ID Set to {self.id} next is {self.nextID}, active Scene: {self.activeScene}")
        with open("scenes.json", "r") as file:
          data = json.load(file) # loads file
          self.text = data[menu] #filter the json array
          for content in self.text:
              if tarid == content["id"]:
                return content["text"]


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
    def advancedType(self):
       print("TODO: NEED TO MAKE IT ALLOW FOR COMPARING EXISTENCE OF SEPERATE WORD THAT EXIST IN THE STRING 'jim went to the store' and user input 'jim store' so i need to write logic where this is true as its false because of python logic")

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
    player = Player()
    scenes = dialogueManager()
    input = inputSystem()
    Main_Menu()
    scenes.getDialogue("gameIntro")