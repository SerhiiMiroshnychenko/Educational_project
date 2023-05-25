# Створити абстрактну базу даних, що містить 3 класи, основний користувач,
# та два можливих профілі (читач або редактор)

class Reader:
    def __init__(self):
        self.read_only = True
        self.write_comments = True
        self.give_mark = False

    def create(self):
        print('Comment created')

    def set_mark(self, mark):
        print(f'Mark set to {mark}')




class Redactor:
    def __init__(self):
        self.read_only = False
        self.write_comments = False
        self.give_mark = True

    def create(self):
        print('Topic created')

    def set_mark(self, mark):
        print(f'Mark set to {mark}')


class User:
    def __init__(self, username, password, birth_data, first_name, last_name):
        self.username = username
        self.password = password
        self.birth_data = birth_data
        self.first_name = first_name
        self.last_name = last_name

    def create_reader_profile(self):
        self.profile = Reader()

    def create_redactor_profile(self):
        self.profile = Redactor()

    def create(self):
        self.profile.create()

    def set_mark(self, mark):
        self.profile.set_mark(mark)

if __name__ == '__main__':
    user1 = User('Tom15', '12345', '11.11.1991', 'Tom', 'White')
    user1.create_reader_profile()
    user1.create()
    user1.set_mark('quiz')
    user1.create_redactor_profile()
    user1.create()
    user1.set_mark('quiz')
