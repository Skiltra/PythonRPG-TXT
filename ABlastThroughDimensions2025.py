from random import randint
from os import system, name
from time import sleep
import sys
import json

gameState = True

class dialogueManager:
    def __init__(self):
      self.activeScene = None # assigning strings
      self.id = None
      self.nextID = None
      self.text = []

    def getDialogue(self,jsonheading, jsonIncrement=0):
      self.id = jsonIncrement
      self.activeScene = self.getJSON(jsonheading, self.id)
      while self.activeScene:
          print(self.text)
          jsonIncrement += 1
      self.id = None

    def getJSON(self, menu, tarid):
        with open("scenes.json", "r") as file:
          data = json.load(file)
          self.text = data["menu"] # this string is reference to what file in json
          print(data)
          sleep(5)
          return id # TODO: not full done

class inputSystem:
    def _init_(self):
      self.options = [] # Used for storing options
      self.variable = None # Used for checking previous options
      self.userInput = None # used for comparing user data
  
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
           if self.userInput in choice.advancedType():
              scenes.getDialogue("continue, and unpause getDialogue")
    def advancedType(self):
       print("TODO: NEED TO MAKE IT ALLOW FOR COMPARING EXISTENCE OF SEPERATE WORD THAT EXIST IN THE STRING 'jim went to the store' and user input 'jim store' so i need to write logic where this is true as its false because of python logic")

class Player:
  def __init__(self):
     self.inventory = []
     self.element = None
     self.money = 1
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
  scenes.getDialogue("menu")
  gameend()
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
    sys.exit(0)

if __name__ == "__main__":
  while gameState:
    print(" \n Welcome to the Adventure Game!")
    player = Player()
    scenes = dialogueManager()
    choice = inputSystem()
    Main_Menu()