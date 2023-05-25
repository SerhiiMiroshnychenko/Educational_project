# Створити декоратор, який буде виводити інформацію про функцію,
# яка викликана, але також сам декоратор
# має приймати параметер, що відповідатиме за увімкнення виводу додаткової
# інформації, та вимкення.
DEBUG = True

def get_docstring():
    def get_docstring_dec(func):
        def wrap():
            global DEBUG
            if DEBUG == True:
                print(f"Function {func.__name__}\n{func.__doc__}")
                print('=' * 30)
                print()
            func()

        return wrap

    return get_docstring_dec


@get_docstring()
def main():
    """This function does absolutely nothing"""
    print("No")

main()
DEBUG = False
main()


