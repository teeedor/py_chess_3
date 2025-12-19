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

def make_move(board,piece_index,xs,ys,xt,yt):
    #if move is in moveset
    if (in_move_set(board[piece_index][1][1],board[piece_index][1][0],xs,ys,xt,yt)):
        #if move is allowed by board state
        #move is to empty space
        target_piece = get_piece(board,xt,yt)
        source_piece = get_piece(board,xs,ys)

#--- TESTS ---
def test_pawn():
    global valid, wrong, VERBOSE
    ptype = "Pawn"
    #Standard Pawn Testing Board
    b1 = [((2,2),("W","P")),((6,2),("W","P")),((3,3),("B","p")),((5,3),("B","p")),
          ((5,6),("W","P")),((6,6),("W","P")),((4,7),("B","p")),((7,7),("B","p")),
          ((8,2),("W","P")),((8,3),("B","p")),((1,7),("W","P")),((1,6),("B","p")),]

              # Wpawn 1 moves 
    moves1 = [(2,2,2,1,False),(2,2,1,2,False),(2,2,3,3,True),(2,2,1,3,False),(2,2,2,3,True),(2,2,2,4,True),
              # Wpawn 2 moves
              (6,2,6,1,False),(6,2,7,2,False),(6,2,7,3,False),(6,2,6,3,True),(6,2,6,4,True),(6,2,5,3,True),
              # Bpawn 1 moves
              (4,7,4,8,False),(4,7,3,7,False),(4,7,3,6,False),(4,7,4,6,True),(4,7,4,5,True),(4,7,5,6,True),
              # Bpawn 2 moves
              (7,7,7,8,False),(7,7,8,7,False),(7,7,8,6,False),(7,7,7,6,True),(7,7,7,5,True),(7,7,6,6,True),
              # Wpawn 3 moves
              (8,2,8,3,False),(8,2,8,4,False),
              # Bpawn 3 moves
              (1,7,1,6,False),(1,7,1,5,False)]
    
    draw(b1)
    loc_valid = 0
    loc_wrong = 0
    for move in moves1:
        xs,ys,xt,yt,expected = move[0], move[1], move[2], move[3], move[4]
        pcolor = get_piece(b1, xs, ys)[0]
        actual = False

        if in_move_set(ptype,pcolor,xs,ys,xt,yt):             
            if is_valid_move(b1,xs,ys,xt,yt):
                if VERBOSE:
                    actual = True
                    print(green+"GOOD MOVE"+reset)
            else:
                if VERBOSE:
                    actual = False
                    print(red+"BAD MOVE"+reset)
        else:
            if VERBOSE:
                actual = False
                print(red+"BAD MOVE"+reset)
        # Keeping track of Passed and Failed Tests
        if actual == expected:
            loc_valid += 1
        else:
            loc_wrong += 1

        # check if move is both valid and in moveset
    print(yellow+"Previous Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    print(yellow+"Pawn Tests "+green+"\tPassed: "+str(loc_valid)+yellow+" / "+red+"Failed: "+str(loc_wrong)+reset)
    print("---------------------------------------")
    valid = valid + loc_valid
    wrong = wrong + loc_wrong

def test_knight():
    global valid, wrong, VERBOSE
    ptype = "Knight"
    #standard knight testing board
    b1 = [((3,3),("W","H")),
          ((2,1),("W","H")),((4,1),("W","H")),((1,4),("W","H")),((5,4),("W","H")),
          ((1,2),("B","h")),((5,2),("B","h")),((2,5),("B","h")),((4,5),("B","h")),
          ((6,7),("W","H"))]

              # First four moves check collision detection
    moves1 = [(3,3,2,1,False),(3,3,1,2,True),(3,3,1,4,False),(3,3,2,5,True),
              # Second four moves check capture 
              (3,3,4,5,True),(3,3,5,4,False),(3,3,5,2,True),(3,3,4,1,False),
              # Next six moves check normal movement 
              (6,7,5,5,True),(6,7,4,6,True),(6,7,4,8,True),(6,7,8,8,True),(6,7,8,6,True),(6,7,7,5,True),
              # Next two moves check offboard move 
              (6,7,5,9,False),(6,7,7,9,False)]
              
    
    draw(b1)
    loc_valid = 0
    loc_wrong = 0
    for move in moves1:
        xs,ys,xt,yt,expected = move[0], move[1], move[2], move[3], move[4]
        pcolor = get_piece(b1, xs, ys)[0]
        actual = False

        if in_move_set(ptype,pcolor,xs,ys,xt,yt):             
            if is_valid_move(b1,xs,ys,xt,yt):
                if VERBOSE:
                    actual = True
                    print(green+"GOOD MOVE"+reset)
            else:
                if VERBOSE:
                    actual = False
                    print(red+"BAD MOVE"+reset)
        else:
            if VERBOSE:
                actual = False
                print(red+"BAD MOVE"+reset)
        # keeping track of passed and failed tests
        if actual == expected:
            loc_valid += 1
        else:
            loc_wrong += 1
            print(red+"!!!TEST NOT RETURNING WHAT IS EXPECTED!!!"+reset)

        # check if move is both valid and in moveset
    print(yellow+"Previous Tests "+green+"\tpassed: "+str(valid)+yellow+" / "+red+"failed: "+str(wrong)+reset)
    print(yellow+"Knight Tests "+green+"\tpassed: "+str(loc_valid)+yellow+" / "+red+"failed: "+str(loc_wrong)+reset)
    print("---------------------------------------")
    valid = valid + loc_valid
    wrong = wrong + loc_wrong

def test_rook():
    global valid, wrong, VERBOSE
    ptype = "Rook"
    #standard rook testing board
    b1 = [((4,4),("w","r")),
                           ((6,4),("b","h")),((2,4),("b","b")),((4,6),("b","k")),
         ((4,2),("b","r")),((3,5),("b","r"))]
    # first four moves check collision detection
    moves1 = [(4,4,7,4,False),(4,4,4,7,False),(4,4,1,4,False),(4,4,4,1,False),
              # second four moves checking capture
              (4,4,6,4,True),(4,4,4,6,True),(4,4,2,4,True),(4,4,4,2,True),
              # third 4 moves checking for moving off the board
              (4,2,9,2,False),(4,2,-2,2,False),(4,2,4,-2,False),(3,5,3,9,False)]
    
    draw(b1)
    loc_valid = 0
    loc_wrong = 0
    for move in moves1:
        xs,ys,xt,yt,expected = move[0], move[1], move[2], move[3], move[4]
        pcolor = get_piece(b1, xs, ys)[0]
        actual = False

        if in_move_set(ptype,pcolor,xs,ys,xt,yt):             
            if is_valid_move(b1,xs,ys,xt,yt):
                if VERBOSE:
                    actual = True
                    print(green+"GOOD MOVE"+reset)
            else:
                if VERBOSE:
                    actual = False
                    print(red+"BAD MOVE"+reset)
        else:
            if VERBOSE:
                actual = False
                print(red+"BAD MOVE"+reset)
        # keeping track of passed and failed tests
        if actual == expected:
            loc_valid += 1
        else:
            loc_wrong += 1

        # check if move is both valid and in moveset
    print(yellow+"Previous Tests "+green+"\tpassed: "+str(valid)+yellow+" / "+red+"failed: "+str(wrong)+reset)
    print(yellow+"Rook Tests "+green+"\tpassed: "+str(loc_valid)+yellow+" / "+red+"failed: "+str(loc_wrong)+reset)
    print("---------------------------------------")
    valid = valid + loc_valid
    wrong = wrong + loc_wrong

def test_bishop():
    global valid, wrong, VERBOSE
    ptype = "Bishop"
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

        if in_move_set(ptype,"W",xs,ys,xt,yt):
            if is_valid_move(b1,xs,ys,xt,yt):             
                if VERBOSE:
                    actual = True
                    print(green+"GOOD MOVE"+reset)
            else:
                if VERBOSE:
                    actual = False
                    print(red+"BAD MOVE"+reset)
        else:
            if VERBOSE:
                actual = False
                print(red+"BAD MOVE"+reset)
        # Keeping track of Passed and Failed Tests
        if actual == expected:
            loc_valid += 1
        else:
            loc_wrong += 1

        # check if move is both valid and in moveset
    print(yellow+"Previous Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    print(yellow+"Bishop Tests "+green+"\tPassed: "+str(loc_valid)+yellow+" / "+red+"Failed: "+str(loc_wrong)+reset)
    print("---------------------------------------")
    valid = valid + loc_valid
    wrong = wrong + loc_wrong

def test_queen():
    global valid, wrong, VERBOSE
    ptype = "Queen"
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

        if in_move_set(ptype,"W",xs,ys,xt,yt):
            if is_valid_move(b1,xs,ys,xt,yt):             
                if VERBOSE:
                    actual = True
                    print(green+"GOOD MOVE"+reset)
            else:
                if VERBOSE:
                    actual = False
                    print(red+"BAD MOVE"+reset)
        else:
            if VERBOSE:
                actual = False
                print(red+"BAD MOVE"+reset)
        # Keeping track of Passed and Failed Tests
        if actual == expected:
            loc_valid += 1
        else:
            loc_wrong += 1

        # check if move is both valid and in moveset
    print(yellow+"Previous Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    print(yellow+"Queen Tests "+green+"\tPassed: "+str(loc_valid)+yellow+" / "+red+"Failed: "+str(loc_wrong)+reset)
    print("---------------------------------------")
    valid = valid + loc_valid
    wrong = wrong + loc_wrong

def test_king():
    global valid, wrong, VERBOSE
    ptype = "King"
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

    draw(b1)
    loc_valid = 0
    loc_wrong = 0
    for move in moves1:
        xs,ys,xt,yt,expected = move[0], move[1], move[2], move[3], move[4]
        pcolor = get_piece(b1, xs, ys)[0]
        actual = False

        if in_move_set(ptype,pcolor,xs,ys,xt,yt):             
            if is_valid_move(b1,xs,ys,xt,yt):
                if VERBOSE:
                    actual = True
                    print(green+"GOOD MOVE"+reset)
            else:
                if VERBOSE:
                    actual = False
                    print(red+"BAD MOVE"+reset)
        else:
            if VERBOSE:
                actual = False
                print(red+"BAD MOVE"+reset)
        # Keeping track of Passed and Failed Tests
        if actual == expected:
            loc_valid += 1
        else:
            loc_wrong += 1
            print(red+"!!!---NOT EXPECTED TEST RESULT---!!!"+reset)

        # check if move is both valid and in moveset
    print(yellow+"Previous Tests "+green+"\tPassed: "+str(valid)+yellow+" / "+red+"Failed: "+str(wrong)+reset)
    print(yellow+"King Tests "+green+"\tPassed: "+str(loc_valid)+yellow+" / "+red+"Failed: "+str(loc_wrong)+reset)
    valid = valid + loc_valid
    wrong = wrong + loc_wrong

def run_tests():
    global valid, wrong
    # Running all test functions
    test_pawn() # Written - WORKING
    test_knight() # Written - WORKING
    test_rook() # Written - WORKING
    test_bishop() # Written - WORKING
    test_queen() # Written - WORKING
    test_king() # Written - WORKING

    # Grand Total PASS / FAIL
    print(blue + "---------------------------------------" + reset)
    print( green + "GRAND TOTAL PASSED: " + str(valid) + reset )
    print( red + "GRAND TOTAL FAILED: " + str(wrong) + reset )
    print(blue + "---------------------------------------" + reset)

run_tests()
