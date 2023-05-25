from contextlib import contextmanager

@contextmanager
def open_file(name, mode, encoding='utf-8'):
    f = open(name, 'r', encoding=encoding)
    copy_file = f.read()
    f.close()
    try:
        f = open(name, mode, encoding=encoding)
        yield f
    except Exception as e:
        name = f'copy_{name}'
        new_file = open(name, 'w', encoding=encoding)
        print(copy_file, e.__class__, e, file=new_file)
        new_file.close()
    else:
          print('All right!')
    finally:
        f.close()
        print(f.closed)


if __name__ == '__main__':
    with open_file('some_file.txt', 'w') as f:
        f.write('Hello Python!')


    with open_file('some_file.txt', 'r') as f:
        print(f.read())