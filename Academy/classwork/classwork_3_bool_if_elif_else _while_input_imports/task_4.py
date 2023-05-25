while 'true':
    print('"q" == вихід')
    country = input("Enter your country: ")
    if country == 'q':
        break
    elif country.isalpha():
        print(country.capitalize())
    else:
        print('What\'s wrong!')
