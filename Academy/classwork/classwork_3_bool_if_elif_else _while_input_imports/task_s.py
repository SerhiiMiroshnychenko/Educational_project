stars = int(input('Please enter amount of stars: '))
counter = 1
while counter < stars * 2:
    if counter <= 5:
        print('*' * counter)
    else:
        print('*' * (stars - (counter % stars)))
    counter += 1
