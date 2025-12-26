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

#def draw_move_path(board,xs,ys,xt,yt):
    # this function does the same as the draw function,
    # but it will add a red path over the attempted move path
    # I may just modify the OG draw function to add this as a toggle
    
def make_move(board,piece_index,xs,ys,xt,yt):
    #if move is in moveset
    if (in_move_set(board[piece_index][1][1],board[piece_index][1][0],xs,ys,xt,yt)):
        #if move is allowed by board state
        #move is to empty space
        target_piece = get_piece(board,xt,yt)
        source_piece = get_piece(board,xs,ys)

def read_in_move(board,white_turn):
    while True:
        if white_turn:
            print("It is Whites turn, where would you like to move? ")
        else:
            print("It is Blacks turn, where would you like to move? ")

        # Checks if player turn and piece being moved are same color
        while True:
            try:
                xs = int(input("X of source: "))
                ys = int(input("Y of source: "))
            except ValueError:
                print(red+"That is not a number"+reset)
                break # Doesn't work as expected

            source = get_piece(board,xs,ys)
            if white_turn and source[0] == "W":
                print(green+"Excellent Selection"+reset)
                break 
            elif not white_turn and source[0] == "B":
                print(green+"Excellent Selection"+reset)
                break
            elif xs < 1 or xs > 8 or ys < 1 or ys > 8:
                print(red+"Choice is not on the board, Please Choose again"+reset)
            else:
                print(red+"First Piece Choice is invalid, Please Choose again"+reset)

        # checks if target is on the board
        while True:
            try:
                xt = int(input("X of target: "))
                yt = int(input("Y of target: "))
            except ValueError:
                print(red+"That is not a number"+reset)
                break # Doesn't work as expected

            if xt < 1 or xt > 8 or yt < 1 or yt > 8: 
                print(red+"Choice is not on the board, Please Choose again"+reset)

        # return verified inputs
        return xs, ys, xt, yt 
