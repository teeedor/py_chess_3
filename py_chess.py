#Third attempt at programming chess in Python
#design document created
#do not program anything that has not been fully designed

#pieces are stored in a 2d array
#the draw() function iterates through this array and draws the current board

#white goes first
#game asks player for move
#checks if is validmove based on moveset
#checks if is validmove based on current board state
    #this includes a piece being on the move target
    #or a piece being in the way of the move target

#Basic Movesets for pieces
#pawn: move one space in color direction, except if first move. can capture diagonal. are transformed when getting to end of board
#Rook: moves in straight lines, can Castle
#Knight: Moves in L's, easiest of the high value pieces to program
#bishops: move in diagonals
#Queen: combo of Rook and Bishop Movement
#King: Need to constantly check if the king is in peril

#Scoreboard that keeps track of captured piece values

import os # to clear the screen
from move_sets import get_piece

def make_board(mode):
    board = []
    if mode == 1:
        #sparsly populated board
        board = [((3,4),("W","K")),((7,2),("B","p")),((2,2),("W","P")),((7,1),("B","h"))]
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
    output = "" #starts empty
    for x_val in range(1,9):
        #x_val, y_val
        #for every x value in the line
        #if that x,y loc is in the board list, then put the piece in the output string
        for piece in board:
            if piece[0][0] == x_val and piece[0][1] == y_val:
                string = " " + piece[1][1]
                break # can only be one piece at location, so break out of loop
                #if there is a piece at the current board location
            else:
                #if there is no piece at board location
                if (x_val % 2 + y_val) % 2 == 1:
                    string = " #"
                else:
                    string = "  "
    #after the entire loop, Draw the String
        output += string
    print(str(y_val) + output)

def draw(board):
    #Clear screen
    os.system('cls')
    #loop through the 2d board and print a piece if there is one at that location
    for y in range(8,0,-1):
        draw_line(y, board) #draw entire y line
    #entire board is drawn, maybe add white and black labels?
    print("  1 2 3 4 5 6 7 8") 

board = make_board(1)
draw(board)
print(get_piece(board,3,4))
