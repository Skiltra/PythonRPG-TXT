import sys
import multiprocessing  # For running multiple loops later
from Game.events import DialogueManager as dialogue
from Game.player import Player
from pathlib import Path
import json

initialize = True
sceneLoader = "backroom"


class Game: # TODO: figure out location in player.py
    state = False

    def __init__(self, sceneStart, npc, locations):
        self.data = {}
        self.scenes = sceneStart
        self.npc = npc
        self.locations = locations

    def loadData(self, **args):
        json = args.get("json")
        if json:
            with open(json, "r", encoding='utf-8') as f:
                self.data = f.read()
                print("loaded data")

    def getJSON(self, menu, tarid):
        self.scenes = menu
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
                  self.scenes = self.id[2]
              else:
                 print("all json conditions failed")

####################################################################
class InputSystem: # TODO: consider combining into menu system
    FILE_DIR = Path(__file__) # TODO: path location

    def _init_(self):
      self.options = [] # storing user options
      self.variable = None # checking chosen option
      self.userInput = None # comparing user data
      self.jason = {} # relating to save somehow


class MenuSystem:
    def __init__(self):
        self.menu = {}

    def mainMenu(self):
       print("ext game etc, future for difficulty")
    def startGame(self):
        scenes.getDialogue("logo")
        scenes.getDialogue("menu")

    def saveGame(self):
        with open("save.json", "w") as f:
            json.dump(self.jason, f)

    def endGame(self):
        gameState = False

############################ Loop and Exit Functions ############################
if __name__ == "__main__":
  while Game.state:
    if initialize:
      scenes = dialogue(sceneLoader)
      menu = MenuSystem()
      playing = Player()
      # econ = market()
      print("Initialized Game States")
      initialize = False
    elif playing:
        menu.startGame()
    else:
        print("main while loop failed")