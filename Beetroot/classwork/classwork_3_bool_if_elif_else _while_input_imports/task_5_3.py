height = int(input('Введіть висоту піраміди: '))
counter = 1
while counter < height * 2:
    print('*' * counter if counter <= 5 else '*' * (height - (counter % height)))
    counter += 1
