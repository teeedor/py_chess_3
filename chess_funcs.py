# --- chess_funcs.py ---
# This file draws and makes new boards
# also holds misc functions related to the game

#pieces are stored as a list of nested tuples ((x_val,y_val),(Color,Type))
#board[piece index][location or piece][Final Value]
#board[0][0][1] = first piece in list/coordinates/y coordinate
#the draw() function iterates through this array and draws the current board

#white goes first
#game asks player for move
#checks if is validmove based on moveset
#checks if is validmove based on current board state
    #this includes a piece being on the move target
    #or a piece being in the way of the move target

#Basic Movesets for pieces coded in "move_sets.py"
#Scoreboard that keeps track of captured piece values

import os # to clear the screen
# the next import creates a circle and messes up compilation
# move the make_move() function to other file
#from move_sets import in_move_set, is_valid_move

# Colors for formatting Strings
red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"

def get_piece(board,x,y):
    # Iterate through piece list and figure out if there is a piece there
    for piece in board:
        if piece[0][0] == x and piece[0][1] == y: 
            # Return color and type
            output = (piece[1][0],piece[1][1])
            break
        else:
            output = ("N","N")
    return output

def filled(board,x,y):
    # just says whether a location has a piece or not
    for piece in board:
        if piece[0][0] == x and piece[0][1] == y: 
            return True
        else:
            return False

def make_board(mode):
    # all tests in self_test.py generate their own custom boards
    board = []
    if mode == 1:
        #sparsly populated board
        board = [((6,3),("W","H")),((5,2),("W","P")),((3,2),("W","P")),((2,3),("B","h")),
                 ((6,6),("B","r")),
                 ((4,4),("W","H")),((6,2),("B","b")),((2,2),("W","B")),((2,6),("B","b"))]
        return board
    elif mode == 2:
        #full standard board
        board = [((1,1),("W","R")),((2,1),("W","H")),((3,1),("W","B")),((4,1),("W","K")),
                 ((5,1),("W","Q")),((6,1),("W","B")),((7,1),("W","H")),((8,1),("W","R")),
                 ((1,2),("W","P")),((2,2),("W","P")),((3,2),("W","P")),((4,2),("W","P")),
                 ((5,2),("W","P")),((6,2),("W","P")),((7,2),("W","P")),((8,2),("W","P")),
                 ((1,7),("B","p")),((2,7),("B","p")),((3,7),("B","p")),((4,7),("B","p")),
                 ((5,7),("B","p")),((6,7),("B","p")),((7,7),("B","p")),((8,7),("B","p")),
                 ((1,8),("B","h")),((2,8),("B","h")),((3,8),("B","b")),((4,8),("B","k")),
                 ((5,8),("B","q")),((6,8),("B","b")),((7,8),("B","h")),((8,8),("B","r"))]
        return board
    else:
        return board

def draw_line(y_val, board):
    output = "" 
    for x_val in range(1,9):
        #loop through x vals, populate output string with piece or no piece
        for piece in board:
            if piece[0][0] == x_val and piece[0][1] == y_val:
                string = " " + piece[1][1]
                #Only one piece can be at loc, so break from loop
                break 
            else:
                #No piece at loc, draw checkerboard
                if (x_val % 2 + y_val) % 2 == 1:
                    string = " #"
                else:
                    string = "  "
    #after the entire loop, Draw the String
        output += string
    print("\t  "+str(y_val) + output)

def draw(board):
    #os.system('cls') #Clear screen
    #Draw each horizontal line of the board from top to bottom

    print("\n") 
    for y in range(8,0,-1):
        #Draw entire y_val line
        draw_line(y, board)
    #Coordinate Marks
    print("\t    1 2 3 4 5 6 7 8") 
    print("\n") 

def find_index(board,x,y):
    index = next(
        (i for i, t in enumerate(board) if t[0] == (x,y)),
        "None"
    )

def remove_piece(board,x,y):
    index = next(
        (i for i, t in enumerate(board) if t[0] == (x,y)),
        "None"
    )
    board = board.pop(index)

#def draw_move_path(board,xs,ys,xt,yt):
    # this function does the same as the draw function,
    # but it will add a red path over the attempted move path
    # I may just modify the OG draw function to add this as a toggle
    
def make_move(board,xs,ys,xt,yt):
    target_filled = False
    #get index of source and target Pieces if no target piece, set them both the same

    # get index of moving piece
    source_index = find_index(board,xs,ys)
    if filled(board,xt,yt): # if theres a piece in the target
        target_index = find_index(board,xt,yt) # get its Index
        target_filled = True

    #remove target from board and store it in case we need it for later 
    if target_filled:
        pass
    else:

        print("HERE 2")
    #move source to targets loc
    board = board + ((xt,yt),board[source_index][1])
    return board

def read_in_move(board,white_turn):
    # Read in move start loc
    #   Check that loc is on board
    #   Check there is a piece at start loc
    #   Check that it is same color as current mover
    # Read in move end loc
    #   Check that loc is on board
    #   There is either no piece or other color at end loc
    #   
    while True:
        # Whose turn is it?
        if white_turn:
            print("It is Whites turn, what piece would you like to move? ")
        else:
            print("It is Blacks turn, what piece would you like to move? ")

        # SOURCE
        # Read in source loc
        xs = int(input("X of source: "))
        ys = int(input("Y of source: "))

        # Checks if source loc is on board
        if (xs or ys) not in [1,2,3,4,5,6,7,8]:
            print(red+"Either Not a number or not on the board, Try again"+reset)
        else:
            print(green+"Start loc input looks good"+reset)
        
        # Compares chosen piece to current mover color
        source = get_piece(board,xs,ys)

        if white_turn and source[0] == "W":
            print(green+"Excellent Selection (White)"+reset)
        elif not white_turn and source[0] == "B":
            print(green+"Excellent Selection (Black)"+reset)
        else:
            print(red+"Bad Selection, piece and mover color are different"+reset)

        # TARGET
        # Read in target loc
        xt = int(input("X of target: "))
        yt = int(input("Y of target: "))
        
        # Checks if target loc is on board
        if (xt or yt) not in [1,2,3,4,5,6,7,8]:
            print(red+"Either Not a number or not on the board, Try again"+reset)
        else:
            print(green+"End loc input looks good"+reset)
        
        # Loops piece selection if it doesn't succeed
        if (xs and ys and xt and yt) in [1,2,3,4,5,6,7,8]:
            # return verified inputs
            print("All inputs valid, returning to main")
            return xs, ys, xt, yt 
        else:
            #try inputs again
            print("Something went wrong, enter your move again")
            enter = input("Press Enter to try another piece")
            os.system('cls') #Clear screen
            draw(board)
