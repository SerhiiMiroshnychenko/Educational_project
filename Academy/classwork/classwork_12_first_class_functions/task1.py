def computer():
    try:
        command_dict = {
            "copy": lambda: print('Я копіюю'),
            "insert": lambda: print('Я вставляю'),
            "cut": lambda: print('Я вирізаю'),
            "find": lambda: print('Я знаходжу'),
            "print": lambda: print('Я друкую'),
        }
        command_dict[input('Введіть команду: ')]()
        return True
    except KeyError as err:
        print('Не визначена команда')
        return False


if __name__ == '__main__':  # вибачте, довелося використати один if :-)
    c = True
    while c:
        c = computer()
