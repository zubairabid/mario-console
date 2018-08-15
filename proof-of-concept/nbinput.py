import sys
import select
import tty
import termios
import time
import subprocess as sp

def isData():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

old_settings = termios.tcgetattr(sys.stdin)
try:
	tty.setcbreak(sys.stdin.fileno())

	i = 0
	while 1:
		print(i)
		time.sleep(0.1)
		sp.call('clear', shell=True)
		i += 1

		if isData():
			c = sys.stdin.read(1)
			if c == '\x71' or c == '\x51':         # x1b is ESC
				break
	
finally:
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
