class Person:
    def __init__(self, first_name:str, last_name:str):
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    @property
    def full_name(self):
        return f'{self.first_name.title()} {self.last_name.title()}'

    @property
    def initials(self):
        return self.first_name[0].upper() + self.last_name[0].upper()

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first.title()
        self.last_name = last.title()

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None
        print('Deleted')


cj = Person('carl', 'johnson')
print(cj.full_name)
print(cj.initials)

cj.first_name = 'bOris'
print(cj.full_name)
print(cj.initials)

try:
    cj.full_name = 'Rishi Sunak'
    print(cj.first_name)
    print(cj.full_name)
    print(cj.initials)
except AttributeError as e:
    print(e)

del cj.full_name
print(cj.first_name, cj.last_name)




