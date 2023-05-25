# Task 3
# from typing import Optional
import doctest


def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers

    >>> mult(2, 4) == 8
    True

    >>> mult(2, 0) == 0
    True

    >>> mult(2, -4)
    Traceback (most recent call last):
    ValueError: This function works only with positive integers
    """
    if n > 0:
        return a if n == 1 else a + mult(a, n - 1)
    elif n == 0:
        return 0
    else:
        raise ValueError("This function works only with positive integers")


if __name__ == "__main__":
    print(mult(2, 4))
    print(mult(2, 0))
    try:
        print(mult(2, -4))
    except ValueError as error:
        print(error.__class__, error)
    doctest.testmod()
