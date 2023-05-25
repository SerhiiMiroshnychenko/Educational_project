# Створити модель поведінки працівників IT (Junior, Middle, Senior, TeamLead) використавши поліморфізм

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def work(self):
        print('Searching for job')

class Junior(Person):
    def work(self):
        print('I try to work, but sometimes I need help')

    def relax(self):
        print('Relaxing with my coworkers')


class Middle(Person):
    def work(self):
        print('I am working, but sometimes I googling')

    def relax(self):
        print('Relaxing with my computer')


class Senior(Person):
    def work(self):
        print('I work hard now')

    def relax(self):
        print('No time to relax')


class TeamLead(Person):
    def work(self):
        print('Just give tasks')

    def relax(self):
        print('Relaxing more')


j = Junior('My name', 22, 'Rivne')
m = Middle('Mid', 30, 'Kyiv')
s = Senior('Frank', 32, 'Lviv')
t = TeamLead('Leo', 28, 'Rivne')

for worker in [j, m, s, t]:
    worker.work()
    worker.relax()