numbers = list(range(1, 11))
print(numbers)
even_numbers = list(range(2, 22, 2))
print(even_numbers)
squares = []
cubes = list()
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    cubes.append(value ** 3)
print(squares)
print(cubes)
dublings = [number * 2 for number in range(1, 11)]


def stat(lists):
    print("\nСтатистика для ", (lists))
    print(min(lists))
    print(max(lists))
    print(sum(lists))


stat(numbers)
stat(even_numbers)
stat(squares)
stat(cubes)
stat(dublings)
