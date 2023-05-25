spam = 'Глобальний попередньо визначений спам.'

def scope_test():
    def do_local():
        spam = "Локальний (local) спам визначений у функції do_local."
        print('Виклик із функції do_local: ', spam)

    def do_nonlocal():
        nonlocal spam # The nonlocal keyword is used to work with variables inside nested functions,
                      # where the variable should not belong to the inner function.
        spam = "Nonlocal спам перевизначений у функції do_nonlocal."
        print('Виклик із функції do_nonlocal: ', spam)

    def do_global():
        global spam
        spam = "Глобальний (global) спам перевизначений у функції do_global."
        print('Виклик із функції do_global: ', spam)

    spam = "Тестовий (test) спам визначений в тілі функції scope_test."
    do_local()
    print("Виклик із функції scope_test, після виклику функції do_local:", spam)
    do_nonlocal()
    print("Виклик із функції scope_test, після виклику функції do_nonlocal:", spam)
    do_global()
    print("Виклик із функції scope_test, після виклику функції do_global:", spam)

print('Найперший виклик (глобальний namespace): ', spam)
scope_test()
print("Останній виклик (глобальний namespace): ", spam)
