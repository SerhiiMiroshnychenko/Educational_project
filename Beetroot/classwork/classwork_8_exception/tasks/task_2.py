def make_operation(operator: str, *args: int or float) -> int or float:
    """A version of a simple calculator"""
    try:
        result = args[0]
        for number in args[1:]:
            assert operator in '+-*/', 'Wrong operator!'
            match operator:
                case '+':
                    result += number
                case '-':
                    result -= number
                case '*':
                    result *= number
                case '/':
                    result /= number
        return result
    except Exception as err:
        print(f'\nПомічена помилка: {err.__class__}.')
        print('Причина:', err)
        return 'Розрахунок не відбувся через некоректно введені данні.'


if __name__ == '__main__':
    print(make_operation('//', 10, 2, 3.0, .5))
    print(make_operation('/', 10, 2, 3.0, 0))
    print(make_operation('+', '10', 2, 3.0, .5))
    print(make_operation(10, 2, 3.0, .5))
    print(make_operation('*'))
    print(make_operation('*', '-', 2, 3.0, .5))
