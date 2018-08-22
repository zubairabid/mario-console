from colorama import Fore, Back, Style

class Generic:
    '''
    Every object in the game inherits from here.
    '''
    def __repr__(self):
        return 'Generic object for everything'

    def __str__(self):
        return Back.BLUE + ' '

    def __init__(self):
        pass

    def getSize(self):
        pass

    def setSize(self):
        pass

    def getLoc(self):
        pass

    def setLoc(self):
        pass


class Thing(Generic):
    def __repr__(self):
        return 'Generic object for everything'

    def __str__(self):
        return Back.MAGENTA + ' '

    def __init__(self):
        super().__init__()


class Brick(Thing):

    def __repr__(self):
        return 'Generic object for everything'

    def __str__(self):
        return Back.MAGENTA + ' '

    def __init__(self):
        super().__init__()
        self.code = 6


class HidBrick(Brick):

    def __init__(self):
        super().__init__()
        self.code = 8
