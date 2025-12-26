# THIS FILE IS FOR IMPORTING AND RUNNING ALL OTHER FUNCTIONS
# --- main.py ---

#import move_sets, chess_funcs 
from test_chess import run_tests
from chess_funcs import make_board, draw, read_in_move

# Run Tests
#run_tests()

# --- Main Game Logic ---
# Initial Variables
# White goes first
white_turn = True
# Make Standard Game Board
board = make_board(2)
# Scores start at 0
w_score = 0
b_score = 0
# Piece Point Values
val_p, val_k, val_b, val_r, val_q = 1, 3, 3, 5, 9

# Game Loop
#while(has_kings(board)): # still need to write this function
while True: #only used for Testing 
    # Draw the Board
    draw(board)
    # Read in move from current player
    xs, ys, xt, yt = read_in_move(board,white_turn)
    #if filled(board,xs,ys):
        
    # Checks Performed during Move attempt
        # In move set
        # valid Capture
        # no Piece in way of movement
        # does the state after the move put your king in check?
        # if there is a capture, adjust the corresponding Score
        # rotate the turn only if the move was valid and went through
        #white_turn = not white_turn
# End Game Loop
