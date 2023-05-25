# Змоделювати поведінку "освітніх процесів".
# Використати модель персона-школяр-студент-працівник.
# В базовому класі реалізувати getter (отримання ім'я та ступеня)
# & setter (задання ступеня освіти),
# а в дочірніх класах перевизначити останній
# додавши перевірку на отримання попереднього ступеня).
class Person:
    _grade = 0
    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value


class School(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self._grade = self.grade

    @property
    def grade(self):
        if self.check_grade():
            self.up_grade()
        return self._grade

    @classmethod
    def check_grade(cls):
        return cls._grade == 0

    @classmethod
    def up_grade(cls):
        cls._grade += 1



class Student(School):
    def __init__(self, name: str):
        super().__init__(name)
        self._grade = self.grade

    @property
    def grade(self):
        if self.check_grade():
            self.up_grade()
        return self._grade

    @classmethod
    def check_grade(cls):
        return cls._grade == 1

class Worker(Student):
    def __init__(self, name: str):
        super().__init__(name)
        self._grade = self.grade

    @property
    def grade(self):
        if self.check_grade():
            self.up_grade()
        return self._grade

    @classmethod
    def check_grade(cls):
        return cls._grade == 2

c1 = School('Tom')
print(c1.grade)
c2 = Student('Anna')
print(c2.grade)
c3 = Worker('Toma')
print(c3.grade)
