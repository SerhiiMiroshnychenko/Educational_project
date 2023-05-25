# 1101011 = 1 · 26 + 1 · 25 + 0 · 24 + 1 · 23 + 0 · 22 +
# 1 · 21 + 1 · 20 = 64 + 32 + 0 + 8 + 0 + 2 + 1 = 107

number = input('Введіть двійкове число:')
number = number[::-1]
result = 0
for ind, char in enumerate(number):
    add_ = int(char) * 2 ** ind
    result += add_
print(result)
