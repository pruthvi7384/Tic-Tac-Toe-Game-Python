# =============Tic Tac toe Game===========

# =========Logic========
    # board
    # dispaly board
    # play game
    # cheack wai]n
        # check rows
        # check columns
        # check diagonals
    # cheack tie
    # flip player
# =======X==Logic==X======

# ======Global==============

# Game Board
board = ['-','-','-',
         '-','-','-',
         '-','-','-']

# if game is still going
game_stll_going = True

# who won? or tie
winner = None

# Current Player is X

current_player = "X"

# Dispaly Board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    
def play_game():
    
    # Display initial board
    display_board()
    
    # while the game is still going
    while game_stll_going:
        
        # handle a single turn of an arbitrary player
        handle_turn(current_player)
        
        # check if the game has ended
        check_if_game_over()
        
        # Flip to the other player
        flip_player()
        
    # The game has ended
    if winner =="X" or winner =="O":
        print(winner + " Won. ")
    elif winner == None:
        print(" Tie. ")

# Handale a single turn of an arbitry player
def handle_turn(player):
    
    print(player + "'s turn.")
    positions = input("Choose a position from 1-9 ")
    
    valid = False
    while not valid:
        while positions not in ["1","2","3","4","5","6","7","8","9"]:
            positions = input("Invalid input. Choose a position from 1-9 ")
        positions = int(positions) - 1
        
        if board[positions] =="-":
            valid = True
        else:
            print("You cant go there. Go again.")
    
    board[positions] = player
    
    display_board()
    
def check_if_game_over():
    check_for_winner()
    check_if_tie()
    
def check_for_winner():
    # set up global veriables
    global winner
    # check rows
    row_winner = check_row()
    # check columns
    columns_winner = check_column()
    # check diagonals
    diagonals_winner = check_diagonals()
    
    # Get The Winner
    if row_winner:
        # There was a win
        winner = row_winner
    elif columns_winner:
        # There was a winne
        winner = columns_winner
    elif diagonals_winner:
        # There was a win
        winner = diagonals_winner
    else:
        # There was no win
        winner = None
    return

def check_row():
    # set global variables
    global game_stll_going
    
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any of the rows have all the same (and is not emptey)
    if row_1 or row_2 or row_3:
        game_stll_going= False
    # Return the Winner ( X or O )
    if row_1:
       return board[0]
    elif row_2:
       return board[3]
    elif row_3:
       return board[6]
    return

def check_column():
    # set global variables
    global game_stll_going
    
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any of the rows have all the same (and is not emptey)
    if column_1 or column_2 or column_3:
        game_stll_going= False
    # Return the Winner ( X or O )
    if column_1:
       return board[0]
    elif column_2:
       return board[1]
    elif column_3:
       return board[2]
    return

def check_diagonals():
     # set global variables
    global game_stll_going
    
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    
    # if any of the rows have all the same (and is not emptey)
    if diagonals_1 or diagonals_2 :
        game_stll_going= False
    # Return the Winner ( X or O )
    if diagonals_1:
       return board[0]
    elif diagonals_2:
       return board[6]
    return

def check_if_tie():
    # set global variables
    global game_stll_going
    if "-" not in board:
        game_stll_going= False
    return

def flip_player():
    # Set Global Veribal Here
    global current_player
    # Flip Player Here ( Player Change )
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()

# ===========X==Tic Tac toe Game==X=========