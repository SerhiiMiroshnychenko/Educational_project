# Реалізуйте програму, яка зчитує ціле число, що вводиться з командного рядка,
# і записує у текстовий файл інформацію, щодо парності або непарності числа.
# 1. Програма працює поки користувач не закриє її за допомогою команди
# 2. Здійснити запис за допомогою print: число - парне або не парне
# 3. Один раз викликати відкриття файлу і при закритті програми закрити і сам файл

def check_numbers():
    """Перевіряє на парність та результат записує в файл"""
    print('По закінченні введіть <q>')
    while True:
        try:
            number = input('Введіть число: ')
            if number == 'q':
                break
            result = 'парне' if int(number) % 2 == 0 else 'не парне'
            with open('results.txt', 'a', encoding='UTF-8') as file:
                print(f'Число <{number}> - {result}', sep='\n', file=file)
        except Exception as error:
            print(f'\nПомічена помилка: {error.__class__}.')
            print('Причина:', error)


if __name__ == '__main__':
    check_numbers()



