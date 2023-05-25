
class OpenFile:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        if issubclass(exc_type, BaseException):
            self.file.write(str(exc_type))
        if self.file:
            self.file.close()
        return True

    def method(self):
        raise Exception('some exception')


with OpenFile('temp.txt', 'r+') as open_file:
    print('Start reading file')
    print(open_file.file.read())
    open_file.method()












# Розширити атрибути класу та добавити перевірку на помилки при закритті файлу
