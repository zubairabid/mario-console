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

    def getLocation(self):
        return (self.row, self.col)

    def setLocation(self, row_in, col_in):
        self.row = row_in
        self.col = col_in

class Thing(Generic):
    pass

class Back(Generic):
    pass
