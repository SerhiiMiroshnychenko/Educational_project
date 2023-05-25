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


#schoolchild
class Schoolchild(Person):
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

class Student(Person):
    def __init__(self, name: str, gender: str, age: int, height:float, width:int, specialization:str, year: int=1):
        super().__init__(name, gender, age, height, width)
        if 1 <= year <= 5:
            self.year = year
        elif year > 5:
            self.year = 5
        else:
            self.year = 1
        self.special = specialization


    def study(self):
        print(f"I'm studying {self.special}")

    def go_school(self):
        print(f"I am going to my University. I am in my first {self.year} of University.")

    @staticmethod
    def do_homework():
        print("I am doing my homework.")

    @staticmethod
    def pass_exam():
        print("I am passing the exam.")

    def up_grade(self):
        if self.year < 5:
            self.year += 1
            print(f'I am in my first {self.year} of University.!')
        else:
            print('I graduated from the University!')

class Teacher(Schoolchild):
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


if __name__ == '__main__':
    junior = Person('Junior', 'boy', 5, 1.1, 15)
    junior.speak()
    junior.eat()
    junior.sleep()
    sarah = Schoolchild('Sarah', 'girl', 15, 1.5, 50, 9)
    sarah.speak()
    sarah.go_school()
    sarah.love('bill')
    sarah.love('tom')
    sarah.up_grade()
    amanda = Student('Amanda', 'women', 25, 1.7, 60, 'math', 1)
    amanda.speak()
    amanda.study()
    amanda.pass_exam()
    amanda.go_school()
    barbara = Teacher('Barbara', 'women', 35, 1.7, 60, 'math', 1, 5000)
    barbara.speak()
    barbara.study()
    barbara.pass_exam()
    barbara.go_school()
    barbara.teaching()
    barbara.get_salary()
