from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row 
#print ship_col

for turn in range(4):
    guess_row = int(input("Chute uma linha: "))
    guess_col = int(input("Chute uma coluna: "))

    if guess_row == ship_row and guess_col == ship_col:
      print ("Parabéns! Você afundou o navio!")
      break
    else:
      if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print ("Ih, acho que você isolou a bomba.")
      elif(board[guess_row][guess_col] == "X"):
        print ("Você já tentou essa opção.")
      else:
        print ("Você errou o navio!")
        board[guess_row][guess_col] = "X"
      print ("Turno", turn + 1)
      print_board(board)
      if turn == 3:
        print ("Fim de jogo")