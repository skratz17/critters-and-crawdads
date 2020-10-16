from animals import Animal
from movements import Walking
from capabilities import Scheduleable

class Sheep(Animal, Walking, Scheduleable):
    def __init__(self, name, shift):
        Animal.__init__(self, name, 'Sheepalia', 'Steak')
        Walking.__init__(self, 20, 4)
        Scheduleable.__init__(self, shift)