
def part2b():
    print("")
    answer_side = input("As you attempt to follow him using your watch, you see you are now at a shipyard. You can either go North or South. ").lower()
    if answer_side in ["south", "s"]:
        print("")
        print("You head south")
        south_cargo()
    elif answer_side in ["north", "n"]:
        print("")
        print("You head north")
        print("You reach the cargo hold of the shipyard. You see great ships being loaded with crates. You hear voices coming from the right side of the reception area; they don't sound friendly.")
        hiding()
    else:
        print("Invalid answer. Why don't you try again?")
        part2b()

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
        hiding()

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
        crates()

def dragon_crate():
    print("")
    print("You go into the marked crate. Inside, you find bags upon bags of drugs. There’s a Chinese man who glares at you, his eyes narrowing. He doesn't seem pleased to see you. He shouts, 'What are you doing here?' His voice echoes through the crate, making you flinch.")
    score -= 10
    answer_dragon = input("You hastily leave the crate, your heart pounding. Do you try the other crate? ").lower()
    if answer_dragon in ["yes", "y"]:
        print("")
        print("You enter the unmarked crate.")
        print("The watch glows and transforms, seemingly upgraded in a way you instinctively recognise.")
        # add location to part 2c here please
    elif answer_dragon in ["no", "n"]:
        hiding()
    else:
        print("Invalid answer. Why don't you try again?")
        score -= 10
        dragon_crate()

def unmarked_crate():
    print("")
    print("You hide in the crate, listening as the voices grow fainter and fainter.")
    print("The watch glows and transforms, seemingly upgraded in a way you instinctively recognise.")
    score += 10
    # add location to part 2c here please

def ship():
    print("")
    print("You try to sneak inside one of the cargo ships.")
    if element == "Wind":
        print("")
        print("You conjure a gust of wind that sends boxes toppling over. As the men scramble to see what's happened, you seize the moment and slip into the ship unnoticed. Your heart races as you make your way deeper into the shadows.")
        print("As you explore the ship, you stumble upon a stack of papers. Some are yellowed with age, while others look as if they’re from a time yet to come. Among them, you find a drawing of your watch. Instantly, you feel your understanding of the watch deepen, as if the very sight of the picture unlocks hidden knowledge within you. What secrets could this watch be holding?")
        print("The watch glows and transforms, seemingly upgraded in a way you instinctively recognise.")
        score += 10
        # add location to part 2c here please
    else:
        print("")
        print("You attempt to sneak into the ship, but you’re spotted. Fortunately, they're far enough away that you gain a head start as you begin running. Your heart races as you hide, realising you’re near the unloaded crates.")
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
    print("")
    print("You enter the backroom and immediately spot two men. Their expressions harden as they recognize you. They advance, clearly in league with the man who attacked you earlier.")
    if "revolver" in inventory:
        print("")
        print("Quickly, you take out your revolver and aim at one of the men. You shoot, and he falls to the ground. The other man is momentarily stunned but then advances. Before he can take out his own gun, you shoot him as well.")
        print("You are stunned at your own reflexes; shooting those men seemed second nature...")
        office()
    else:
        print("")
        print("With no weapon of your own, one of the two men takes out his gun and shoots you. Your watch glows, distracting the men, and you flee.")
        print("You decide to hide in a nearby crate and promptly pass out.")
        print("You wake up groggy. Hours must have passed. You go back into the backroom and the room looks different. Notes that weren't there before are now scattered on the table. You read them—they seem to outline a timeline.")
        score -= 10
        health -= 50
        # add location to part 2c here please

def office():
    print("")
    print("With the two unconscious men at your feet, you face a decision: Do you take a moment to look around for more clues, or do you leave quickly? ")
    key_or_not = input("Do you look around? ").lower()
    if key_or_not in ["yes", "y"]:
        print("")
        print("You look around, but find nothing of note. Rummaging through the pockets of the two incapacitated men, you discover two keys. One must be for the office. Without hesitation, you head in that direction.")
        print("You unlock the office door and find it completely empty, except for a mysterious box. Using the second key you found, you open it.")
        print("Inside, you discover a map that appears to chart all the paths your watch can travel through time. Every twist and turn laid out, waiting for you to explore.")
        score += 20
        # add location to part 2c here please
    elif key_or_not in ["no", "n"]:
        print("")
        # add location to part 2c here please

def south_cargo():
    print("")
    print("You stumble around for hours, clearly lost. Every corner looks the same, and the weight of confusion settles in.")
    print("Eventually, you find an office near the docks. Inside, you discover stacks of papers. You read them—they seem to outline a timeline for some sort of master plan, mapping out events both past and future.")
    print("This timeline might hold the key to your next move.")
    score -= 10
    # add location to part 2c here please
