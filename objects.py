class Generic:
    '''
    Every object in the game inherits from here.
    '''
    def __repr__():
        return 'Generic object for everything'

    def __str__():
        return '_'


class Person(Generic):
    '''
    Generic class for all living beings in the game
    '''
    def __init__(self):
        '''
        Location is a default property of all "people"
        '''
        self.row = 0
        self.col = 0

    def __str__(self):
        return 'I'

    def getLocation(self):
        return (self.row, self.col)

    def setLocation(self, row_in, col_in):
        self.row = row_in
        self.col = col_in

class Thing(Generic):
    pass

class Back(Generic):
    pass

class Mario(Person):
    '''
    Defines the player object
    '''
    def __init__(self):
        super().__init__()

        self.row = 30 # change hardcode
        self.col = 16 # change hardcode

        self.width = 2
        self.height = 3

        self.image = [['.', 'o'],
                    [']', '['],
                    ['|', '|']]

    def move(self, direction):
        if direction == -1:
            self.col -= 1
        elif direction == 1:
            self.col += 1

    def setSize(self, w, h):
        self.width = w
        self.height = h
