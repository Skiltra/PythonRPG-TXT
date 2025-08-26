# TODO
- [ ] Work on `dialogueManager()` display & `getJSON()` parsing
- [ ] JSON Scene Editor (nice to have)
- [ ] New Toggle Based Inventory System

**Consider**
- [ ] Check `eval()` relating to passing arguments into python from json conditions and making executions
- [ ] NPC Speaks to Player by Name

# Overview
**Scenes**: 20(story) + 2(base)

This is the second version from the first file using the same general plot, but making it more scalable which the other file from *Oct 2024*. isnt. This is mostly a personal project to make it more efficient which isnt suppose to be impressive.

The main improvement to the new version is, it has classes with functions which actually achieve some of the ideas we had planning, 

**Old Overview** <br>
Based on a small team prototyping some ideas, as a compromise we implementing all version of the plot through the idea of it being "time travel" through time hence the titles used for it is known as:
- Times Ascent
- A Black Through Dimensions

# Documentation
This is me trying to explain the code more of a unprofessional guide to the idea
## 1 Adding Dialogue
the `getDialogue()` function will indentify the JSON array using the scene.json.  when adding new dialogue you must have an object with these 3 nesserily components:
1. id  # help with tracking scene progress 
2. text # for display cannot display otherwise
3. nextID # if this is not present the loop breaks because nothing else is called
by default it should go in its own direction but sometimes when input is expectet its possible its called manually instead of the automatic process by getDialogue

other important attributes in json are:
1. conditions # this deal with getDialogue having to determine true condition on its own as well as custom
2. action # whenever some exeuciton is needed this is the object that is parsed into python code

in order it is as written in scenes.json id>type>text>nextID>action

## 2 inputHandler
>[!NOTE] Details if inputSystem Class
>This is from the usage of input assigned to variables but putting it into a single function to extend ontop of the built-in `input()`

## 3 Locations
Previsouly the idea was to use a x and y coordinate about 30x30 'pixels' to mimic location. this was not a nessery component though
>[!IMPORTANT] Future Development
>1.  Could be done through the player class as the simplest solutions 
>2. as its non essentially this may or may not be complete

## 4 Player Class
- movePOS is suppose to be for 'random events' which never got implemented but was proposed its just skeleton code atm
- inventory previoly used perimiter but as its not quantitative simply use an on of system for a simpler approach