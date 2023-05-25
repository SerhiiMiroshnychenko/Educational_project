

class Open:
    successful_counter = 0
    failed_counter = 0
    def __init__(self, name, mode='r', encoding='utf-8'):
        self.name = name
        self.mode = mode
        self.encoding = encoding
        self.file = None

    @classmethod
    def successful_counter_add(cls):
        cls.successful_counter += 1

    @classmethod
    def failed_counter_add(cls):
        cls.failed_counter += 1

    def __enter__(self):
        print('Calling __enter__;')
        try:
            self.opened_file = open(file=self.name, mode=self.mode, encoding=self.encoding)
            print(f'The file {self.name} is opened: {not self.opened_file.closed}')
            return self.opened_file
        except FileNotFoundError as error:
            print(error.__class__, error.args)


    def __exit__(self, exc_type, exc_value, exc_traceback):

        print('Calling __exit__;')
        self.opened_file.close()
        print(f'The file {self.name} is closed: {self.opened_file.closed}')

        if exc_type:
            Open.failed_counter_add()
            return True
        else:
            Open.successful_counter_add()
            return None



if __name__ == '__main__':
    # with Open('sample.txt', 'w') as opened_file:
    #     opened_file.write('PYTHON IS GREAT!')

    # with Open('demo.txt', 'r') as opened_file:
    #     print(opened_file.read())
    #
    try:
        with Open('demo1.txt', 'r') as opened_file:
            print(opened_file.read())
    except (FileNotFoundError, AttributeError) as error:
        print(error.__class__, error)
    #
    # try:
    #     with Open(123, 'r') as opened_file:
    #         print(opened_file.read())
    # except OSError as error:
    #     print(error.__class__, error)
    #
    # try:
    #     with Open('demo.txt', 'w') as opened_file:
    #         opened_file.write(wrong_context)
    # except NameError as error:
    #     print(error.__class__, error)
    #
    # with Open('demo.txt', 'a') as opened_file:
    #     opened_file.write('BEETROOT IS NICE!')
    # try:
    #     with Open('demo.txt', 'x') as opened_file:
    #         opened_file.write('Text for test 1.')
    # except FileExistsError as e:
    #     print(e.__class__, e)

    print(f'Successful_counter = {Open.successful_counter};')
    print(f'Failed_counter = {Open.failed_counter};')
