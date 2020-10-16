from animals import Animal
from movements import Walking
from capabilities import Scheduleable

class Goat(Animal, Walking, Scheduleable):
    def __init__(self, name, shift):
        Animal.__init__(self, name, 'Goatalia', 'a apple')
        Walking.__init__(self, 12, 4)
        Scheduleable.__init__(self, shift)

    def feed(self):
        print(f"Bah bah feed the goat named {self.name}")