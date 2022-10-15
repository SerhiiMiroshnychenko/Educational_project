from tamagotchi import Tamagotchi


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
