# Task 2

# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces,
# and curly brackets are "balanced."

import doctest
from task_3_1 import Stack  # type: ignore


def brackets_balancing(content: str) -> bool:
    """
    Function that reverse string
    :param content: str
    :return: is brackets in the content balanced: bool

    >>> brackets_balancing('10 * (2 + 3)')
    True

    >>> brackets_balancing('10 * 2 + 3)')
    False

    >>> brackets_balancing('10 * (2 + 3')
    False

    >>> brackets_balancing('10 * {2 + 3}')
    True

    >>> brackets_balancing('10 * 2 + 3}')
    False

    >>> brackets_balancing('10 * {2 + 3')
    False

    >>> brackets_balancing('10 * [2 + 3]')
    True

    >>> brackets_balancing('10 * 2 + 3]')
    False

    >>> brackets_balancing('10 * [2 + 3')
    False

    >>> brackets_balancing('10 * (2 + 3]')
    False

    >>> brackets_balancing('10 * [2 + 3}')
    False

    >>> brackets_balancing('10 * {2 + 3)')
    False

    >>> brackets_balancing(123)
    Traceback (most recent call last):
    TypeError: object of type 'int' has no len()
    """

    pair_checker_1: Stack = Stack(len(content))
    pair_checker_2: Stack = Stack(len(content))
    pair_checker_3: Stack = Stack(len(content))

    brackets: set = {'(', ')', '{', '}', '[', ']'}
    content_set: set = set(list(content))

    if not brackets & content_set:
        return True

    for char in content:
        match char:
            case '(':
                pair_checker_1.push(char)
            case ')':
                try:
                    pair_checker_1.pop()
                except IndexError:
                    return False
            case '{':
                pair_checker_2.push(char)
            case '}':
                try:
                    pair_checker_2.pop()
                except IndexError:
                    return False
            case '[':
                pair_checker_3.push(char)
            case ']':
                try:
                    pair_checker_3.pop()
                except IndexError:
                    return False

    return pair_checker_1.is_empty() & pair_checker_2.is_empty() & pair_checker_3.is_empty()


if __name__ == '__main__':
    print('Is balanced:')
    print('\t"10 * 2 + 3":', brackets_balancing('10 * 2 + 3'))
    print('\t"10 * (2 + 3)":', brackets_balancing('10 * (2 + 3)'))
    print('\t"10 * (2 + 3":', brackets_balancing('10 * (2 + 3'))
    print('\t"10 * 2 + 3)":', brackets_balancing('10 * 2 + 3)'))
    print('\t"10 * {2 + 3}"d:', brackets_balancing('10 * {2 + 3}'))
    print('\t"10 * {2 + 3":', brackets_balancing('10 * {2 + 3'))
    print('\t"10 * 2 + 3}":', brackets_balancing('10 * 2 + 3}'))
    print('\t"10 * [2 + 3]":', brackets_balancing('10 * [2 + 3]'))
    print('\t"10 * 2 + 3]":', brackets_balancing('10 * 2 + 3]'))
    print('\t"10 * [2 + 3":', brackets_balancing('10 * [2 + 3'))
    print('\t"10 * (2 + 3]":', brackets_balancing('10 * (2 + 3]'))
    print('\t"10 * [2 + 3}":', brackets_balancing('10 * [2 + 3}'))
    print('\t"10 * {2 + 3)":', brackets_balancing('10 * {2 + 3)'))
    doctest.testmod()
