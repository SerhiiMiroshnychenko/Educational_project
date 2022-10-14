class Tamagotchi:
    def __init__(self, animal_type):
        self.animal_type = animal_type
        self.name = None
        self.thirst = 0  # спрага
        self.hunger = 0  # голод
        self.health = 100  # здоров'я
        self.life = (self.health + (100 - self.thirst) + (100 - self.hunger)) // 3  # життя

    def set_name(self):
        self.name = (input("Назвіть свого улюбленця: ")).title()

    def drink(self):
        if self.thirst > 0:
            print(f"{self.name} п'є...")
            self.thirst -= 1
        else:
            print(f"{self.name} не хоче пити!")

    def eat(self):
        if self.hunger > 0:
            print(f"{self.name} їсть...")
            self.hunger -= 1
        else:
            print(f"{self.name} не голодний!")









