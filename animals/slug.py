from animals import Animal
from movements import Slithering

class Slug(Animal, Slithering):
    def __init__(self, name):
        Animal.__init__(self, name, 'Slugalia', 'amoeba')
        Slithering.__init__(self, 1, 1)