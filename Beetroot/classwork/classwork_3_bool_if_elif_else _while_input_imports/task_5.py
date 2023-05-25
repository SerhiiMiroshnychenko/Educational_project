k, d = 1, 1
height = input('Введіть висоту піраміди: ')
if height.isdigit():
    for i in range(int(height) * 2):
        print('*' * k)
        if k == int(height):
            d = -1
        k += d
else:
    print('Використовуйте лише числа!')
