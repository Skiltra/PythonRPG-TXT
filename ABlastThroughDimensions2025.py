import os
import sys
from Scripts.events import dialogueManager as dialogue
from Scripts.player import Player
from pathlib import Path
import json

gameState = True
intialize = True
sceneLoader = "backroom"


class GameState: # TODO: figure out location in player.py
    def __init__(self, scenes, npc, locations):
        self.data = {}
        self.scenes = scenes
        self.npc = npc
        self.locations = locations

    def loadData(self, **args):
        json = args.get("json")
        if json:
            with open(json, "r", encoding='utf-8') as f:
                self.data = f.read()
                print("loaded data")

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

####################################################################
class inputSystem: # TODO: consider combining into menu system
    FILE_DIR = Path(__file__) # TODO: path location  

    def _init_(self):
      self.options = [] # storing user options
      self.variable = None # checking chosen option
      self.userInput = None # comparing user data
      self.jason = {} # relating to save somehow


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

    def saveGame(self):
        with open("save.json", "w") as f:
            json.dump(self.jason, f)

    def endGame():
        gameState = False

############################ Loop and Exit Functions ############################
if __name__ == "__main__":
  while gameState:
    if enablin:
      scenes = dialogue(sceneLoader)
      menu = menuSystem()
      playing = Player()
      # econ = market()
      print("Initialized Game States")
      enablin = False
    elif playing:
      menu.startGame()
    else: 
       print("main while loop failed")