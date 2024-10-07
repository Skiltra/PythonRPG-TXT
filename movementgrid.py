
# import random

gridx = 0
gridy = 0

playerx = gridx
playery = gridy

def intro():
    action = input
    if action == "no":
        endgame()

def endgame():
    print("end")