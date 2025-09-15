from time import sleep
import json
import tkinter as tk

gameState = True
enablin = True
sceneLoader = "backroom"
counter = 0

class dialogueManager:
    def __init__(self):
      self.scene = sceneLoader
      self.id = ["active",0,1]
      self.text = []
      self.action = None

    def getDialogue(self,jsonheading=sceneLoader, jsonIncrement=0): #TODO: do something with increment or ELSE
      print(f"{self.scene}")
      if self.id[1] < self.id[2]: # WORKS AS INTENDED
          self.scene = self.getJSON(jsonheading, self.id[1])
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
        print(f"dataDEBUG: C{counter}, ID{self.id}, ACT{self.action}")
        with open("scenes.json", "r", encoding='utf-8') as file:
          data = json.load(file) 
          self.text = data[menu]
          for content in self.text:
              self.action = content.get("conditions")
              counter +=1
              if tarid == self.id:
                  return content["text"]
              if isinstance(self.id[2], str):
                  global sceneLoader
                  print(">Switching JSON Array")
                  self.id[2] = 0
                  self.scene = self.id[2]
    def callExec(self):
       print("TODO: use player class when re-added to get functions")
       self.action = None

class inputSystem:
    def _init_(self):
      self.options = [] # storing user options
      self.variable = None # checking chosen option
      self.userInput = None # comparing user data

    def inputHandler(self, option, list=None):
        tk.entry(self.userInput)
        if option == "choices":
           print("find way to have choice")
        if option == "determine":
           print("using conditions, also passes to getDialogue class variables")

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
def Game_Exit ():
  with open("save.txt", "w") as file:
      print("TODO: need save instances for sceneLoader and future player class")
  choice = input('Press Q to Quit')
  if choice == 'q':
    gameState = False

if __name__ == "__main__":
  while gameState:
    if enablin:
      print("Initialized Game States")
      scenes = dialogueManager()
      inputs = inputSystem()
      enablin = False
    Main_Menu()
    if scenes.scene == None:
       sceneLoader = scenes.scene
    scenes.getDialogue()