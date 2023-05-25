# Write a Python program to detect the number of local variables declared in a function.
def show_locals(function):
    """Show the local variables of a function"""
    name = function.__name__
    vars_number = function.__code__.co_nlocals
    local_vars = function.__code__.co_varnames
    print(f'Кількість локальних змінних у функції <{name}>: {vars_number} шт.\nА саме: {local_vars}')
