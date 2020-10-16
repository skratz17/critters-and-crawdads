from animals import Animal
from movements import Walking
from capabilities import Scheduleable

class Donkey(Animal, Walking, Scheduleable):
    def __init__(self, name, shift):
        Animal.__init__(self, name, "Donkinalia", "cans")
        Walking.__init__(self, 100, 4)
        Scheduleable.__init__(self, shift)