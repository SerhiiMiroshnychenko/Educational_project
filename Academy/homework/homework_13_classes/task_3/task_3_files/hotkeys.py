def hotkeys():
    """Функція, що показує правила користування"""
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ['Action description', 'Hot keys']
    table.add_row(['Turns on the first channel', 'f'])
    table.add_row(['Turns on the last channel', 'l'])
    table.add_row(['Turns on the N channel', 'N'])
    table.add_row(['Turns on the next channel', 'n'])
    table.add_row(['Turns on the previous channel', 'p'])
    table.add_row(['Returns the name of the current channel', 'c'])
    table.add_row(['Answer if the channel N or "name" exists', 'e'])
    table.add_row(['Exit the program', ''])
    print(table)


if __name__ == '__main__':
    hotkeys()
