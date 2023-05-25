import file_2

try:
    import file_3
except ModuleNotFoundError:
    print('Файл не знайдено...')

import sys
from pprint import pprint

sys.path.insert(2, r'D:\Python\Beetroot\homework\homework_8_modules_and_standard_library\task_2\folder_1')

try:
    import file_3
except ModuleNotFoundError:
    print('Файл не знайдено...')
