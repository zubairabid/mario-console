from screen import Screen
from time import monotonic as timer

class Game:

    def __init__(self, level, time):
        self.screen = Screen(18, 48)
        # if level == 0:

        self.stime = timer()
        self.etime = self.stime + time

    def getTRemain(self):
        return self.etime - timer()

    def getTPast(self):
        return timer() - self.stime
