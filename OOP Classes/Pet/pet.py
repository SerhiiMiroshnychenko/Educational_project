from prettytable import PrettyTable
from tamagotchi import Tamagotchi


pet_type = None
pet = None


def get_pet_type():
    """Повертає тип тваринки."""
    global pet_type
    if not pet_type:
        pet_type = input("Яку тваринку бажаєте? Введіть вид: ")
    return pet_type


def set_new_pet():
    """Створює нову тваринку."""
    global pet, pet_type
    if pet_type and not pet:
        pet = Tamagotchi(pet_type)
        return pet
    else:
        pass


print("Заведи улюбленця і доглядай його місяць.")
day = 0
while True:
    get_pet_type()
    set_new_pet()
    day += 1
    print(f"\n\t{pet_type} {pet.name.upper()}\tДЕНЬ {day}.")
    table = PrettyTable()
    table.field_names = ["Життя", "Здоров'я", "Спрага", "Голод", "Настрій", "Втома"]
    table.add_row([pet.life, pet.health, pet.thirst, pet.hunger, pet.mood, pet.tired])
    print(table)
    print(f"\nОбери активності свого улюбленця:")
    print(f"""D(drink) - пити, E(eat) - їсти, P(play) - грати, S(sleep) - спати.""")
    pet.command()
    pet.finish_day()











