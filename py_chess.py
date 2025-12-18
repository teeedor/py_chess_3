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

red = "\033[91m"
green = "\033[92m"
yellow = "\033[93m"
blue = "\033[94m"
reset = "\033[0m"
VERBOSE = True
#TESTING VALUES
valid, wrong = 0,0

def make_board(mode):
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
    elif mode == 3:
        #Rook Test Board
        board = [((4,4),("W","R")),((6,4),("B","h")),((2,4),("B","b")),((4,6),("B","k")),
                 ((4,2),("B","r")),((2,1),("B","h")),((3,1),("B","b")),((8,1),("B","k"))]
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
    #os.system('cls') #Clear screen
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
#Make Testing Functions
def test_rook():
    global valid, wrong
    #Standard Rook Testing Board
    b1 = [((4,4),("W","R")),
                           ((6,4),("B","h")),((2,4),("B","b")),((4,6),("B","k")),
         ((4,2),("B","r")),((3,5),("B","r"))]
    # first four moves check collision detection
    moves1 = [(4,4,7,4,False),(4,4,4,7,False),(4,4,1,4,False),(4,4,4,1,False),
              # Second Four Moves checking capture
              (4,4,6,4,True),(4,4,4,6,True),(4,4,2,4,True),(4,4,4,2,True),
              # Third 4 Moves checking for moving off the board
              (4,2,9,2,False),(4,2,-2,2,False),(4,2,4,-2,False),(3,5,3,9,False)]
    
    draw(b1)
    loc_valid = 0
    loc_wrong = 0
    for move in moves1:
        xs,ys,xt,yt,expected = move[0], move[1], move[2], move[3], move[4]
        actual = False

        if is_valid_move(b1,xs,ys,xt,yt):             
            if in_move_set("R","W",xs,ys,xt,yt):
                actual = True
            else:
                actual = False
        else:
            actual = False
        # Keeping track of Passed and Failed Tests
        if actual == expected:
            loc_valid += 1
        else:
            loc_wrong += 1

        # check if move is both valid and in moveset
    print(yellow+"Previous Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    valid = valid + loc_valid
    wrong = wrong + loc_wrong
    print(yellow+"Rook Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    print("---------------------------------------")

def test_bishop():
    global valid, wrong
    #Standard Rook Testing Board
    b1 = [((4,4),("W","B")),
                           ((6,6),("B","h")),((6,2),("B","b")),((2,2),("B","k")),
         ((4,2),("B","r")),((2,6),("B","r"))]
    # first four moves check collision detection
    moves1 = [(4,4,7,7,False),(4,4,7,1,False),(4,4,1,1,False),(4,4,1,7,False),
              # Second Four Moves checking capture
              (4,4,6,6,True),(4,4,6,2,True),(4,4,2,2,True),(4,4,2,6,True),
              # Third 4 Moves checking for moving off the board
              (4,4,9,9,False),(4,4,-1,-1,False),(4,4,-1,9,False),(4,4,9,-1,False)]
    
    draw(b1)
    loc_valid = 0
    loc_wrong = 0
    for move in moves1:
        xs,ys,xt,yt,expected = move[0], move[1], move[2], move[3], move[4]
        actual = False

        if in_move_set("B","W",xs,ys,xt,yt):
            if is_valid_move(b1,xs,ys,xt,yt):             
                actual = True
            else:
                actual = False
        else:
            actual = False
        # Keeping track of Passed and Failed Tests
        if actual == expected:
            loc_valid += 1
        else:
            loc_wrong += 1

        # check if move is both valid and in moveset
    print(yellow+"Previous Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    valid = valid + loc_valid
    wrong = wrong + loc_wrong
    print(yellow+"Bishop Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    print("---------------------------------------")

def test_queen():
    global valid, wrong
    #Standard Queen Testing Board
    b1 = [((4,4),("W","Q")),
                           ((6,6),("B","h")),((6,2),("B","b")),((2,2),("B","k")),
         ((4,2),("B","r")),((2,6),("B","r")),((2,4),("B","r")),((4,6),("B","r")),
         ((6,4),("B","r"))]
    # first 4 moves check bishop collision detection
    moves1 = [(4,4,7,7,False),(4,4,7,1,False),(4,4,1,1,False),(4,4,1,7,False),
              # Second Four Moves checking bishop capture
              (4,4,6,6,True),(4,4,6,2,True),(4,4,2,2,True),(4,4,2,6,True),
              # Third 4 Moves checking for moving off the board
              (4,4,9,9,False),(4,4,-1,-1,False),(4,4,-1,9,False),(4,4,9,-1,False),
              # Fourth 4 four moves check rook collision detection
              (4,4,7,4,False),(4,4,4,1,False),(4,4,1,4,False),(4,4,4,7,False),
              # Fifth 4 Moves checking rook capture
              (4,4,6,4,True),(4,4,4,2,True),(4,4,2,4,True),(4,4,4,6,True),
              ]
    
    draw(b1)
    loc_valid = 0
    loc_wrong = 0
    for move in moves1:
        xs,ys,xt,yt,expected = move[0], move[1], move[2], move[3], move[4]
        actual = False

        if in_move_set("Q","W",xs,ys,xt,yt):
            if is_valid_move(b1,xs,ys,xt,yt):             
                actual = True
            else:
                actual = False
        else:
            actual = False
        # Keeping track of Passed and Failed Tests
        if actual == expected:
            loc_valid += 1
        else:
            loc_wrong += 1

        # check if move is both valid and in moveset
    print(yellow+"Previous Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    valid = valid + loc_valid
    wrong = wrong + loc_wrong
    print(yellow+"Queen Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    print("---------------------------------------")

def test_king():
    global valid, wrong
    #Standard King Testing Board
    b1 = [((2,2),("W","K")),
          ((3,2),("B","h")),((1,2),("B","b")),((2,3),("B","k")),((2,1),("B","r")),
          ((1,3),("B","r")),((3,1),("B","r")),((1,1),("B","r")),((3,3),("B","r")),
          ((6,6),("W","K")),
          ((5,6),("W","H")),((5,5),("W","B")),((6,5),("W","K")),((7,5),("W","R")),
          ((7,6),("W","R")),((7,7),("W","R")),((6,7),("W","R")),((5,7),("W","R"))]
    # first 8 moves check correct capture
    moves1 = [(2,2,3,2,True),(2,2,1,2,True),(2,2,2,3,True),(2,2,2,1,True),
              (2,2,1,3,True),(2,2,3,1,True),(2,2,1,1,True),(2,2,3,3,True),
              # second 8 moves check for trying to capture wrong color piece 
              (6,6,7,6,False),(6,6,5,6,False),(6,6,6,7,False),(6,6,6,5,False),
              (6,6,5,7,False),(6,6,7,5,False),(6,6,5,5,False),(6,6,7,7,False),
              # Third 4 moves check for off board input
              (6,6,9,9,False),(6,6,0,0,False),(6,6,9,2,False),(6,6,2,9,False)]

    # Second 8 moves check collision detection
    
    draw(b1)
    loc_valid = 0
    loc_wrong = 0
    for move in moves1:
        xs,ys,xt,yt,expected = move[0], move[1], move[2], move[3], move[4]
        actual = False

        if is_valid_move(b1,xs,ys,xt,yt):             
            if in_move_set("K","W",xs,ys,xt,yt):
                actual = True
            else:
                actual = False
        else:
            actual = False
        # Keeping track of Passed and Failed Tests
        if actual == expected:
            loc_valid += 1
        else:
            loc_wrong += 1

        # check if move is both valid and in moveset
    print(yellow+"Previous Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    valid = valid + loc_valid
    wrong = wrong + loc_wrong
    print(yellow+"King Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    print("---------------------------------------")

def test_knight():
    pass

def test_pawn():
    global valid, wrong
    #Standard Pawn Testing Board
    b1 = [((2,2),("W","P")),((6,2),("W","P")),((3,3),("B","p")),((5,3),("B","p")),
          ((5,6),("W","P")),((6,6),("W","P")),((4,7),("B","p")),((7,7),("B","p"))]
    #  
    moves1 = [(2,2,2,1,False),(2,2,1,2,False),(2,2,3,3,True),(2,2,1,3,True),(2,2,2,4,True),(2,2,2,4,True),
              # second 8 moves check for trying to capture wrong color piece 
              (6,6,7,6,False),(6,6,5,6,False),(6,6,6,7,False),(6,6,6,5,False),
              (6,6,5,7,False),(6,6,7,5,False),(6,6,5,5,False),(6,6,7,7,False),
              # Third 4 moves check for off board input
              (6,6,9,9,False),(6,6,0,0,False),(6,6,9,2,False),(6,6,2,9,False)]

    # Second 8 moves check collision detection
    
    draw(b1)
    loc_valid = 0
    loc_wrong = 0
    for move in moves1:
        xs,ys,xt,yt,expected = move[0], move[1], move[2], move[3], move[4]
        actual = False

        if is_valid_move(b1,xs,ys,xt,yt):             
            if in_move_set("K","W",xs,ys,xt,yt):
                actual = True
            else:
                actual = False
        else:
            actual = False
        # Keeping track of Passed and Failed Tests
        if actual == expected:
            loc_valid += 1
        else:
            loc_wrong += 1

        # check if move is both valid and in moveset
    print(yellow+"Previous Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    valid = valid + loc_valid
    wrong = wrong + loc_wrong
    print(yellow+"Pawn Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)

# Running all test functions
test_rook() # run the tests - WORKING
test_bishop() # run the tests - WORKING
test_queen() # run the tests - WORKING
test_king() # run the tests - WORKING
test_knight() # NOT WRITTEN YET
test_pawn() # NOT WRITTEN YET

# Grand Total PASS / FAIL
print(blue + "---------------------------------------" + reset)
print( green + "GRAND TOTAL PASSED: " + str(valid) + reset )
print( red + "GRAND TOTAL FAILED: " + str(wrong) + reset )
print(blue + "---------------------------------------" + reset)
