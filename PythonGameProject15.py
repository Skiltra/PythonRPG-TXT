
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
  Choices = ["new Game", "exit", 1, 2]
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
    print(f"your previous score was {score}")
    print("1. new game.")
    print("2. exit.")
    gameoptions = input()
    if gameoptions == "new game" or 1:
      sleep(2)
      clear()
      Character_Choice ()
    elif gameoptions == "exit" or 2:
      sleep(2)
      clear()
      Game_Exit ()
    else:
      print("Please enter a valid choice.")
      sleep(2)
      clear()
      Main_Menu ()
      
def Character_Choice ():
    Element = ["earth", "water", "fire", "wind"]
    print("Please type your name to get started.")
    name = input()
    print("Good luck, " +name+ ".")
    Element_Type = ""
    while Element_Type not in Element:
        print("Please enter your element; \n - earth \n - water \n - fire \n - wind")
        Element_Type = input()
        if Element_Type == "earth":
            print("You are an Earth element")
            sleep(2)
            clear()
            Game_Start ()
        elif Element_Type == "water":
            print("You are an Water element")
            sleep(2)
            clear()
            Game_Start ()
        elif Element_Type == "fire":
            print("You are an Fire element")
            sleep(2)
            clear()
            Game_Start ()
        elif Element_Type == "wind":
            print("You are an Wind element")
            sleep(2)
            clear()
            Game_Start ()
        else:
            print("Please enter a valid choice.")
            Character_Choice()

def Game_Start ():
  Choices_List = ["yes", "no"]
  print("You awake at the Hospital after a near death fatality. Whilst you sit up and relax the watch has cured the big scars and broken bones in your body. \n You feel full of life. Looking closely at the watch you notice a button on it. \n As you press it, you nptice you are travelling through a different dimesion.")
  choices = ""
  while choices not in Choices_List:
    print("As you turn around, you see a Waylayman. He asks you are you a merchant? \n - yes \n - no.")
    choices = input()
    if choices == "yes":
      print("Maybe I can interest you in some of my goods. It seems somehting is troubling you can I help you. \n Can you please help me with directions? \n To the West there is a village, to your North there is a forest and to the East is a bandit camp.")
      sleep(5)
      clear()
      Game_Start_Directions ()
    elif choices == "no":
      print("I see no problem.\n Can you please help me with directions. \n To the West there is a village, to your North there is a forest and to the East is a bandit camp")
      sleep(5)
      clear()
      Game_Start_Directions ()
    else:
      print("Please enter, Yes or No.")   

# Medieval Setting

def Game_Start_Directions ():
  gamestartDirections = ["village", "forest", "bandit camp"]
  part1locations = ""
  while part1locations not in gamestartDirections:
    print("Please enter if you wish to go: \n - village, \n - forest \n - bandit camp")
    part1locations = input()
    if part1locations == "village":
      print("This is the village.")
      sleep(5)
      clear()
      Part_1_The_Village ()
    elif part1locations == "forest":
      print("This is the forest.")
      sleep(5)
      clear()
      Part_1_The_Forest ()
    elif part1locations == "bandit camp":
      print("This is the Bandit Camp.")
      sleep(5)
      clear()
      Part_1_The_Bandit_Camp ()
    else:
      print("Please enter a valid option for the adventure game.")   
      
def Part_1_The_Village ():
  part1villagelocations = ["elders Hut", "manor"]
  print("You arrive at the village and you are greeted by an farmer. The farmer tells you about the Elders Hut and the Manor")
  part1choices = ""
  while part1choices not in part1villagelocations:
    print("Do you wish to go the: \n - elders hut \n - the Mmnor")
    part1choices = input()
    if part1choices == "elders Hut":
      print("This is the Elders Hut.")
      sleep(5)
      clear()
      Part_1_The_Elders_Hut ()
    elif part1choices == "manor":
      print("This is the Manor.")
      sleep(5)
      clear()
      Part_1_The_Manor ()
    else:
      print("Please enter a valid option for the adventure game.")
      
def Part_1_The_Elders_Hut ():
  print("You arrive at the Elders hut, you decice to help the farmers to fight the Lords Army. \n As you fight off the army, you are stopped by the peasants rebellion. You decide to take camp at the mountains. \n As you get to the mountains you stop near Obsidan Camp, unaware of a dragon nearby.")
  sleep(5)
  clear()
  Part_1_Dragon_Attack ()
      
def Part_1_The_Manor ():
  print("You decide to go to the manor, and help the lord along with the lords’ soldier to make the people pay the taxes. \n They fight back and the peasants are held back to a mountain. \n Out of the obsidan mine comes an Dragon.")
  sleep(5)
  clear()
  Part_1_Dragon_Attack ()

# Testing Inventory
def Part_1_The_Forest ():
  flowertype = ["flower", "herb"]
  print("You arrive at the forest, as you do you see a Witch.\n The witch tells you to collec a special herb for her. She tells you to the mountains to find one")
  mountainchoice = ""
  while mountainchoice not in flowertype:
    print("At the mountain you pick up a: \n - flower \n - herb, \n which do you want to go for.\n After picking it up you head back to check with the witch.\n The witch chesks to see what you have got.")
    mountainchoice = input()
    if mountainchoice == "flower":
      print("This is not the correct flower. However if you go to the Obsidan near the mountain then this will be disregarded.")
      sleep(5)
      clear()
      Part_1_Dragon_Attack ()
    elif mountainchoice == "herb":
      print("This is the one, as a reward I shall give you this antidote to cure the poison. \n As you plan to leave, the Dragon appears.")
      global inventory
      inventory.append("antidote")
      sleep(5)
      clear()
      Part_1_Dragon_Attack ()
    else:
      print("Please enter a valid option for the adventure game.")
      
def Part_1_The_Bandit_Camp ():
  playerbanditactions = ["work with bandits", "attack bandits", "spy on bandits"]
  banditachoice = ""
  while banditachoice not in playerbanditactions:
    print("You are at the Bandit camp, please type if you want to: \n - work with Bandits  \n - attack bandits \n - spy on nandits")
    banditachoice = input()
    if banditachoice == "work with Bandits":
      print("You are to spy on the goblins.\n As you listen to the goblins conversation they talk about dragons weakness to fire from water. \n A mighty dragon appears.")
      sleep(5)
      clear()
      Part_1_Dragon_Attack ()
    elif banditachoice == "attack bandits":
      print("You decide to fight the bandits and are wounded. After being taken prisioner, they then try to use you as bait the defeat the dragon. \n The dragon kills them off and you run.")
      sleep(5)
      clear()
      Part_1_Dragon_Attack ()
    elif banditachoice == "spy on bandits":
      print("You decide to spy on the bandits, and sneak into there camp. They talk about goblins over the river and about obsidian mine. \n As you explore you run into a dragon")
      sleep(5)
      clear()
      Part_1_Dragon_Attack ()
    else:
      print("Please enter a valid option for the adventure game.")
      
def Part_1_Dragon_Attack ():
    Dragonattackpath = ["worked with bandits", "attacked bandits", "spied on bandits and travelled to goblin camp.", "spied on bandits and travelled to obsidan mine"]
    dragonaction = ""
    while dragonaction not in Dragonattackpath:
        print("You see a Drgaon waiting to attack you, Please type whether you: \n - worked with Bandits \n - attacked Bandits \n - spied on bandits and travelled to obsidan mine \n - spied on bandits and travelled to goblin camp")
        dragonaction = input()
        if dragonaction == "worked with bandits":
            print("The dragon closes in on attack.\n With the power of water you succeed in dragon fight get for this dragon evaaporates and has to flee.")
            sleep(5)
            clear()
            Part_2_Chasing_Asilant ()
        elif dragonaction == "attacked bandits":
            print("The dragon swoops in low to attack you \n. You are hurt by oncoming dragon attack. You try to chase down the dragon.")
            sleep(5)
            clear()
            Part_2_Chasing_Asilant ()
        elif dragonaction == "spied on bandits and travelled to goblin camp":
            print("You spied on the bandits and visited the goblin camp to find out to use water on the dragon. \n with the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            sleep(5)
            clear()
            Part_2_Chasing_Asilant ()
        elif dragonaction == "spied on bandits and travelled to obsidan mine":
            print("You spied on the bandits and went straight to Obsidan Mine. \n when the dragon attacks you manage to scrape the dragon to make it bleed. The Dragon escapes.")
            sleep(5)
            clear()
            Part_2_Chasing_Asilant ()
        else:
            print("Please enter a valid option for the adventure game.")
            
def Part_2_Chasing_Asilant ():
    print("The player changes into a new time periodas the watch was glowing now and it opened a new path for him towards an office.\n. As you eneter the office there is a note that talks about a ritual to beat the dragon\nBefore you can move any further a Man appears who then teleports away when you see him.\nYou chase him using your path from the watch. When you speak to him he seems to want to undo all the actions you have done\nThe enemey assilant tells him to stop, you do not know what you are dealing wiyj. Then he shifts away into another dimension")
    sleep(10)
    clear()
    part2b ()
  
# Shafia    
def part2b():
    print("")
    answer_side = input("As you attempt to follow him using your watch, you see you are now at a shipyard. You can either go North or South. ").lower()
    if answer_side in ["south", "s"]:
        print("")
        print("You head south")
        sleep(5)
        clear()
        south_cargo()
    elif answer_side in ["north", "n"]:
        print("")
        print("You head north \n You reach the cargo hold of the shipyard. You see great ships being loaded with crates. You hear voices coming from the right side of the reception area; they don't sound friendly. ")
        sleep(5)
        clear()
        hiding()
    else:
        print("Invalid answer. Why don't you try again?")
        part2b ()

def hiding():
    print("")
    answer_hiding = input("Where will you go? Hide in one of the crates, slip inside the ship, or head to the reception area? ").lower()
    if answer_hiding in ["crates", "crate"]:
        print("")
        print("You head towards the crates.")
        sleep(5)
        clear()
        crates()
    elif answer_hiding in ["ship", "inside ship"]:
        print("")
        print("You head towards the ship.")
        sleep(5)
        clear()
        ship()
    elif answer_hiding == "reception":
        print("")
        print("You head towards the reception.")
        sleep(5)
        clear()
        reception()
    else:
        print("Invalid answer. Why don't you try again?")
        hiding ()

def crates():
    print("")
    answer_crate = input("You see two crates: one marked with a dragon symbol and the other unmarked. Which one do you hide in? ").lower()
    if answer_crate in ["marked", "dragon"]:
        print("")
        print("You go towards the crate marked with the dragon symbol.")
        sleep(5)
        clear()
        dragon_crate()
    elif answer_crate == "unmarked":
        print("")
        print("You go towards the unmarked crate.")
        sleep(5)
        clear()
        unmarked_crate()
    else:
        print("Invalid answer. Why don't you try again?")
        crates ()

def dragon_crate():
    print("")
    print("You go into the marked crate. Inside, you find bags upon bags of drugs. There’s a Chinese man who glares at you, his eyes narrowing. \n He doesn't seem pleased to see you. He shouts, 'What are you doing here?' His voice echoes through the crate, making you flinch.")
    global score
    score -= 10
    answer_dragon = input("You hastily leave the crate, your heart pounding. Do you try the other crate? ").lower()
    if answer_dragon in ["yes", "y"]:
        print("")
        print("You enter the unmarked crate. \n The watch glows and transforms, seemingly upgraded in a way you instinctively recognise.")
        sleep(5)
        clear()
        P2_suprisemysteryman ()
        # add location to part 2c here please
    elif answer_dragon in ["no", "n"]:
        sleep(5)
        clear()
        hiding()
    else:
        print("Invalid answer. Why don't you try again?")
        score -= 10
        dragon_crate ()

def unmarked_crate():
    print("")
    print("You hide in the crate, listening as the voices grow fainter and fainter \n The watch glows and transforms, seemingly upgraded in a way you instinctively recognise.")
    global score
    score += 10
    sleep(5)
    clear()
    P2_suprisemysteryman ()
    # add location to part 2c here please

def ship():
  global score
  print("")
  print("You try to sneak inside one of the cargo ships.")
  if element == "Wind":
    print("")
    print("You conjure a gust of wind that sends boxes toppling over. As the men scramble to see what's happened, you seize the moment and slip into the ship unnoticed. Your heart races as you make your way deeper into the shadows. \n As you explore the ship, you stumble upon a stack of papers. Some are yellowed with age, \n while others look as if they’re from a time yet to come. Among them, you find a drawing of your watch. \n Instantly, you feel your understanding of the watch deepen, as if the very sight of the picture unlocks hidden knowledge within you. \n What secrets could this watch be holding? \n The watch glows and transforms, seemingly upgraded in a way you instinctively recognise.")
    score += 10
    sleep(5)
    clear()
    P2_suprisemysteryman ()
    # add location to part 2c here please
  else:
    print("")
    print("You attempt to sneak into the ship, but you’re spotted. Fortunately, they're far enough away that you gain a head start as you begin running. \n Your heart races as you hide, realising you’re near the unloaded crates.")
    crate_again = input("Do you opt for the crates instead? ").lower()
  if crate_again in ["yes", "y"]:
    sleep(5)
    clear()
    crates()
  elif crate_again in ["no", "n"]:
    sleep(5)
    clear()
    hiding()
  else:
    print("Invalid answer. Why don't you try again?")
    ship()

def reception():
    print("")
    reception_ans = input("You reach the reception area, finding it deserted. The reception desk is empty. Do you take a moment to look around before venturing into the backroom? ").lower()
    if reception_ans in ["no", "n"]:
        print("")
        sleep(5)
        clear()
        backroom()
    elif reception_ans in ["yes", "y"]:
        print("")
        print("You scan the reception area and spot a revolver lying on a table. The weight of the situation hits you as you pick it up.")
        print("A door labelled 'Head Office' is locked, but the backroom is unlocked.")
        inventory.append("revolver")
        sleep(5)
        clear()
        backroom()
    else:
        print("Invalid answer. Why don't you try again?")
        reception ()

def backroom():
  global score, health  
  print("")
  print("You enter the backroom and immediately spot two men. Their expressions harden as they recognize you. They advance, clearly in league with the man who attacked you earlier.")
  if "revolver" in inventory:
    print("")
    print("Quickly, you take out your revolver and aim at one of the men. You shoot, and he falls to the ground. \n The other man is momentarily stunned but then advances. Before he can take out his own gun, you shoot him as well. \n You are stunned at your own reflexes; shooting those men seemed second nature...")
    sleep(5)
    clear()
    office()
  else:
    print("")
    print("With no weapon of your own, one of the two men takes out his gun and shoots you. Your watch glows, distracting the men, and you flee. \n You decide to hide in a nearby crate and promptly pass out \n You wake up groggy. Hours must have passed. You go back into the backroom and the room looks different. \n Notes that weren't there before are now scattered on the table. You read them—they seem to outline a timeline.")
    score -= 10
    health -= 50
    sleep(5)
    clear()
    P2_suprisemysteryman ()
    # add location to part 2c here please

def office():
  global score
  print("")
  print("With the two unconscious men at your feet, you face a decision: Do you take a moment to look around for more clues, or do you leave quickly? ")
  key_or_not = input("Do you look around? ").lower()
  if key_or_not in ["yes", "y"]:
    print("")
    print("You look around, but find nothing of note. Rummaging through the pockets of the two incapacitated men, you discover two keys. One must be for the office. \n Without hesitation, you head in that direction. \n You unlock the office door and find it completely empty, except for a mysterious box. Using the second key you found, you open it. \n Inside, you discover a map that appears to chart all the paths your watch can travel through time. Every twist and turn laid out, waiting for you to explore")
    score += 20
    sleep(5)
    clear()
    P2_suprisemysteryman ()
    # add location to part 2c here please
  elif key_or_not in ["no", "n"]:
    print("")
    sleep(5)
    clear()
    P2_suprisemysteryman ()
    # add location to part 2c here please

def south_cargo():
  global score
  print("")
  print("You stumble around for hours, clearly lost. Every corner looks the same, and the weight of confusion settles in. \n Eventually, you find an office near the docks. Inside, you discover stacks of papers. \n You read them—they seem to outline a timeline for some sort of master plan, mapping out events both past and future. \n This timeline might hold the key to your next move.")
  score -= 10
  sleep(5)
  clear()
  P2_suprisemysteryman ()
  # add location to part 2c here please

# William    
def P2_suprisemysteryman ():
  global health
  mysterymanchoices = ["ambushed by mysterious figure", "attack mysterious figure"]
  print("You arrive at the location and see a Mysterious Figure")
  mysteriousfigure = ""
  while mysteriousfigure not in mysterymanchoices:
    print("As you attack you are either: \n - ambushed by mysterious figure \n - attack mysterious figure")
    mysteriousfigure = input()
  if mysteriousfigure == "ambushed by mysterious figure":
    print("He quickly flees scene clearly not wanting to engage in battle \n. You find a path leading to the clearing in the forest some puzzle to unlock a door")
    health -=10
    print(f"your health is {health})
    sleep(5)
    clear()
    Puzzle ()
  elif mysteriousfigure == "attack mysterious figure":
    print("You follow a blood trail of a stone alligned in the forest patch and puzzle")
    sleep(5)
    clear()
    Puzzle ()
  else:
    print("Please enter a valid option for the adventure game.")
    P2_suprisemysteryman ()

def Puzzle ():
  elementtypes = ["wind", "earth", "water", "fire"]
  print("It asks you to align the stone based on what elements oppose, based on the following statements \n. A series of 3 phrases for each stone mural, a description of element, its opposed element and it's paired element")
  elementspuzzle = ""
  global health, score
  while elementspuzzle not in elementtypes:
    print("Earth is strong against water, but is weak against?")
    Earthinput = input()
    print("Water is strong against Fire, but is weak against?")
    Waterinput = input()
    print("Fire is strong against wind, but is weak against?")
    Fireinput = input()
    print("Wind is strong against Earth, but is weak against?")
    Windinput = input()
    if Earthinput!= "wind" or Waterinput != "earth" or Fireinput != "water" or Windinput !="fire":
      print("You fail and a result you die after being attacked by all elements")
      health -= 150
      score +=10
      sleep(5)
      clear()
      gameend()
      break
    elif Earthinput == "wind" and Waterinput == "earth" and Fireinput == "water" and Windinput =="fire":
      print("Player succeeds rock moves and the player discovers a locked door but the player has additional abilities since completing the puzzle \n Watch Upgrades \n With this the player senses several locations to head to")
      sleep(5)
      clear()
      directions_List ()
      break
    else:
      print("Please enter a valid option for the adventure game.")
      Puzzle () 
    
# Oscars bit   
def directions_List ():
  part2_cave_bridge = ["bridge", "cave"]
  part2locations = ""
  while part2locations not in part2_cave_bridge:
    print("Which way would you like to go? \n - bridge \n - cave?")
    part2locations = input()
    if part2locations == "bridge":
      print("You reach a bridge")
      sleep(5)
      clear()
      Part_2_Bridge ()
    elif part2locations == "cave":
      print("You reach a cave entrace")
      sleep(5)
      clear()
      Part_2_Cave ()
    else:
      print ("Please enter a valid direction")
      directions_List ()

def Part_2_Bridge ():
  part2bridgeoptions = ["cross bridge", "go back"]
  part2bridge = ""
  print("You come across and old rickety bridge")
  while part2bridge not in part2bridgeoptions:
    print("Would you like to: \n - cross bridge \n - go back?")
    part2bridge = input()
    if part2bridge == "cross bridge":
      print("you cross the bridge and it collapases dropping you into the river getting swept up in it's current. \n You wash up on a beach a your watch starts to glow, you notice a object letting of the same glow and pick it up")
      inventory.append("lockpick")
      sleep(5)
      clear()
      Part_2_Cabin ()
    elif part2bridge == "go back_start":
      sleep(5)
      clear()
      directions_List ()
    else:
      print("Please enter a valid direction.")
      Part_2_Bridge ()

def Part_2_Cabin ():
  global inventory
  print("As you continue to walk on you sense the presence of another key to upgrade the watch")
  print("You follow it to a cabin and enter")
  inventory.append("key")
  mysteryconfront ()
  
def Part_2_Cave ():
  cavedirections= ["proceed", "back"]
  print("You stand at the entrance of a dark ominous cave.")
  part2cave = ""
  while part2cave not in cavedirections:
    print("Do you enter the cave or try the other direction? \n - proceed \n - back")
    part2cave = input()
    if part2cave == "proceed":
      print("You enter the cave and sense a time object nearby. \n You go in the direction you sense the time object. \n It's a sword it seems to glow when near the watch, you pick it up")
      inventory.append("sword")
      mysteryconfront ()
    elif part2cave == "back":
      sleep(5)
      clear()
      directions_List ()
    else:
      print("Please enter a valid direction.")
      Part_2_Cave ()

# this is contents of you main.py work file, can skip this. End screen, Game Exit and main game start up at bottom has been modified by Kiren.
# Unlocking of the Door.  Needs testing that the and statement does not need index to mention, also idea of replacing sword with damaged sword for later outcomes of dragon fight
def mysteryconfront():
  mysteryconfontfight = ["convince", "attack", "fire"]
  mysteryconfontactions = ""
  global element, inventory, health
  print("You come across the door and use the key both ways, finally unlocking it. \n As the door opens, you hear the mechanism inside the rock moving. \n You back away from the door, and a man quickly jumps in front of you, blocking the way to the contents inside. \n what do you decide to do: \n - convince \n - attack \n - fire")
  mysteryconfontactions = input()
  if mysteryconfontactions == "attack":
    if "sword" in inventory:
      print("you defeat him\n you feel much more stronger now, perhaps its the watch doing it")
      inventory.append("strong")
      P3_dragonfound()
    else:
      print("With no weapon of your own, you are no match for the dragon.")
      health -= 20
      P3_barelydragon ()
      # insert next section
  elif mysteryconfontactions == "convince":
    if "lockpick" in inventory:
          inventory.append("companion")
          print("Using the combined power of both indivudals with watches you track down the alien\nyou barter your lockpick for the item he took from the hidden door that you tried solving before he interupted you")
          inventory.append("glowing berries")
          inventory.remove("lockpick")
          P3_dragoncompanion()
    else:
          print("You fail to pick the lock")
          #add where this would go
          mysteryconfront()
  elif mysteryconfontactions == "fire":
      if element == "fire":
          print(f"you defeat your opponent with the elemental knowledge of {element} and from that you encapsule him in a fire cacoon and defeat him, he turns to ashes and his belonging burn with him")
          P3_dragonfound()
      else:
            print("You do not have the elemental knowledge of fire, try again?")
            mysteryconfront()
  else:
          print("failed input for mystery confront returning")
          mysteryconfront()

# check this code
def P3_mysteryAmbush(): # need direction into other function
  global inventory, health
  if inventory == "antidote":
        inventory.remove("antidote")
        P3_dragonfound ()
  else:
        inventory.append("poisened")
        health -= 20 # change if not impactful enough
        P3_dragonfound ()
        
def P3_mysteryfire():
    print(f"you defeat your opponent wiht the elemental knowledge of {element} and from that you encapsule him in a fire cacoon and defeat him, he turns to ashes and his belonging burn with him")
    P3_dragonfound()
    
# P3 Alien and Dragon does not seem to work
def P3_dragonfound():
    DragonFight = ["flee", "attack"]
    fightactions = ""
    global health, inventory
    while fightactions not in DragonFight:
      fightactions = input("\n You see the dragon, what do you want to do next: \n - flee \n - attack")
      print("you found the dragon and now you attack it")
      if fightactions == "attack" and "glowing berries" in inventory and "poisened" not in inventory:
        health += 10 # missing exit function
        P3_windragon ()
        break
      elif fightactions == "attack":
        health -= 10
        P3_windragon ()
        break
      else:
        print("you try very hard to defeat the dragon, you barely make it out")
        health -= 40
        P3_barelydragon()

def P3_dragoncompanion():
    dragoncompanioncommands = ["", ""]
    helperfordragon = ""
    global health, inventory
    while helperfordragon not in dragoncompanioncommands:
      helperfordragon = input()
      if inventory == "revolver":
        print("while fighting the dragon knowing how impossible it is to survive, your companion is about to get attacked\n You quickly throw the gun towards him\n he shoots the dragon and you win")
        P3_windragon()
      else:
        print("The dragon leaps to your companion and kills him, but you manage to stab the dragon in its belly when its vulnerable, hence you absorb the power of the dragon and compnaion\n you feel strange absorbing your companion power as in something is not right")
        inventory.append("corrupted")
        P3_barelydragon()

def P3_barelydragon():
    global health, inventory
    if health >= 60:
        print("you are ambushed it appear the aliens found you first, but you manages to surive")
        gameend()
    else:
        print("the alien ambush you but you are no match for them and you are shot by their blaster rifles")
        health -= 150
        gameend()
      
def P3_windragon():
  global health, score
  if health >= 40:
    print("finally you find where the aliens are you manage to setup an ambush, and with the elemnt of surpise you manage to take most out having to fight one by one what remains")
    score += 10
    gameend()
  else:
    gameend()
      
# Ending Screens: someone make functions rename if needed but connect to other events if not
def gameend():
  global score, health
  with open("scorelog.txt", "w") as file:
    file.write(str(score))
  if health >= 1:
    print(f"you completed the game with a score of {score} and your remaining health was {health}")
    print("""
  ____                            ___                 _ 
 / ___| __ _ _ __ ___   ___      / _ \__   _____ _ __| |
| |  _ / _` | '_ ` _ \ / _ \    | | | \ \ / / _ \ '__| |
| |_| | (_| | | | | | |  __/    | |_| |\ V /  __/ |  |_|
 \____|\__,_|_| |_| |_|\___|     \___/  \_/ \___|_|  (_)

  """)
    sleep(2)
    clear()
    Main_Menu ()
  else:
    print(f"you lost the game with a score of {score}") 
    print("""

  ____                            ___                 _ 
 / ___| __ _ _ __ ___   ___      / _ \__   _____ _ __| |
| |  _ / _` | '_ ` _ \ / _ \    | | | \ \ / / _ \ '__| |
| |_| | (_| | | | | | |  __/    | |_| |\ V /  __/ |  |_|
 \____|\__,_|_| |_| |_|\___|     \___/  \_/ \___|_|  (_)

  """)
    sleep(2)
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
    print("Welcome to the Adventure Game!")
    print("You can choose to walk in multiple directions to find a way out.")
    Main_Menu ()