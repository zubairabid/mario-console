from objects import Generic
from colorama import Fore, Back, Style

class Back(Generic):
    def __repr__(self):
        return 'Generic object for everything'

    def __str__(self):
        return Back.BLUE + ' '

    def __init__(self):
        super().__init__()
        self.code = 0

class Cloud(Back):
    def __init__(self):
        super().__init__()
        self.code = 1
