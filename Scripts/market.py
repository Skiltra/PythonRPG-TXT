###########################################// TESTING \\#############################################
from player import locations # BUG circular import
import random


class markets:
    def __init__(self):
        self.trader = 0
        self.traders = {
            "Trader1": {"goods":0, "potions": 5, "foods": 9}, #Example here, number represent days required for shop
            "Trader2": {"weapons": 0, "armor": 5, "test":9},
        }
    def trading(self, target): # TODO:  In Progress
        for locations.day in self.trader:
            if target in self.traders :
                    self.trader += 1

class economy:
    enabled = True
    def __init__(self):
        self.growth = 0.1
        self.supplyBase = {
             "bread": 0.7,
             "sword":0.08,
             "potion": 0.3
        }
        if economy.enabled:
             self.makeEconomy
             enabled = False
    
    def makeEconomy(self):
         newGrowth = random.random() # TODO: make this based on something else
         self.growth *= newGrowth
         print("set supply of the market class")
         print("set new growth // should be based on something else")

market = markets()
market.trading("person")