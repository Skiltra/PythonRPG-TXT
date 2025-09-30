###########################################// TESTING \\#############################################

class markets:
    def __init__(self):
        traders = {
            "Trader1": {"goods":0, "potions": 5, "foods": 9}, #Example here, number represent days
            "Trader2": {0},
            "Trader3": {0}
        }
    def trading(self, target, actor):
        print("TODO: figure out simple system for trading")

class economy:
    def __init__(self):
        growth = 0.1