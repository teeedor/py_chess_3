#this file will have all move set related functions

#Movesets for
#Pawn
#Rook
#Knight
#Bishop
#Queen
#King

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
#def in_move_set(xs,ys,xt,yt):
    
