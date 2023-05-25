import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(' ')
enter_log = logging.getLogger('ENTER')
exit_log = logging.getLogger('EXIT')
start_log = logging.getLogger('START')
count_log = logging.getLogger('COUNT')
report_log = logging.getLogger('REPORT')

class Open:
    successful_counter = 0
    failed_counter = 0
    def __init__(self, name, mode='r', encoding='utf-8'):
        start_log.info(f'\nThe start operation with file <{name}> (mode="{mode}"):')
        self.name = name
        self.mode = mode
        self.encoding = encoding
        self.file = None

    @classmethod
    def successful_counter_add(cls):
        cls.successful_counter += 1
        count_log.info(f'SUCCESSFUL counter added to {cls.successful_counter}.')

    @classmethod
    def failed_counter_add(cls):
        cls.failed_counter += 1
        count_log.info(f'FAILED counter added to {cls.failed_counter}.')

    def __enter__(self):
        enter_log.info('Calling __enter__;')

        try:
            if self.mode != 'x':
                self.file = open(self.name, 'r', encoding=self.encoding)
                self.copy_file = self.file.read()
                enter_log.info(f'The file <{self.name}> was copied.')
                self.file.close()
        except BaseException as error:
            enter_log.error(f'Tried to read: {error.__class__} {error}')

        try:
            self.file = open(self.name, self.mode, encoding=self.encoding)
            enter_log.info(f'The file <{self.name}> was opened in "{self.mode}"-mode and returned.')
            return self.file
        except BaseException as error:
            enter_log.error(f'Tried to open in "{self.mode}": {error.__class__} {error}')
            self.failed_counter_add()
            raise error
        finally:
            self.report('ENTER')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        exit_log.info('Calling __exit__;')

        if exc_type:

            exit_log.error(f'ERROR in EXIT: {exc_type} {exc_value} {exc_traceback}')

            self.failed_counter_add()

            if self.file:
                try:
                    with open(f'{self.name}', 'w', encoding=self.encoding) as new_file:
                        print(self.copy_file, file=new_file, end='')
                        exit_log.info(f'The file <{self.name}> was repaired successfully.')
                except BaseException as error:
                    exit_log.error(f'{error.__class__} {error}')
            self.report('EXIT (fail)')

            return True

        else:

            exit_log.info(f'The operation with file <{self.name}> (mode="{self.mode}") is successful.')
            self.successful_counter_add()

            self.report('EXIT (success)')

            return None

    def report(self, place):
        report_log.info(f'Report in {place}:')
        if self.file:
            report_log.info(f'Check 1: the file <{self.name}> is closed: {self.file.closed}.')
            if not self.file.closed:
                if place != 'ENTER':
                    self.file.close()
                    report_log.info(f'Check 2: the file <{self.name}> is closed: {self.file.closed}.')
                else:
                    report_log.info(f'Check 2: the file <{self.name}> is opened and sent to "EXIT".')
        else:
            report_log.info(f'The file <{self.name}> was not created.')


if __name__ == '__main__':
    logging.info('\n\n----------1. Success(1) is expected:')
    with Open('demo.txt', 'w') as opened_file:
        opened_file.write('PYTHON IS GREAT!')

    logging.info('\n\n----------2. Success(2) is expected:')
    with Open('demo.txt', 'r') as opened_file:
        logger.info(f'The file content: <<{opened_file.read()}>>.')

    try:
        logging.info('\n\n----------3. Fail(1) is expected:')
        with Open('demo1.txt', 'r') as opened_file:
            logger.info(f'The file content: <<{opened_file.read()}>>.')
    except FileNotFoundError as error:
        logger.error(f'{error.__class__} {error}\n')

    try:
        logging.info('\n\n----------4. Fail(2) is expected:')
        with Open(123, 'r') as opened_file:
            print(opened_file.read())
    except OSError as error:
        logger.error(f'{error.__class__} {error}\n')

    try:
        logging.info('\n\n----------5. Fail(3) is expected:')
        with Open('demo.txt', 'w') as opened_file:
            opened_file.write(wrong_context)
    except NameError as error:
        logger.error(f'{error.__class__} {error}\n')

    logging.info('\n\n----------6. Success(3) is expected:')
    with Open('demo.txt', 'a') as opened_file:
        opened_file.write('BEETROOT IS NICE!')

    try:
        logging.info('\n\n----------7. Fail(4) is expected:')
        with Open('demo2.txt', 'x') as opened_file:
            opened_file.write('HELLO 2023!')
    except FileExistsError as error:
        logger.error(f'{error.__class__} {error}\n')

    try:
        logging.info('\n\n----------8. Fail(5) is expected:')
        with Open('demo.txt', 'x') as opened_file:
            opened_file.write('SAMPLE TEXT...')
    except FileExistsError as error:
        logger.error(f'{error.__class__} {error}\n')

    logger.critical(f'Successful_counter = {Open.successful_counter};')
    logger.critical(f'Failed_counter = {Open.failed_counter};')
