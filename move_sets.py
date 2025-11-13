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

#only checks if the piece can make that move, regardless of board
#input: start loc and target loc
def in_move_set(ptype,pcolor,xs,ys,xt,yt):
    print(ptype + " is trying to move from (" + str(xs) + ", " + str(ys) +
          ") to (" + str(xt) + ", " + str(yt) + ")")
    
    #PAWN
    VERBOSE = True
    if ptype == "P" or ptype == "p":
        #get pieces color
        #if white, pawn moves in positive y, black moves in negative y
        #if piece is on homerow, allow for big first move
        #also need to factor in Capture movement
        print("PAWN")
    #ROOK BASIC MOVESET COMPLETE
    if ptype == "R" or ptype == "r":
        deltax = xt - xs
        deltay = yt - ys
        #if one of the deltas is 0, then it has to be in a line
        if deltax == 0 or deltay == 0:
            return True
    #BISHOP
    if ptype == "B" or ptype == "b":
        print("BISHOP")   
    #KNIGHT
    if ptype == "H" or ptype == "h":
        print("KNIGHT")   
    #QUEEN
    if ptype == "Q" or ptype == "q":
        print("QUEEN")  
    #KING
    if ptype == "K" or ptype == "k":
        print("KING")  

