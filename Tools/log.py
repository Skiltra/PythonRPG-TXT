import logging
import os

# TODO: implement some logging system write file and error handling


class Scoreboard:
        """Replacing the original in main.py score with a class"""
        def __init__(self):
            self.score = 0

        def getScore(self):
                  if os.path.exists("data/scorelog.txt"):
                    type = "a"
                  else:
                    type = "w"
                  with open("data/scorelog.txt", type) as file:
                    file.write(str(self.score))


class Logger:
    """a way to log things about the game for debug/runtime reasons; logging persistence"""
    def __init__(self):
            self.text = {}