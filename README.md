Project to brush up on git and python skills 

=== Basic Plan for PyChess ===
                                   
Pieces are stored in a 2d array  ((x,y),(color,piece))

Will be drawn by the Draw() function

White starts, player chooses a move 

Checks Validity
    Move set
    Board State
    King in check
        make sure move doesn't put your king in check

add a scoreboard
use a graphics library to render a prettier board

=== CURRENT STATE ===
    Piece movesets complete
    ALL - DONE

    Check Path for valid move
    ALL - DONE

    Movement Tests
    ALL - DONE
    
    PLAYING THE GAME
    Check for Valid input
    Check for move validity on board
    Check if move puts king in check
    Reflect the move in the data structure
    change score if needed
    rotate the Turn

=== FUTURE PLANS ===
    Change from terminal Draw to window Draw with Tkinter
    Have random Mode
    Create new Types of Pieces (Research)
    Create online multiplayer
