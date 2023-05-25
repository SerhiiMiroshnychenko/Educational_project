class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.__salary = salary

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.__salary)


# creating object of a class
emp = Employee('Jessa', 10000)

# accessing public data members
# print("Name: ", emp.name, 'Salary:', emp.__salary)

# calling public method of the class
# emp.show()


# direct access to private member using name mangling
# print('Salary:', emp._Employee__salary)


# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"


# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)
        # super().__init__()

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)


# c = Employee("Jessa")
# c.show()
#
# # Direct access protected data member
# print('Project:', c._project)


class Student:
    def __init__(self, name, age):
        # private member
        self.name = name
        self.__age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        if age < 6:
            print('Too young')
        else:
            self.__age = age


stud = Student('Jessa', 14)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())

# changing age using setter
# stud.__age = -1
stud.set_age(-1)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())
stud.set_age(15)
print('Name:', stud.name, stud.get_age())
