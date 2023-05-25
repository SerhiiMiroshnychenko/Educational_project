## Написати програму яка містить набір базових команд на копм'ютері
# (копіювати, вставити, вирізати,
# знайти, надрукувати)
# Зчитувати у користувача конктретну команду і виводити повідомлення
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


def computer():
    try:
        command_dict = {
            "copy": copy_,
            "insert": insert_,
            "cut": cut_,
            "find": find_,
            "print": print_,
        }
        print(command_dict[input('Введіть команду: ')]())
        return True
    except KeyError as err:
        print('Не визначена команда')
        return False


if __name__ == '__main__':  # вибачте, довелося використати один if :-)
    c = True
    while c:
        c = computer()
