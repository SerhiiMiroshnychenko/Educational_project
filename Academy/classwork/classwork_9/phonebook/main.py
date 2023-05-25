from helper import print_commands, print_result, read_values
from file import read_dataset, write_dataset
from manager import create, update, delete
from searching import search


# add printing result
def phonebook(dataset_file):
    while True:
        print_commands()
        book = read_dataset(dataset_file)
        command = input('Введіть команду: ')
        match command:
            case 'n':
                data = read_values()
                book = create(book, data)
                write_dataset(book, dataset_file)
            case element if element in ['sf', 'sl', 'sfl', 'sp', 'sct', 'sc']:
                search(book, command)
            case 'up':
                update()
                write_dataset(book, dataset_file)
            case 'del':
                delete()
                write_dataset(book, dataset_file)
            case 'exit':
                print('Вихід з програми')
                break
            case _:
                print('Не вірно введена команда')


if __name__ == '__main__':
    phonebook('files/dataset.json')
    