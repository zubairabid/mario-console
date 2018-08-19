import numpy as np
from colorama import Fore, Back, Style

import time

import maps

class Screen:

    def __init__(self, dim_i, dim_j, level, game):
        '''
        Initializes screen with dimensions j (x-axis), i (y-axis)
        '''

        self.game = game

        # Set up map
        self.map = np.array([[0 for col in range(1000)] for row in range(dim_i)])
        self.loadMap(0)

        # Set up screen. Contains a display and a buffer
        # self.scr = np.array([[0 for col in range(dim_j)] for row in range(dim_i)])

        self.offset = 0
        self.dim_i = dim_i
        self.dim_j = dim_j


    def position(self, obj):
        size = obj.getSize()
        print(str(type(obj.i)) + "\t" + str(type(size[0]))+ "\t" + str(type(obj.code)))
        self.map[(obj.i+1-size[0]):(obj.i+1), (obj.j-1):(obj.j-1+size[1])] = obj.code
        # self.map[30:32, 1:3] = obj.code

    def add(self, obj, from_i, to_i, from_j, to_j):
        self.map[from_i:to_i, from_j:to_j] = obj.code


    def loadMap(self, level):
        print("loading map")
        for component in maps.maps[level]:
            vst = component[0]
            vh = component[2]
            hst = component[1]
            hh = component[3]
            self.map[vst:vst + vh, hst:hst + hh] = component[4]


    def render(self):
        for i in self.map:
            for j in range(self.offset, self.offset + self.dim_j):
                char = ''
                if i[j] == 0:
                    char = Back.BLUE + ' '
                if i[j] == 1:
                    char = Back.RED + ' '
                if i[j] == 2:
                    char = Back.MAGENTA + ' '
                print(char, end='')
                # print(self.gamestate.codes[i[j]].__str__(), end='')
            print(Style.RESET_ALL)

    def update(self, mario):
        # Update background
        pass
        # Update interactible

        # Update Mario
        # if self.scr[mario.row, mario.col - 1] == mario:
        #     self.scr[mario.row, mario.col - 1] = Generic()
        #
        # if self.scr[mario.row, mario.col + 1] == mario:
        #     self.scr[mario.row, mario.col + 1] = Generic()
        #
        # if self.scr[mario.row-1, mario.col] == mario:
        #     self.scr[mario.row-1, mario.col] = Generic()
        #
        # if self.scr[mario.row+1, mario.col] == mario:
        #     self.scr[mario.row+1, mario.col] = Generic()
        #
        #
        # self.scr[mario.row, mario.col] = mario
        # self.scr[mario.row, mario.col + 1] = mario.image[mario.row, 1]
        # self.scr[mario.row - 1, mario.col] = mario.image[mario.row - 1, 0]
        # self.scr[mario.row - 1, mario.col + 1] = mario.image[mario.row - 1, 1]
        # self.scr[mario.row - 2, mario.col] = mario.image[mario.row - 2, 0]
        # self.scr[mario.row - 2, mario.col + 1] = mario.image[mario.row - 2, 1]
