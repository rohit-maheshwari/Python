import Items
import Player

foodItems = []
item = Items.FoodItem("Hot Coffee", Items.FoodItem.STATE_LIQUID, Items.FoodItem.TEMP_HOT)
foodItems.append(item)
item = Items.FoodItem("Cold Water", Items.FoodItem.STATE_LIQUID, Items.FoodItem.TEMP_COLD)
foodItems.append(item)
item = Items.FoodItem("Steamed Vegetables", Items.FoodItem.STATE_SOLID, Items.FoodItem.TEMP_HOT)
foodItems.append(item)
item = Items.FoodItem("Ice Cream", Items.FoodItem.STATE_SOLID, Items.FoodItem.TEMP_COLD)
foodItems.append(item)

defenseItems = []
item = Items.DefenseItem("Chef's Hat", Items.DefenseItem.TYPE_CLOTH, Items.DefenseItem.SIZE_SMALL)
defenseItems.append(item)
item = Items.DefenseItem("Apron", Items.DefenseItem.TYPE_CLOTH, Items.DefenseItem.SIZE_LARGE)
defenseItems.append(item)
item = Items.DefenseItem("Mixing Bowl", Items.DefenseItem.TYPE_METAL, Items.DefenseItem.SIZE_SMALL)
defenseItems.append(item)
item = Items.DefenseItem("Cookie Sheet", Items.DefenseItem.TYPE_METAL, Items.DefenseItem.SIZE_LARGE)
defenseItems.append(item)

playerName = input("What is your name? ")
player1 = Player.Chef(playerName, 1)
player2 = Player.Chef("Robo-Cook", 2)

for i in range(1,2):
    print("")
    print(str.format("DING DING! ROUND {}", i))
    player1Food = player1.selectItem(foodItems)
    player1Defense = player1.selectItem(defenseItems)
    player2Food = player2.selectItem(foodItems)
    player2Defense = player2.selectItem(defenseItems)
    player1DefenseBonus = player1Defense.calculateBonus(player2Food)
    player2DefenseBonus = player2Defense.calculateBonus(player1Food)
    player1Score = 100 - player2DefenseBonus
    player2Score = 100 - player1DefenseBonus
    player1.addScore(player1Score)
    player2.addScore(player2Score)
    print("")
    print(str.format("{} scored {} by throwing {} against {}'s {}", player1.name,player1Score,player1Food.name,player2.name,player2Defense.name))
    print(str.format("{} scored {} by throwing {} against {}'s {}", player2.name,player2Score,player2Food.name,player1.name,player1Defense.name))
    print(str.format("Current Scores: {} has {}, {} has {}", player1.name, player1Score, player2.name, player2Score))
    print("")
    
print("Game Over! Final Scores:")
print(str.format("{} = {}", player1.name, player1Score))
print(str.format("{} = {}", player2.name, player2Score))
    
    
    
    
    
    
