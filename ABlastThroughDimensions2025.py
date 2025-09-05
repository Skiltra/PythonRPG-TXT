from time import sleep
import json

gameState = True
enablin = True
sceneLoader = "ship"

class dialogueManager:
    def __init__(self):
      self.activeScene = None
      self.id = None
      self.nextID = 1
      self.text = []
      self.action = None

    def getDialogue(self,jsonheading, jsonIncrement=0):
      if self.id != None:
          self.id = jsonIncrement 
      self.text = self.getJSON(jsonheading, self.id)
      if self.action:
          inputs.callExec()
      elif type(self.nextID) is str: 
          self.activeScene = self.nextID
          self.text = self.getJSON(self.activeScene, self.nextID)
      else:
          print("Sequence Check Failed; either all false or first run")
      while self.activeScene:
          if self.text != None and type(self.nextID) is int:
            print(f"{self.text}")
            sleep(5)
          if self.nextID > self.id:
            self.text = self.getJSON(self.activeScene, self.nextID)
            print(f">Assigning New Text from {self.nextID}")
          else:
             print(f"DEBUG FALLBACK; text{self.text} id {self.id} nextID {self.nextID}")
             self.getJSON(self.activeScene, self.nextID)

    def getJSON(self, menu, tarid):
        print(f">ID Set at {self.id} nextIs {self.nextID}, activeScene: {self.activeScene}")
        with open("scenes.json", "r", encoding='utf-8') as file:
          data = json.load(file) 
          self.text = data[menu] 
          for content in self.text:
              self.nextID = content.get("nextID")
              # if content == data["conditions"]:
              #     self.action = content.get("conditions")
              if tarid == content["id"]:
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
        if option == "typing":
           print("")

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
      print(" \n Initialized Game States")
      scenes = dialogueManager()
      inputs = inputSystem()
      enablin = False
    Main_Menu()
    if scenes.activeScene != None:
       sceneLoader = scenes.activeScene
    scenes.getDialogue(sceneLoader)