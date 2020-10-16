from animals import Animal
from movements import Walking
from capabilities import Scheduleable

class Horse(Animal, Walking, Scheduleable):
    def __init__(self, name, shift):
        Animal.__init__(self, name, 'Horsealia', 'crabapple')
        Walking.__init__(self, 500, 4)
        Scheduleable.__init__(self, shift)