# Розробити програму для введення обліку студентів в університеті.
# Програма має містити клас Університет та
# клас Студент. В Університеті має бути бюджет (приватна змінна),
# список доступних спеціальностей та список
# прикріплених студентів. В Сутенті має бути ім'я, спеціальність
# на якій навчається, список оцінок та навність
# стипендії зробити захищеними та приватними відповідно. До класу
# Університет необхідно добавити метод, який приймає
# студента на навчання та виділяює на нього кошти, а також метод
# що приймає фінансування від меценатів. У класі
# Студента необхідно створити геттер та сеттер для оцінок (отримання
# списку та додавання нової оцінки, з обмеженням
# в кількості). Як приклад застосування, створити екземпляр класу
# університету, студента та застосувати до них методи.

class Student:
    def __init__(self, name: str, specialty: str, stipend: float = 0):
        self.name = name
        self.specialty = specialty
        self._marks = []
        self.__stipend = stipend

    def get_marks(self):
        return self._marks

    def set_mark(self, mark):
        print(f'{self.name} отримав відмітку {mark}.')
        if len(self._marks) >= 15:
            del self._marks[0]
        self._marks.append(mark)
    def return_quality(self):
        if sum(self._marks) / len(self._marks) >= 4:
            return 'stipend'
        elif sum(self._marks) / len(self._marks) < 3:
            return 'very bad'
        else:
            return 'so so'
    def get_stipend(self):
        if self.return_quality() == 'stipend':
            print(f'{self.name} тепер отримує стипендію.')
            self.__stipend = 1000.0


class University:
    def __init__(self, name: str, specialties: list, budget: float):
        self.name = name
        self.specialties = specialties
        self.__budget = budget
        self._students = []

    def add_student(self, student: Student):
        if len(self._students) <= 100 and student.specialty in self.specialties:
            print(f'{student.name} поступив в Університет.')
            self._students.append(student)

    def del_student(self):
        for student in self._students:
            if student.return_quality() == 'very bad':
                print(f'{student.name} відчислений з Університет через погану успішність.')
                self._students.remove(student)


    def get_funds(self, amount):
        self.__budget += amount


if __name__ == '__main__':
    tom = Student('Tom', 'math')
    ben = Student('Ben', 'geography')
    harvard = University('Harvard', ['math', 'geography', 'medicine'], 100000.0)
    harvard.add_student(tom)
    harvard.add_student(ben)
    tom.set_mark(5)
    tom.set_mark(4)
    tom.set_mark(5)
    ben.set_mark(3)
    ben.set_mark(2)
    ben.set_mark(1)
    print(tom.get_marks())
    print(ben.get_marks())
    tom.get_stipend()
    harvard.del_student()





