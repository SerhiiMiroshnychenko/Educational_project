import calendar


class Person:
    def __init__(self, name, sex ):
        self.name = name
        self.sex = sex
        self.status = False # Walk or not

    def walk(self):
        self.status = True
        print(f'{self.name} walking')

    def lie_down(self):
        self.status = False
        print(f'{self.name} lie down')

    def call(self):
        if self.name == "Max":
            print(f"Yeh, you are right, my name is {self.name}")


class Schoolboy(Person):
    def __init__(self, name, sex, school_bag):
        super().__init__(name, school_bag)
        self.school_bag = school_bag

    def go_to_school(self):
        print(f'O, you have a {self.school_bag}, you are ready go to school')


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.age = age

    def first_party(self):
        if self.age > 18:
            print('Today party hard')
        else:
            print("Mom said - 'No alcohol under 18'")


class Worker(Person):
    def __init__(self, name, age, work_place, day):
        super().__init__(name, age)
        self.work_place = work_place
        self.day = day

    def my_work(self):
        if self.day in list(calendar.day_name)[:5]:
            print(f"NOOOO it's {self.day}, another work day in {self.work_place}")
        else:
            print("Happy weekend")


if __name__ == '__main__':
    per = Person('maks', 'm')
    per.walk()
    per.lie_down()
    per.call()
    pupil = Schoolboy('maks', 'm', "School bag")
    pupil.go_to_school()
    stud = Student("maks", 20)
    stud.first_party()
    old = Worker("maks", 20, "McDonald's", 'Friday')
    old.my_work()