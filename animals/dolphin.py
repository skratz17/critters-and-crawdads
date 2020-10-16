from animals import Animal
from movements import Swimming

class Dolphin(Animal, Swimming):
    def __init__(self, name):
        Animal.__init__(self, name, "Dolphinalia", "minnows")
        Swimming.__init__(self, 25, 1000)