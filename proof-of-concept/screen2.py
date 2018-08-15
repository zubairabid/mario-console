import numpy as np

import sys
import select
import tty
import termios

import subprocess as sp
import time


def isData():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []) 


disp = np.ones((10,10))


old_settings = termios.tcgetattr(sys.stdin)
try:
	tty.setcbreak(sys.stdin.fileno())

	i = 1
	while 1:
		termios.tcflush(sys.stdin, termios.TCIOFLUSH)
		print(disp)
		time.sleep(0.06)
		sp.call('clear', shell=True)
		i += 0.0005

		if isData():
			c = sys.stdin.read(1)
			
			if c == '\x57' or c == '\x77':
				disp = disp + i
			
			
			if c == '\x41' or c == '\x61':
				disp = disp - i
			
			
			if c == '\x44' or c == '\x64':
				disp = disp * i
			
			
			if c == '\x53' or c == '\x73':
				disp = disp // i
			
			
			if c == '\x71' or c == '\x51':
				break

finally:
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

