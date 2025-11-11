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

