from pythonds.basic import Stack  # type: ignore

def binary_number(number):
    result = Stack()
    while number:
        result.push(number%2)
        number //= 2

    return ''.join(str(result.pop()) for _ in range(result.size()))

if __name__ == '__main__':
    print(binary_number(12345))
    print(bin(12345).replace("0b", ""))
