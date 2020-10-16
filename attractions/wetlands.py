from attractions import Attraction

class Wetlands(Attraction):
    def __init__(self, name, description = ""):
        super().__init__(name, description)

    def add_animal(self, animal):
        try:
            if animal.swim_speed > -1:
                super().add_animal(animal)
        except AttributeError:
            print(f"{animal} cannot be put in {self.name} as it cannot swim")