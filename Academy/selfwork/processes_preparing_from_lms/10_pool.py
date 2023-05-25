"""
The `Pool` class can be used to manage a fixed number of workers for simple
cases where the work to be done can be broken up and distributed between
the workers independently. The return values from the jobs are collected
and returned as a list. The pool arguments include the number of processes,
and a function to run when starting the task process (invoked once per child).

Клас `Pool` можна використовувати для простого керування фіксованою кількістю працівників
випадки, коли роботу, яку потрібно виконати, можна розділити та розподілити між ними
працівники самостійно. Повернені значення від завдань збираються
і повертається як список. Аргументи пулу включають кількість процесів,
і функція, яка запускається під час запуску процесу завдання
(викликається один раз для кожного дочірнього елемента).
"""
"""
POOL
"""
import multiprocessing
import time


def f(x):
    return x * x

def main():
    with multiprocessing.Pool(processes=4) as pool:
        result = pool.apply_async(f, (10,))  # evaluate "f(10)" asynchronously in a single process
        print(result.get(timeout=1))  # prints "100" unless your computer is *very* slow

        print(pool.map(f, range(10)))  # prints "[0, 1, 4,..., 81]"

        it = pool.imap(f, range(10))
        print(next(it))  # prints "0"
        print(next(it))  # prints "1"
        print(it.next(timeout=1))  # prints "4" unless your computer is *very* slow

        result = pool.apply_async(time.sleep, (10,))

        try:
            print(result.get(timeout=1))  # raises multiprocessing.TimeoutError
        except multiprocessing.context.TimeoutError as e:
            print(e.__class__, e)



if __name__ == "__main__":
    main()