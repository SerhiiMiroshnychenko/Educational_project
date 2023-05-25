"""
Виконуючи паралельне програмування, як правило,
краще уникати використання спільного стану, наскільки
 це можливо. Це особливо актуально при використанні кількох процесів.

Однак, якщо вам дійсно потрібно використовувати спільні дані,
 багатопроцесорна обробка надає кілька способів зробити це.

Аргументи «d» і «i», які використовуються під час створення
змінних num і arr, є кодами типу, які використовуються модулем
масиву: «d» вказує на число з точкою що плаває подвійної точності,
а «i» вказує на ціле число зі знаком. Ці спільні об'єкти будуть
безпечними для процесів і потоків.
"""

import multiprocessing

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

def main():
    print(num.value)
    print(arr[:])

    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])


if __name__ == "__main__":
    num = multiprocessing.Value('d', 0.0)
    arr = multiprocessing.Array('i', range(10))
    main()
