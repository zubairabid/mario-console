import numpy as np
from objects import Generic

class Screen:

    def __init__(self, dim_i, dim_j):
        '''
        Initializes screen with dimensions j (x-axis), i (y-axis)
        '''

        # Set up screen. Contains a display and a buffer
        self.scr = np.array([[Generic()]*(dim_j*2)]*dim_i)

        self.dim_i = dim_i
        self.dim_j = dim_j

        self.scroll = (0, dim_j)

    def render(self):
        for i in range(self.dim_i):
            for j in range(self.scroll[0], self.scroll[1]):
                print(self.scr[i, j].__str__(), end='')
            print()

    def update(self, mario):
        # Update background

        # Update interactible

        # Update Mario
        if self.scr[mario.row, mario.col - 1] == mario:
            self.scr[mario.row, mario.col - 1] = Generic()

        if self.scr[mario.row, mario.col + 1] == mario:
            self.scr[mario.row, mario.col + 1] = Generic()

        if self.scr[mario.row-1, mario.col] == mario:
            self.scr[mario.row-1, mario.col] = Generic()

        if self.scr[mario.row+1, mario.col] == mario:
            self.scr[mario.row+1, mario.col] = Generic()


        self.scr[mario.row, mario.col] = mario
        # self.scr[mario.row, mario.col + 1] = mario.image[mario.row, 1]
        # self.scr[mario.row - 1, mario.col] = mario.image[mario.row - 1, 0]
        # self.scr[mario.row - 1, mario.col + 1] = mario.image[mario.row - 1, 1]
        # self.scr[mario.row - 2, mario.col] = mario.image[mario.row - 2, 0]
        # self.scr[mario.row - 2, mario.col + 1] = mario.image[mario.row - 2, 1]
