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


get_pet_type()
set_new_pet()
print(pet.__dict__)
get_pet_type()
set_new_pet()
print(pet.__dict__)
pet = None
pet_type = None
get_pet_type()
set_new_pet()
print(pet.__dict__)





