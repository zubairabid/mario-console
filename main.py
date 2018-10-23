'''
Main file of execution
'''

import time

from colorama import init

from util import NBInput
from util import clear
from util import keypress

from gamestate import Game

import configs

if __name__ == "__main__":
    '''
    game loop, environment setup, etc. happens here
    '''

    # setting up Colorama
    init()

    # sets up keyboard INPUT
    KEYS = NBInput()

    ##########################
    # Set up the environment #
    ##########################

    try:
        ######################################
        # Start the actual game configs here #
        ######################################

        # clear screen and enable non blocking INPUT
        clear()
        KEYS.nbTerm()
        LEVEL = 0

        print("Choose level you want to play:\n0\t1\t2")
        LEVEL = int(KEYS.getCh())

        if LEVEL > 2 or LEVEL < 0:
            print('Choice out of bounds. Resetting to 0')
            LEVEL = 0

        # Start a new Game with level
        # the screen used is a property of the game object
        LIVES = configs.MAX_LIFE

        STATUS = 0
        POINTS = 0

        while LIVES > 0:
            GAME = Game(LEVEL, configs.STD_TIME, LIVES)

            # Level screen
            GAME.levelScreen(LEVEL, LIVES, POINTS)
            KEYS.flush()
            KEYS.getCh()

            # Game loop executes as time remains
            while GAME.getTRemain() > 0:

                # FRAME stores the time remaining at the start of rendering
                # a frame, so as to calculate how long actually rendering it
                # took, and to maintain a framerate
                FRAME = GAME.getTRemain()

                # repaint screen
                GAME.repaint()

                # poll for INPUT
                INPUT = ''
                if KEYS.kbHit():
                    INPUT = KEYS.getCh()

                # process INPUT
                CIN = keypress(INPUT)
                if CIN == -1:
                    STATUS = 2
                    break

                # run game mechanics for each cycle
                STATUS = GAME.changeState(CIN)
                if STATUS != 0:
                    break

                # Clear INPUT buffer to prevent delayed response
                KEYS.flush()

                # Maintains some sort of framerate
                while FRAME - GAME.getTRemain() < 0.1:
                    continue

            # Game quit
            if STATUS == 2:
                break
            # Level up
            if STATUS == 1:
                STATUS = 0
                LEVEL += 1
                POINTS += GAME.points + GAME.getTRemain()//1
                continue

            if LEVEL >= 3:
                break

            # If here, death has happened.
            LIVES -= 1

    finally:
        time.sleep(0.5)
        clear()
        print("GAME OVER. Final points: " + str(POINTS) +
              "\nPress any key to exit")

        KEYS.flush()
        KEYS.getCh()
        # Switch back to the original terminal state
        KEYS.orTerm()
