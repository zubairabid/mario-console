from screen import Screen
from people import Mario
from backgrounds import Back
from backgrounds import Cloud
from objects import Brick

from time import monotonic as timer
from util import clear

class Game:

    def __init__(self, level, time):
        self.screen = Screen(36, 96, level, self)
        # if level == 0:
        # self.screen.loadMap(0)

        self.player = Mario(self)

        # 0: Back, 1: Cloud (Back) ...  5. Mario, 6. Brick
        self.codes = [Back(), Cloud(), Back(), Back(), Back(), self.player, Brick()]

        self.screen.position(self.player)

        # game timer starts now
        self.stime = timer()
        self.etime = self.stime + time

    def changeState(self, keypress):

        # Apply mario movement
        self.player.move(keypress)

        # Update background (right/left)
        if self.player.getLoc()[1] > self.screen.offset + 32:
            self.screen.offset += 1

        # Update enemies
        # Apply gravity
        self.player.vertical()

        # Check interactions

    def repaint(self):
        clear()
        self.screen.render()
        self.headline()

    def getTRemain(self):
        return self.etime - timer()

    def getTPast(self):
        return timer() - self.stime

    def getTime(self):
        return timer()

    def headline(self):
        print('TIME LEFT: ' + str(self.getTRemain()))
