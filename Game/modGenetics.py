

REMOVE_data = {} # testing only

class Gene:
        """This provides the dna which could be used for 2d or 3d assets but itself will not create npc just return dna on perimeter"""
        geneSys = None

        def __init__(self):
                print("geneSys Utilized")
                self.getRoot() # TODO: RENAME

        @classmethod
        def getRoot(cls):
                print("1. DEFINES UNIQUE DNA FOR ETHNIC LIKE [ORC, HUMAN]")
                cls._template = "body.json" # BUG not valid code, SKELETON
                print("assign Initial NPC DNA when called")



class AssetSelector:
        """handles assets selection using the float division formula without needing a manual define for total asset count"""
        def __init__(self):
                print("TODO")
