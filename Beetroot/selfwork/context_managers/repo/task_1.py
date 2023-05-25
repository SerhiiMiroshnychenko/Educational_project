import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(' ')
enter_log = logging.getLogger('ENTER')
exit_log = logging.getLogger('EXIT')
start = logging.getLogger('START')

class Open:
    successful_counter = 0
    failed_counter = 0
    def __init__(self, name, mode='r', encoding='utf-8'):
        start.info(f'\nThe start operation with file <{name}>:')
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
        enter_log.info('Calling __enter__;')
        if self.mode != 'x':
            try:
                self.test_file = open(self.name, 'r', encoding=self.encoding)
            except BaseException as error:
                self.failed_counter_add()
                if error == PermissionError:
                    enter_log.critical('PERMISSION ERROR!')
                    enter_log.debug(
                        f'Successful_counter = {Open.successful_counter}\nFailed_counter = {Open.failed_counter};')
                enter_log.info(f'The file "{self.name}" cannot be opened with mode "{self.mode}" and encoding "{self.encoding}".')
                enter_log.error(f'{error.__class__} {error}')
                enter_log.critical(f'The operation is failed in <{self.failed_counter}> times.')
            finally:
                try:
                    self.test_file.close()
                except AttributeError as error:
                    enter_log.error(f'{error.__class__} {error}')
            self.file = open(self.name, 'r', encoding=self.encoding)
            enter_log.info(f'The file {self.name} is opened: {not self.file.closed}')
            self.copy_file = self.file.read()
            self.file.close()
        try:
            self.file = open(self.name, self.mode, encoding=self.encoding)
            enter_log.info(f'Open the file "{self.name}" with mode "{self.mode}" and encoding "{self.encoding}".')
        except FileExistsError as error:
            enter_log.info(f'The file "{self.name}" cannot be opened with mode "{self.mode}" and encoding "{self.encoding}".')
            enter_log.error(f'{error.__class__} {error}')
        except PermissionError as error:
            enter_log.critical('PERMISSION ERROR!')
            self.successful_counter_add()
            enter_log.debug(f'Successful_counter = {Open.successful_counter}\nFailed_counter = {Open.failed_counter};')
            enter_log.info(
                f'The file "{self.name}" cannot be opened with mode "{self.mode}" and encoding "{self.encoding}".')
            enter_log.error(f'{error.__class__} {error}')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        exit_log.info('Calling __exit__;')
        if exc_type:
            self.failed_counter_add()
            exit_log.critical(f'The operation is failed in <{self.failed_counter}> times.')
            if self.mode != 'x':
                with open(f'{self.name}', 'w', encoding=self.encoding) as new_file:
                    print(self.copy_file, file=new_file, end='')
            exit_log.error(f'{exc_type} {exc_value} {exc_traceback}')
            if self.file:
                try:
                    self.file.close()
                except FileNotFoundError as error:
                    exit_log.error(f'{error.__class__} {error}')
                finally:
                    exit_log.info(f'The file "{self.name}" is closed: {self.file.closed}.')
            exit_log.info(f'The end operation with file {self.name}.\n')
            return True

        else:
            self.successful_counter_add()
            exit_log.critical(f'The operation is successful in <{self.successful_counter}> times.')
            try:
                self.file.close()
            except FileNotFoundError as error:
                exit_log.error(f'{error.__class__} {error}')
            finally:
                exit_log.info(f'The file "{self.name}" is closed: {self.file.closed}.')
                exit_log.info(f'The end operation with file {self.name}.\n')
                return None

if __name__ == '__main__':
    with Open('demo.txt', 'w') as opened_file:
        opened_file.write('PYTHON IS GREAT!')

    with Open('demo.txt', 'r') as opened_file:
        logger.info(f'The file content: <<{opened_file.read()}>>.')

    try:
        with Open('demo1.txt', 'r') as opened_file:
            logger.info(f'The file content: <<{opened_file.read()}>>.')
    except FileNotFoundError as error:
        logger.error(f'{error.__class__} {error}\n')

    try:
        with Open(123, 'r') as opened_file:
            print(opened_file.read())
    except OSError as error:
        logger.error(f'{error.__class__} {error}\n')

    try:
        with Open('demo.txt', 'w') as opened_file:
            opened_file.write(wrong_context)
    except NameError as error:
        logger.error(f'{error.__class__} {error}\n')

    with Open('demo.txt', 'a') as opened_file:
        opened_file.write('BEETROOT IS NICE!')
    try:
        with Open('demo2.txt', 'x') as opened_file:
            opened_file.write('HELLO 2023!')
    except FileExistsError as error:
        logger.error(f'{error.__class__} {error}\n')

    try:
        with Open('demo.txt', 'x') as opened_file:
            opened_file.write('SAMPLE TEXT...')
    except FileExistsError as error:
        logger.error(f'{error.__class__} {error}\n')

    logger.critical(f'Successful_counter = {Open.successful_counter};')
    logger.critical(f'Failed_counter = {Open.failed_counter};')
