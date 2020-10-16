from attractions import Attraction

class SnakePit(Attraction):
    def __init__(self, name, description = ""):
        super().__init__(name, description)
    
    def add_animal(self, animal):
        try:
            if animal.slither_speed > -1:
                super().add_animal(animal)
        except AttributeError:
            print(f"{animal} does not slither and cannot live in {self.name}")