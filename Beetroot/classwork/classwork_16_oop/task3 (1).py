class University:
    def __init__(self, name: str, initial_budget: int):
        self.name = name
        self._budget = initial_budget
        self.spec = ['Engineering', 'Law', 'Medicine', 'Computer Science']
        self._students = []

    def admit(self, student):
        if student.spec in self.spec:
            self._students.append(student)
            self._budget -= 420
            print(f'{student.name} was admitted to {self.name}')
        else:
            print("Sorry, we don't have that speciality!")

    def patreon(self, money: int):
        self._budget += money
        print(f'{self.name} received {money} UAH from a patron.')

    def get_budget(self):
        print(f'{self.name} has {self._budget} UAH')

    def get_students(self):
        if self._students:
            print(self.name, 'students:')
            for student in self._students:
                print(' ', '-', student.name)
        else:
            print('No students yet!')


class Student:
    def __init__(self, name: str, spec: str, has_scholarship: bool):
        self.name = name
        self._scholarship = has_scholarship
        self.__marks = dict()
        self.spec = spec

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

    def get_marks(self):
        return self.__marks

    def add_mark(self):
        subj = input("Which subject? ")
        mark = int(input(f"Which mark did {self.name} get? "))
        self.__marks.setdefault(subj, list())
        if len(self.__marks[subj]) < 10:
            self.__marks[subj].append(mark)
            print('Mark added')
        else:
            print('Too much marks already!')

    def marks(self):
        print(self.name, 'has these marks:')
        for i in self.__marks.keys():
            print(' ', i, end=': ')
            print(', '.join(str(j) for j in self.__marks[i]))
            # print()


def main():
    nlao = University('NLAO', 1_000_000)
    seva = Student('Seva', 'Law', False)
    nlao.get_budget()
    nlao.patreon(69_420)
    nlao.get_budget()
    nlao.admit(seva)
    nlao.get_budget()
    nlao.get_students()
    seva.add_mark()
    seva.add_mark()
    seva.add_mark()
    seva.marks()


if __name__ == "__main__":
    main()
