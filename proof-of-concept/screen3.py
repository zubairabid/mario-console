import numpy as np

import sys
import select
import tty
import termios

import subprocess as sp
import time

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool 

#from multiprocessing import Process

pool = ThreadPool(2)

disp = np.ones((10,10))

def isData():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []) 

def keyplus():
	if isData():
		c =  sys.stdin.read(1)
		
		if c == '\x57' or c == '\x77':
			disp[5:,] = disp[5:,] + i

		if c == '\x44' or c == '\x64':
			disp[5:,] = disp[5:,] * i

		if c == '\x51' or c == '\x71':
			return 0	
	return 1

def keyminus():
	if isData():
		c = sys.stdin.read(1)
		
		if c == '\x41' or c == '\x61':
			disp[:5,] = disp[:5,] - i

		if c == '\x53' or c == '\x73':
			disp[:5,] = disp[:5,] // i

		if c == '\x51' or c == '\x71':
			return 0

	return 1


old_settings = termios.tcgetattr(sys.stdin)
try:
	tty.setcbreak(sys.stdin.fileno())

	i = 1
	while 1:
		termios.tcflush(sys.stdin, termios.TCIOFLUSH)
		print(disp)
		time.sleep(1)
		sp.call('clear', shell=True)
		i += 0.5

		result = pool.map(keypress, [0, 1])
		#Process(target=keyplus()).start()
		#Process(target=keyminus()).start()
		
		if result[0] == 0 or result[1] == 0:
			break

finally:
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

