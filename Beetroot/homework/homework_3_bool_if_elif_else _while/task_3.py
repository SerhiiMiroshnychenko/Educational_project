# Task 3 - The math quiz program.
# Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong, and then responds with a message accordingly.

import random


def quiz():
    """The math quiz function"""
    how_much_numbers = random.randint(2, 5)
    task = str(random.randint(0, 9))
    for variant in range(1, how_much_numbers):
        operator = random.choice(['+', '-', '*', '/', '//', '%', '**'])
        if operator in ['/', '//']:
            number = str(random.randint(1, 9))
        else:
            number = str(random.randint(0, 9))
        task += operator + number
    result = eval(task)
    return task, result


print('Математична вікторина! (для виходу введіть "q")')
while True:
    expression = quiz()
    answer = input(f'Введіть результат розрахунку: {expression[0]} = ')
    if answer == 'q':
        break
    print('Все вірно! Ще один:' if answer == str(expression[1])
          else f'Не вірно... Правильна відповідь: {expression[1]} Ще один:')

