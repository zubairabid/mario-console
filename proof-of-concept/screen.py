import numpy as np
import subprocess as sp
import time

b = np.zeros((80,48))
for i in range(100):
	print(i)
	time.sleep(0.2)
	sp.call('clear', shell=True)
