import Input
import Items
import random

class Chef:
    TYPE_HUMAN = 1
    TYPE_ROBOT = 2
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.score = 0
        return
        
    def selectItem(self, items):
        if self.type == Chef.TYPE_HUMAN:
            print("")
            print("Available items:")
            for i in range(0,len(items)):
                print(str.format("{} - {}",i,items[i].name))
            itemNum = Input.Validator.get_integer(self.name + ", which item do you select? ",0,len(items)-1)
        else:
            self.type = Chef.TYPE_ROBOT
            itemNum = random.randrange(0,len(items))
        return items[itemNum]
        
    def addScore(self, scoreIncrease):
        self.score = self.score + scoreIncrease
        return