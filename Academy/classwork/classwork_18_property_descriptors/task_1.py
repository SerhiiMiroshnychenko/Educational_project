# cтворити клас Student, який має два базових атрибути що описують студента, property що повертає його
# повне ім'я, staticmethod який для кожного студента повертає один і той самий університет,
# а також classmetod який повертає назву класу та прізвище (ім'я) студента. Бонус: створити документаційний рядок та
# вивести його.

class Student:
    def __init__(self, first: str, second: str):
        self.first = first.capitalize()
        self.second = second.capitalize()
        self.__info = f'{self.first} {self.second} is learning in {self.get_university()}'


    def __get_full(self):
        return f'{self.first} {self.second}'

    @property
    def info(self):
        return self.__info


    @staticmethod
    def get_university():
        return 'Harvard'

    @classmethod
    def get_information(cls):
        return cls.__name__

    full_name = property(
        fget = __get_full,
        doc="The student is really good!"
    )

s1 = Student('Boris', 'Jonson')
print(s1.full_name)
print(s1.get_information())
print(s1.get_university())
print(Student.full_name.__doc__)
print(s1.__class__.full_name.__doc__)
print(s1.get_university())
print(s1.info)
