class Attraction: # attraction more like abstraction
    def __init__(self, name, description = ""):
        self.name = name
        self.description = description
        self.__animals = list()

    def __str__(self):
        lines = [ 
            f"{self.name} - {self.description}",
            "~~~~~~~~~~~~",
            "Inhabitants:"
        ]
        lines = lines + [ f"\t{str(animal)}" for animal in self.__animals ]
        return "\n".join(lines)

    def add_animal(self, animal):
        self.__animals.append(animal)
        print(f"{animal} now lives in {self.name}")

    @property
    def last_animal_added(self):
        return self.__animals[-1]