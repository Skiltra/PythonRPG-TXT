import os
import sys
# TODO: figure out imports of files

gameState = True
enablin = True
sceneLoader = "backroom"

class inputSystem:
    def _init_(self):
      self.options = [] # storing user options
      self.variable = None # checking chosen option
      self.userInput = None # comparing user data


class menuSystem:
    def __init__(self):
        self.menu = {}

    def mainMenu(self):
       print("ext game etc, future for difficulty")
    def startGame(self):
        print("""\n
    _      ____  _           _     _____ _                           _     
   / \    | __ )| | __ _ ___| |_  |_   _| |__  _ __ ___  _   _  __ _| |__  
  / _ \   |  _ \| |/ _` / __| __|   | | | '_ \| '__/ _ \| | | |/ _` | '_ \ 
 / ___ \  | |_) | | (_| \__ \ |_    | | | | | | | | (_) | |_| | (_| | | | |
/_/__ \_\ |____/|_|\__,_|___/\__| _ |_| |_| |_|_|  \___/ \__,_|\__, |_| |_|
|  _ \(_)_ __ ___   ___ _ __  ___(_) ___  _ __  ___            |___/       
| | | | | '_ ` _ \ / _ \ '_ \/ __| |/ _ \| '_ \/ __|                       
| |_| | | | | | | |  __/ | | \__ \ | (_) | | | \__ \                       
|____/|_|_| |_| |_|\___|_| |_|___/_|\___/|_| |_|___/                       \n
        """)
        # scenes.getDialogue("menu")
    def endGame():
        gameState = False

############################ Loop and Exit Functions ############################
if __name__ == "__main__":
  while gameState:
    if enablin:
      # scenes = dialogueManager()
      inputs = inputSystem()
      menu = menuSystem()
      print("Initialized Game States")
      enablin = False
    menu.startGame()