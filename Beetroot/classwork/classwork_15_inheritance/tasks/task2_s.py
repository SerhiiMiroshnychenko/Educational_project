"""
Задача. Створити освітню ієрархію класів.
Клас Person. Описує людину.
Клас Школярик.
Клас Студента.
Клас Робітника.
"""


class Person:
    def __init__(self, name: str, age: int, sex: str):
        self.age = age
        self.sex = sex
        self.name = name

    def birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}")


class Pupil(Person):
    def __init__(self, name: str, age, sex, c_no, school):
        super().__init__(name, age, sex)
        self.c_no = c_no
        self.school = school


class Student(Person):
    def __init__(self, name: str, age, sex, course, uni):
        super().__init__(name, age, sex)
        self.course = course
        self.uni = uni


class Worker(Person):
    def __init__(self, name: str, age, sex, job, experience):
        super().__init__(name, age, sex)
        self.job = job
        self.experience = experience


seva = Student('Seva', 35, 'm', 'Python', 'Beetroot')
print(seva.__dict__)
seva.birthday()
print(seva.__dict__)
