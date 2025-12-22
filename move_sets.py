# --- move_sets.py ---
# This file contains the logic to check if a chess move
# is valid both within the standard piece move set 
# and in relation to the current board state
# NEED TO ADD CHECKING FOR MATE FUNCTION
# NEED TO ADD EN PASSANT FUNCTIONALITY
# NEED TO ADD CASTLING FUNCTIONALITY
# NEED TO ADD PAWN UPGRADING

from chess_funcs import get_piece

#Codes for coloring Strings
red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"
VERBOSE = False
VERBOSE_BASIC = True
# get the piece at a location on the given board

# Checks if there is a piece in the way of attempted movement
def is_valid_move(board,xs,ys,xt,yt):
    # Calc dx and dy for all functions
    deltax = xt - xs
    deltay = yt - ys

    # TESTING FLAG
    global VERBOSE
    VERBOSE_NAME = False
    global VERBOSE_BASIC
    empty_target = False
    can_capture = False

    # setting up Variables and objects
    target_piece = get_piece(board,xt,yt)
    source_piece = get_piece(board,xs,ys)
    pcolor = source_piece[0]
    
    # populate p_type Var
    p_type = "Piece"
    if source_piece[1] in ("R","r"): p_type = "Rook"
    if source_piece[1] in ("B","b"): p_type = "Bishop"
    if source_piece[1] in ("Q","q"): p_type = "Queen"
    if source_piece[1] in ("P","p"): p_type = "Pawn"
    if source_piece[1] in ("K","k"): p_type = "King"
    if source_piece[1] in ("H","h"): p_type = "Knight"
    
        
    # Populate "empty_target" and "can_capture" Vars
    if (target_piece == ("N","N")):
        empty_target = True
    else:
        empty_target = False 
        # Compare source and target piece colors
        if target_piece[0] != source_piece[0]:
            # if different, potentially able to capture
            if VERBOSE:
                print(green + "Can Capture!" + reset)
            can_capture = True
        else:
            if VERBOSE:
                print(red + "Cannot Capture :( / Both Pieces are the same color" + reset)
            pass

# --- Check PAWN move Validity ---
    if source_piece[1] == "P" or source_piece[1] == "p":
        if VERBOSE_NAME:
            print("Pawn")
                
        # White Piece = +deltay
        if pcolor == "W" and deltay == 1 and deltax == 0:
            if target_piece != ("N","N"):
                if VERBOSE:
                    print("Piece in the Way!") 
                return False
            else:
                if VERBOSE:
                    print("No Piece in the Way!") 
                return True
        # White Piece first Move Jump
        if pcolor == "W" and ys == 2 and deltay == 2 and deltax == 0:
            if target_piece != ("N","N") or get_piece(board,xt,yt-1) != ("N","N"):
                if VERBOSE:
                    print("Piece in the Way!") 
                return False
            else:
                if VERBOSE:
                    print("No Piece in the Way!") 
                return True

        # Black Piece = -deltay
        if pcolor == "B" and deltay == -1 and deltax == 0:
            if target_piece != ("N","N"):
                if VERBOSE:
                    print("Piece in the Way!") 
                return False
            else:
                if VERBOSE:
                    print("No Piece in the Way!") 
                return True
        # Black Piece first Move Jump
        if pcolor == "B" and ys == 7 and deltay == -2 and deltax == 0:
            if target_piece != ("N","N") or get_piece(board,xt,yt+1) != ("N","N"):
                if VERBOSE:
                    print("Piece in the Way!") 
                return False
            else:
                if VERBOSE:
                    print("No Piece in the Way!") 
                return True

        # Check for diagonal Move in Direction White Pawn
        if pcolor == "W" and deltay == 1 and abs(deltax) == 1 and target_piece[0] == "B":
            if VERBOSE:
                print(green + "White Pawn Can Capture!" + reset) 
            return True
        elif pcolor == "B" and deltay == -1 and abs(deltax) == 1 and target_piece[0] == "W":
            if VERBOSE:
                print(green + "Black Pawn Can Capture!" + reset) 
            return True
        else:
            if VERBOSE:
                print(red + "Pawn Can't Capture!" + reset) 
            return False

# --- Check KNIGHT move Validity ---
    if source_piece[1] == "H" or source_piece[1] == "h":
        if VERBOSE_NAME:
            print("Knight")
        if empty_target == False and can_capture == False:
            if VERBOSE:
                print(str(xt) + "," + str(yt))
            return False
        return True

# --- Check ROOK move Validity ---
    if source_piece[1] == "R" or source_piece[1] == "r":
        if VERBOSE_NAME:
            print("Rook")
        # Vertical Lines
        if deltax == 0: 
            # Positive Movement
            if deltay > 0:
                for i in range(1, deltay):
                    # Piece in the way
                    if get_piece(board,xs,ys+i) != ("N","N"):
                        if VERBOSE:
                            print("Piece in the way at ("+ str(xs) + "," + str(ys+i)+")")
                        return False      
            # Negative Movement
            else:
                for i in range(-1, deltay, -1):
                    # Piece in the way
                    if get_piece(board,xs,ys+i) != ("N","N"):
                        if VERBOSE:
                            print("Piece in the way at ("+ str(xs) + "," + str(ys+i)+")")
                        return False
        # Horizontal Lines
        if deltay == 0:
            # Positive Movement
            if deltax > 0:
                for i in range(1, deltax):
                    # Piece in the way
                    if get_piece(board,xs+i,ys) != ("N","N"):
                        if VERBOSE:
                            print("Piece in the way at ("+ str(xs+i) + "," + str(ys)+")")
                        return False
            # Negative Movement
            else:
                for i in range(-1, deltax,-1):
                    # Piece in the way
                    if get_piece(board,xs+i,ys) != ("N","N"):
                        if VERBOSE:
                            print("Piece in the way at ("+ str(xs+i) + "," + str(ys)+")")
                        return False

        # TESTING OUTPUT
        if VERBOSE:
            print("No piece in the way!")
        if can_capture and empty_target == False:
            if VERBOSE:
                print("Potentially able to capture Target Piece")
            return True
        elif not can_capture and not empty_target:
            if VERBOSE:
                print("Not able to capture Target Piece")
            return False
        elif empty_target:
            if VERBOSE:
                print("No Piece at Target")
            return True

# --- Check BISHOP move Validity ---
    if source_piece[1] == "B" or source_piece[1] == "b":
        if VERBOSE_NAME:
            print("Bishop")
        # POS X and POS Y
        if deltax > 0:
            if deltay > 0:
               for i in range(1, deltay):
                    # Piece in the way
                    if get_piece(board,xs+i,ys+i) != ("N","N"):
                        if VERBOSE:
                            print("Piece in the way ("+ str(xs+i) + "," + str(ys+i)+")")
                        return False      
        # POS X and NEG Y
            else: 
                for i in range(1, deltax):
                    # Piece in the way
                    if get_piece(board,xs+i,ys-i) != ("N","N"):
                        if VERBOSE:
                            print("Piece in the way ("+ str(xs+i) + "," + str(ys-i)+")")
                        return False      
        # NEG X and POS Y
        else:
            if deltay > 0:
                for i in range(1, deltay):
                    # Piece in the way
                    if get_piece(board,xs-i,ys+i) != ("N","N"):
                        if VERBOSE:
                            print("Piece in the way ("+ str(xs-i) + "," + str(ys+i)+")")
                        return False      
        # NEG X and NEG Y
            else:
                for i in range(1, abs(deltax)):
                    # Piece in the way
                    if get_piece(board,xs-i,ys-i) != ("N","N"):
                        if VERBOSE:
                            print("Piece in the way ("+ str(xs-i) + "," + str(ys-i)+")")
                        return False      

        # TESTING OUTPUT
        if VERBOSE:
            print("No piece in the way!")
        if can_capture and empty_target == False:
            if VERBOSE:
                print("Potentially able to capture Target Piece")
            return True
        elif not can_capture and not empty_target:
            if VERBOSE:
                print("Not able to capture Target Piece")
            return False
        elif empty_target:
            if VERBOSE:
                print("No Piece at Target")
            return True

# --- Check QUEEN move Validity ---
    if source_piece[1] == "Q" or source_piece[1] == "q":
        if VERBOSE_NAME:
            print("Queen")
        # Rook Movement
        if deltax == 0 or deltay == 0: 
            # Vertical Lines
            if deltax == 0: 
                # Positive Movement
                if deltay > 0: 
                    for i in range(1, deltay):
                        # Piece in the way
                        if get_piece(board,xs,ys+i) != ("N","N"):
                            if VERBOSE:
                                print("Piece in the way at ("+ str(xs) + "," + str(ys+i)+")")
                            return False      
                # Negative Movement
                else: 
                    for i in range(-1, deltay, -1):
                        # Piece in the way
                        if get_piece(board,xs,ys+i) != ("N","N"):
                            if VERBOSE:
                                print("Piece in the way at ("+ str(xs) + "," + str(ys+i)+")")
                            return False

            # Horizontal Lines
            if deltay == 0: 
                # Positive Movement
                if deltax > 0: 
                    for i in range(1, deltax):
                        # Piece in the way
                        if get_piece(board,xs+i,ys) != ("N","N"):
                            if VERBOSE:
                                print("Piece in the way at ("+ str(xs+i) + "," + str(ys)+")")
                            return False
                # Negative Movement
                else: 
                    for i in range(-1, deltax,-1):
                        # Piece in the way
                        if get_piece(board,xs+i,ys) != ("N","N"):
                            if VERBOSE:
                                print("Piece in the way at ("+ str(xs+i) + "," + str(ys)+")")
                            return False
        # Bishop Movement
        else: 
            # POS X and POS Y
            if deltax > 0:
                if deltay > 0: 
                   for i in range(1, deltay):
                        # Piece in the way
                        if get_piece(board,xs+i,ys+i) != ("N","N"):
                            if VERBOSE:
                                print("Piece in the way ("+ str(xs+i) + "," + str(ys+i)+")")
                            return False      
            # POS X and NEG Y
                else: 
                    for i in range(1, deltax):
                        # Piece in the way
                        if get_piece(board,xs+i,ys-i) != ("N","N"):
                            if VERBOSE:
                                print("Piece in the way ("+ str(xs+i) + "," + str(ys-i)+")")
                            return False      
            # NEG X and POS Y
            else:
                if deltay > 0: 
                    for i in range(1, deltay):
                        # Piece in the way
                        if get_piece(board,xs-i,ys+i) != ("N","N"):
                            if VERBOSE:
                                print("Piece in the way ("+ str(xs-i) + "," + str(ys+i)+")")
                            return False      
            # NEG X and NEG Y
                else: 
                    for i in range(1, abs(deltax)):
                        # Piece in the way
                        if get_piece(board,xs-i,ys-i) != ("N","N"):
                            if VERBOSE:
                                print("Piece in the way ("+ str(xs-i) + "," + str(ys-i)+")")
                            return False      

        # TESTING OUTPUT
        if VERBOSE:
            print("No piece in the way!")
        if can_capture and empty_target == False:
            if VERBOSE:
                print("Able to capture Target Piece")
            return True
        elif not can_capture and not empty_target:
            if VERBOSE:
                print("Not able to capture Target Piece")
            return False
        elif empty_target:
            if VERBOSE:
                print("No Piece at Target")
            return True

# --- Check KING move Validity ---
    if source_piece[1] == "K" or source_piece[1] == "k":
        if VERBOSE_NAME:
            print("King")
        if empty_target == False and can_capture == False:
            return False

        # TESTING OUTPUT
        if VERBOSE:
            print("No piece in the way!")
        if can_capture and empty_target == False:
            if VERBOSE:
                print("Able to capture Target Piece")
            return True
        elif not can_capture and not empty_target:
            if VERBOSE:
                print("Not able to capture Target Piece")
            return False
        elif empty_target:
            if VERBOSE:
                print("No Piece at Target")
            return True

# Checks if the attempted move is allowed by the piece
def in_move_set(ptype,pcolor,xs,ys,xt,yt):
    # Calculate dx and dy
    deltax = xt - xs
    deltay = yt - ys

    # TESTING FLAG
    global VERBOSE 
    global VERBOSE_BASIC
    
    # Basic Movement attempt notification
    if VERBOSE_BASIC:
        print("--- "+ ptype +" moving from ("+ str(xs) +","+ str(ys) +
              ") to ("+ str(xt) +","+ str(yt) +") ---")

    # Check if the input values are on the board
    if (xs > 8 or ys > 8 or xt > 8 or yt > 8) or (xs < 1 or ys < 1 or xt < 1 or yt < 1):
        if VERBOSE:
            print(red + "These values are not on the board, try a different move." + reset)
        return False
    
# --- Check PAWN move set ---
    if ptype == "P" or ptype == "p" or ptype == "Pawn":
        # White Piece 1 space forward move 
        if pcolor == "W" and deltay == 1 and deltax == 0:
            if VERBOSE:
                print("Valid Move!") 
            return True
        # White Piece 2 space forward move
        if pcolor == "W" and ys == 2 and deltay == 2 and deltax == 0:
            if VERBOSE:
                print("Valid Move!") 
            return True
        # Black Piece 1 space forward move 
        if pcolor == "B" and deltay == -1 and deltax == 0:
            if VERBOSE:
                print("Valid Move!") 
            return True
        # Black Piece 2 space forward move
        if pcolor == "B" and ys == 7 and deltay == -2 and deltax == 0:
            if VERBOSE:
                print("Valid Move!") 
            return True
        # White Diagonal Move / Capture 
        if pcolor == "W" and deltay == 1 and abs(deltax) == 1:
            if VERBOSE:
                print("Valid Capture Move!") 
            return True
        # Black Diagonal Move / Capture 
        if pcolor == "B" and deltay == -1 and abs(deltax) == 1:
            if VERBOSE:
                print("Valid Capture Move!") 
            return True

# --- Check ROOK move set ---
    if ptype == "R" or ptype == "r" or ptype == "Rook":
        # If either delta is 0, movement must be in a line
        if (deltax == 0 or deltay == 0):
            if VERBOSE:
                print("Valid Move!") 
            return True

# --- Check BISHOP move set ---
    if ptype == "B" or ptype == "b" or ptype == "Bishop":
        # If both Deltas are equal, must be a diagonal
        if abs(deltax) == abs(deltay):
            if VERBOSE:
                print("Valid Move!") 
            return True

# --- Check KNIGHT move set ---
    if ptype == "H" or ptype == "h" or ptype == "Knight":
        # Check for L movement
        if (abs(deltax) == 2 and abs(deltay) == 1) or (abs(deltax) == 1 and abs(deltay) == 2):
            if VERBOSE:
                print("Valid Move!") 
            return True

# --- Check QUEEN move set ---
    if ptype == "Q" or ptype == "q" or ptype == "Queen":
        #Rook Movement
        if (deltax == 0 or deltay == 0):
            if VERBOSE:
                print("Valid Move!") 
            return True
        #Bishop Movement
        if abs(deltax) == abs(deltay):
            if VERBOSE:
                print("Valid Move!") 
            return True

# --- Check KING move set ---
    if ptype == "K" or ptype == "k" or ptype == "King":
        # X Movement
        if abs(deltax) == 1 and abs(deltay) == 0:
            if VERBOSE:
                print("Valid Move!") 
            return True
        # Y Movement
        if abs(deltax) == 0 and abs(deltay) == 1:
            if VERBOSE:
                print("Valid Move!") 
            return True
        # Diagonal
        if abs(deltax) == 1 and abs(deltay) == 1:
            if VERBOSE:
                print("Valid Move!") 
            return True

    # Missed all valid move types
    if VERBOSE:
        print("Not Valid Move :'( / End of move_sets.py File")
    return False
