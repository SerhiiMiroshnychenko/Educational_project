def count_lines(name: str) -> int:
    """Counts the number of lines"""
    with open(name) as file_object:
        contents = file_object.readlines()
        return len(contents)


def count_words(name: str) -> int:
    """Counts the number of words"""
    with open(name) as file_object:
        words = file_object.read().split(' ')
        return len(words)


def count_chars(name: str) -> int:
    """Counts the number of characters"""
    with open(name) as file_object:
        chars = list(file_object.read().replace(' ', '').replace('\n', ''))
        return len(chars)


def count_bite(name: str) -> int:
    """Counts the number of bites"""
    with open(name, 'rb') as file_object:
        byte_ = 0
        while True:
            b = file_object.read(1)
            byte_ += 1
            if not b:
                break
        return byte_


def test(name: str) -> tuple:
    """Forms the characteristics of the file"""
    return count_lines(name), count_words(name), count_chars(name), count_bite(name)


def show_test(name: str) -> None:
    """Show the characteristics of the file"""
    from prettytable import PrettyTable

    table = PrettyTable()
    table.field_names = ['Ім\'я файла', 'Рядків', 'Слів', 'Символів', 'Байтів']
    table.add_row([name, test(name)[0], test(name)[1], test(name)[2], test(name)[3]])
    print(table)


if __name__ == '__main__':

    show_test('mymod.py')
