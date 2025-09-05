# TODO
- [x] Work on `dialogueManager()` display & `getJSON()` parsing
- [ ] JSON Scene Editor (nice to have)
- [ ] New Toggle Based Inventory System
Commit "While dialogue currently not ran, broken before this loop"
**Considering**
- [ ] Check `eval()` relating to passing arguments into python from json conditions and making executions
- [ ] NPC Speaks to Player by Name

# Overview
**Scenes**: 20(story) + 2(base)
started as a collarative project dedicated to learning python a plot design was made as a team and everything in the `ABlastThroughDimensions.py` from *2024*, names given to it where [Times Ascent, A Blast Through Dimensions], this file is V0.1

This is the V0.2 version (`python v3.12`)from the first file using the same general plot, but making it more scalable which the other file from *Oct 2024*. isnt. This is mostly a personal project to make it more efficient which isnt suppose to be impressive.

# Documentation
Trying to describe the general idea around the functions that may or may not exist
## 1 Adding Dialogue
the `getDialogue()` function will display dialogue and handle increments, and call `getJSON()` to grab from the scene.JSON, the relevant objects are
1. id; handle which text to display
2. nextID; currently implies everything is incremented by 1 from current id

>Hierarchy: id>conditions>text>nextID

### Conditions and Actions (WIP V0.2)
This is what is stored in the `scenes.json` an object has a key value  assigned to `conditions`.

1. conditions whether it should continue to display text, follow by 'then' implying execution

## 2 inputHandler (WIP V0.2)

## 3 Locations (WIP TBD)
Previsouly the idea was to use a x and y coordinate about 30x30 'pixels' to mimic location. this was not a nessery component though
>[!IMPORTANT] Future Development
>1.  Could be done through the player class as the simplest solutions 
>2. as its non essentially this may or may not be complete

## 4 Player Class (WIP TBD)
- movePOS is suppose to be for 'random events' which never got implemented but was proposed its just skeleton code atm
- inventory previoly used perimiter but as its not quantitative simply use an on of system for a simpler approach
- Conditions being stored for branching paths using JSON `conditions` object
## a. Inventory
Toggle based, works kind of like game conditions atm[^1]

[^1]: different from JSON conditions which handles execution