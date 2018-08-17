from screen import Screen
from objects import Mario
from time import monotonic as timer

class Game:

    def __init__(self, level, time):
        self.screen = Screen(36, 96)
        # if level == 0:

        self.player = Mario()
        self.screen.scr[self.player.row, self.player.col] = self.player

        self.stime = timer()
        self.etime = self.stime + time

    def getTRemain(self):
        return self.etime - timer()

    def getTPast(self):
        return timer() - self.stime

    def getTime(self):
        return timer()

    def headline(self):
        print('TIME LEFT: ' + str(self.getTRemain()))
