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
        if self.mode != 'x':
            try:
                self.test_file = open(self.name, 'r', encoding=self.encoding)
            except BaseException as error:
                self.failed_counter_add()
                print(f'\nThe file "{self.name}" cannot be opened with mode "{self.mode}" and encoding "{self.encoding}".')
                print(error.__class__, error)
                print(f'The operation is failed in <{self.failed_counter}> times.')
            finally:
                try:
                    self.test_file.close()
                except AttributeError as er:
                    print(er.__class__, er)
            self.file = open(self.name, 'r', encoding=self.encoding)
            print(f'The file {self.name} is opened: {not self.file.closed}')
            self.copy_file = self.file.read()
            self.file.close()
        try:
            self.file = open(self.name, self.mode, encoding=self.encoding)
            print(f'\nOpen the file "{self.name}" with mode "{self.mode}" and encoding "{self.encoding}".')
        except (FileExistsError, PermissionError) as error:
            print(f'\nThe file "{self.name}" cannot be opened with mode "{self.mode}" and encoding "{self.encoding}".')
            print(error.__class__, error)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Calling __exit__;')
        if exc_type:
            self.failed_counter_add()
            print(f'The operation is failed in <{self.failed_counter}> times.')
            if self.mode != 'x':
                with open(f'{self.name}', 'w', encoding=self.encoding) as new_file:
                    print(self.copy_file, file=new_file, end='')
            print(exc_type, exc_value, exc_traceback)
            if self.file:
                try:
                    self.file.close()
                except FileNotFoundError as err:
                    print(err.__class__, err)
                finally:
                    print(f'The file "{self.name}" is closed: {self.file.closed}.')
            return True

        else:
            self.successful_counter_add()
            print(f'The operation is successful in <{self.successful_counter}> times.')
            try:
                self.file.close()
            except FileNotFoundError as err:
                print(err.__class__, err)
            finally:
                print(f'The file "{self.name}" is closed: {self.file.closed}.')
                return None

if __name__ == '__main__':
    with Open('demo.txt', 'w') as opened_file:
        opened_file.write('PYTHON IS GREAT!')

    with Open('demo.txt', 'r') as opened_file:
        print(f'The file content: <<{opened_file.read()}>>.')

    try:
        with Open('demo1.txt', 'r') as opened_file:
            print(opened_file.read())
    except FileNotFoundError as error:
        print(error.__class__, error)

    try:
        with Open(123, 'r') as opened_file:
            print(opened_file.read())
    except OSError as error:
        print(error.__class__, error)

    try:
        with Open('demo.txt', 'w') as opened_file:
            opened_file.write(wrong_context)
    except NameError as error:
        print(error.__class__, error)

    with Open('demo.txt', 'a') as opened_file:
        opened_file.write('BEETROOT IS NICE!')
    try:
        with Open('demo2.txt', 'x') as opened_file:
            opened_file.write('HELLO 2023!')
    except FileExistsError as e:
        print(e.__class__, e)
    try:
        with Open('demo.txt', 'x') as opened_file:
            opened_file.write('SAMPLE TEXT...')
    except FileExistsError as e:
        print(e.__class__, e)

    print(f'Successful_counter = {Open.successful_counter};')
    print(f'Failed_counter = {Open.failed_counter};')
