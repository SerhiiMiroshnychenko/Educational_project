# Task 3
# A simple calculator.
# Create a function called make_operation, which takes in a simple
# arithmetic operator as a first parameter (to keep things simple
# let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments
# (only numbers) as the second parameter. Then return the sum or product
# of all the numbers in the arbitrary parameter. For example:
# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42


def make_operation(operator: str, *args: int or float) -> int or float:
    """A version of a simple calculator"""
    result = args[0]
    for number in args[1:]:
        match operator:
            case '+':
                result += number
            case '-':
                result -= number
            case '*':
                result *= number
            case '/':
                try:
                    result /= number
                except ZeroDivisionError:
                    print('Zero Division Error!')
                    return None
    return result


if __name__ == '__main__':
    print(make_operation('+', 10, 2, 3.0, .5))
    print(make_operation('-', 10, 2, 3.0, .5))
    print(make_operation('*', 10, 2, 3.0, .5))
    print(make_operation('/', 10, 2, 3.0, .5))
