# Task 5
import doctest


def sum_of_digits(digit_string: str) -> int:
    """
    >>> sum_of_digits('26') == 8
    True

    >>> sum_of_digits('test')
    Traceback (most recent call last):
    ValueError: input string must be digit string
    """

    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")

    return int(digit_string) if len(digit_string) == 1\
        else int(digit_string[0]) + sum_of_digits(digit_string[1:])

    # if len(digit_string) == 1:
    #     return int(digit_string)
    # else:
    #     return int(digit_string[0]) + sum_of_digits(digit_string[1:])


if __name__ == "__main__":
    print(sum_of_digits('26'))
    print(sum_of_digits('9'))
    print(sum_of_digits('1234567890'))
    try:
        print(sum_of_digits('test'))
    except ValueError as error:
        print(error.__class__, error)
    doctest.testmod()
