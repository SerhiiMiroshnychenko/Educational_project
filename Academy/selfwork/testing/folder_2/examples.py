class Person:
    head = 1
    body = 1
    hand = 2
    leg = 2
    def __init__(self, name: str, gender: str, age: int, height:float, width:int):
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height
        self.width = width
        self.love_time = 0
    @staticmethod
    def breathe():
        print("I'm breathing.")

    @staticmethod
    def drink():
        print("I'm drinking.")

    def eat(self):
        print(f"I'm eating. My width is also {self.width} kg.")

    def sleep(self):
        print(f"I'm sleeping. When I sleep I grow. I am already {self.height} m tall!")

    @staticmethod
    def move():
        print("I'm moving.")

    def speak(self):
        print(f'Hello, my name is {self.name} and'
              f' I’m a {self.gender} of {self.age} years old.')

    def love(self, honey_name: str):
        self.love_time += 1
        print(f'I love {honey_name.capitalize()}! I am {self.love_time} time in love!')

class Student(Person):
    def __init__(self, name: str, gender: str, age: int, height:float, width:int, grade: int=1):
        super().__init__(name, gender, age, height, width)
        if 1 <= grade <= 12:
            self.grade = grade
        elif grade > 12:
            self.grade = 12
        else:
            self.grade = 1

    @staticmethod
    def study():
        print("I'm studying.")

    def go_school(self):
        print(f"I am going to my school. I'm already in the {self.grade} grade.")

    @staticmethod
    def do_homework():
        print("I am doing my homework.")

    @staticmethod
    def pass_exam():
        print("I am passing the exam.")

    def up_grade(self):
        if self.grade < 12:
            self.grade += 1
            print(f'I went to the {self.grade} grade!')
        else:
            print('I graduated from school!')


class Dog:
    age_factor = 7
    def __init__(self, dog_name:str, dog_age:int):
        self.dog_name = dog_name.capitalize()
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * self.age_factor