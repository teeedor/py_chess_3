#Third attempt at programming chess in Python

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
from move_sets import get_piece, in_move_set, is_valid_move

def make_board(mode):
    board = []
    if mode == 1:
        #sparsly populated board
        board = [((8,1),("W","K")),((1,8),("B","p")),((6,8),("W","P")),((8,4),("B","h")),
                 ((8,8),("B","r")),
                 ((6,4),("W","B")),((4,6),("B","b")),((5,2),("W","B")),((4,2),("B","b"))]
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
    print(str(y_val) + output)

def draw(board):
    os.system('cls') #Clear screen
    #Draw each horizontal line of the board from top to bottom
    for y in range(8,0,-1):
        #Draw entire y_val line
        draw_line(y, board)
    #Coordinate Marks
    print("  1 2 3 4 5 6 7 8") 

def make_move(board,piece_index,xs,ys,xt,yt):
    #if move is in moveset
    if (in_move_set(board[piece_index][1][1],board[piece_index][1][0],xs,ys,xt,yt)):
        #if move is allowed by board state
        #move is to empty space
        target_piece = get_piece(board,xt,yt)
        source_piece = get_piece(board,xs,ys)

#init Logic
b = make_board(1)
draw(b)
#WORKING ON MAKE_MOVE() and IS_VALID_MOVE() RIGHT NOW
is_valid_move(b,8,8,1,8)
is_valid_move(b,8,8,8,1)
#is_valid_move(b,1,1,1,4)
#is_valid_move(b,1,1,4,1)
