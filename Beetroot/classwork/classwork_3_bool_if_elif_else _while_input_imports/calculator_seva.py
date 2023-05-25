from math import sin, cos, sqrt
import sys


def main():
    numbers = [int(x) for x in input('Go on, enter your numbers, separated by comma: ').split(',')]
    oper = input(
        'Please choose an operation:\n  1. Cosinus\n  2. Sinus\n  3. Square root\n  4. Exponent\n  Or use "exit" to exit\n')
    match oper:
        case '1':
            print(', '.join([str(cos(x)) for x in numbers]))
        case '2':
            print(', '.join([str(sin(x)) for x in numbers]))
        case '3':
            print(', '.join([str(sqrt(x)) for x in numbers]))
        case '4':
            print(', '.join([str(x ** x) for x in numbers]))
        case 'exit':
            sys.exit()
        case _:
            print('Please select from a list of operations')


if __name__ == "__main__":
    main()