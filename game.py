import random


inventory = []

def Game_Start ():
  Choices = ["Yes", "No"]
  print("You awake at the Hospital after a near death fatality. Whilst you sit up and relax the watch has cured. The big scars and broken bones in your body were feeling repaied. You felt full of life. Looking closely at the watch you notice a button on it. As you press it, you nptice you are travelling through a different dimesion.")
  userInput = ""
  while userInput not in Choices:
    print("As you turn around, you see a Waylayman. He asks you are you a merchant?.")
    userInput = input()
    if userInput == "Yes":
      print("Maybe I can interest you in some of my goods. It seems somehting is troubling you can I help you.")
      print("Can you please help me with directions.")
      print("To the West there is a village, to your North there is a forest and to the East is a bandit camp.")
      Game_Start_Directions ()
    elif userInput == "No":
      print("I see no problem.")
      print("Can you please help me with directions.")
      print("To the West there is a village, to your North there is a forest and to the East is a bandit camp.")
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
  print("You arrive at the Elders hut, you decice to help the farmers to fight the Lords Army")
  print("As you fight off the army, you are stopped by the peasants rebellion. You decide to take camp at the mountains")
  print("As you get to the mountains you stop near Obsidan Camp, unaware of a dragon nearby")
  Part_1_Dragon_Attack ()
      
def Part_1_The_Manor ():
  print("You decide to go to the manor, and help the lord along with the lords’ soldier to make the people pay the taxes.")
  print("They fight back and the peasant are held back to a mountain.")
  print("Out of the obsidan mine comes an Dragon..")
  Part_1_Dragon_Attack ()
      
def Part_1_The_Forest ():
  directions = ["Flower", "Herb"]
  print("You arrive at the forest, as you do you see a Witch.")
  print("The witch tells you to collec a special herb for her. She tells you to the mountains to find one")
  userInput = ""
  while userInput not in directions:
    print("At the mountain you see a Flower and a Hern, which do you want to go for.")
    print("After picjing it up you head back to check with the witch.")
    print("The witch chesks to see what you have got.")
    userInput = input()
    if userInput == "Flower":
      print("This is not the correct flower. However if you go to the Obsidan near the mountain then this will be disregarded.")
      Part_1_Dragon_Attack ()
    elif userInput == "Herb":
      print("This is the one, as a reward I shall give you this antidote to cure poison.")
      print("As you plan to leave, the Dragon appears.")
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
      print("You are to spy on the goblins.")
      print("As you listen to the goblins convseartion they ttalk about dragons weakness to fire from water.")
      print("An dragon appears.") 
      Part_1_Dragon_Attack ()
    elif userInput == "Attack Bandits":
      print("You decide to fight the bandits and are wounded. After being taken prisoner they try to use upoi as bait the defeat the dragon. ")
      print("The dragon kills them off and you run.")
      Part_1_Dragon_Attack ()
    elif userInput == "Spy on Bandits":
      print("You decide to spy on the bandits, and sneak into there camp they talk about goblins over the river and about obsidan mine")
      print("As you explore you run into a dragon.")
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
            print("The dragon closes in on attack.")
            print("with the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.") 
            Part_2_Chasing_Asilant ()
        elif userInput == "Attacked Bandits":
            print("The dragon swoops in low to attack you ")
            print("You are hurt by oncoming dragon attack. You try to chase down the dragon.")
            Part_2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Goblin Camp":
            print("You spied on the bandits and visited the gobline camp to finf out to use water on the dragon.")
            print("with the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            Part_2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Obsidan Mine":
            print("You spied on the bandits and went straight to Obsidan Mine")
            print("when dragon attacks you manage to scrape the dragon to make it bleed. The Dragon escapes.")
            Part_2_Chasing_Asilant ()
        else:
            print("Please enter a valid option for the adventure game.")
            
def Part_2_Chasing_Asilant ():
  print("The player changes into a new time periodas the watch was glowing now and it opened a new path for him towards an office.")
  print("As you eneter the office there is a note that talks about a ritual to beat the dragon.")
  print("Before you can move any further a Man appears who then teleports away when you see him.")
  print("You chase him using your path from the watch. When you speak to him he seems to want to undo all the actions you have done")
  print("The enemey assilant tells him to stop, you do not know what you are dealing wiyj. Then he shifts away into another dimension.")
  Part_2_Shipyard ()
  
def Part_2_Shipyard ():
    Directions = ["North", "South"]
    userInput = ""
    while userInput not in Directions:
        print("As you attenpt to follow him uisng your watch you see you are now at an shipyard. You can either go North or South")
        userInput = input()
        if userInput == "North":
            print("The dragon closes in on attack.")
            print("with the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.") 
            Part_2_Chasing_Asilant ()
        elif userInput == "Attacked Bandits":
            print("The dragon swoops in low to attack you ")
            print("You are hurt by oncoming dragon attack. You try to chase down the dragon.")
            Part_2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Goblin Camp":
            print("You spied on the bandits and visited the gobline camp to finf out to use water on the dragon.")
            print("with the power of water you succeed in dragon fight get for this dragon evaraporates and has to flee.")
            Part_2_Chasing_Asilant ()
        elif userInput == "Spied on Bandits and Travelled to Obsidan Mine":
            print("You spied on the bandits and went straight to Obsidan Mine")
            print("when dragon attacks you manage to scrape the dragon to make it bleed. The Dragon escapes.")
            Part_2_Chasing_Asilant ()
        else:
            print("Please enter a valid option for the adventure game.")


        

if __name__ == "__main__":
  while True:
    print("Welcome to the Adventure Game!")
    print("As an avid traveler, you have decided to visit the Catacombs of Paris.")
    print("However, during your exploration, you find yourself lost.")
    print("You can choose to walk in multiple directions to find a way out.")
    print("Let's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    Game_Start()


def Load_Area1 ():
    directions = ["Ambushed by Mysterious Figure", "Attack Mysterious Figure"]
    userinput = ""
    while userinput not in directions:
        print["What would you like to do?"]
        userinput = input{}
        if userinput == "Ambushed by Mysterious Figure"
        print("Health-10")
        print("He quickly flees scene clearly not wanting to engage in battle")
        print("You find a path leading to the clearing in the forest some puzzle to unlock a door")
        Puzzle ()
        elif userinput == "Attack Mysterious Figure"
        print("You follow a blood trail of a stone alligned in the forest patch and puzzle")
        Puzzle ()


        def Puzzle ():
            print("It asks you to align the stone based on what elements oppose, based on the following statements")
            print("A series of 3 phrases for each stone mural, a description of element, its opposed element and it's paired element")
            userinput = input{}
            if userinput == "Player Failed"
            print("Player dies and is attacked by all elements")
            print("End Screen")
            elif userinput == "Player Succeeds"
            print("Player succeeds rock moves and the player discovers a locked door but the player has additional abilities since completing the puzzle")
            print("Watch Upgrades")
            print("With this the player senses several locations to head to")


            