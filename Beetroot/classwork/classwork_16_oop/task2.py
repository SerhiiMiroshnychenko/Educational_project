from random import choice

class Person:
    head = 1
    body = 1
    hand = 2
    leg = 2
    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.gender = gender
        self.age = age
        self.love_time = 0

    def __str__(self):
        return f"Here is {self.name.capitalize()}!"

class Baby(Person):
    ...

class Adult(Baby):
    def __init__(self,name: str, gender: str, age: int, baby = None):
        super().__init__(name, gender, age)
        self.baby = baby

    def __add__(self, other):
        if self.gender == 'female' and self.gender != other.gender:
            name = input('Babies name:')
            gender = choice(['male', 'female'])
            self.baby = Baby(name, gender, 0)
            print(self.baby.__str__())
            return self.baby

if __name__ == '__main__':
    viktoria = Adult('Victoria', 'female', 30)
    viktor = Adult('Victor', 'male', 35)
    baby = viktoria.__add__(viktor)

