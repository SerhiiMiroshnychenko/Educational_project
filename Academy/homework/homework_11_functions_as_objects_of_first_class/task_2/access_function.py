# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)
def access_function(f_out, arg=None):
    """The function to access a function inside a function"""
    f_in = f_out(lambda x: x)
    print(f'Функція <{f_out.__name__}> містить в собі функцію <{f_in.__name__}>')
    if arg:
        print(f'Результат виклику функції {f_in.__name__}({arg}) =  {f_in(arg)}')
        result = f_in(arg)
    else:
        print(f'Результат виклику функції {f_in.__name__}() = ', end='')
        f_in()
        result = None
    return result

"""
Де:
    f_out -> досліджувана функція, яка містить в собі іншу функцію
            (повинна приймати як аргументи іншу функцію та інші аргументи)
    f_in -> внутрішня функція, до функціоналу якої ми хочемо отримати доступ
            (змінює аргумент переданий в f_out та передає в функцію-аргумент)
    return f_in(arg) -> дозволяє зберегти результат роботи внутрішньої функції
                        в змінну
"""