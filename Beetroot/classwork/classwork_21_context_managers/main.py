class FileOpen:

    def __init__(self, name, mode, encoding='utf-8'):
        self.name = name
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.name, 'r', encoding=self.encoding)
        self.copy_file = self.file.read()
        self.file.close()
        self.file = open(self.name, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_value, trace):
        if exc_type:
            with open(f'copy_{self.name}', 'w', encoding=self.encoding) as new_file:
                new_file.write(self.copy_file)
                print(exc_type, exc_value, trace)
            self.file.close()
            return True
        else:
            print('All right!')
            self.file.close()
            return None

with FileOpen('test.txt', 'w') as file:
    file.write('Hello, Python!')

with FileOpen('test.txt', 'r') as file:
    print(file.read())

