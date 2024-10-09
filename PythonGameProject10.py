
from random import randint

inventory = []
element = []
health = 100
score = 0

# Kiren
def Main_Menu ():
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
  userInput = ""
  while userInput not in Choices:
    print("1. new game.")
    print("2. exit.")
    userInput = input()
    if userInput == "new game" or 1:
      Character_Choice ()
    elif userInput == "exit" or 2:
      Game_Exit ()
    else:
      print("Please enter a valid choice.")
      
def Character_Choice ():
    Element = ["earth", "water", "fire", "wind"]
    print("Please type your name to get started")
    name = input()
    print("Good luck, " +name+ ".")
    Element_Type = ""
    while Element_Type not in Element:
        print("Please enter your element; earth, water, fire or wind")
        Element_Type = input()
        if Element_Type == "earth":
            print("You are an Earth element")
            Game_Start ()
        elif Element_Type == "water":
            print("You are an Water element")
            Game_Start ()
        elif Element_Type == "fire":
            print("You are an Fire element")
            Game_Start ()
        elif Element_Type == "wind":
            print("You are an Wind element")
            Game_Start ()
        else:
            print("Please enter a valid choice.")
            Game_Start ()

def Game_Start ():
  Choices = ["yes", "no"]
  print("You awake at the Hospital after a near death fatality. Whilst you sit up and relax the watch has cured the big scars and broken bones in your body. \n You feel full of life. Looking closely at the watch you notice a button on it. \n As you press it, you nptice you are travelling through a different dimesion.")
  userInput = ""
  while userInput not in Choices:
    print("As you turn around, you see a Waylayman. He asks you are you a merchant?.")
    userInput = input()
    if userInput == "yes":
      print("Maybe I can interest you in some of my goods. It seems somehting is troubling you can I help you. \n Can you please help me with directions? \n To the West there is a village, to your North there is a forest and to the East is a bandit camp.")
      Game_Start_Directions ()
    elif userInput == "no":
      print("I see no problem.\n Can you please help me with directions. \n To the West there is a village, to your North there is a forest and to the East is a bandit camp")
      Game_Start_Directions ()
    else:
      print("Please enter, Yes or No.")   

# Medieval Setting

def Game_Start_Directions ():
  Directions = ["west 2", "north 2 east 1", "east 2"]
  userInput = ""
  while userInput not in Directions:
    print("Please enter if you wish to go west 2 to the Village, north 2 east 1 to the forest or east 2 to the bandit camp")
    userInput = input()
    if userInput == "west 2":
      print("This is the village.")
      Part_1_The_Village ()
    elif userInput == "north 2 east 1":
      print("This is the forest.")
      Part_1_The_Forest ()
    elif userInput == "east 2":
      print("This is the Bandit Camp.")
      Part_1_The_Bandit_Camp ()
    else:
      print("Please enter a valid option for the adventure game.")   
      
def Part_1_The_Village ():
  directions = ["elders Hut", "manor"]
  print("You arrive at the village and you are greeted by an farmer. The farmer tells you about the Elders Hut and the Manor")
  userInput = ""
  while userInput not in directions:
    print("Do you wish to go the elders hut or the Mmnor")
    userInput = input()
    if userInput == "elders Hut":
      print("This is the Elders Hut.")
      Part_1_The_Elders_Hut ()
    elif userInput == "manor":
      print("This is the Manor.")
      Part_1_The_Manor ()
    else:
      print("Please enter a valid option for the adventure game.")
      
def Part_1_The_Elders_Hut ():
  print("You arrive at the Elders hut, you decice to help the farmers to fight the Lords Army. \n As you fight off the army, you are stopped by the peasants rebellion. You decide to take camp at the mountains. \n As you get to the mountains you stop near Obsidan Camp, unaware of a dragon nearby.")
  Part_1_Dragon_Attack ()
      
def Part_1_The_Manor ():
  print("You decide to go to the manor, and help the lord along with the lords’ soldier to make the people pay the taxes. \n They fight back and the peasants are held back to a mountain. \n Out of the obsidan mine comes an Dragon.")
  Part_1_Dragon_Attack ()

# Testing Inventory
def Part_1_The_Forest ():
  directions = ["flower", "herb"]
  print("You arrive at the forest, as you do you see a Witch.\n The witch tells you to collec a special herb for her. She tells you to the mountains to find one")
  userInput = ""
  while userInput not in directions:
    print("At the mountain you see a Flower and a Herb, which do you want to go for.\n After picking it up you head back to check with the witch.\n The witch chesks to see what you have got.")
    userInput = input()
    if userInput == "flower":
      print("This is not the correct flower. However if you go to the Obsidan near the mountain then this will be disregarded.")
      Part_1_Dragon_Attack ()
    elif userInput == "herb":
      print("This is the one, as a reward I shall give you this antidote to cure the poison. \n As you plan to leave, the Dragon appears.")
      global inventory
      inventory.append("antidote")
      Part_1_Dragon_Attack ()
    else:
      print("Please enter a valid option for the adventure game.")
      
def Part_1_The_Bandit_Camp ():
  Directions = ["work with bandits", "attack bandits", "spy on bandits"]
  userInput = ""
  while userInput not in Directions:
    print("You are at the Bandit camp, please type if you want to Work with Bandits or Attack Bandits or Spy on Bandits")
    userInput = input()
    if userInput == "work with Bandits":
      print("You are to spy on the goblins.\n As you listen to the goblins conversation they talk about dragons weakness to fire from water. \n A mighty dragon appears.")
      Part_1_Dragon_Attack ()
    elif userInput == "attack bandits":
      print("You decide to fight the bandits and are wounded. After being taken prisioner, they then try to use you as bait the defeat the dragon. \n The dragon kills them off and you run.")
      Part_1_Dragon_Attack ()
    elif userInput == "spy on bandits":
      print("You decide to spy on the bandits, and sneak into there camp. They talk about goblins over the river and about obsidian mine. \n As you explore you run into a dragon")
      Part_1_Dragon_Attack ()
    else:
      print("Please enter a valid option for the adventure game.")
      
def Part_1_Dragon_Attack ():
    Directions = ["worked with bandits", "attacked bandits", "spied on bandits and travelled to goblin camp.", "spied on bandits and travelled to obsidan mine"]
    userInput = ""
    while userInput not in Directions:
        print("You see a Drgaon waiting to attack you, Please type whether you Worked with Bandits or Attacked Bandits or Spied on Bandits and went to Obsidan Mine or Travel to Goblin Camp")
        userInput = input()
        if userInput == "worked with bandits":
            print("The dragon closes in on attack.\n With the power of water you succeed in dragon fight get for this dragon evaaporates and has to flee.")
            Part_2_Chasing_Asilant ()
        elif userInput == "attacked bandits":
            print("The dragon swoops in low to attack you \n. You are hurt by oncoming dragon attack. You try to chase down the dragon.")
            Part_2_Chasing_Asilant ()
        elif userInput == "spied on bandits and travelled to goblin camp":
            print("You spied on the bandits and visited the goblin camp to find out to use water on the dragon. \n with the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            Part_2_Chasing_Asilant ()
        elif userInput == "spied on bandits and travelled to obsidan mine":
            print("You spied on the bandits and went straight to Obsidan Mine. \n when the dragon attacks you manage to scrape the dragon to make it bleed. The Dragon escapes.")
            Part_2_Chasing_Asilant ()
        else:
            print("Please enter a valid option for the adventure game.")
            
def Part_2_Chasing_Asilant ():
    print("The player changes into a new time periodas the watch was glowing now and it opened a new path for him towards an office.\n. As you eneter the office there is a note that talks about a ritual to beat the dragon\nBefore you can move any further a Man appears who then teleports away when you see him.\nYou chase him using your path from the watch. When you speak to him he seems to want to undo all the actions you have done\nThe enemey assilant tells him to stop, you do not know what you are dealing wiyj. Then he shifts away into another dimension")
    part2b ()
  
# Shafia    
def part2b():
    print("")
    answer_side = input("As you attempt to follow him using your watch, you see you are now at a shipyard. You can either go North or South. ").lower()
    if answer_side in ["south", "s"]:
        print("")
        print("You head south")
        south_cargo()
    elif answer_side in ["north", "n"]:
        print("")
        print("You head north \n You reach the cargo hold of the shipyard. You see great ships being loaded with crates. You hear voices coming from the right side of the reception area; they don't sound friendly. ")
        hiding()
    else:
        print("Invalid answer. Why don't you try again?")

def hiding():
    print("")
    answer_hiding = input("Where will you go? Hide in one of the crates, slip inside the ship, or head to the reception area? ").lower()
    if answer_hiding in ["crates", "crate"]:
        print("")
        print("You head towards the crates.")
        crates()
    elif answer_hiding in ["ship", "inside ship"]:
        print("")
        print("You head towards the ship.")
        ship()
    elif answer_hiding == "reception":
        print("")
        print("You head towards the reception.")
        reception()
    else:
        print("Invalid answer. Why don't you try again?")

def crates():
    print("")
    answer_crate = input("You see two crates: one marked with a dragon symbol and the other unmarked. Which one do you hide in? ").lower()
    if answer_crate in ["marked", "dragon"]:
        print("")
        print("You go towards the crate marked with the dragon symbol.")
        dragon_crate()
    elif answer_crate == "unmarked":
        print("")
        print("You go towards the unmarked crate.")
        unmarked_crate()
    else:
        print("Invalid answer. Why don't you try again?")

def dragon_crate():
    print("")
    print("You go into the marked crate. Inside, you find bags upon bags of drugs. There’s a Chinese man who glares at you, his eyes narrowing. \n He doesn't seem pleased to see you. He shouts, 'What are you doing here?' His voice echoes through the crate, making you flinch.")
    global score
    score -= 10
    answer_dragon = input("You hastily leave the crate, your heart pounding. Do you try the other crate? ").lower()
    if answer_dragon in ["yes", "y"]:
        print("")
        print("You enter the unmarked crate. \n The watch glows and transforms, seemingly upgraded in a way you instinctively recognise.")
        # add location to part 2c here please
    elif answer_dragon in ["no", "n"]:
        hiding()
    else:
        print("Invalid answer. Why don't you try again?")
        score -= 10

def unmarked_crate():
    print("")
    print("You hide in the crate, listening as the voices grow fainter and fainter \n The watch glows and transforms, seemingly upgraded in a way you instinctively recognise.")
    global score
    score += 10
    P2_suprisemysteryman
    # add location to part 2c here please

def ship():
  global score
  print("")
  print("You try to sneak inside one of the cargo ships.")
  if element == "Wind":
    print("")
    print("You conjure a gust of wind that sends boxes toppling over. As the men scramble to see what's happened, you seize the moment and slip into the ship unnoticed. Your heart races as you make your way deeper into the shadows. \n As you explore the ship, you stumble upon a stack of papers. Some are yellowed with age, \n while others look as if they’re from a time yet to come. Among them, you find a drawing of your watch. \n Instantly, you feel your understanding of the watch deepen, as if the very sight of the picture unlocks hidden knowledge within you. \n What secrets could this watch be holding? \n The watch glows and transforms, seemingly upgraded in a way you instinctively recognise.")
    score += 10
    P2_suprisemysteryman
    # add location to part 2c here please
  else:
    print("")
    print("You attempt to sneak into the ship, but you’re spotted. Fortunately, they're far enough away that you gain a head start as you begin running. \n Your heart races as you hide, realising you’re near the unloaded crates.")
    crate_again = input("Do you opt for the crates instead? ").lower()
  if crate_again in ["yes", "y"]:
    crates()
  elif crate_again in ["no", "n"]:
    hiding()
  else:
    print("Invalid answer. Why don't you try again?")
    ship()

def reception():
    print("")
    reception_ans = input("You reach the reception area, finding it deserted. The reception desk is empty. Do you take a moment to look around before venturing into the backroom? ").lower()
    if reception_ans in ["no", "n"]:
        print("")
        backroom()
    elif reception_ans in ["yes", "y"]:
        print("")
        print("You scan the reception area and spot a revolver lying on a table. The weight of the situation hits you as you pick it up.")
        print("A door labelled 'Head Office' is locked, but the backroom is unlocked.")
        inventory.append("revolver")
        backroom()
    else:
        print("Invalid answer. Why don't you try again?")

def backroom():
  global score, health  
  print("")
  print("You enter the backroom and immediately spot two men. Their expressions harden as they recognize you. They advance, clearly in league with the man who attacked you earlier.")
  if "revolver" in inventory:
    print("")
    print("Quickly, you take out your revolver and aim at one of the men. You shoot, and he falls to the ground. \n The other man is momentarily stunned but then advances. Before he can take out his own gun, you shoot him as well. \n You are stunned at your own reflexes; shooting those men seemed second nature...")
    office()
  else:
    print("")
    print("With no weapon of your own, one of the two men takes out his gun and shoots you. Your watch glows, distracting the men, and you flee. \n You decide to hide in a nearby crate and promptly pass out \n You wake up groggy. Hours must have passed. You go back into the backroom and the room looks different. \n Notes that weren't there before are now scattered on the table. You read them—they seem to outline a timeline.")
    score -= 10
    health -= 50
    P2_suprisemysteryman
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
    P2_suprisemysteryman
    # add location to part 2c here please
  elif key_or_not in ["no", "n"]:
    print("")
    P2_suprisemysteryman
    # add location to part 2c here please

def south_cargo():
  global score
  print("")
  print("You stumble around for hours, clearly lost. Every corner looks the same, and the weight of confusion settles in. \n Eventually, you find an office near the docks. Inside, you discover stacks of papers. \n You read them—they seem to outline a timeline for some sort of master plan, mapping out events both past and future. \n This timeline might hold the key to your next move.")
  score -= 10
  P2_suprisemysteryman
  # add location to part 2c here please

# William    
def P2_suprisemysteryman ():
  global health
  directions = ["Ambushed by Mysterious Figure", "Attack Mysterious Figure"]
  print("You arrive at the location and see a Mysterious Figure")
  userinput = ""
  while userinput not in directions:
    print("As you attack you are either ambushed by Mysterious Figure or you attack the Mysterious Figure first")
    userinput = input()
  if userinput == "Ambushed by Mysterious Figure":
    print("He quickly flees scene clearly not wanting to engage in battle \n. You find a path leading to the clearing in the forest some puzzle to unlock a door")
    health -=10
    print(health)
    Puzzle ()
  elif userinput == "Attack Mysterious Figure":
    print("You follow a blood trail of a stone alligned in the forest patch and puzzle")
    Puzzle ()
  else:
    print("Please enter a valid option for the adventure game.")

def Puzzle ():
  outcomes = ["Wind", "Earth", "Water", "Fire"]
  print("It asks you to align the stone based on what elements oppose, based on the following statements \n. A series of 3 phrases for each stone mural, a description of element, its opposed element and it's paired element")
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
      print("Player succeeds rock moves and the player discovers a locked door but the player has additional abilities since completing the puzzle \n Watch Upgrades \n With this the player senses several locations to head to")
      directions_List ()
    else:
      print("Please enter a valid option for the adventure game.")    
    
# Oscars bit   
def directions_List ():
  directions = ["West", "East"]
  userInput = ""
  while userInput not in directions:
    print("Which way would you like to go? West or East?")
    userInput = input()
    if userInput == "West":
      print("You reach a bridge")
      Part_2_Bridge ()
    elif userInput == "East":
      print("You reach a cave entrace")
      Part_2_Cave ()
    else:
      print ("Please enter a valid direction")

def Part_2_Bridge ():
  directions = ["Cross_Bridge", "Go back_Start"]
  userInput = ""
  print("You come across and old rickety bridge")
  while userInput not in directions:
    print("Would you like to cross or go back and try the other direction?")
    userInput = input()
    if userInput == "Cross_Bridge":
      print("you cross the bridge and it collapases dropping you into the river getting swept up in it's current. \n You wash up on a beach a your watch starts to glow, you notice a object letting of the same glow and pick it up")
      inventory.append("Lockpick")
      Part_2_Cabin ()
    elif userInput == "Go back_Start":
      directions_List ()
    else:
      print("Please enter a valid direction.")

def Part_2_Cabin ():
  global inventory
  print("As you continue to walk on you sense the presence of another key to upgrade the watch")
  print("You follow it to a cabin and enter")
  inventory.append("Key")
  mysteryconfront ()
  
def Part_2_Cave ():
  directions= ["Proceed", "Go Back"]
  print("You stand at the entrance of a dark ominous cave.")
  userInput = ""
  while userInput not in directions:
    print("Do you enter the cave or try the other direction?")
    userInput = input()
    if userInput == "Proceed":
      print("You enter the cave and sense a time object nearby. \n You go in the direction you sense the time object. \n It's a sword it seems to glow when near the watch, you pick it up")
      inventory.append("Sword")
      mysteryconfront ()
    elif userInput == "Go Back":
      directions_List ()
    else:
      print("Please enter a valid direction.")

# Unlocking of the Door.  Needs testing that the and statement does not need index to mention, also idea of replacing sword with damaged sword for later outcomes of dragon fight
def mysteryconfront():
    Directions = ["convince", "attack", "fire"]
    userInput = ""
    global element, inventory
    while userInput or element not in Directions:
        print("You come across the door, you have the key, you Use key the key both ways and finally unlock it\n you back away from the door as it opens you hear its mechanism inside the rock moving.\n you see the man who quickly jumps in front of you blocking the way to the content of inside.")
        userInput = input()
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
            print(f"you defeat your opponent with the elemental knowledge of {element} and from that you encapsule him in a fire cacoon and defeat him, he turns to ashes and his belonging burn with him")
            P3_dragonfound()
        else:
            P3_mysteryAmbush()

def P3_mysteryAmbush():
  global inventory, health
  if inventory == "antidote":
    inventory.remove("antidote")
    P3_dragonfound()
  else:
    inventory.append("poisened")
    health -= 20
    P3_dragonfound()

# P3 Alien and Dragon does not seem to work
def P3_dragonfound():
    Directions = ["flee", "attack"]
    userInput = ""
    global health, inventory, element
    while userInput not in Directions:
      print("You come across a dragon\b you can try to flee or attack")
      userInput = input()
      if inventory == "glowing berries" and userInput == "attack":
        health += 10 # missing exit function
        P3_windragon()
      elif userInput == "attack":
         P3_barelydragon()
      elif userInput == "flee" and element == "fire":
        print("the dragons attack does not harm you, but it lands on the ground to attack physically")
        P3_barelydragon()
      elif userInput == "flee":
        health -= 40
        print("You try to flee but are spotted, it set you alight as you had your back turned")
        P3_barelydragon()
      else:
        print("invalid input")

def P3_dragoncompanion():
    Directions = ["attack"]
    userInput = ""
    global health, inventory
    while userInput not in Directions:
      print("you and your companion quickly see a dragon approaching\n type attack")
      userInput = input()
      if userInput == "attack" and inventory == "revolver":
        print("while fighting the dragon knowing how impossible it is to survive, your companion is about to get attacked\n You quickly throw the gun towards him\n he shoots the dragon and you win")
        P3_windragon()
      elif userInput == "attack" and inventory == "companion":
        print("The dragon leaps to your companion and kills him, but you manage to stab the dragon in its belly when its vulnerable, hence you absorb the power of the dragon and compnaion\n you feel strange absorbing your companion power as in something is not right")
        inventory.remove("companion")
        inventory.append("corrupted")
        P3_barelydragon()
      else:
         print("invalid input, try again")

# Dragon Fight Outcomes
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
    print("""

  ____                            ___                 _ 
 / ___| __ _ _ __ ___   ___      / _ \__   _____ _ __| |
| |  _ / _` | '_ ` _ \ / _ \    | | | \ \ / / _ \ '__| |
| |_| | (_| | | | | | |  __/    | |_| |\ V /  __/ |  |_|
 \____|\__,_|_| |_| |_|\___|     \___/  \_/ \___|_|  (_)

  """)

  ____                            ___                 _ 
 / ___| __ _ _ __ ___   ___      / _ \__   _____ _ __| |
| |  _ / _` | '_ ` _ \ / _ \    | | | \ \ / / _ \ '__| |
| |_| | (_| | | | | | |  __/    | |_| |\ V /  __/ |  |_|
 \____|\__,_|_| |_| |_|\___|     \___/  \_/ \___|_|  (_)

  """)


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