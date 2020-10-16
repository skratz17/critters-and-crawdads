from animals import Animal
from movements import Slithering

class Worm(Animal, Slithering):
    def __init__(self, name):
        Animal.__init__(self, name, 'Wormalia', 'leaf')
        Slithering.__init__(self, 1, 1)