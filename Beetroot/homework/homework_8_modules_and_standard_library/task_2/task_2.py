import sys
from pprint import pprint
import file_1


pprint(sys.path)  # Покажемо список посилань за якими Python шукає модулі

# Спробуємо імпортувати test_file.py
try:
    import test_file
    pprint(dir())  # Покажемо список імен доступних у поточному модулі
    test_file.say_hi()  # Спроба викликати функцію say_hi()
except ModuleNotFoundError:
    print('Файл не знайдено...')  # Покажемо повідомлення про помилку

# Додамо фолдер homework_1_first_steps до списку шляхів пошуку
sys.path.insert(2, r'D:\Python\Beetroot\homework\homework_1_first_steps')
pprint(sys.path)  # Покажемо список посилань за якими Python шукає модулі
pprint(dir())  # Покажемо список імен доступних у поточному модулі

# Знов спробуємо імпортувати test_file.py
try:
    import test_file
    pprint(dir())
    test_file.say_hi()
except ModuleNotFoundError:
    print('Файл не знайдено...')
