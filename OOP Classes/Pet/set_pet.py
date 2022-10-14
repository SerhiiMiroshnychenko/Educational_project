from tamagotchi import Tamagotchi

pet_type = None


def set_pet_type(type_your_pet):
    if not type_your_pet:
        type_your_pet = input("Обери, яку тваринку бажаєш: ")
        return type_your_pet
    else:
        return None


def set_pet(type_your_pet):
    if type_your_pet:
        new_pet = Tamagotchi(type_your_pet)
        return new_pet
    else:
        pass


your_pet = set_pet(set_pet_type(pet_type))
print(your_pet.__dict__)

