from time import sleep
import json
import tkinter as tk

gameState = True
enablin = True
sceneLoader = "ship"
counter = 0 # BUG: debug only; using to check for loop consistency

class dialogueManager:
    def __init__(self):
      self.activeScene = None
      self.id = 0
      self.nextID = 1
      self.text = []
      self.action = None

    def getDialogue(self,jsonheading, jsonIncrement=0):
      self.text = self.getJSON(jsonheading, self.id)
      if self.nextID > self.id:
          self.text = self.getJSON(self.activeScene, self.nextID)
          print(f">Assigning New Text from {self.nextID}")
      # if self.action: # TODO: Uncommemt
      #     inputs.callExec()
      else:
          print("Sequence Check Failed; either all false or first run")
          self.text = self.getJSON(self.activeScene, self.nextID)
      while self.activeScene:
          if self.text != None and type(self.nextID) is int:
            print(f"{self.text} DATA TESTING: C{counter}, ID{self.id}, NID{self.nextID}")
            sleep(5)
          elif type(self.nextID) is str:
            self.activeScene = self.nextID
            self.text = self.getJSON(self.activeScene, self.nextID)        

    def getJSON(self, menu, tarid):
        self.activeScene = menu
        global counter
        with open("scenes.json", "r", encoding='utf-8') as file:
          data = json.load(file) 
          self.text = data[menu] 
          for content in self.text:
              self.nextID = content.get("id")
              counter +=1
              if tarid == content["id"]: # BUG:  ids not changing need fix see DATA TESTING when run
                  return content["text"]
              if isinstance(self.nextID, str):
                  print(">Switching JSON Array")
                  self.nextID = 0
                  self.activeScene = self.nextID
    def callExec(self):
       print("TODO: use player class when re-added to get functions")
       self.action = None

class inputSystem:
    def _init_(self):
      self.options = [] # Used for storing options
      self.variable = None # Used for checking previous options
      self.userInput = None # used for comparing user data

    def inputHandler(self, option, list=None):
        tk.entry()
        print("pause getDialogue through activeScene")
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
    if scenes.activeScene != None:
       sceneLoader = scenes.activeScene
    scenes.getDialogue(sceneLoader)