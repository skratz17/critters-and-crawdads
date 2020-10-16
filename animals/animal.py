from datetime import date

class Animal:
    next_chip_number = 1

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        self.__chip_number = Animal.next_chip_number

        Animal.next_chip_number += 1

    def feed(self):
        print(f"{self.name} was fed {self.food} on {date.today().strftime('%m/%d/%Y')}")

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, num):
        raise AttributeError('Assignment to chip_number is restricted.')