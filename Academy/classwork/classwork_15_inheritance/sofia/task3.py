# Створити абстрактну базу даних, що містить 3 класи, основний користувач,
# та два можливих профілі (читач або редактор)

class User:
    def __init__(self, username, password, birth_day, gender):
        self.username = username
        self.password = password
        self.birth_day = birth_day
        self.gender = gender
        self.profile = None

    def create_reader_profile(self):
        if self.profile is None:
            self.profile = Reader()
        else:
            print('Profile has been already created')

    def create_redactor_profile(self):
        if self.profile is None:
            self.profile = Redactor()
        else:
            print('Profile has been already created')

    def create_topic(self):
        if not self.profile.read_only:
            self.profile.create()
        else:
            print('You are not redactor')

    def create_comments(self):
        if self.profile.read_only:
            self.profile.create()
        else:
            print('You are not reader')

    def set_mark(self):
        self.profile.set_mark(5)


class Reader:
    def __init__(self):
        self.read_only = True
        self.give_mark = True
        self.write_comments = True

    def create(self):
        print('Comment created')

    def set_mark(self, point):
        print(f'This topic achieved {point} points')


class Redactor:
    def __init__(self):
        self.read_only = False
        self.give_mark = True
        self.write_comments = False

    def create(self):
        print('Create topic')

    def set_mark(self, point):
        print(f'This topic achieved {point} points')


user = User('Sofia', 'qwerty', '01/10/1999', 'female')
user.create_reader_profile()
user.create_redactor_profile()
user.create_comments()
user.create_topic()
user.set_mark()
