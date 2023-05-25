# Task 1

# Write a program that reads in a sequence of characters and
# prints them in reverse order, using your implementation of Stack.

import doctest
from task_3_1 import Stack  # type: ignore


def string_reverse(text: str) -> str:
    """
    Function that reverse string
    :param text: str
    :return: reversed text: str

    >>> string_reverse('hello')
    'olleh'

    >>> string_reverse(123)
    Traceback (most recent call last):
    TypeError: object of type 'int' has no len()
    """

    result = Stack(len(text))
    for char in text:
        result.push(char)

    return ''.join(str(result.pop()) for _ in range(result.size()))


if __name__ == '__main__':
    print(string_reverse('PYTHON'))
    doctest.testmod()
