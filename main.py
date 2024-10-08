import random

inventory = []
element = []
score = 0
health = 100

# Program First Called Function
def Game_Start ():
  Choices = ["Yes", "No"]
  print("You awake at the Hospital after a near death fatality. Whilst you sit up and relax the watch has cured. The big scars and broken bones in your body were feeling repaired. You felt full of life. Looking closely at the watch you notice a button on it. As you press it, you nptice you are travelling through a different dimesion.")
  userInput = ""
  while userInput not in Choices:
    print("As you turn around, you see a Waylayman. He asks you are you a merchant?.")
    userInput = input()
    if userInput == "Yes":
      print("Maybe I can interest you in some of my goods. It seems somehting is troubling you can I help you.\n Can you please help me with directions?\nTo the West there is a village, to your North there is a forest and to the East is a bandit camp.")
      Game_Start_Directions ()
    elif userInput == "No":
      print("I see no problem.\n Can you please help me with directions\nTo the West there is a village, to your North there is a forest and to the East is a bandit camp")
      Game_Start_Directions ()
    else:
      print("Please enter Yes or No.")   

# Medieval Setting
def Game_Start_Directions ():
  Directions = ["West 2", "North 2 East 1", "East 2"]
  userInput = ""
  while userInput not in Directions:
    print("Please eneter if you wish to go \n - West 2 to the Village, \n - North 2 East 1 to the forest or \n - East 2 to the bandit camp")
    userInput = input()
    if userInput == "West 2":
      print("This is the village.")
      P1_The_Village ()
    elif userInput == "North 2 East 1":
      print("This is the forest.")
      P1_The_Forest ()
    elif userInput == "East 2":
      print("This is the Bandit Camp.")
      P1_The_Bandit_Camp ()
    else:
      print("Please enter a valid option for the adventure game.")   

# Part 1 - Three Paths
def P1_The_Village ():
  directions = ["Elders Hut", "Manor"]
  print("You arrive at the village and you are greeted by an farmer. The farmer tells you about the Elders Hut and the manor")
  userInput = ""
  while userInput not in directions:
    print("Do you wish to go the Elders Hut or the manor")
    userInput = input()
    if userInput == "Elders Hut":
      print("This is the Elders Hut.")
      P1_The_Elders_Hut ()
    elif userInput == "Manor":
      print("This is the Manor.")
      P1_The_Manor ()
    else:
      print("Please enter a valid option for the adventure game.")

def P1_The_Elders_Hut ():
  print("You arrive at the Elders hut, you decice to help the farmers to fight the Lords Army\n As you fight off the army, you are stopped by the peasants rebellion. You decide to take camp at the mountains\nAs you get to the mountains you stop near Obsidan Camp, unaware of a dragon nearby")
  P1_Dragon_Attack ()

def P1_The_Manor ():
  print("You decide to go to the manor, and help the Lord along with the lord's soldier to make the people pay the taxes.\n They fight back and the peasant are held back to a mountain.\nOut of the obsidan mine comes an Dragon..")
  P1_Dragon_Attack ()

def P1_The_Forest ():
  directions = ["Flower", "Herb"]
  print("You arrive at the forest, as you do you see a Witch.\nThe witch tells you to collect a special herb for her. She tells you to the mountains to find one")
  userInput = ""
  while userInput not in directions:
    print("At the mountain you see a Flower and a Herb, which do you want to go for.\nAfter picking it up you head back to check with the witch.\nThe witch chesks to see what you have got.")
    userInput = input()
    if userInput == "Flower":
      print("This is not the correct flower. However if you go to the Obsidan near the mountain then this will be disregarded.")
      P1_Dragon_Attack ()
    elif userInput == "Herb":
      print("This is the one, as a reward I shall give you this antidote to cure poison. \nAs you plan to leave, the Dragon appears.")
      global inventory
      inventory.append("antidote")
      P1_Dragon_Attack ()
    else:
      print("Please enter a valid option for the adventure game.")

def P1_The_Bandit_Camp ():
  Directions = ["Work with Bandits", "Attack Bandits", "Spy on Bandits"]
  userInput = ""
  while userInput not in Directions:
    print("You are at the Bandit camp, please type if you want to Work with Bandits or Attack Bandits or Spy on Bandits")
    userInput = input()
    if userInput == "Work with Bandits":
      print("You are to spy on the goblins.\nAs you listen to the goblins convseartion they talk about dragons weakness to fire from water.\nA mighty dragon appears.")
      P1_Dragon_Attack ()
    elif userInput == "Attack Bandits":
      print("You decide to fight the bandits and are wounded. After being taken prisoner they try to use upon as bait the defeat the dragon.\nThe dragon kills them off and you run.")
      P1_Dragon_Attack ()
    elif userInput == "Spy on Bandits":
      print("You decide to spy on the bandits, and sneak into there camp they talk about goblins over the river and about obsidian mine\nAs you explore you run into a dragon")
      P1_Dragon_Attack ()
    else:
      print("Please enter a valid option for the adventure game.")

def P1_Dragon_Attack ():
    Directions = ["Worked with Bandits", "Attacked Bandits", "Spied on Bandits and Travelled to Goblin Camp.", "Spied on Bandits and Travelled to Obsidan Mine"]
    userInput = ""
    while userInput not in Directions:
        print("You see a Drgaon waiting to attack you, Please type whether you Worked with Bandits or Attacked Bandits or Spied on Bandits and went to Obsidan Mine or Travel to Goblin Camp")
        userInput = input()
        if userInput == "Worked with Bandits":
            print("The dragon closes in on attack.\nwith the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            P2_Chasing_Asilant ()
        elif userInput == "Attacked Bandits":
            print("The dragon swoops in low to attack you\nYou are hurt by oncoming dragon attack. You try to chase down the dragon.")
            P2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Goblin Camp":
            print("You spied on the bandits and visited the goblin camp to find out to use water on the dragon.\n with the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            P2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Obsidan Mine":
            print("You spied on the bandits and went straight to Obsidan Mine\n when dragon attacks you manage to scrape the dragon to make it bleed. The Dragon escapes.")
            P2_Chasing_Asilant ()
        else:
            print("Please enter a valid option for the adventure game.")

# Part 2
def P2_Chasing_Asilant ():
  print("""The player changes into a new time periodas the watch was glowing now and it opened a new path for him towards an office.\nAs you eneter the office there is a note that talks about a ritual to beat the dragon\nBefore you can move any further a Man appears who then teleports away when you see him.\nYou chase him using your path from the watch. When you speak to him he seems to want to undo all the actions you have done\nThe enemey assilant tells him to stop, you do not know what you are dealing wiyj. Then he shifts away into another dimension""")
  P2_Shipyard ()
  
def P2_Shipyard (): #Issue: this entire code loops on itself, also naming of the function doesnt align with story flow chart
    Directions = ["North", "South"]
    userInput = ""
    while userInput not in Directions:
        print("As you attenpt to follow him using your watch you see you are now at an shipyard. You can either go North or South")
        userInput = input()
        if userInput == "North":
            print("The dragon closes in on attack.\nwith the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            P2_Chasing_Asilant ()
        elif userInput == "Attacked Bandits":
            print("The dragon swoops in low to attack you\nYou are hurt by oncoming dragon attack. You try to chase down the dragon.")
            P2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Goblin Camp":
            print("You spied on the bandits and visited the gobline camp to finf out to use water on the dragon.\nwith the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            P2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Obsidan Mine":
            print("You spied on the bandits and went straight to Obsidan Mine\nwhen dragon attacks you manage to scrape the dragon to make it bleed. The Dragon escapes.")
            P2_Chasing_Asilant ()
        else:
            print("Please enter a valid option for the adventure game.")
# Shafire Code Link to Before

# William Code Link to Shafire code
def P2_suprisemysteryman ():
    directions = ["Ambushed by Mysterious Figure", "Attack Mysterious Figure"]
    userinput = ""
    global health
    while userinput not in directions:
        print["What would you like to do?"]
        userinput = input()
        if userinput == "Ambushed by Mysterious Figure": #wont work due to it not being a choice, will need a condition before and a simple "defend from ambush" and "attack mystery man"
          print("He quickly flees scene clearly not wanting to engage in battle\nYou find a path leading to the clearing in the forest some puzzle to unlock a door")
          health -= 10
          Puzzle()
        elif userinput == "Attack Mysterious Figure":
          print("You follow a blood trail of a stone alligned in the forest patch and puzzle")
          Puzzle()

def Puzzle ():
  outcomes = ["Wind", "Earth", "Water", "Fire"]
  print("It asks you to align the stone based on what elements oppose, based on the following statements\nA series of 3 phrases for each stone mural, a description of element, its opposed element and it's paired element")
  userinput = ""
  global health
  while userinput not in outcomes:
    print("Earth is strong against water, but is weak against?")
    Earthinput = input()
    print("Water is strong against Fire, but is weak against?")
    Waterinput = input()
    print("Fire is strong against wind, but is weak against?")
    Fireinput = input()
    print("Wind is strong against Earth, but is weak against?")
    Windinput = input()
    if Earthinput != "Wind" or Waterinput != "Earth" or Fireinput != "Water" or Windinput !="Fire":
      print("You fail and a result you die after being attacked by all elements")
      health -= 150
      gameend()
    elif Earthinput == "Wind" and Waterinput == "Earth" and Fireinput == "Water" and Windinput =="Fire":
      print("Player succeeds rock moves and the player discovers a locked door but the player has additional abilities since completing the puzzle")
      print("Watch Upgrades")
      print("With this the player senses several locations to head to")
      directions_List ()
    else:
      print("Please enter a valid option for the adventure game.")  

# P2 Loacting objects and Mystery Man
def P2_locatingWatchObjects():
    Directions = ["West", "East"]
    userInput = ""
    global inventory
    print("with this the player senses several location of the item needed to unlock the door, East is a path leading to a cliffside, and west towards a bridge following a road")
    while userInput not in Directions:
      if userInput == "West":
        print("As you are travelling west you cross a bridge, the bridge suddenly collapses you flow with the current down the river\n You arrive on a shore which curves into another tributuary river\n You sense an Item is nearby with the watches ability\nthe player travels and finds a hollow bit of sand and digs up and finds a lockpick, it is the item being senses")
        inventory.append("lockpick")
      elif userInput == "East":
        print("coming close to cliff a cave is seen, you enter the cave\n You see a glowing sword, you pick up the sword which is one of the items sense by the watch")
        inventory.append("sword")
      else:
        P2_keyfound()

def P2_keyfound():
    Directions = ["West", "East"]
    userInput = ""
    global invenory
    while userInput not in Directions:
      print("You continue from where you are at and continue towards another location it has a different sense and is close\n You come across a key, 'this must be it' you exclaim in excitement")
      inventory.append("key")
      if element == "fire":
        P3_mysteryfire()
      else:
        mysteryconfront()

# Unlocking of the Door.  Needs testing that the and statement does not need index to mention, also idea of replacing sword with damaged sword for later outcomes of dragon fight
def mysteryconfront():
    Directions = ["convince", "attack"]
    userInput = ""
    global element, inventory
    print("You come across the door, you have the key, you Use key the key both ways and finally unlock it\n you back away from the door as it opens you hear its mechanism inside the rock moving.\n you see the man who quickly jumps in front of you blocking the way to the content of inside.")
    while userInput not in Directions:
      if userInput == "attack" and inventory == "sword":
        print("you defeat him\nyou feel much more stronger now, perhaps its the watch doing it")
        inventory.append("strong")
        P3_dragonfound()
      elif userInput == "convince" and inventory == "lockpick":
        inventory.append("companion")
        print("Using the combined power of both indivudals with watches you track down the alien\nyou barter your lockpick for the item he took from the hidden door that you tried solving before he interupted you")
        inventory.append("glowing berries")
        inventory.remove("lockpick")
        P3_dragoncompanion()
      elif element == "fire":
        print("you use the combined power of the watch and encapsule him")
        P3_mysteryfire()
      else:
        P3_mysteryfail()

## check this code
def P3_mysteryfail(): # need direction into other function
    Directions = ["", ""]
    userInput = ""
    global inventory, health
    while userInput not in Directions:
      if inventory == "antidote":
        inventory.remove("antidote")
      else:
        inventory.append("poisened")
        health -= 20 # change if not impactful enough

def P3_mysteryfire():
    Directions = ["West", "East"]
    userInput = ""
    print(f"you defeat your opponent wiht the elemental knowledge of {element} and from that you encapsule him in a fire cacoon and defeat him, he turns to ashes and his belonging burn with him")

# P3 Alien and Dragon
def P3_dragonfound():
    Directions = ["flee", "attack"]
    userInput = ""
    global health, inventory
    while userInput not in Directions:
      if inventory == "glowing berries" and "poisened" not in inventory:
        health += 10 # missing exit function
      else:
        print("you try very hard to defeat the dragon, you barely make it out")
        health -= 40
        P3_barelydragon()

def P3_dragoncompanion():
    Directions = ["", ""]
    userInput = ""
    global health, inventory
    while userInput not in Directions:
      if inventory == "revolver":
        print("while fighting the dragon knowing how impossible it is to survive, your companion is about to get attacked\n You quickly throw the gun towards him\n he shoots the dragon and you win")
        P3_windragon()
      else:
        print("The dragon leaps to your companion and kills him, but you manage to stab the dragon in its belly when its vulnerable, hence you absorb the power of the dragon and compnaion\n you feel strange absorbing your companion power as in something is not right")
        inventory.append("corrupted")
        P3_barelydragon()

def P3_barelydragon():
    Directions = ["", ""]
    userInput = ""
    global health, inventory
    while userInput not in Directions:
      if health >= 60:
        print("you are ambushed it appear the aliens found you first, but you manages to surive")
        gameend()
      else:
        print("the alien ambush you but you are no match for them and you are shot by their blaster rifles")
        health -= 150
        gameend()

def P3_windragon():
  Directions = ["", ""]
  userInput = ""
  while userInput not in Directions:
    if health >= 40:
      print("finally you find where the aliens are you manage to setup an ambush, and with the elemnt of surpise you manage to take most out having to fight one by one what remains")
      gameend()
    else:
      gameend()

# Ending Screens: someone make functions rename if needed but connect to other events if not
def gameend():
  global score, health
  if health >= 1:
    print(f"you completed the game with a score of {score} and your remaining health was {health}")
  else:
    print(f"you lost the game with a score of {score}") 

# Main Program dont edit: make all code above
if __name__ == "__main__":
  while True:
    print("Welcome to the Adventure Game!\nAs an avid traveler, you have decided to visit the Catacombs of Paris.\nHowever, during your exploration, you find yourself lost.\nYou can choose to walk in multiple directions to find a way out.\nLet's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    Game_Start()