from screen import Screen
from people import Mario
from people import Mushroom
from backgrounds import Back
from backgrounds import Cloud
from objects import Brick

from util import clear

from time import monotonic as timer
from random import random
from random import randrange

class Game:
    '''
    Class to define an individual game
    Each game is represented as an object
    '''

    def __init__(self, level, time):
        '''
        Initializes game, includes:
        1. Setup map+screen, player 1, position player on map
        2. Set numeric codes for class instances
        3. Starts the game timer
        4. Initializes any other variables needed for each game
        '''

        self.screen = Screen(36, 96, level, self)

        self.player = Mario(self)

        # 0: Back, 1: Cloud (Back) ...  5. Mario, 6. Brick
        self.codes = [Back(), Cloud(), Back(), Back(), Back(), self.player, Brick()]
        for temp in range(100): # Change later
            self.codes.append(None)

        self.screen.position(self.player)

        self.stime = timer()
        self.etime = self.stime + time

        # self.count - 20 indicates number of generic
        # enemies onscreen within any cycle
        self.count = 20
        self.count_l = 20

    def changeState(self, keypress):
        '''
        Calculates and applies changes within each cycle
        '''

        # Apply mario movement
        self.player.move(keypress)

        # Update background (right/left)
        if self.player.getLoc()[1] > self.screen.offset + 32:
            self.screen.offset += 1

        # Generate any enemies
        self.generateEnemy()

        # Apply gravity and movement
        for enemy in range(self.count_l, self.count):
            self.codes[enemy].vertical()
            self.codes[enemy].move()
        self.player.vertical()

        # Check interactions
        for enemy in range(self.count_l, self.count):
            if self.codes[enemy].lives <= 0:
                print("ENEMY DED")
                self.erase(enemy, 1, self.codes[enemy].i, self.codes[enemy].j)
                self.count_l += 1

        if self.player.lives <= 0:
            print('YOU SHOULD BE DEAD')
    def generateEnemy(self):
        '''
        Creates an enemy
        '''

        if(random() < 0.01):
            lj = self.screen.offset + 90 + randrange(10)
            li = 1
            mush = Mushroom(self, self.count, li, lj)
            self.screen.position(mush)
            self.codes[self.count] = mush
            self.count += 1

    def erase(self, obj, dir, pi, pj):
        if dir == 1:
            i = pi
            j = pj + 1
        elif dir == 2:
            i = pi
            j = pj - 1
        elif dir == 3:
            i = pi - 1
            j = pj
        elif dir == 4:
            i = pi + 1
            j = pj

        if self.screen.map[i,j] == obj:
            self.screen.add(Back(), i, i+1, j, j+1)
            for k in range(1,5):
                self.erase(obj, k, i, j)

    def delete(self):
        pass

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
        print('LIVES LEFT: ' + str(self.player.lives))
