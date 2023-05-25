import timeit


mycode1 = '''
def set_list_1():
    new_list = []
    c = 0
    while c < 1000000:
        new_list.append(c)
        c += 1
    return new_list
'''
mycode2 = '''
def set_list_1():
    new_list = []
    for i in range(1000000):
        new_list.append(i)
    return new_list
'''
mycode3 = '''
def set_list_3():
    return [i for i in range(1000000)]
'''
mycode4 = '''
def set_list_4():
    return list(range(1000000))
'''
mycodes = [mycode1, mycode2, mycode3, mycode4]

for code in mycodes:
    times = timeit.repeat(stmt=code,
                          repeat=5,
                          number=1000000)
    print(times)

