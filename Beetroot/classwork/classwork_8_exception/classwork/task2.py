# Розширити написаний калькулятор добавивши до нього обробники помилок.

def make_operation(operator, *args):  # args містить рядоки замість чисел
    if args and check_numbers(args):
        if operator == '+':
            return sum(args)

        elif operator == '-':
            result = args[0]  # IndexError
            for i in range(len(args) - 1):
                result -= args[i + 1]
            return result

        elif operator == '*':
            result = 1
            for arg in args:
                result *= arg
            return result

        elif operator == '/':
            result = args[0]  # ZeroDivisionError
            for i in range(len(args) - 1):
                try:
                    result /= args[i + 1]
                except ZeroDivisionError:
                    continue
            return result

        else:
            print('Wrong operator, just + or - or * or /')
    else:
        print('No arguments or have a string')


def check_numbers(number_list):
    for number in number_list:
        if isinstance(number, str):
            return None
    return number_list


print(make_operation('/', 1, 2, 3, 0))


def checkout_error(number_list):
    try:
        for number in number_list:
            for symbol in ['[', ']', '(', ')', ',', '*']:
                if symbol in number:
                    raise TypeError
        for i in range(len(number_list)):
            if number_list[i].isalpha():
                raise ValueError
            else:
                number_list[i] = float(number_list[i])
    except TypeError:
        print('Введені дані є некоректиними')
        return []
    except ValueError:
        print('Не можемо перетворити символ у число')
        return []
    else:
        return number_list


if __name__ == '__main__':
    try:
        numbers = input('Введіть кількість аргументів: ')
        if numbers.isalpha():
            raise ValueError
        list_ = [input(f'Введіть {i + 1} аргумент: ') for i in range(int(numbers))]
        operator = input('Введіть оператор: ')
        list_ = checkout_error(list_)
        print(make_operation(operator, *list_))
    except ValueError:
        print('Ви ввели рядок замість числа')
