## Написати програму яка містить набір базових команд на комп'ютері
# (копіювати, вставити, вирізати,
# знайти, надрукувати)
# Зчитувати у користувача конкретну команду і виводити повідомлення
# на екран. Не використовувати if та match.

def copy_():
    return 'Я копіюю'


def insert_():
    return 'Я вставляю'


def cut_():
    return 'Я вирізаю'


def find_():
    return 'Я знаходжу'


def print_():
    return 'Я друкую'

def default():
    return 'Не відома функція'


def computer():
        command_dict = {
            "copy": copy_,
            "insert": insert_,
            "cut": cut_,
            "find": find_,
            "print": print_,
        }
        print(func:=command_dict.get(input('Введіть команду: '), default)())


if __name__ == '__main__':  # вибачте, довелося використати один if :-)
    for count in range(6):
        computer()
