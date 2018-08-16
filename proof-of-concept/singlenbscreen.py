import sys
import select
import tty
import termios

import subprocess as sp
import time

import numpy as np

def isData():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def keyPress():
	if isData():
		c = sys.stdin.read(1)

		if c == '\x51' or c == '\x71':
			return 0
		
		if c == '\x57' or c == '\x77':
			return 1

		return 2
	return 2

def gameLoop(disp):
	old_settings = termios.tcgetattr(sys.stdin)
	try:
		tty.setcbreak(sys.stdin.fileno())

		while 1:
			termios.tcflush(sys.stdin, termios.TCIOFLUSH)
			print(disp)
			time.sleep(0.1)
			sp.call('clear', shell=True)

			op = keyPress()
			if op == 0:
				break
			elif op == 1:
				disp += 1
	finally:
		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def main():
	disp = np.zeros((10,10))
	gameLoop(disp)

main()
