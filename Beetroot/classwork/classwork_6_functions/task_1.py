number, base = tuple(map(int, input('Enter i and k (divide by space): ').split(' ')))

result = []
while number // base != 0:
    result.append(number % base)
    number //= base
result.append(number % base)

result.reverse()
print(*result, sep='')
