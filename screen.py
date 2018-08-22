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
        self.map = np.array([[0 for col in range(600)] for row in range(dim_i)])
        self.getMap(level)
        # self.randomMap()

        # Set up screen. Contains a display and a buffer
        # self.scr = np.array([[0 for col in range(dim_j)] for row in range(dim_i)])

        self.offset = 0
        self.dim_i = dim_i
        self.dim_j = dim_j


    def position(self, obj):
        size = obj.getSize()
        self.map[(obj.i+1-size[0]):(obj.i+1), (obj.j-1):(obj.j-1+size[1])] = obj.code
        # self.map[30:32, 1:3] = obj.code

    def add(self, obj, from_i, to_i, from_j, to_j):
        self.map[from_i:to_i, from_j:to_j] = obj.code

    def getMap(self, level):
        print('Loading level ' + str(level))
        for component in maps.genlevel(level):
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
                    char = Back.BLUE + Fore.BLACK + ' '
                if i[j] == 1:
                    char = Back.WHITE + '0'
                if i[j] == 5:
                    char = Back.RED + ' '
                if i[j] == 6:
                    char = Back.GREEN + '.'
                if i[j] == 7:
                    char = Back.CYAN + '*'
                if i[j] == 8:
                    char = Back.YELLOW + 'X'
                if i[j] >= 20:
                    char = Back.BLACK + '^'
                print(char, end='')
                # print(self.gamestate.codes[i[j]].__str__(), end='')
            print(Style.RESET_ALL)
