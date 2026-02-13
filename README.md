# Overview
Started as a collarative project dedicated to learning python a plot design was made as a team and everything in the `ABlastThroughDimensions.py` from *2024*, names given to it where [Times Ascent, A Blast Through Dimensions], this file is V0.1

This is the V0.2 version (`python v3.12`)from the first file using the same general plot, but making it more scalable which the other file from *Oct 2024*. isnt. This is mostly a personal project to make it more efficient which isnt suppose to be impressive.git config --global gpg.format ssh

---
# <u>Documentation</u>
Trying to describe the general idea around the functions that may or may not exist
## 1 Parsing
Technically its just loading data into a thing called parser but it deal with handing over the relevant segments of data to modules

## 2 Player & NPC Objects
- [ ] Inventory Mention
- [ ] Location Implementation (as in how npc objet determine where they are)


- movePOS is suppose to be for 'random events' which never got implemented but was proposed its just skeleton code atm
- inventory previoly used perimiter but as its not quantitative simply use an on of system for a simpler approach
- Conditions being stored for branching paths using JSON `conditions` object


# 3 Events Hnadling
- [ ] getDialogue part of it
- [ ] Location Event Module/Class



### Conditions & Actions (WIP V0.2)
This is what is stored in the `scenes.json` an object has a key value  assigned to `conditions`.
1. conditions whether it should continue to display text, follow by 'then' implying execution


### b. Locations (WIP TBD)
locations is simply global conditions based on a `position system` using x and y, not implemented but was the simplest idea for a beginning to build onto.
- using strings to identify location or a JSON locations data with name and returning it in a python location class
- x and y kept track by the player class
- using a 15\*15 grid instead of the 30\*30 grid


# Other Details
Cant figure out where to store this:
**Scenes**: 20(story) + 2(base)
2. scorelog.txt is remnant of a scoring system which can be seen in the none 2025 file, this may be changed to the player classmodule