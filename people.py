from objects import Generic
import backgrounds
from colorama import Fore, Back, Style

class Person(Generic):
    '''
    Generic class for all living beings in the game
    '''
    def __init__(self, game, i = 0, j = 0):
        '''
        Location is a default property of all "people"
        '''
        super().__init__()
        self.game = game
        self.i = i
        self.j = j
        self.jstate = 0

    def __str__(self):
        return Back.RED + 'I'

    def getLoc(self):
        return (self.i, self.j)

    def setLoc(self, i, j):
        self.i = i
        self.j = j

    def getSize(self):
        return (1,1)

    def collision(self, dir):
        if dir == 1:
            for i in range(self.i+1-self.getSize()[0],self.i+1):
                if self.game.screen.map[i,self.j+self.getSize()[1]] >= 5:
                    return True
        elif dir == 2:
            for i in range(self.i+1-self.getSize()[0],self.i+1):
                if self.game.screen.map[i,self.j-2] >= 5:
                    return True
        elif dir == 3:
            for j in range(self.j-1,self.j-1+self.getSize()[1]):
                if self.game.screen.map[self.i-self.getSize()[0],j] >= 5:
                    return True
        elif dir == 4:
            for j in range(self.j-1,self.j-1+self.getSize()[1]):
                if self.game.screen.map[self.i+1,j] >= 5:
                    return True
        return False

    def move(self, key):
        if key=='\x44' or key == '\x64': # d, go right
            if not self.collision(1): # right collison
                self.j += 1

                t_i = self.i+1
                f_i = self.i+1-self.getSize()[0]

                del_j = self.j-1
                add_j = self.j-1+self.getSize()[1]

                self.game.screen.add(backgrounds.Back(), f_i, t_i, del_j-1, del_j)
                self.game.screen.add(self, f_i, t_i, add_j-1, add_j)

        if key == '\x41' or key == '\x61': # a, go left
            if not self.collision(2): # left collison
                self.j -= 1

                t_i = self.i+1
                f_i = self.i+1-self.getSize()[0]

                add_j = self.j-1
                del_j = self.j-1+self.getSize()[1]

                self.game.screen.add(backgrounds.Back(), f_i, t_i, del_j, del_j+1)
                self.game.screen.add(self, f_i, t_i, add_j, add_j+1)

        if key == '\x57' or key == '\x77': #w, go up
            if self.jstate == 0:
                self.jstate = 7

    def vertical(self):
        if self.jstate > 0:
            if not self.collision(3): # up collison
                # if self.game.screen.map[self.i-self.getSize()[0], self.j:self.j+self.getSize()[1]].any(0):
                self.jstate -= 1

                self.i -= 1

                t_j = self.j+1
                f_j = self.j+1-self.getSize()[1]

                del_i = self.i+1
                add_i = self.i+1-self.getSize()[0]

                self.game.screen.add(backgrounds.Back(), del_i, del_i+1, f_j, t_j)
                self.game.screen.add(self, add_i, add_i+1, f_j, t_j)
            else:
                self.jstate = 0
        else:
            if not self.collision(4): # down collison
            # if self.game.screen.map[self.i+1, self.j] == 0 and self.game.screen.map[self.i+1, self.j+1] == 0:
                self.i += 1

                t_j = self.j+1
                f_j = self.j+1-self.getSize()[1]

                add_i = self.i+1
                del_i = self.i+1-self.getSize()[0]

                self.game.screen.add(backgrounds.Back(), del_i-1, del_i, f_j, t_j)
                self.game.screen.add(self, add_i-1, add_i, f_j, t_j)



class Mario(Person):

    def __init__(self, game):
        super().__init__(game, 31, 3)

        self.code = 5

    def getSize(self):
        return (2,2)
