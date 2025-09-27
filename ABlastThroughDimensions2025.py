from time import sleep
import json
import sys
import sqlite3 as sql 

gameState = True
enablin = True
sceneLoader = "backroom"
counter = 0

class dialogueManager:
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
            print(f"{self.text} dataDEBUG: C{counter}, ID{self.id}, ACT{self.action}")
            sleep(5)
          if type(self.id[2]) is str:
            global sceneLoader
            self.scene = self.id[2]
            sceneLoader = self.getJSON(self.scene, self.id[2])      

    def getJSON(self, menu, tarid):
        self.scene = menu
        global counter
        print(f">getJSON DEBUG: C{counter}, ID{self.id}, ACT:{self.actionNotify}")
        with open("scenes.json", "r", encoding='utf-8') as file:
          data = json.load(file) 
          self.text = data[menu]
          for content in self.text:
              self.action = content.get("conditions")
              counter +=1
              if tarid == self.id:
                  return content["text"]
              elif isinstance(self.id[2], str):
                  global sceneLoader
                  print(">Switching JSON Array")
                  self.id[2] = 0
                  self.scene = self.id[2]
              else:
                 print("all json conditions failed")
    def loadDB(name):
       if name in enablin: # TRYING SOME THINGS THIS HAS NO DIRECT CONNECTION
          print("from json load into sql")
          print("generate new file name from existing")
       sql.connect(f"{name}.db")


class inputSystem:
    def _init_(self):
      self.options = [] # storing user options
      self.variable = None # checking chosen option
      self.userInput = None # comparing user data

    def inputHandler(self, option, list=None):
        if option == "choices":
           print("find way to have choice")
        if option == "determine":
           print("using conditions, also passes to getDialogue class variables")


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
        scenes.getDialogue("menu")
    def endGame():
        gameState = False

############################ Loop and Exit Functions ############################
if __name__ == "__main__":
  while gameState:
    if enablin:
      scenes = dialogueManager()
      inputs = inputSystem()
      menu = menuSystem()
      print("Initialized Game States")
      enablin = False
    menu.startGame()