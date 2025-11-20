#this file will have all move set related functions

#piece in the way?
#is_valid_move?
#function to get the color and type of a location
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
    #checks if there is a piece in target location
    target_piece = get_piece(board,xt,yt)
    source_piece = get_piece(board,xs,ys)
    if (target_piece == ("N","N")):
        if VERBOSE:
            print("------------")
            print("Empty Target Location")
        empty_target = True
    else:
        if VERBOSE:
            print("------------")
            print("Filled Target Location")

        empty_target = False 
    if source_piece[1] == "H" or source_piece[1] == "h":
        #knight Expection, can jump
        if VERBOSE:
            print("Knight")
        return True
    if source_piece[1] == "R" or source_piece[1] == "r":
        #Rook, look for something in the way 
        deltax = xt - xs
        deltay = yt - ys
        if VERBOSE:
            #print("Rook")
            pass
        if deltax == 0: # Vertical Lines
            if deltay > 0: # positive movement
                #regular movement
                for i in range(1, deltay-1):
                    if get_piece(board,xs,ys+i) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way")
                            print(str(xs) + "," + str(ys+i))
                        return False      
            else: # negative movement BROKEN
                for i in range(-1, deltay+1, -1):
                    print(i)
                    if get_piece(board,xs,ys+i) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way")
                            print(str(xs) + "," + str(ys+i))
                        return False

        if deltay == 0: # Horizontal Lines
            if deltax > 0: # positive movement
                #regular movement
                for i in range(1, deltax-1):
                    if get_piece(board,xs+i,ys) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way")
                            print(str(xs+i) + "," + str(ys))
                        return False
            else: # negative movement
                for i in range(-1, deltax+1,-1):
                    if get_piece(board,xs+i,ys) != ("N","N"):
                        #piece in the way
                        if VERBOSE:
                            print("Piece in the way")
                            print(str(xs+i) + "," + str(ys))
                        return False
        if VERBOSE:
            print("No piece in the way!")
        return True

    if source_piece[1] == "B" or source_piece[1] == "b":
        #knight Expection, can jump
        if VERBOSE:
            print("Bishop")
         
        #return True
    #checks if can capture based on color 
    #checks if something is in the way of movement for pieces
#only checks if the piece can make that move, regardless of board
#input: start loc and target loc

def in_move_set(ptype,pcolor,xs,ys,xt,yt):
    VERBOSE = True
    #Check if the input values are valid
    if ((xs or ys or xt or yt) > 8) or ((xs or ys or xt or yt) < 1):
        print("These values are not on the board, try a different move.")
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
        if deltax == 0 or deltay == 0:
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
