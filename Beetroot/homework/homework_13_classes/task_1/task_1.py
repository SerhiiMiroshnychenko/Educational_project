# A Person class
# Make a class called Person. Make the __init__() method take firstname,
# lastname, and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from
# the person containing, for example like this: “Hello, my name is Carl
# Johnson and I’m 26 years old”.A Person class

class Person:
    gender_dict = {'male': 'man', 'female': 'woman', 'man': 'man', 'woman': 'woman'}
    def __init__(self, firstname: str=None, lastname: str=None, gender: str=None, age: int=None):
        self.firstname = firstname.capitalize() if firstname else ''
        self.lastname = lastname.capitalize() if lastname else ''
        self.fullname = f'{self.firstname} {self.lastname}' if firstname and lastname else self.firstname + self.lastname

        if not self.fullname:
            self.fullname = 'unknown'
        self.gender = gender if gender in self.gender_dict else None
        self.age = age or 'few'

    def talk(self):
        print(f'Hello, my name is {self.fullname} and'
              f' I’m a {self.gender_dict.get(self.gender, "person").lower()} of {self.age} years old.')

if __name__ == '__main__':
    serhii = Person('Serhii', 'Sternenko', 'male', 33)
    serhii.talk()
    viktoria = Person('viktoria', 'tkachenko', 'woman', 30)
    viktoria.talk()
    sasha = Person('sasha', 'BOGUN', 'druid', 25)
    sasha.talk()
    pasha = Person('pavlo', 'pavlenko')
    pasha.talk()
    grisha = Person('grygoriy', gender='man', age=45)
    grisha.talk()
    ivan = Person(lastname='Mazepa', gender='male', age=75)
    ivan.talk()
    anonim = Person()
    anonim.talk()