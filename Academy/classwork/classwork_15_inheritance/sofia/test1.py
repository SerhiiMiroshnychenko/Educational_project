# Створити абстрактну базу даних, що містить 3 класи, основний користувач,
# та два можливих профілі (читач або редактор)

class Reader:
    def __init__(self):
        self.read_only = True
        self.write_comments = True
        self.give_mark = True

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
    def __init__(self, username, password, birth_date, first_name, last_name):
        self.username = username
        self.password = password
        self.birth_date = birth_date
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
    user = User('SofiaBeetroot', 'qwerty', '01/10/1999', 'Sofia', 'Orzhekhovska')
    user.create_reader_profile()
    user.create()
    user.set_mark(5)
    user.create_redactor_profile()
    user.create()
    user.set_mark(5)

