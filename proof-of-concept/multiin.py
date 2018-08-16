import sys
import select
import tty
import termios # for non-blocking inpuy in Linux

import subprocess as sp # for printing to console

from multiprocessing.dummy import Pool as ThreadPool # For 2p support

import time
from random import randrange

import numpy as np



i = ["w not pressed", "b not pressed"]
temp = np.ones((10,10))

def randomsleep(num):
	while 1:
		print(num)
		time.sleep(randrange(5))

def isData():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def keyLoop(state):
	
	if isData():
		c = sys.stdin.read(1)
				
		if c == '\x71' or c == '\x51': # keypress 'q'
			return 0

		if state == 0:
			if c == '\x77' or c == '\x57': # keypress 'w'
				#i[0] = "w pressed"
				temp[:5,] = 10
		if state == 1:
			if c == '\x62' or c == '\x42': # kepress 'b'
				#i[1] = "b pressed"
				temp[5:,] = 10

		else:
			if state == 0:
				#i[0] = "w not pressed"
				temp[:5,] = 1
			if state == 1:
				#i[1] = "b not pressed"
				temp[5:,] = 1


#results = pool.map(randomsleep, [1,2,3,4,5])
old_settings = termios.tcgetattr(sys.stdin)
try:
	tty.setcbreak(sys.stdin.fileno())
	
	while 1:
		termios.tcflush(sys.stdin, termios.TCIOFLUSH) # flushes input in buffer to avoid lag

		print(temp)
		time.sleep(0.1)
		sp.call('clear', shell=True)

		pool = ThreadPool(4)
		results = pool.map(keyLoop, [0, 1])
	
		if results[0] == 0 or results[1] == 0:
			break

		pool.close()
		pool.join()


finally:
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


