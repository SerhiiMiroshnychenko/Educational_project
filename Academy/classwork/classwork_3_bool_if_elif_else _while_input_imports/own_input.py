# Створити модуль для роботи з різними типами даних, що вводяться з клавіатури
# 1. Звичайне читання
# 2. Читання цілих чисел
# 3. Читання десяткових чисел
# 4. Читання тексту та розділення його на слова (за розділовими знаками ".", ",", "-")
# 5. Читання списку чисел розділених комами (поєднати перетворення на ціле та десяткове)

def str_input():
    return input('Enter sentence: ')


def int_input(number):
    if number.isnumeric():
        return int(number)
    else:
        print('Error')
        return None


def float_input(number):
    number_without_point = number.replace('.', '')
    if number_without_point.isnumeric() and '.' in number:
        return float(number)
    else:
        print('Error')
        return None


def text_input(text):
    text = text.replace('.', ' ').replace(',', ' ').replace('-', ' ').replace('  ', ' ')
    return text.split(' ')


def numbers_input(numbers):
    numbers = numbers.split(',')
    for position in range(len(numbers)):
        if '.' in numbers[position]:
            numbers[position] = float_input(numbers[position])
        else:
            numbers[position] = int_input(numbers[position])
    return numbers
