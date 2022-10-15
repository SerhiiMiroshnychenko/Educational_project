class Tamagotchi:
    def __init__(self, animal_type):
        self.animal_type = animal_type
        self.name = (input("Назвіть свого улюбленця: ")).title()
        self.health = 100  # здоров'я
        self.thirst = 0    # спрага
        self.hunger = 0    # голод
        self.tired = 0     # втома
        self.mood = 50 + (self.health + (100 - self.thirst) + (100 - self.hunger) + (100 - self.tired)) // 8  # настрій
        self.life = (self.health + (100 - self.thirst) + (100 - self.hunger) + (100 - self.tired) + self.mood) // 5

    def drink(self):
        if self.thirst > 0:
            print(f"{self.name} п'є...")
            self.thirst -= 5
        else:
            print(f"{self.name} не хоче пити!")

    def eat(self):
        if self.hunger > 0:
            print(f"{self.name} їсть...")
            self.hunger -= 5
        else:
            print(f"{self.name} не голодний!")

    def play(self):
        if self.mood < 100:
            print(f"{self.name} грається!")
            self.mood += 5
        else:
            print(f"{self.name} вже веселий!")

    def sleep(self):
        if self.tired > 0:
            print(f"{self.name} спить...")
            self.tired -= 5
        else:
            print(f"{self.name} не втомився!")

    def command(self):
        command = input("Твоя команда: ")
        if command in "DEPSdeps":
            if command.upper() == 'D':
                return self.drink()
            elif command.upper() == 'E':
                return self.eat()
            elif command.upper() == 'P':
                return self.play()
            elif command.upper() == 'S':
                return self.sleep()
        else:
            print("Використовуйте тільки літери DEPS.")

    def finish_day(self):
        self.thirst += 1
        self.hunger += 1
        self.tired += 1
        self.mood -= 2
        self.life = (self.health + (100 - self.thirst) + (100 - self.hunger) + (100 - self.tired) + self.mood) // 5







