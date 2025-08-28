
from random import randint
from os import system, name
from time import sleep
import os

inventory = []
element = []
health = 100
score = 0

# Kiren
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def Main_Menu ():
  global score
  if os.path.exists("scorelog.txt"):
    type = "a"
  else:
    type = "w"
  with open("scorelog.txt", type) as file:
    file.write(str(score))
  Choices = ["1", "2"]
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
  gameoptions = ""
  while gameoptions not in Choices:
    print(f" \n your previous score was {score}")
    print(" \n 1. new game. \n")
    print(" 2. exit. \n")
    gameoptions = input()
    if gameoptions == "1":
      sleep(2)
      clear()
      Character_Choice ()
    elif gameoptions == "2":
      sleep(2)
      clear()
      Game_Exit ()
    else:
      print(" \n Please enter a valid choice. \n")
      sleep(2)
      clear()
      Main_Menu ()
      
def Character_Choice ():
    Element = ["1", "2", "3", "4"]
    print(" \n Please type your name to get started. \n\n")
    name = input()
    print(" \n Good luck, " +name+ ". \n")
    Element_Type = ""
    while Element_Type not in Element:
        print(" \n Please enter your element; \n\n 1. earth \n 2. water \n 3. fire \n 4. wind \n")
        Element_Type = input()
        if Element_Type == "1":
            print("You are an Earth element")
            sleep(2)
            clear()
            Game_Start ()
        elif Element_Type == "2":
            print("You are an Water element")
            sleep(2)
            clear()
            Game_Start ()
        elif Element_Type == "3":
            print("You are an Fire element")
            sleep(2)
            clear()
            Game_Start ()
        elif Element_Type == "4":
            print("You are an Wind element")
            sleep(2)
            clear()
            Game_Start ()
        else:
            print("Please enter a valid choice.")
            Character_Choice()

def Game_Start ():
  Choices_List = ["1", "2"]
  print(" \n You awake at the Hospital after a near death fatality. Whilst you sit up and relax the watch has cured the big scars and broken bones in your body. \n You feel full of life. Looking closely at the watch you notice a button on it. \n As you press it, you notice you are travelling through a different dimension. \n")
  choices = ""
  while choices not in Choices_List:
    print(" \n As you turn around, you see a Waylayman. He asks youn are you a merchant? \n\n 1. yes \n 2. no. \n")
    choices = input()
    if choices == "1":
      print(" \n Maybe I can interest you in some of my goods. It seems something is troubling you, can I help you? \n Can you please help me with directions? \n To the West there is a village, to your North there is a forest and to the East is a bandit camp. \n")
      sleep(5)
      clear()
      Game_Start_Directions ()
    elif choices == "2":
      print(" \n I see no problem.\n Can you please help me with directions. \n To the West there is a village, to your North there is a forest and to the East is a bandit camp. \n")
      sleep(5)
      clear()
      Game_Start_Directions ()
    else:
      print(" \n Please enter, Yes or No. \n")   

# Medieval Setting

def Game_Start_Directions ():
  gamestartDirections = ["1", "2", "3"]
  part1locations = ""
  while part1locations not in gamestartDirections:
    print(" \n Please enter if you wish to go to: \n\n 1. village, \n 2. forest \n 3. bandit camp \n")
    part1locations = input()
    if part1locations == "1":
      print(" \n This is the village. \n")
      sleep(5)
      clear()
      Part_1_The_Village ()
    elif part1locations == "2":
      print(" \n This is the forest. \n")
      sleep(5)
      clear()
      Part_1_The_Forest ()
    elif part1locations == "3":
      print(" \n This is the Bandit Camp. \n")
      sleep(5)
      clear()
      Part_1_The_Bandit_Camp ()
    else:
      print(" \n Please enter a valid option for the adventure game. \n")   
      
def Part_1_The_Village ():
  part1villagelocations = ["1", "2"]
  print(" \n You arrive at the village and you are greeted by an farmer. The farmer tells you about the Elders Hut and the Manor \n")
  part1choices = ""
  while part1choices not in part1villagelocations:
    print(" \n Do you wish to go the: \n\n 1. elders hut \n 2. the Mmnor \n")
    part1choices = input()
    if part1choices == "1":
      print(" \n This is the Elders Hut. \n")
      sleep(5)
      clear()
      Part_1_The_Elders_Hut ()
    elif part1choices == "2":
      print(" \n This is the Manor. \n")
      sleep(5)
      clear()
      Part_1_The_Manor ()
    else:
      print(" \n Please enter a valid option for the adventure game. \n")
      
def Part_1_The_Elders_Hut ():
  print(" \n You arrive at the Elders hut, you decide to help the farmers to fight the Lords Army. \n As you fight off the army, you are stopped by the peasants rebellion. You decide to take camp at the mountains. \n As you get to the mountains you stop near Obsidan Camp, unaware of a dragon nearby. \n")
  sleep(5)
  clear()
  Part_1_Dragon_Attack ()
      
def Part_1_The_Manor ():
  print(" \n You decide to go to the manor, and help the lord along with the lords’ soldier to make the people pay the taxes. \n They fight back and the peasants hold you back to a mountain. \n Out of the obsidan mine comes an Dragon. \n")
  sleep(5)
  clear()
  Part_1_Dragon_Attack ()

# Testing Inventory
def Part_1_The_Forest ():
  flowertype = ["1", "2"]
  print(" \n You arrive at the forest, as you do you see a Witch.\n The witch tells you to collect a special herb for her. She tells you to the mountains to find one \n")
  mountainchoice = ""
  while mountainchoice not in flowertype:
    print(" \n At the mountain you pick up a: \n\n 1. flower \n 2. herb, \n which do you want to go for.\n After picking it up you head back to check with the witch.\n The witch checks to see what you have got. \n")
    mountainchoice = input()
    if mountainchoice == "1":
      print(" \n This is not the correct flower. However if you go to the Obsidan, near the mountain then this will be disregarded. \n")
      sleep(5)
      clear()
      Part_1_Dragon_Attack ()
    elif mountainchoice == "2":
      print(" \n This is the one, as a reward I shall give you this antidote to cure poisons. \n As you plan to leave, the Dragon appears. \n")
      global inventory
      inventory.append("antidote")
      sleep(5)
      clear()
      Part_1_Dragon_Attack ()
    else:
      print(" \n Please enter a valid option for the adventure game. \n")
      
def Part_1_The_Bandit_Camp ():
  playerbanditactions = ["1", "2", "3"]
  banditachoice = ""
  while banditachoice not in playerbanditactions:
    print(" \n You are at the bandit camp, please type if you want to: \n\n 1. work with bandits  \n 2. attack bandits \n 3. spy on bandits \n")
    banditachoice = input()
    if banditachoice == "1":
      print(" \n You are to spy on the goblins.\n As you listen to the goblins conversation, they talk about the dragons weakness to water. \n A mighty dragon appears. \n")
      sleep(5)
      clear()
      Part_1_Dragon_Attack ()
    elif banditachoice == "2":
      print(" \n You decide to fight the bandits and are wounded. After being taken prisoner, they then try to use you as bait to defeat the dragon. \n The dragon ills them off and you run. \n")
      sleep(5)
      clear()
      Part_1_Dragon_Attack ()
    elif banditachoice == "3":
      print(" \n You decide to spy on the bandits, and sneak into there camp. They talk about goblins over the river and about obsidian mine. \n As you explore you run into a dragon \n")
      sleep(5)
      clear()
      Part_1_Dragon_Attack ()
    else:
      print("\n Please enter a valid option for the adventure game. \n")
      
def Part_1_Dragon_Attack ():
    Dragonattackpath = ["1", "2", "3.", "4"]
    dragonaction = ""
    while dragonaction not in Dragonattackpath:
        print(" \n You see a Dragon waiting to attack you, Please type whether you: \n\n 1. worked with bandits \n 2. attacked bandits \n 3. spied on bandits and travelled to goblin camp \n 4. spied on bandits and travelled to obsidan mine \n")
        dragonaction = input()
        if dragonaction == "1":
            print(" \n The dragon closes in on attack.\n With the power of water you succeed in the dragon fight, as it evaporates it has to flee. \n")
            sleep(5)
            clear()
            Part_2_Chasing_Asilant ()
        elif dragonaction == "2":
            print(" \n The dragon swoops in low to attack you \n. You are hurt by the oncoming dragon attack. You try to chase down the dragon. \n")
            sleep(5)
            clear()
            Part_2_Chasing_Asilant ()
        elif dragonaction == "3":
            print(" \n You spied on the bandits and visited the goblin camp to find out how to use water on the dragon. \n with the power of water you succeed in the dragon fight, get for this beating the dragon. the dragon evaraporates and has to flee. \n")
            sleep(5)
            clear()
            Part_2_Chasing_Asilant ()
        elif dragonaction == "4":
            print(" \n You spied on the bandits and went straight to Obsidan Mine. \n when the dragon attacks you, you manage to scrape the dragon to make it bleed. The Dragon escapes. \n")
            sleep(5)
            clear()
            Part_2_Chasing_Asilant ()
        else:
            print("Please enter a valid option for the adventure game.")
            
def Part_2_Chasing_Asilant ():
    print(" \n The player changes into a new time period, as the watch was glowing now and it opened a new path for him towards an office.\n. As you enter the office, there is a note that talks about a ritual to beat the dragon. \n Before you can move any further, a man appears, who starts running away from you.\n. You chase him using your path from the watch. When you speak to him he seems to want to undo all the actions you have done. \n The enemey assilant tells you to stop, you do not know what you are dealing with, he says. Then he shifts away into another dimension \n")
    sleep(10)
    clear()
    part2b ()
  
# Shafia    
def part2b():
    answer_side = input(" \n As you attempt to follow him using your watch, you see you are now at a shipyard. You can either go North or South, \n which way do you want to go. \n\n 1. south 2. north \n\n").lower()
    if answer_side in ["south", "s", "1"]:
        print(" \n You head south \n\n")
        sleep(5)
        clear()
        south_cargo()
    elif answer_side in ["north", "n", "2"]:
        print(" \n You head north \n You reach the cargo hold of the shipyard. You see great ships being loaded with crates. You hear voices coming from the right side of the reception area; they don't sound friendly. \n\n")
        sleep(5)
        clear()
        hiding()
    else:
        print(" \n Invalid answer. Why don't you try again? \n\n")
        part2b ()

def hiding():
    answer_hiding = input(" \n Where will you go? Hide in one of the crates, slip inside the ship, or head to the reception area? \n where would you like to go: \n\n 1. crates \n 2. ship \n 3. reception \n\n").lower()
    if answer_hiding in ["crates", "crate", "1"]:
        print(" \n You head towards the crates. \n\n")
        sleep(5)
        clear()
        crates()
    elif answer_hiding in ["ship", "inside ship", "2"]:
        print(" \n You head towards the ship. \n\n")
        sleep(5)
        clear()
        ship()
    elif answer_hiding in ["reception", "3"]:
        print(" \n You head towards the reception. \n\n")
        sleep(5)
        clear()
        reception()
    else:
        print(" \n Invalid answer. Why don't you try again? \n\n")
        hiding ()

def crates():
    answer_crate = input("\n You see two crates: one marked with a dragon symbol and the other unmarked. \n Which one do you hide in? \n\n 1. marked \n 2. unmarked \n\n").lower()
    if answer_crate in ["marked", "dragon", "1"]:
        print(" \n You go towards the crate marked with the dragon symbol. \n\n")
        sleep(5)
        clear()
        dragon_crate()
    elif answer_crate in ["unmarked", "2"]:
        print(" \n You go towards the unmarked crate \n\n")
        sleep(5)
        clear()
        unmarked_crate()
    else:
        print(" \n Invalid answer. Why don't you try again? \n\n")
        crates ()

def dragon_crate():
    print("\n You go into the marked crate. Inside, you find bags upon bags of drugs. There’s a Chinese man who glares at you, his eyes narrowing. \n He doesn't seem pleased to see you. He shouts, 'What are you doing here?' His voice echoes through the crate, making you flinch. \n\n")
    global score
    score -= 10
    print(" \n your score is" + str(score))
    answer_dragon = input("\n You hastily leave the crate, your heart pounding. \n Do you try the other crate? \n\n 1. yes \n 2. no \n\n").lower()
    if answer_dragon in ["yes", "y", "1"]:
        print(" \n You enter the unmarked crate. \n The watch glows and transforms, seemingly upgraded in a way you instinctively recognise. \n\n")
        sleep(5)
        clear()
        P2_suprisemysteryman ()
        # add location to part 2c here please
    elif answer_dragon in ["no", "n", "2"]:
        sleep(5)
        clear()
        hiding()
    else:
        print(" \n Invalid answer. Why don't you try again? \n\n")
        score -= 10
        print(" \n your score is" + str(score))
        dragon_crate ()

def unmarked_crate():
    print(" \n You hide in the crate, listening as the voices grow fainter and fainter \n The watch glows and transforms, seemingly upgraded in a way you instinctively recognise. \n\n")
    global score
    score += 10
    print(" \n your score is" + str(score))
    sleep(5)
    clear()
    P2_suprisemysteryman ()
    # add location to part 2c here please

def ship():
  global score
  print(" \n You try to sneak inside one of the cargo ships. \n\n")
  if element == "Wind":
    print(" \n You conjure a gust of wind that sends boxes toppling over. As the men scramble to see what's happened, you seize the moment and slip into the ship unnoticed. Your heart races as you make your way deeper into the shadows. \n As you explore the ship, you stumble upon a stack of papers. Some are yellowed with age, \n while others look as if they’re from a time yet to come. Among them, you find a drawing of your watch. \n Instantly, you feel your understanding of the watch deepen, as if the very sight of the picture unlocks hidden knowledge within you. \n What secrets could this watch be holding? \n The watch glows and transforms, seemingly upgraded in a way you instinctively recognise. \n\n")
    score += 10
    print( "\n your score is" + str(score))
    sleep(5)
    clear()
    P2_suprisemysteryman ()
    # add location to part 2c here please
  else:
    print(" \n You attempt to sneak into the ship, but you’re spotted. Fortunately, they're far enough away that you gain a head start as you begin running. \n Your heart races as you hide, realising you’re near the unloaded crates. \n\n")
    crate_again = input(" \n Do you opt for the crates instead? \n\n 1. yes \n 2. no \n\n").lower()
  if crate_again in ["yes", "y", "1"]:
    sleep(5)
    clear()
    crates()
  elif crate_again in ["no", "n", "2"]:
    sleep(5)
    clear()
    hiding()
  else:
    print(" \n Invalid answer. Why don't you try again? \n\n")
    ship()

def reception():
    reception_ans = input(" \n You reach the reception area, finding it deserted. The reception desk is empty. \n Do you take a moment to look around before venturing into the backroom? \n\n 1. yes \n 2. no \n\n").lower()
    if reception_ans in ["no", "n", "1"]:
        sleep(5)
        clear()
        backroom()
    elif reception_ans in ["yes", "y", "2"]:
        print(" \n You scan the reception area and spot a revolver lying on a table. The weight of the situation hits you as you pick it up.  \n A door labelled 'Head Office' is locked, but the backroom is unlocked \n\n")
        inventory.append("revolver")
        sleep(5)
        clear()
        backroom()
    else:
        print(" \n Invalid answer. Why don't you try again? \n\n")
        reception ()

def backroom():
  global score, health  
  print(" \n You enter the backroom and immediately spot two men. Their expressions harden as they recognize you. They advance, clearly in league with the man who attacked you earlier. \n\n")
  if "revolver" in inventory:
    print(" \n Quickly, you take out your revolver and aim at one of the men. You shoot, and he falls to the ground. \n The other man is momentarily stunned but then advances. Before he can take out his own gun, you shoot him as well. \n You are stunned at your own reflexes; shooting those men seemed second nature... \n\n")
    sleep(5)
    clear()
    office()
  else:
    print(" \n With no weapon of your own, one of the two men takes out his gun and shoots you. Your watch glows, distracting the men, and you flee. \n You decide to hide in a nearby crate and promptly pass out \n You wake up groggy. Hours must have passed. You go back into the backroom and the room looks different. \n Notes that weren't there before are now scattered on the table. You read them—they seem to outline a timeline. \n\n")
    score -= 10
    health -= 50
    print(" \n your score is" + str(score))
    print(" \n your health is" + str(health))
    sleep(5)
    clear()
    P2_suprisemysteryman ()
    # add location to part 2c here please

def office():
  global score
  print(" \n With the two unconscious men at your feet, you face a decision: Do you take a moment to look around for more clues, or do you leave quickly? \n\n ")
  key_or_not = input(" \n Do you look around? \n\n 1. yes \n 2. no \n\n").lower()
  if key_or_not in ["yes", "y", "1"]:
    print(" \n You look around, but find nothing of note. Rummaging through the pockets of the two incapacitated men, you discover two keys. One must be for the office. \n Without hesitation, you head in that direction. \n You unlock the office door and find it completely empty, except for a mysterious box. Using the second key you found, you open it. \n Inside, you discover a map that appears to chart all the paths your watch can travel through time. Every twist and turn laid out, waiting for you to explore \n\n")
    score += 20
    print(" \n your score is" + str(score))
    sleep(5)
    clear()
    P2_suprisemysteryman ()
    # add location to part 2c here please
  elif key_or_not in ["no", "n", "2"]:
    sleep(5)
    clear()
    P2_suprisemysteryman ()
    # add location to part 2c here please

def south_cargo():
  global score
  print(" \n You stumble around for hours, clearly lost. Every corner looks the same, and the weight of confusion settles in. \n Eventually, you find an office near the docks. Inside, you discover stacks of papers. \n You read them, they seem to outline a timeline for some sort of master plan, mapping out events both past and future. \n This timeline might hold the key to your next move. \n\n")
  score -= 10
  print(" \n your score is" + str(score))
  sleep(5)
  clear()
  P2_suprisemysteryman ()
  # add location to part 2c here please

# William    
def P2_suprisemysteryman ():
  global health
  mysterymanchoices = ["1", "2"]
  print(" \n You arrive at the location and see a Mysterious Figure \n\n")
  mysteriousfigure = ""
  while mysteriousfigure not in mysterymanchoices:
    print(" \n As you attack you are either: \n\n 1. ambushed by mysterious figure \n 2. attack mysterious figure \n")
    mysteriousfigure = input()
  if mysteriousfigure == "1":
    print(" \n He launches an attack, to damage you. Then he quickly flees scene clearly not wanting to engage in battle \n. You find a path leading to the clearing in the forest some puzzle to unlock a door \n\n")
    health -=10
    print("your health is" + str(health))
    sleep(5)
    clear()
    Puzzle ()
  elif mysteriousfigure == "2":
    print(" \n You attempt to launch an attack on him, but he flees before you can. You follow a blood trail of a stone alligned in the forest patch and puzzle \n\n")
    sleep(5)
    clear()
    Puzzle ()
  else:
    print(" \n Please enter a valid option for the adventure game. \n\n")
    P2_suprisemysteryman ()

def Puzzle ():
  elementtypes = ["1", "2", "3", "4"]
  print(" \n It asks you to align the stone based on what elements oppose, based on the following statements \n. A series of 3 phrases for each stone mural, a description of element, its opposed element and it's paired element \n\n")
  elementspuzzle = ""
  global health, score
  while elementspuzzle not in elementtypes:
    print( "\n Earth is strong against water, but is weak against? \n\n 1. Earth 2. Water 3. Fire 4. Wind \n\n")
    Earthinput = input()
    print(" \n Water is strong against Fire, but is weak against? \n\n 1. Earth 2. Water 3. Fire 4. Wind \n\n")
    Waterinput = input()
    print(" \n Fire is strong against wind, but is weak against? \n\n 1. Earth 2. Water 3. Fire 4. Wind \n\n")
    Fireinput = input()
    print(" \n Wind is strong against Earth, but is weak against? \n\n 1. Earth 2. Water 3. Fire 4. Wind \n\n")
    Windinput = input()
    if Earthinput!= "4" or Waterinput != "1" or Fireinput != "2" or Windinput !="3":
      print(" \n You fail and a result you die after being attacked by all elements. \n\n")
      health -= 150
      print(" \n your health is" + str(health))
      sleep(5)
      clear()
      gameend()
      break
    elif Earthinput == "4" and Waterinput == "1" and Fireinput == "2" and Windinput =="3":
      print("\n Player succeeds rock moves and the player discovers a locked door but the player has additional abilities since completing the puzzle \n Watch Upgrades \n with this the player senses several locations to head to \n\n")
      score +=10
      print(" \n your score is" + str(score))
      sleep(5)
      clear()
      directions_List ()
      break
    else:
      print(" \n Please enter a valid option for the adventure game. \n\n")
      Puzzle () 
    
# Oscars bit   
def directions_List ():
  part2_cave_bridge = ["1", "2"]
  part2locations = ""
  while part2locations not in part2_cave_bridge:
    print(" \n Which way would you like to go? \n\n 1. bridge \n 2. cave? \n")
    part2locations = input()
    if part2locations == "1":
      print(" \n You reach a bridge \n\n")
      sleep(5)
      clear()
      Part_2_Bridge ()
    elif part2locations == "2":
      print(" \n You reach a cave entrace \n\n")
      sleep(5)
      clear()
      Part_2_Cave ()
    else:
      print (" \n Please enter a valid direction \n\n")
      directions_List ()

def Part_2_Bridge ():
  part2bridgeoptions = ["1", "2"]
  part2bridge = ""
  print(" \n You come across and old rickety bridge. \n\n")
  while part2bridge not in part2bridgeoptions:
    print(" \n Would you like to? \n\n 1. cross bridge \n 2. go back \n")
    part2bridge = input()
    if part2bridge == "1":
      print(" \n you cross the bridge and it collapases dropping you into the river getting swept up in it's current. \n You wash up on a beach a your watch starts to glow, you notice a object letting of the same glow and pick it up. \n\n")
      inventory.append("lockpick")
      sleep(5)
      clear()
      Part_2_Cabin ()
    elif part2bridge == "2":
      sleep(5)
      clear()
      directions_List ()
    else:
      print(" \n Please enter a valid direction. \n\n")
      Part_2_Bridge ()

def Part_2_Cabin ():
  global inventory
  print(" \n As you continue to walk on you sense the presence of another key to upgrade the watch. \n\n")
  print(" \n You follow it to a cabin and enter. \n\n")
  inventory.append("key")
  mysteryconfront ()
  
def Part_2_Cave ():
  cavedirections= ["1", "2"]
  print(" \n You stand at the entrance of a dark ominous cave. \n\n")
  part2cave = ""
  while part2cave not in cavedirections:
    print(" \n Do you enter the cave or try the other direction? \n\n 1. proceed \n 2. go back \n")
    part2cave = input()
    if part2cave == "1":
      print(" \n You enter the cave and sense a time object nearby. \n You go in the direction you sense the time object. \n It's a sword it seems to glow when near the watch, you pick it up \n\n")
      inventory.append("sword")
      mysteryconfront ()
    elif part2cave == "2":
      sleep(5)
      clear()
      directions_List ()
    else:
      print(" \n Please enter a valid direction. \n\n")
      Part_2_Cave ()

# this is contents of you main.py work file, can skip this. End screen, Game Exit and main game start up at bottom has been modified by Kiren.
# Unlocking of the Door.  Needs testing that the and statement does not need index to mention, also idea of replacing sword with damaged sword for later outcomes of dragon fight
def mysteryconfront():
  mysteryconfontactions = ""
  global element, inventory, health
  print(" \n You come across the door and use the key both ways, finally unlocking it. \n As the door opens, you hear the mechanism inside the rock moving. \n You back away from the door, and a man quickly jumps in front of you, blocking the way to the contents inside. \n what do you decide to do: \n\n 1. convince \n 2. attack \n 3. fire \n")
  mysteryconfontactions = input()
  if mysteryconfontactions == "2":
    if "sword" in inventory:
      print(" \n you defeat him \n you feel much more stronger now, perhaps its the watch doing it \n")
      inventory.append("strong")
      P3_dragonfound()
    else:
      print(" \n With no weapon of your own, you are no match for the dragon. \n")
      health -= 20
      print("your health is" + str(health))
      P3_barelydragon ()
      # insert next section
  elif mysteryconfontactions == "1":
    if "lockpick" in inventory:
          inventory.append("companion")
          print(" \n Using the combined power of both indivudals with watches you track down the alien\nyou barter your lockpick for the item he took from the hidden door that you tried solving before he interupted you. \n")
          inventory.append("glowing berries")
          inventory.remove("lockpick")
          P3_dragoncompanion()
    else:
          print(" \n You do not have the required lockpick to open the door \n")
          #add where this would go
          P3_barelydragon ()
  elif mysteryconfontactions == "3":
      if element == "fire":
          print(f" \n you defeat your opponent with the elemental knowledge of {element} and from that you encapsule him in a fire cacoon and defeat him, he turns to ashes and his belonging burn with him \n.")
          P3_dragonfound()
      else:
            print(" \n You do not have the elemental knowledge of fire, try again? \n")
            P3_mysteryAmbush()
  else:
          print(" \n failed input for mystery confront returning \n")
          mysteryconfront()

def P3_mysteryAmbush(): # need direction into other function
  global inventory, health
  if inventory == "antidote":
        print (" \n Your poison has now been removed. \n\n")
        inventory.remove("antidote")
        sleep(5)
        clear()
        P3_dragonfound ()
  else:
        inventory.append("poisoned")
        print (" \n you have been poisoned, your health will now decrease. \n\n")
        health -= 20 # change if not impactful enough
        print(" \n your health is" + str(health))
        sleep(5)
        clear()
        P3_dragonfound ()
        
def P3_mysteryfire():
    print(f" \n you defeat your opponent with the elemental knowledge of {element} and from that you encapsule him in a fire cacoon and defeat him, he turns to ashes and his belonging burn with him. \n\n")
    sleep(5)
    clear()
    P3_dragonfound()
    
# P3 Alien and Dragon does not seem to work
def P3_dragonfound():
    DragonFight = ["1", "2"]
    fightactions = ""
    global health, inventory
    while fightactions not in DragonFight:
      fightactions = input(" \n You see the dragon, what do you want to do next: \n\n 1. flee \n 2. attack \n")
      print(" \n you found the dragon and now you attack it. \n\n")
      if fightactions == "2" and "glowing berries" in inventory and "poisoned" not in inventory:
        health += 10 # missing exit function
        print(" \n your health is" + str(health))
        sleep(5)
        clear()
        P3_windragon ()
        break
      elif fightactions == "2":
        health -= 10
        sleep(5)
        clear()
        P3_windragon ()
        break
      else:
        print(" \n you try very hard to defeat the dragon, you barely make it out. \n\n")
        health -= 40
        print("your health is" + str(health))
        sleep(5)
        clear()
        P3_barelydragon()

def P3_dragoncompanion():
    dragoncompanioncommands = ["", ""]
    helperfordragon = ""
    global health, inventory
    while helperfordragon not in dragoncompanioncommands:
      helperfordragon = input()
      if inventory == "revolver":
        print(" \n while fighting the dragon knowing how impossible it is to survive, your companion is about to get attacked\n You quickly throw the gun towards him\n he shoots the dragon and you win. \n\n")
        sleep(5)
        clear()
        P3_windragon()
      else:
        print(" \n The dragon leaps to your companion and kills him, but you manage to stab the dragon in its belly when its vulnerable, hence you absorb the power of the dragon and compnaion\n you feel strange absorbing your companion power as in something is not right. \n\n")
        inventory.append("corrupted")
        sleep(5)
        clear()
        P3_barelydragon()

def P3_barelydragon():
    global health, inventory
    if health >= 60:
        print(" \n you are ambushed it appear the aliens found you first, but you manages to surive. \n\n")
        sleep(5)
        clear()
        gameend()
    else:
        print(" \n the alien ambush you but you are no match for them and you are shot by their blaster rifles. \n\n")
        health -= 150
        print(" \n your health is" + str(health))
        sleep(5)
        clear()
        gameend()
      
def P3_windragon():
  global health, score
  if health >= 40:
    print(" \n finally you find where the aliens are you manage to setup an ambush, and with the elemnt of surpise you manage to take most out having to fight one by one what remains. \n\n")
    score += 10
    print(" \n your score is" + str(score))
    sleep(5)
    clear()
    gameend()
  else:
    sleep(5)
    clear()
    gameend()
      
# Ending Screens: someone make functions rename if needed but connect to other events if not
def gameend():
  global score, health
  with open("scorelog.txt", "w") as file:
    file.write(str(score))
  if health >= 1:
    print(f" \n you completed the game with a score of {score} and your remaining health was {health} \n\n")
    print("""
  ____                            ___                 _ 
 / ___| __ _ _ __ ___   ___      / _ \__   _____ _ __| |
| |  _ / _` | '_ ` _ \ / _ \    | | | \ \ / / _ \ '__| |
| |_| | (_| | | | | | |  __/    | |_| |\ V /  __/ |  |_|
 \____|\__,_|_| |_| |_|\___|     \___/  \_/ \___|_|  (_)

  """)
    sleep(10)
    clear()
    Main_Menu ()
  else:
    print(f" \n you lost the game with a score of {score} \n\n") 
    print("""

  ____                            ___                 _ 
 / ___| __ _ _ __ ___   ___      / _ \__   _____ _ __| |
| |  _ / _` | '_ ` _ \ / _ \    | | | \ \ / / _ \ '__| |
| |_| | (_| | | | | | |  __/    | |_| |\ V /  __/ |  |_|
 \____|\__,_|_| |_| |_|\___|     \___/  \_/ \___|_|  (_)

  """)
    sleep(10)
    clear()
    Game_Exit ()

# Ending Screens: someone make functions rename if needed but connect to other events if not
# def gamewin():

# def gamedefeat():
  
  Main_Menu ()

def Game_Exit ():
  choice = input('Press Q to Quit')
  if choice == 'q':
    # break or return or..
    import sys
    sys.exit(0)

if __name__ == "__main__":
  while True:
    print(" \n Welcome to the Adventure Game! \n You can choose to walk in multiple directions to find a way out. \n\n")
    Main_Menu ()