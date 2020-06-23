from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 2)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_row1 = ship_row +1
ship_col = random_col(board)

for turn in range(4):
  print ("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_row = guess_row - 1
  guess_col = int(input("Guess Col: "))
  guess_col = guess_col - 1

  if (guess_row == ship_row or guess_row == ship_row1) and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print ("Game Over")
    print_board(board)


print("This was the board and B is where the battleship was...")
board[ship_row][ship_col] = "B"
board[ship_row1][ship_col] = "B"
print_board(board)

ship_row = ship_row + 1
ship_row1 = ship_row1 + 1
ship_col = ship_col + 1
    
print(str.format("({},{})", ship_row, ship_col))
print(str.format("({},{})", ship_row1, ship_col))
