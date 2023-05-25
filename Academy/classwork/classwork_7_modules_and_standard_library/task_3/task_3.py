# Task 3. Відворити структуру проекту
# project
#     module1
#         data_folder
#             file.txt
#     module2
#         server.py
# Відкрити file.txt з модуля main не вказуючи шляху вручну, а отримати його за допомогою бібліотеки os

import os

os.mkdir('project')
os.mkdir('project/module1')
os.mkdir('project/module1/data_folder')
with open('project/module1/data_folder/file.txt', 'w') as f:
    f.write('Find me!')
os.mkdir('project/module2')
with open('project/module2/server.py', 'w') as f:
    context = """import os

main_path = os.path.dirname(os.path.abspath('__file__'))
new_path = main_path.replace('module2', 'module2\\data_folder')
result_path = os.path.join(new_path, 'file.txt')
print(result_path)
"""
    f.write(context)
