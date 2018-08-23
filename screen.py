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
        self.loadMap(level)

        # offset from where map starts displaying on screen
        self.offset = 0

        # height, width of map
        self.dim_i = dim_i
        self.dim_j = dim_j

    def loadMap(self, level):
        '''
        Calls the random map generator to get a map for level specified
        '''
        print('Loading level ' + str(level))
        for component in maps.genlevel(level):
            vst = component[0] # y1
            vh = component[2] # x1
            hst = component[1] # y2 - y1
            hh = component[3] # x2 - x1
            self.map[vst:vst + vh, hst:hst + hh] = component[4]

    def position(self, obj):
        '''
        Given an object, it places it on the map's[i,j] as defined by object's
        i, j and getSize()
        '''
        size = obj.getSize()

        from_i = obj.i+1-size[0]
        to_i = obj.i+1
        from_j = obj.j-1
        to_j = obj.j-1+size[1]

        self.map[from_i:to_i, from_j:to_j] = obj.code

    def add(self, obj, from_i, to_i, from_j, to_j):
        '''
        Places obj.code within range specified
        '''
        self.map[from_i:to_i, from_j:to_j] = obj.code

    def render(self):
        '''
        Generates the screen
        '''

        trackc = 0 # Used to render Mario's character properly
        sky = Back.BLUE
        brick = Back.GREEN

        if self.game.level == 2:
            sky = Back.BLACK
            brick = Back.MAGENTA

        for i in self.map:
            for j in range(self.offset, self.offset + self.dim_j):

                char = ''

                if i[j] == 0: # Sky
                    char = sky + Fore.BLACK + ' '

                if i[j] == 1: # Clouds
                    char = Back.WHITE + '0'

                if i[j] == 5: # Mario
                    if trackc == 0 or trackc == 2:
                        char = 'O'
                    else:
                        char = '|'
                    trackc += 1
                    char = sky + Fore.RED + char

                if i[j] == 6: # Brick
                    char = brick + '.'

                if i[j] == 7: # PowerUp
                    char = Back.CYAN + '*'

                if i[j] == 8: # Hidden Brick
                    char = Back.YELLOW + 'X'

                if i[j] == 9: # Coins
                    char = sky + Fore.YELLOW + 'O'

                if i[j] >= 20: # Enemy
                    char = Back.RED + Fore.BLACK + '^'

                print(char, end='')

            print(Style.RESET_ALL+'')
