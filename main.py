import random

inventory = []
element = []
health = 100

def Game_Start ():
  Choices = ["Yes", "No"]
  print("You awake at the Hospital after a near death fatality. Whilst you sit up and relax the watch has cured. The big scars and broken bones in your body were feeling repaied. You felt full of life. Looking closely at the watch you notice a button on it. As you press it, you nptice you are travelling through a different dimesion.")
  userInput = ""
  while userInput not in Choices:
    print("As you turn around, you see a Waylayman. He asks you are you a merchant?.")
    userInput = input()
    if userInput == "Yes":
      print("""Maybe I can interest you in some of my goods. It seems somehting is troubling you can I help you.\n Can you please help me with directions?\nTo the West there is a village, to your North there is a forest and to the East is a bandit camp.""")
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
    print("Please eneter if you wish to go West 2 to the Village, North 2 East 1 to the forest or East 2 to the bandit camp")
    userInput = input()
    if userInput == "West 2":
      print("This is the village.")
      Part_1_The_Village ()
    elif userInput == "North 2 East 1":
      print("This is the forest.")
      Part_1_The_Forest ()
    elif userInput == "East 2":
      print("This is the Bandit Camp.")
      Part_1_The_Bandit_Camp ()
    else:
      print("Please enter a valid option for the adventure game.")   
      
def Part_1_The_Village ():
  directions = ["Elders Hut", "Manor"]
  print("You arrive at the village and you are greeted by an farmer. The farmer tells you about the Elders Hut and the manor")
  userInput = ""
  while userInput not in directions:
    print("Do you wish to go the Elders Hut or the manor")
    userInput = input()
    if userInput == "Elders Hut":
      print("This is the Elders Hut.")
      Part_1_The_Elders_Hut ()
    elif userInput == "Manor":
      print("This is the Manor.")
      Part_1_The_Manor ()
    else:
      print("Please enter a valid option for the adventure game.")
      
def Part_1_The_Elders_Hut ():
  print("You arrive at the Elders hut, you decice to help the farmers to fight the Lords Army\n As you fight off the army, you are stopped by the peasants rebellion. You decide to take camp at the mountains\nAs you get to the mountains you stop near Obsidan Camp, unaware of a dragon nearby")
  Part_1_Dragon_Attack ()
      
def Part_1_The_Manor ():
  print("You decide to go to the manor, and help the lord along with the lords’ soldier to make the people pay the taxes.\n They fight back and the peasant are held back to a mountain.\nOut of the obsidan mine comes an Dragon..")
  Part_1_Dragon_Attack ()

# Testing Inventory
def Part_1_The_Forest ():
  directions = ["Flower", "Herb"]
  print("You arrive at the forest, as you do you see a Witch.\nThe witch tells you to collec a special herb for her. She tells you to the mountains to find one")
  userInput = ""
  while userInput not in directions:
    print("At the mountain you see a Flower and a Hern, which do you want to go for.\nAfter picjing it up you head back to check with the witch.\nThe witch chesks to see what you have got.")
    userInput = input()
    if userInput == "Flower":
      print("This is not the correct flower. However if you go to the Obsidan near the mountain then this will be disregarded.")
      Part_1_Dragon_Attack ()
    elif userInput == "Herb":
      print("This is the one, as a reward I shall give you this antidote to cure poison. \nAs you plan to leave, the Dragon appears.")
      global inventory
      inventory.append("antidote")
      Part_1_Dragon_Attack ()
    else:
      print("Please enter a valid option for the adventure game.")
      
def Part_1_The_Bandit_Camp ():
  Directions = ["Work with Bandits", "Attack Bandits", "Spy on Bandits"]
  userInput = ""
  while userInput not in Directions:
    print("You are at the Bandit camp, please type if you want to Work with Bandits or Attack Bandits or Spy on Bandits")
    userInput = input()
    if userInput == "Work with Bandits":
      print("You are to spy on the goblins.\nAs you listen to the goblins convseartion they ttalk about dragons weakness to fire from water.\nA mighty dragon appears.")
      Part_1_Dragon_Attack ()
    elif userInput == "Attack Bandits":
      print("You decide to fight the bandits and are wounded. After being taken prisoner they try to use upoi as bait the defeat the dragon.\nThe dragon kills them off and you run.")
      Part_1_Dragon_Attack ()
    elif userInput == "Spy on Bandits":
      print("You decide to spy on the bandits, and sneak into there camp they talk about goblins over the river and about obsidian mine\nAs you explore you run into a dragon")
      Part_1_Dragon_Attack ()
    else:
      print("Please enter a valid option for the adventure game.")
      
def Part_1_Dragon_Attack ():
    Directions = ["Worked with Bandits", "Attacked Bandits", "Spied on Bandits and Travelled to Goblin Camp.", "Spied on Bandits and Travelled to Obsidan Mine"]
    userInput = ""
    while userInput not in Directions:
        print("You see a Drgaon waiting to attack you, Please type whether you Worked with Bandits or Attacked Bandits or Spied on Bandits and went to Obsidan Mine or Travel to Goblin Camp")
        userInput = input()
        if userInput == "Worked with Bandits":
            print("The dragon closes in on attack.\nwith the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            Part_2_Chasing_Asilant ()
        elif userInput == "Attacked Bandits":
            print("The dragon swoops in low to attack you\nYou are hurt by oncoming dragon attack. You try to chase down the dragon.")
            Part_2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Goblin Camp":
            print("You spied on the bandits and visited the goblin camp to find out to use water on the dragon.\n with the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            Part_2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Obsidan Mine":
            print("You spied on the bandits and went straight to Obsidan Mine\n when dragon attacks you manage to scrape the dragon to make it bleed. The Dragon escapes.")
            Part_2_Chasing_Asilant ()
        else:
            print("Please enter a valid option for the adventure game.")

# Part 2

def Part_2_Chasing_Asilant ():
  print("""The player changes into a new time periodas the watch was glowing now and it opened a new path for him towards an office.\nAs you eneter the office there is a note that talks about a ritual to beat the dragon\nBefore you can move any further a Man appears who then teleports away when you see him.\nYou chase him using your path from the watch. When you speak to him he seems to want to undo all the actions you have done\nThe enemey assilant tells him to stop, you do not know what you are dealing wiyj. Then he shifts away into another dimension""")
  Part_2_Shipyard ()
  
def Part_2_Shipyard ():
    Directions = ["North", "South"]
    userInput = ""
    while userInput not in Directions:
        print("As you attenpt to follow him using your watch you see you are now at an shipyard. You can either go North or South")
        userInput = input()
        if userInput == "North":
            print("The dragon closes in on attack.\nwith the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            Part_2_Chasing_Asilant ()
        elif userInput == "Attacked Bandits":
            print("The dragon swoops in low to attack you\nYou are hurt by oncoming dragon attack. You try to chase down the dragon.")
            Part_2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Goblin Camp":
            print("You spied on the bandits and visited the gobline camp to finf out to use water on the dragon.\nwith the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            Part_2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Obsidan Mine":
            print("You spied on the bandits and went straight to Obsidan Mine\nwhen dragon attacks you manage to scrape the dragon to make it bleed. The Dragon escapes.")
            Part_2_Chasing_Asilant ()
        else:
            print("Please enter a valid option for the adventure game.")

# Later Segment
def locatingWatchObjects():
    Directions = ["West", "East"]
    userInput = ""
    global invenory
    print("with this the player senses several location of the item needed to unlock the door, East is a path leading to a cliffside, and west towards a bridge following a road")
    while userInput not in Directions:
      if userInput == "West":
        print("As you are travelling west you cross a bridge, the bridge suddenly collapses you flow with the current down the river\n You arrive on a shore which curves into another tributuary river\n You sense an Item is nearby with the watches ability\nthe player travels and finds a hollow bit of sand and digs up and finds a lockpick, it is the item being senses")
        inventory.append("lockpick")
      elif userInput == "East":
        print("coming close to cliff a cave is seen, you enter the cave\n You see a glowing sword, you pick up the sword which is one of the items sense by the watch")
        inventory.append("sword")
      else:
        keyfound()

def keyfound():
    Directions = ["West", "East"]
    userInput = ""
    global invenory
    while userInput not in Directions:
      print("You continue from where you are at and continue towards another location it has a different sense and is close\n You come across a key, 'this must be it' you exclaim in excitement")
      inventory.append("key")
      if element == "fire":
        mysteryfire()
      else:
        mysteryconfront()

# Unlocking of the Door.  Needs testing that the and statement does not need index to mention, also idea of replacing sword with damaged sword for later outcomes of dragon fight
def mysteryconfront():
    Directions = ["West", "East"]
    userInput = ""
    global element, inventory
    print("You come across the door, you have the key, you Use key the key both ways and finally unlock it\n you back away from the door as it opens you hear its mechanism inside the rock moving.\n you see the man who quickly jumps in front of you blocking the way to the content of inside.")
    while userInput not in Directions:
      if userInput == "attack" and inventory == "sword":
        print("you defeat him")
        mysterywin()
      elif element == "fire":
        print("you use the combined power of the watch and encapsule him")
      elif inventory == "lockpick":
        print("you barter your lockpick for the item he took from the hidden door that you tried solving before he interupted you")
        inventory.append("glowing berries")
        inventory.remove("lockpick")
        persuademystery()
      else:
        mysteryfail()

def mysterywin():
    print("you feel much more stronger now, perhaps its the watch doing it")
    while inventory not == "strong":
      inventory.append("strong")

## check this code
def mysteryfail():
    Directions = ["West", "East"]
    userInput = ""
    global inventory, health
    while userInput not in Directions:
      if inventory == "antidote":
        inventory.remove("antidote")
      else:
        inventory.append("poisened")
        health -= 20 # change if not impactful enough

def mysteryfire():
    Directions = ["West", "East"]
    userInput = ""
    print(f"you defeat your opponent wiht the elemental knowledge of {element} and from that you encapsule him in a fire cacoon and defeat him, he turns to ashes and his belonging burn with him")

def persuademystery():
    Directions = ["West", "East"]
    userInput = ""
    while userInput not in Directions:

# Main Program dont edit: make all code above
if __name__ == "__main__":
  while True:
    print("Welcome to the Adventure Game!\nAs an avid traveler, you have decided to visit the Catacombs of Paris.\nHowever, during your exploration, you find yourself lost.\nYou can choose to walk in multiple directions to find a way out.\nLet's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    Game_Start()
