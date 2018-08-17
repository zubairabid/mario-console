from util import NBInput
from util import clear
from util import keypress

import sys
import select

from gamestate import Game

import time

if __name__ == "__main__":
    '''
    game loop, environment setup, etc. Happens here
    '''

    keys = NBInput()

    ##########################
    # Set up the environment #
    ##########################

    try:
        ######################################
        # Start the actual game configs here #
        ######################################

        # clear screen and enable non blocking input
        clear()
        keys.nbTerm()

        print("Choose level you want to play:\n0\t1\t2\t3")
        level = keys.getCh()

        # Start a new Game with level
        # the screen used is a property of the game object
        game = Game(level, 200) # un-hardcode time after

        while game.getTRemain() > 0:

            frame = game.getTRemain()
            clear()

            # repaint screen
            game.headline()
            game.screen.render()

            # poll for input
            op=''
            if keys.kbHit():
                op = keys.getCh()

            # process input
            if(keypress(op) == -1):
                break

            # clear the input buffer
            keys.flush()

            while(frame - game.getTRemain() < 0.2):
                # Maintains some sort of framerate
                continue
    finally:
        # Switch back to the original terminal state
        keys.orTerm()
