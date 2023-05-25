# Створити клас База даних, що має 4 атрибути: назву, пароль та список дат підключень, і параметер що
# відповідає за її наповнення. Створити контекстний менеджер для роботи з базою данних - відкриття бази,
# підключення, запис даних та її закриття.
import datetime
class DataBase:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = []
        self.connection_list = []
        self.connected = False

    def __enter__(self):
        self.connection_list.append(datetime.datetime.now())
        return self

    def connection(self, username, password):
        if username == self.username and password == self.password:
            self.connected = True
        else:
            raise ValueError('No connection.')

    def write(self, data):
        if self.connected:
            self.data.append(data)

    def __exit__(self, exc_type, exc_value, trace):
        if exc_type:
            print(exc_type, exc_value, trace)
        else:
            print('Date base closed.')
        self.connected = False

if __name__ == '__main__':
    with DataBase('Serhii', '123') as db:
        db.connection('Serhii', '123')
        db.write('Beetroot')
        print(db.data)
        print(db.connection_list)
