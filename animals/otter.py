from animals import Animal
from movements import Swimming, Walking

class Otter(Animal, Swimming, Walking):
    def __init__(self, name):
        Animal.__init__(self, name, "Otteralia", "cheetos")
        Swimming.__init__(self, 8, 10)
