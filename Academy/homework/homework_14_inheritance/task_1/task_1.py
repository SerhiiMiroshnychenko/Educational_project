"""
Task 1
School
Make a class structure in python representing people at school.
Make a base class called Person, a class called Student,
and another one called Teacher. Try to find as many methods
and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example,
the name should be a Person attribute, while salary should only be available to the teacher.
"""
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


class Teacher(Student):
    def __init__(self, name: str, gender: str, age: int, height:float, width:int,
                 specialization:str, experience:int=0, salary:int=0):
        super().__init__(name, gender, age, height, width)
        self.specialization = specialization
        self.experience = experience
        self.salary = salary

    def go_school(self):
        print(f"I am going to my school. I work there as a {self.specialization} teacher.")

    def teaching(self):
        print(f'I have been teaching {self.specialization} for {self.experience} years.')

    def assign_homework(self):
        print(f"I'm assigning {self.specialization} homework to my students.")

    def check_homework(self):
        print(f"I'm checking my students' {self.specialization} homework.")

    def change_salary(self, new_salary):
        self.salary = new_salary
        print(f'I have changed my salary to {self.salary}.')

    def get_salary(self):
        print(f'I get my salary of {self.salary} dollars')

    @staticmethod
    def study():
        ...

    @staticmethod
    def do_homework():
        ...

    @staticmethod
    def pass_exam():
        ...

    def up_grade(self):
        ...

