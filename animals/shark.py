from animals import Animal
from movements import Swimming

class Shark(Animal, Swimming):
    def __init__(self, name):
        Animal.__init__(self, name, 'Sharkalia', 'humans')
        Swimming.__init__(self, 50000, 500000)

    def feed(self):
        print("You tried to feed the shark. The shark ate you. Game over.")