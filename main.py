from animals import Dolphin, Donkey, Goat, Horse, Llama
from animals import Marlin, Otter, Pirahna, Python, Shark
from animals import Sheep, Slug, Worm

from attractions import PettingZoo, SnakePit, Wetlands

dolphin = Dolphin('dolphiny')
donkey = Donkey('donky', 'morning')
goat = Goat('goaty', 'morning')
horse = Horse('horsy', 'midday')
llama = Llama('llammy', 'afternoon')
marlin = Marlin('marliny')
otter = Otter('otty')
pirahna = Pirahna('pirahny')
python = Python('pythony')
shark = Shark('sharky')
sheep = Sheep('sheepy', 'afternoon')
slug = Slug('sluggy')
worm = Worm('wormy')

pet_palace = PettingZoo('Pet Palace', 'A place to pet all of your pettable friends')
slither_spot = SnakePit('Slither Spot', 'Probably could have come up with some better alliteration')
wet_world = Wetlands('Wet World', 'It is very wet here')

pet_palace.add_animal(donkey)
pet_palace.add_animal(goat)
pet_palace.add_animal(horse)
pet_palace.add_animal(llama)
pet_palace.add_animal(sheep)

slither_spot.add_animal(python)
slither_spot.add_animal(slug)
slither_spot.add_animal(worm)

wet_world.add_animal(dolphin)
wet_world.add_animal(marlin)
wet_world.add_animal(otter)
wet_world.add_animal(pirahna)
wet_world.add_animal(shark)

print(pet_palace)
print(slither_spot)
print(wet_world)