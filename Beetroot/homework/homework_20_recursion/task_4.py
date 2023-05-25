# Task 4
import doctest


def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
    """

    return input_str[1:] + input_str[0] if len(input_str[1:]) < 2\
        else reverse(input_str[1:]) + input_str[0]

    # if len(input_str[1:]) < 2:
    #     return input_str[1:] + input_str[0]
    # else:
    #     return reverse(input_str[1:]) + input_str[0]


if __name__ == "__main__":
    print(reverse("hello"))
    print(reverse("he"))
    print(reverse("o"))
    doctest.testmod()
