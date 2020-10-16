from attractions import Attraction

class PettingZoo(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal(self, animal):
        try:
            if animal.walk_speed > -1:
                super().add_animal(animal)
        except AttributeError as ex:
            print(f"{animal} cannot be put into the petting zoo as it cannot walk")