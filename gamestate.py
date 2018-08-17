from screen import Screen
from objects import Mario
from time import monotonic as timer

class Game:

    def __init__(self, level, time):
        self.screen = Screen(36, 96)
        # if level == 0:

        player = Mario()
        self.screen.scr[player.row, player.col] = player

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
