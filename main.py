from util import NBInput
from util import clear
import time

if __name__ == "__main__":
    '''
    game loop, environment setup, etc. Happens here
    '''
    clear()
    keys = NBInput()

    try:
        keys.nbTerm()

        i = 1
        while 1:
            keys.flush()
            print(i)
            i+=1
            time.sleep(0.2)
            clear()

            op = ''
            if keys.kbHit():
                op = keys.getCh()

            if op == '\x51' or op == '\x71':
                break

    finally:
        keys.orTerm()
