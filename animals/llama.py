from animals import Animal
from movements import Walking
from capabilities import Scheduleable

class Llama(Animal, Walking, Scheduleable):
    def __init__(self, name, shift):
        Animal.__init__(self, name, 'Llamalia', 'wheat')
        Walking.__init__(self, 15, 4)
        Scheduleable.__init__(self, shift)