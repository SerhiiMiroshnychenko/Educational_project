# Створити список з рандомних чисел рандомної довжини.
# Відфільтрувати його за функцією 5 < x < 50.
# Застосувати до списку корінь з заокругленням до 2 знаків після коми.
# lambda x: 5 < x < 50 - filter
# lambda x: round(x ** 0.5, 2) - map

from random import randint

print(numbers := list(map(lambda n: round(n ** 0.5, 2),
                          (filter(lambda n: 5 < n < 50,
                                  (randint(1, 100) for _ in range(randint(1, 100))))))))
