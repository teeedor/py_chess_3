#this file will have all move set related functions

#Codes for coloring Strings
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
    deltax = xt - xs
    deltay = yt - ys

    #checks if the move is valid based on board state
    VERBOSE = True
    empty_target = False
    can_capture = False
    #checks if there is a piece in target location
    target_piece = get_piece(board,xt,yt)
    source_piece = get_piece(board,xs,ys)
    p_type = "Piece"
    pcolor = source_piece[0]
    if source_piece[1] in ("R","r"): p_type = "Rook"
    if source_piece[1] in ("B","b"): p_type = "Bishop"
    if source_piece[1] in ("Q","q"): p_type = "Queen"
    if source_piece[1] in ("P","p"): p_type = "Pawn"
    if source_piece[1] in ("K","k"): p_type = "King"
    if source_piece[1] in ("H","h"): p_type = "Knight"
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
                print(red + "Cannot Capture :(" + reset)
            pass
#BEGIN PAWN
    if source_piece[1] == "P" or source_piece[1] == "p":
        if VERBOSE:
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
            #looksright#print(str(target_piece)+" , "+str(get_piece(board,xt,yt-1)))
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
        #print(str(pcolor)+" , "+str(deltay)+" , "+str(abs(deltax))+" , "+str(target_piece[0]))
        if pcolor == "W" and deltay == 1 and abs(deltax) == 1 and target_piece[0] == "B":
            if VERBOSE:
                print(green + "Pawn Can Capture!" + reset) 
            return True
        elif pcolor == "B" and deltay == -1 and abs(deltax) == 1 and target_piece[0] == "W":
            if VERBOSE:
                print(green + "Pawn Can Capture!" + reset) 
            return True
        else:
            if VERBOSE:
                print(red + "Pawn Can't Capture!" + reset) 
            return False

        # Check for diagonal Move in Direction Black Pawn
        #print(str(pcolor)+" , "+str(deltay)+" , "+str(abs(deltax))+" , "+str(target_piece[0]))
#END PAWN
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
        if VERBOSE:
            print("Rook is trying to move")
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
               # pass
                print("There is a piece at the target that I can Capture")
                print("Return True")
            return True
        elif not can_capture and not empty_target:
            if VERBOSE:
            #    pass
                print("Return False")
            return False
        elif empty_target:
            if VERBOSE:
               # pass
                print("Return True")
            return True
#END ROOK
#BEGIN BISHOP 
    if source_piece[1] == "B" or source_piece[1] == "b":
        #check for all four possible cases of Bishop Movement
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
            print("No piece in the way!")
        if can_capture and not empty_target:
            if VERBOSE:
               # pass
               print("There is a piece at the target that I can Capture")
               print("Return True")
            return True
        elif not can_capture and not empty_target:
            if VERBOSE:
                #pass
                print("Return False")
            return False
        elif empty_target:
            if VERBOSE:
              #  pass
                print("Return True")
            return True
#END BISHOP         
#BEGIN QUEEN
    if source_piece[1] == "Q" or source_piece[1] == "q":
        #check for all four possible cases of Bishop Movement
        if deltax == 0 or deltay == 0: # Rook Movement
            if deltax == 0: # Vertical Lines
                if deltay > 0: # positive movement
                    #regular movement
                    for i in range(1, deltay):
                        if get_piece(board,xs,ys+i) != ("N","N"):
                            #piece in the way
                            if VERBOSE:
                                print("Piece in the way at ("+ str(xs) + "," + str(ys+i)+")")
                            return False      
                else: # negative movement
                    for i in range(-1, deltay, -1):
                        if get_piece(board,xs,ys+i) != ("N","N"):
                            #piece in the way
                            if VERBOSE:
                                print("Piece in the way at ("+ str(xs) + "," + str(ys+i)+")")
                            return False

            if deltay == 0: # Horizontal Lines
                if deltax > 0: # positive movement
                    #regular movement
                    for i in range(1, deltax):
                        if get_piece(board,xs+i,ys) != ("N","N"):
                            #piece in the way
                            if VERBOSE:
                                print("Piece in the way at ("+ str(xs+i) + "," + str(ys)+")")
                            return False
                else: # negative movement
                    for i in range(-1, deltax,-1):
                        if get_piece(board,xs+i,ys) != ("N","N"):
                            #piece in the way
                            if VERBOSE:
                                print("Piece in the way at ("+ str(xs+i) + "," + str(ys)+")")
                            return False

        else: # Bishop Movement
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
            print("No piece in the way!")
        if can_capture and not empty_target:
            if VERBOSE:
                #pass
                print("There is a piece at the target that I can Capture")
                print("Return True")
            return True
        elif not can_capture and not empty_target:
            if VERBOSE:
                return False
        elif empty_target:
            return True
#END QUEEN
#BEGIN KING
    if source_piece[1] == "K" or source_piece[1] == "k":
        if VERBOSE:
            print("King")
        if not empty_target and not can_capture:
            if VERBOSE:
                print("(king) Target piece is same color")
                print("(king) " + str(xt) + "," + str(yt))
                print("Return False")
                pass
            return False
        return True
#END KING

def in_move_set(ptype,pcolor,xs,ys,xt,yt):
    VERBOSE = False
    #Check if the input values are valid
    if (xs > 8 or ys > 8 or xt > 8 or yt > 8) or (xs < 1 or ys < 1 or xt < 1 or yt < 1):
        if VERBOSE:
                print(red + "These values are not on the board, try a different move." + reset)
        return False
    #testing print statements
    if VERBOSE:
        print(ptype + " is trying to move from (" + str(xs) + ", " + str(ys) +
            ") to (" + str(xt) + ", " + str(yt) + ")")
    
    #Calculate dx and dy
    deltax = xt - xs
    deltay = yt - ys

    #PAWN keep working on
    if ptype == "P" or ptype == "p":
        # White Piece = +deltay
        if pcolor == "W" and deltay == 1 and deltax == 0:
            if VERBOSE:
                print("Valid Move!") 
            return True
        # White Piece first Move Jump
        if pcolor == "W" and ys == 2 and deltay == 2 and deltax == 0:
            if VERBOSE:
                print("Valid Move!") 
            return True
        # Black Piece = -deltay
        if pcolor == "B" and deltay == -1 and deltax == 0:
            if VERBOSE:
                print("Valid Move!") 
            return True
        # Black Piece first Move Jump
        if pcolor == "B" and ys == 7 and deltay == -2 and deltax == 0:
            if VERBOSE:
                print("Valid Move!") 
            return True
        # Check for diagonal Move in Direction Black Pawn
        if pcolor == "W" and deltay == 1 and abs(deltax) == 1:
            if VERBOSE:
                print("Valid Capture Move!") 
            return True
        # Check for diagonal Move in Direction Black Pawn
        if pcolor == "B" and deltay == -1 and abs(deltax) == 1:
            if VERBOSE:
                print("Valid Capture Move!") 
            return True


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

    #QUEEN BASIC MOVESET COMPLETE
    if ptype == "Q" or ptype == "q":
        #Rook Componant
        if (deltax == 0 or deltay == 0):
            if VERBOSE:
                print("Valid Move!") 
            return True
        #Bishop Componant
        if abs(deltax) == abs(deltay):
            if VERBOSE:
                print("Valid Move!") 
            return True

    #KING BASIC MOVESET COMPLETE
    if ptype == "K" or ptype == "k":
        #X Movement
        if abs(deltax) == 1 and abs(deltay) == 0:
            if VERBOSE:
                print("Valid Move!") 
            return True
        #Y Movement
        if abs(deltax) == 0 and abs(deltay) == 1:
            if VERBOSE:
                print("Valid Move!") 
            return True
        #Diagonal
        if abs(deltax) == 1 and abs(deltay) == 1:
            if VERBOSE:
                print("Valid Move!") 
            return True


    if VERBOSE:
        print("Not Valid Move :'(")
    return False
