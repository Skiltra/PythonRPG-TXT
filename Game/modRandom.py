import random

class RollSystem:
    def __init__(self, max=100):
        self.chance = 0.5
        self.flags = 0 # determine long term behavior even for successful actions or repetitious behavior
        self.maxFlags = max # if higher set to 100

    def outcome(self):
       number = random.random()
       if self.chance < number:
          return True
       else:
          return False

    def changeAction(self):
       print(f"{self.flags}")

    @staticmethod
    def basic():
       return random.random()