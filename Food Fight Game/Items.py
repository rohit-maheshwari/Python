class FoodItem:
    STATE_SOLID = 1
    STATE_LIQUID = 2
    TEMP_HOT = 1
    TEMP_COLD = 2
    
    def __init__(self, name, state, temp):
        self.name = name
        self.state = state
        self.temp = temp
        
    
class DefenseItem:
    TYPE_CLOTH = 1
    TYPE_METAL = 2
    SIZE_SMALL = 1
    SIZE_LARGE = 2
    
    def __init__(self, name, type, size):
        self.name = name
        self.type = type
        self.size = size
    
    def calculateBonus(self, foodItem):
        bonus = 0
        
        if foodItem.state == FoodItem.STATE_SOLID and self.size == DefenseItem.SIZE_SMALL:
            bonus = bonus + 25
        if foodItem.state == FoodItem.STATE_LIQUID and self.size == DefenseItem.SIZE_LARGE:
            bonus = bonus + 25
        if foodItem.temp == FoodItem.TEMP_HOT and self.type == DefenseItem.TYPE_CLOTH:
            bonus = bonus + 25
        if foodItem.temp == FoodItem.TEMP_COLD and self.type == DefenseItem.TYPE_METAL:
            bonus = bonus + 25
            
        return bonus