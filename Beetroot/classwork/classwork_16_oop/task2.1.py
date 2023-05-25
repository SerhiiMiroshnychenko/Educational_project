# Розробити програму для введення обліку студентів в університеті. Програма має містити клас Університет та
# клас Студент. В Університеті має бути бюджет (приватна змінна), список доступних спеціальностей та список
# прикріплених студентів. В Сутенті має бути ім'я, спеціальність на якій навчається, список оцінок та навність
# стипендії зробити захищеними та приватними відповідно. До класу Університет необхідно добавити метод, який приймає
# студента на навчання та виділяює на нього кошти, а також метод що приймає фінансування від меценатів. У класі
# Студента необхідно створити геттер та сеттер для оцінок (отримання списку та додавання нової оцінки, з обмеженням
# в кількості). Як приклад застосування, створити екземпляр класу університету, студента та застосувати до них методи.


class University:
    def __init__(self):
        self.__budget = 1000000
        self.specialty_list = ['Прикладна математика', 'Економіка', 'Архітектура', 'Право', 'Теплоенергетика']
        self._student_list = []

    def apply_student(self):
        pass

    def get_funds(self, amount):
        pass


class Student:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self._marks = [] # (Предмет, оцінка) / {предмет: [список оцінок]}
        self.__scholarship = False

    def get_marks(self):
        # Відформатоване виведення
        pass

    def set_mark(self):
        # Обмеження - не більше 15 оцінок
        pass

    def go_to_scholarship(self):
        # if 80% > marks - 5
        pass