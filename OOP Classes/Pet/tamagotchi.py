class Tamagotchi:
    def __init__(self, animal_type):
        self.animal_type = animal_type
        self.name = (input("Назвіть свого улюбленця: ")).title()
        self.health = 100  # здоров'я
        self.thirst = 0    # спрага
        self.hunger = 0    # голод
        self.mood = 50 + (self.health + (100 - self.thirst) + (100 - self.hunger)) // 3  # настрій
        self.life = (self.health + (100 - self.thirst) + (100 - self.hunger) + self.mood) // 4  # життя

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

    def play(self):
        if self.mood < 100:
            print(f"{self.name} грається!")
            self.mood += 1
        else:
            print(f"{self.name} вже веселий!")









