from prettytable import PrettyTable
from tamagotchi import Tamagotchi
from set_pet import get_pet_type, set_new_pet

print("Заведи улюбленця і доглядай його місяць.")

pet_type = None
pet = None
day = 0
get_pet_type()
set_new_pet()

while True:
    day += 1
    print(f"\n\t{pet_type} {pet.name.upper()}\tДЕНЬ {day}.")
    table = PrettyTable()
    table.field_names = ["Життя", "Здоров'я", "Спрага", "Голод", "Настрій"]









