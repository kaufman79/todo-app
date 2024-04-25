# Define the board as a 2D list
board = [[' ' for _ in range(4)] for _ in range(4)]

# Function to print the board
def print_board():
  for row in board:
    print("|", end="")
    for cell in row:
      print(cell + "|", end="")
    print()

# Function to check if a space is empty
def is_empty(row, col):
  return board[row][col] == ' '

# Function to place a marker on the board
def place_marker(marker, row, col):
  if is_empty(row, col):
    board[row][col] = marker
  else:
    print("That space is already occupied!")

# Function to check for a winner (checks rows, columns, and diagonals)
def check_winner(marker):
  # Check rows
  for row in board:
    if all(cell == marker for cell in row):
      return True

  # Check columns
  for col in range(4):
    if all(board[row][col] == marker for row in range(4)):
      return True

  # Check diagonals
  if all(board[i][i] == marker for i in range(4)) or \
     all(board[i][3-i] == marker for i in range(4)):
    return True

  return False

# Function to check for a tie
def check_tie():
  for row in board:
    for cell in row:
      if cell == ' ':
        return False
  return True

# Game loop
current_player = 'X'
game_over = False

while not game_over:
  print_board()

  # Get player input
  try:
    row = int(input(f"Player {current_player}, enter a row (1-4): ")) - 1
    col = int(input(f"Player {current_player}, enter a column (1-4): ")) - 1
  except ValueError:
    print("Invalid input. Please enter integers between 1 and 4.")
    continue

  # Place the marker and check for errors
  place_marker(current_player, row, col)

  # Check for winner or tie
  if check_winner(current_player):
    print_board()
    print(f"Player {current_player} wins!")
    game_over = True
  elif check_tie():
    print_board()
    print("It's a tie!")
    game_over = True

  # Switch turns
  current_player = 'O' if current_player == 'X' else 'X'

print("Thanks for playing!")
