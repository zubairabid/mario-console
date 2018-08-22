from util import NBInput
from util import clear
from util import keypress

import sys
import select

from gamestate import Game

import time
from colorama import init

if __name__ == "__main__":
    '''
    game loop, environment setup, etc. Happens here
    '''

    # setting up Colorama
    init()

    # sets up keyboard input
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
        game = Game(int(level), 200) # un-hardcode time after

        # Game loop executes as time remains
        while game.getTRemain() > 0:

            # frame stores the time remaining at the start of rendering
            # a frame, so as to calculate how long actually rendering it
            # took, and to maintain a framerate
            frame = game.getTRemain()

            # repaint screen
            game.repaint()

            # poll for input
            input=''
            if keys.kbHit():
                input = keys.getCh()

            # process input
            cin = keypress(input)
            if cin == -1:
                break

            # run game mechanics for each cycle
            game.changeState(cin)

            # Clear input buffer to prevent delayed response
            keys.flush()

            # time.sleep(0.05)
            while(frame - game.getTRemain() < 0.1):
                # Maintains some sort of framerate
                continue

    finally:
        # Switch back to the original terminal state
        keys.orTerm()
