# A program that simulates a survey or questionnaire.

message_0 = 'пропоную тобі взяти участь у невеличкому анкетуванні:'
print('\n' + message_0.upper() + '\n' + '-' * 55)
name = input("Введи своє ім'я: ")
name_c = name.title()
file_name = f"{name}.txt"
file_path = f'C:/Users/admin/Desktop/For files/{file_name}'
age = input("Введи свій вік: ")
weight = input("Введи свою вагу: ")
height = input("Введи свій зріст: ")
favorite_dish = input("Введи своє улюблене блюдо: ")
word_1 = 'тільки' if name_c[0] == "Ю" else 'цілих'
word_2 = 'то трішки' if name_c[0] == "Ю" else 'забагато'
word_3 = 'її' if name_c[0] == "В" else 'його'
text1 = f"{name_c} при зрості {height} важить {word_1} {weight} кг.\n"
text2 = f"Все через те, що вже {age} років {word_3} їжа тільки {favorite_dish} і {word_2}.\n"
text = text1 + text2
with open(file_path, 'w') as file_object:
    file_object.write(text)
