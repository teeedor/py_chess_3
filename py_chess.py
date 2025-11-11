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

def draw_line(y_val, board):
    output = "" #starts empty
    for x_val in range(8):
        #x_val, y_val
        #if there is no piece at location, add an X to the Line output String
        #else, add piece to output string
    #after the entire loop, Draw the String

def draw(board):
    #loop through the 2d board and print a piece if there is one at that location
    for y in range(8):
        draw_line(y, board) #draw entire y line
    #entire board is drawn, maybe add white and black labels?
    

