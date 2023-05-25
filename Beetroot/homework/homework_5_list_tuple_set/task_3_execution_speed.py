# Подивимося на швидкість роботи функцій з task_1

import timeit
from task_3 import create_special_numbers, generate_special_numbers

start = timeit.default_timer()
result_1 = create_special_numbers()
stop = timeit.default_timer()
print('Create_special_numbers time:  ', stop - start)

start = timeit.default_timer()
result_2 = generate_special_numbers()
stop = timeit.default_timer()
print('Generate_special_numbers time:  ', stop - start)
