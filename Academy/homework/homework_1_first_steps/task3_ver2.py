"""Task 3"""
# Version 2

# Малюємо "О"
for i in range(5):
    for j in range(10):
        if j == 0 or (i == 0 and j < 9) or (i == 4 and j < 9):
            print('#', end='')
        elif j == 9:
            print('#')
        else:
            print(' ', end='')

# Малюємо "Н"
for i in range(5):
    for j in range(10):
        if j == 0 or (i == 2 and j < 9):
            print('#', end='')
        elif j == 9:
            print('#')
        else:
            print(' ', end='')


