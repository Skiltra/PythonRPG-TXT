# import sys # For sys stuff when better loop exists
# import multiprocessing  # For running multiple loops later
# from pathlib import Path
from Game.mgrEvents import DialogueManager
from Game.mgrActors import Player
import json # loading ./data files

initialize = True
sceneLoader = "backroom"


class Game: # TODO: figure out location in mgrActors.py
    state = False

    def __init__(self, sceneStart, npc, locations):
        self.data = {"scenes": {}, "text": None} # TODO: ALL GAME DATA REPLACING getJSON
        self.scenes = sceneStart
        self.npc = npc
        self.locations = locations
        Game.state = True

    def loadData(self, **args):
        self.data["scenes"] = args.get(sceneLoader)
        if json:
            with open(json, "r", encoding='utf-8') as f:
                self.data = f.read()
                print("loaded data")

####################################################################
class MenuSystem:
    def __init__(self):
        self.menu = {"options","correct", "usersInput"} # TODO: Test to replace input system
        self.inputs = {}
    def getQuiz(self):
            print(f"using {self.menu} implement a quiz with input in menu system")

    @staticmethod
    def saveGame():
        with open("save.json", "w") as f:
            json.dump(game.data, f)

    @staticmethod
    def mainMenu(self):
       print(self, f"ext game etc, future for difficulty")

    @staticmethod
    def startGame():
        scenes.getDialogue("logo")
        scenes.getDialogue("menu")

    @staticmethod
    def endGame():
        Game.state = False # BUG: test from game state class

############################ Loop and Exit Functions ############################
if __name__ == "__main__":
  game = Game()
  while Game.state:
    if initialize:
      scenes = DialogueManager(sceneLoader)
      menu = MenuSystem()
      playing = Player()
      # econ = market()
      print("Initialized Game States")
      initialize = False
    else:
        print("main while loop failed")