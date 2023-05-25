
class FileOpen:

    def __init__(self, name, mode, encoding):
        self.name = name
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.name, self.mode, encoding=self.encoding)
        self.copy_file = self.file.read()
        self.file.seek(0)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            name = self.name.split('/')[-1]
            new_file = open(f'lesson20_context_manager/copy_{name}', 'w', encoding=self.encoding)
            print(self.copy_file, exc_type, exc_val, file=new_file)
            new_file.close()
            self.file.close()
            return True
        else:
            print('All right!')
            self.file.close()
            return None

with FileOpen('lesson20_context_manager/тест.txt', 'r', 'utf-8') as file:
    print(file.read())


with FileOpen('lesson20_context_manager/тест.txt', 'r', 'utf-8') as file:
    raise ValueError('Special test')