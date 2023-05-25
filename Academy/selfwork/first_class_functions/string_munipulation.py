def lower(text):
    return text.lower()

def upper(text):
    return text.upper()

def capitalize(text):
    return text.capitalize()

def title(text):
    return text.title()

def swapcase(text):
    return text.swapcase()

def default():
    return 'Команда відсутня'


command_dict = {'lower': lower,
                'upper': upper,
                'capitalize': capitalize,
                'title': title,
                'swapcase': swapcase}

def string_it():
    print('Доступні команди:-> ', *command_dict.keys(), sep='   ')
    text = input('Введіть текст для перетворення: ')
    print(command_dict.get(input('Введіть команду: '), default)
          (text))

if __name__ == '__main__':
    for command in range(5):
        string_it()
