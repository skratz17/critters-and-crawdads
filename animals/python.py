from animals import Animal
from movements import Slithering

class Python(Animal, Slithering):
    def __init__(self, name):
        Animal.__init__(self, name, 'Snakealia', 'mice')
        Slithering.__init__(self, 5, 25)