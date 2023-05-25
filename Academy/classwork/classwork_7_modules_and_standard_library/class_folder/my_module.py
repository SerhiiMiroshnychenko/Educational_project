print('This will run when the file is imported.')


def my_function():
    print('Executing function. This will only run when the function is called.')


if __name__ == '__main__':
    print('This will get executed only if')
    print('the module is invoked directly.')
    print('It will not run when this module is imported')
    my_function()