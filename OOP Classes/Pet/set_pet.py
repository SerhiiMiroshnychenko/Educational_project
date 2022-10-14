import json
from tamagotchi import Tamagotchi

pet_type = None


def get_pet_type():
    """Повертає тип тваринки."""
    global pet_type
    if not pet_type:
        pet_type = input("Яку тваринку бажаєте? Введіть вид: ")
    return pet_type





