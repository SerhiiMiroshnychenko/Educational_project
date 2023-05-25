class CustomException(Exception):
    counter = 0
    def __new__(cls, *args, **kwargs):
        cls.counter += 1
        return super().__new__(cls)
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg
        with open('logs.txt', encoding='utf-8', mode='a') as f:
            f.write(f'{self.counter}. {self.msg}\n')

    def __str__(self):
        return self.msg

if __name__ == '__main__':
    custom_error = CustomException('Oops, there is the "Custom Error" here!')
    try:
        raise custom_error
    except CustomException as e:
        print(f'{e.__class__} has been detected in {custom_error.counter} time.'
              f'\nThe reason: {e}')
