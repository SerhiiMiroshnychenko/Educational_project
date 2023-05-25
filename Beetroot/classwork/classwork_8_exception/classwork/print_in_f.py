from random import randint

with open('numbers.txt', 'w') as f:
    print(*[randint(0, 9) for _ in range(11)], sep='\n', file=f)

with open('numbers.txt') as f:
    result = sum([int(line) for line in f])

with open('sum_numbers.txt', 'w') as f:
    f.write(str(result))
