#this file will have all move set related functions

#piece in the way?
#is_valid_move?
#function to get the color and type of a location

red = "\033[91m"
green = "\033[92m"
reset = "\033[0m"

def get_piece(board,x,y):
    #iterate through piece list and figure out if there is a piece there
    for piece in board:
        #print(str(piece[0][0]) + ", " + str(piece[0][1]))
        if piece[0][0] == x and piece[0][1] == y: 
            #return color and type
            output = (piece[1][0],piece[1][1])
            break
        else:
            output = ("N","N")
    return output

def is_valid_move(board,xs,ys,xt,yt):
    VERBOSE = True
    #checks if the move is valid based on board state
    empty_target = False
    can_capture = False
    #checks if there is a piece in target location
    target_piece = get_piece(board,xt,yt)
    source_piece = get_piece(board,xs,ys)
    p_type = "Rook" if (source_piece[1] == "R" or source_piece[1] == "r") else "Piece"
    p_type = "Bishop" if (source_piece[1] == "B" or source_piece[1] == "b") else "Piece"
    p_type = "Queen" if (source_piece[1] == "Q" or source_piece[1] == "q") else "Piece"
    p_type = "Pawn" if (source_piece[1] == "P" or source_piece[1] == "p") else "Piece"
    p_type = "King" if (source_piece[1] == "K" or source_piece[1] == "k") else "Piece"
    p_type = "Knight" if (source_piece[1] == "H" or source_piece[1] == "h") else "Piece"
    if VERBOSE:
        print("--- "+ p_type +" moving from ("+ str(xs) +","+ str(ys) +
              ") to ("+ str(xt) +","+ str(yt) +") ---")
    if (target_piece == ("N","N")):
        empty_target = True
    else:
        empty_target = False 
        #if pieces are different colors
        if target_piece[0] != source_piece[0]:
            #able to capture
            if VERBOSE:
                print(green + "Can Capture!" + reset)
            can_capture = True
        else:
            if VERBOSE:
                print("Cannot Capture :(")
            pass
#BEGIN KNIGHT
    if source_piece[1] == "H" or source_piece[1] == "h":
        #knight Exception, can jump
        if VERBOSE:
            print("Knight")
        if not empty_target and not can_capture:
            if VERBOSE:
                print("Target piece is same color")
                print(str(xt) + "," + str(yt))
                print("Return False")
            return False
        return True
#END KNIGHT
#BEGIN ROOK
    if source_piece[1] == "R" or source_piece[1] == "r":
        #Rook, look for something in the way 
        deltax = xt - xs
        deltay = yt - ys
        if VERBOSE:
            # print("Rook is trying to move")
            pass
        if deltax == 0: # Vertical Lines
            if deltay > 0: # positive movement
                #regular movement
                for i in range(1, deltay):
                    if get_piece(board,xs,ys+i) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way at ("+ str(xs) + "," + str(ys+i)+")")
                        return False      
            else: # negative movement BROKEN
                for i in range(-1, deltay, -1):
                    if get_piece(board,xs,ys+i) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way at ("+ str(xs) + "," + str(ys+i)+")")
                           # print("Return False")
                        return False

        if deltay == 0: # Horizontal Lines
            if deltax > 0: # positive movement
                #regular movement
                for i in range(1, deltax):
                    if get_piece(board,xs+i,ys) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way at ("+ str(xs+i) + "," + str(ys)+")")
                           # print("Return False")
                        return False
            else: # negative movement BROKEN
                for i in range(-1, deltax,-1):
                    if get_piece(board,xs+i,ys) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way at ("+ str(xs+i) + "," + str(ys)+")")
                           # print("Return False")
                        return False
        if VERBOSE:
            print("No piece in the way!")
        if can_capture and not empty_target:
            if VERBOSE:
                pass
            #   print("There is a piece at the target that I can Capture")
            #   print("Return True")
            return True
        elif not can_capture and not empty_target:
            if VERBOSE:
                pass
            #    print("Return False")
            return False
        elif empty_target:
            if VERBOSE:
                pass
            #    print("Return True")
            return True
#END ROOK
#BEGIN BISHOP 
    if source_piece[1] == "B" or source_piece[1] == "b":
        #check for all four possible cases of Bishop Movement
        deltax = xt - xs
        deltay = yt - ys
        if deltax > 0:
            if deltay > 0: # pos x pos y
               for i in range(1, deltay):
                    if get_piece(board,xs+i,ys+i) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way ("+ str(xs+i) + "," + str(ys+i)+")")
                        return False      
            else: # pos x neg y
                for i in range(1, deltax):
                    if get_piece(board,xs+i,ys-i) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way ("+ str(xs+i) + "," + str(ys-i)+")")
                        return False      
        else:
            if deltay > 0: # neg x pos y
                for i in range(1, deltay):
                    if get_piece(board,xs-i,ys+i) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way ("+ str(xs-i) + "," + str(ys+i)+")")
                        return False      
            else: # neg x neg y
                for i in range(1, abs(deltax)):
                    if get_piece(board,xs-i,ys-i) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way ("+ str(xs-i) + "," + str(ys-i)+")")
                        return False      
        if VERBOSE:
            print("Bishop")
        if VERBOSE:
            print("No piece in the way!")
        if can_capture and not empty_target:
            if VERBOSE:
                pass
            #   print("There is a piece at the target that I can Capture")
            #   print("Return True")
            return True
        elif not can_capture and not empty_target:
            if VERBOSE:
                pass
            #    print("Return False")
            return False
        elif empty_target:
            if VERBOSE:
                pass
            #    print("Return True")
            return True


#END BISHOP         
        #return True
        #checks if can capture based on color 
        #checks if something is in the way of movement for pieces
        #only checks if the piece can make that move, regardless of board
        #input: start loc and target loc

def in_move_set(ptype,pcolor,xs,ys,xt,yt):
    VERBOSE = False
    #Check if the input values are valid
    if (xs > 8 or ys > 8 or xt > 8 or yt > 8) or (xs < 1 or ys < 1 or xt < 1 or yt < 1):
        print(red + "These values are not on the board, try a different move." + reset)
        return False
    #testing print statements
    if VERBOSE:
        print(ptype + " is trying to move from (" + str(xs) + ", " + str(ys) +
            ") to (" + str(xt) + ", " + str(yt) + ")")

    deltax = xt - xs
    deltay = yt - ys

    #PAWN
    if ptype == "P" or ptype == "p":
        #get pieces color
        #if white, pawn moves in positive y, black moves in negative y
        #if piece is on homerow, allow for big first move
        #also need to factor in Capture movement
        print("PAWN")

    #ROOK BASIC MOVESET COMPLETE
    if ptype == "R" or ptype == "r":
                #if one of the deltas is 0, then it has to be in a line
        if (deltax == 0 or deltay == 0):
            if VERBOSE:
                print("Valid Move!") 
            return True

    #BISHOP BASIC MOVESET COMPLETE
    if ptype == "B" or ptype == "b":
        if abs(deltax) == abs(deltay):
            if VERBOSE:
                print("Valid Move!") 
            return True


    #KNIGHT BASIC MOVESET COMPLETE
    if ptype == "H" or ptype == "h":
        if (abs(deltax) == 2 and abs(deltay) == 1) or (abs(deltax) == 1 and abs(deltay) == 2):
            if VERBOSE:
                print("Valid Move!") 
                return True

    #QUEEN
    if ptype == "Q" or ptype == "q":
        print("QUEEN")
        #combine Bishop and rook movesets
    #KING
    if ptype == "K" or ptype == "k":
        print("KING")  

    print("Not Valid Move :'(")
