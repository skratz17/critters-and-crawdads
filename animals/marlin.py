from animals import Animal
from movements import Swimming

class Marlin(Animal, Swimming):
    def __init__(self, name):
        Animal.__init__(self, name, 'Marlianalia', 'sharks')
        Swimming.__init__(self, 12, 500)