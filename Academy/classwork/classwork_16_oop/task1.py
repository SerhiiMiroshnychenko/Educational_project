# Створити модель поведінки працівників IT
# (Junior, Middle, Senior, TeamLead) використавши поліморфізм

class Person:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city
    def work(self):
        print(f'{self.name.capitalize()} is searching a job.')

class Junior(Person):
    def work(self):
        print(f'My name {self.name.capitalize()}. I try to work, but something I need help')

    def relax(self):
        print(f'{self.name.capitalize()} is relaxing')


class Middle(Person):

    def work(self):
        print(f'My name {self.name.capitalize()}. I am working.')

    def relax(self):
        print(f'{self.name.capitalize()} relaxes very little.')

class Senior(Person):

    def work(self):
        print(f'My name {self.name.capitalize()}. I work hard.')

    def relax(self):
        print(f'{self.name.capitalize()} has no time to relax.')

class TeamLead(Person):

    def work(self):
        print(f'My name {self.name.capitalize()}. I just give task.')

    def relax(self):
        print(f'{self.name.capitalize()} relaxes all time.')

