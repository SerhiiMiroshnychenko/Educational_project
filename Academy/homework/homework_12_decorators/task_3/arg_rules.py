"""Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some rules' checks returns False, the function should return False
and print the reason it failed; otherwise, return the result."""

def arg_rules(max_length: int, type_: type, contains: list):
    def arg_rules_decor(func):
        from functools import wraps
        @wraps(func)
        def wrapper(arg):
            result = f''
            counter = 0
            try:
                if type(arg) != type_:
                    counter += 1
                    result += f'{counter}. Не відповідний тип переданого аргументу: {type(arg)}.\n'
                if len(arg) > max_length:
                    counter += 1
                    result += f'{counter}. Завелика довжина переданого аргументу: {len(arg)}.\n'
                chars = []
                for char in contains:
                    if char not in arg:
                        chars.append(char)
                if chars:
                    counter += 1
                    result += f'{counter}. У переданому аргументі не вистачає {chars}.\n'
            except TypeError as error:
                counter += 1
                result += f'{counter}. Помилка: {error.__class__}. Причина: {error}.\n'
            if result != f'':
                print('Звіт про помилки:\n' + result)
                return False
            else:
                return func(arg)

        return wrapper

    return arg_rules_decor
