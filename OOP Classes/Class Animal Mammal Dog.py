class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} дихає")

    def drink(self):
        print(f"{self.name} п'є")

    def eat(self):
        print(f"{self.name} їсть")

    def move(self):
        print(f"{self.name} рухається")

    def multiply(self, child_name):
        child = Animal(child_name)
        print(f"{self.name} народжує нащадка {child_name}")
        return child


class Mammal(Animal):
    def feed(self):
        print(f"{self.name} годує дитину молоком")

    def multiply(self, child_name):
        child = Mammal(child_name)
        print(f"{self.name} народжує нащадка {child_name}")
        return child


class Dog(Mammal):
    def bark(self):
        print(f"{self.name} гавкає")

    def multiply(self, child_name):
        child = Dog(child_name)
        print(f"{self.name} народжує нащадка {child_name}")
        return child
