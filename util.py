import sys
import select
import tty
import termios

import subprocess as sp

def clear():
    '''
    function to clear the terminal screen
    '''
    sp.call('clear', shell=True)


def keypress(c):
    if c == '\x51' or c == '\x71': # q/Q
        return -1

    elif c == '\x44' or c == '\x64': # d/D
        return 1

    elif c == '\x41' or c == '\x61': #a/A
        return 2

    elif c == '\x57' or c == '\x77': # w/W
        return 3

class NBInput:
    '''
    class to deal with non-blocking input
    '''

    def __init__(self):
        '''
        Initializes the object to be used for non-blocking input.
         - Saves original state at time of function call
         - Conversion to new mode has to be manual
        '''
        self.old_settings = termios.tcgetattr(sys.stdin)


    def nbTerm(self):
        '''
        Sets up the terminal for non-blocking input
        '''
        tty.setcbreak(sys.stdin.fileno())

    def orTerm(self):
        '''
        Sets terminal back to original state
        '''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

    def kbHit(self):
        '''
        returns True if keypress has occured
        '''
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    def getCh(self):
        '''
        returns input character
        '''
        return sys.stdin.read(1)

    def flush(self):
        '''
        clears input buffer
        '''
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)