from animals import Animal
from movements import Swimming

class Pirahna(Animal, Swimming):
    def __init__(self, name):
        Animal.__init__(self, name, 'Pirahnalia', 'secret agents')
        Swimming.__init__(self, 16, 250)