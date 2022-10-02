"""Матеріали по функціям з книги 'Пришвидшенний курс Python' Е.Маттес."""


# Функція без аргументів
def greet_user():  # визначення функції
    """Показати просте вітання."""  # docstring: опис завдання функції
    print("Hello!")  # тіло функції


greet_user()  # виклик функції


# Функція з одним простим аргументом
def greet_user_by_name(user_name):  # де user_name це ПАРАМЕТР функції
    """Показати вітання за ім'ям."""
    print(f"Hi, {user_name.title()}!")


greet_user_by_name("serhii")  # де "serhii" це АРГУМЕНТ функції


# функція з позиційними аргументами
def describe_pet(animal_type, pet_name):
    """Показати інформацію про домашнього улюбленця."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# далі покажемо неодноразовий виклик функції
describe_pet("hamster", "harry")
describe_pet("dog", "willie")
describe_pet("donald", "duck")  # варіант помилкового надання аргументів
describe_pet(pet_name="donald",
             animal_type="duck")  # виклик функції використовуючі ключові аргументи (пари " ім'я:значення")


# функція з уставним значенням аргументу
def describe_pet_for_dogs(pet_name,
                          animal_type="dog"):  # де параметру animal_type надане уставне значення "dog". Тепер його
    # можно не указувати в дужках при виклику функції. Параметри з уставним значенням завжди займають кінцеві позиції.
    """Показати інформацію про домашнього улюбленця."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet_for_dogs("willie")
describe_pet_for_dogs("tom", "cat")  # але ми можемо вказати значення аргументу, відмінне від уставного
describe_pet_for_dogs(animal_type="mouse", pet_name="jerry")  # виклик з ключовими аргументами


# функція, що повертає просте значення
def get_formatted_name(first_name, last_name):
    """Повернути відформатоване повне ім'я"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()  # де return - оператор повернення, а full_name.title() - значення повернення


musician = get_formatted_name("jimi",
                              "hendrix")  # де musician - змінна яка посилається на значення, що повертає відповідний
# виклик функції.
print("\n" + musician)
print(" \n" + get_formatted_name("jimi", "hendrix"))  # одноразовий вивід значення повернення без зберігання в змінну


# функція з необов'язковим аргументом
def get_formatted_name_with_middle(first_name, last_name, middle_name=""):  # де middle_name - необов'язковий аргумент
    """Повернути відформатоване повне ім'я з трьох складових"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name_with_middle("jimi", "hendrix")  # не вказуємо необов'язковий аргумент
print("\n" + musician)

musician = get_formatted_name_with_middle("john", "hooker", "lee")  # вказуємо необов'язковий аргумент
print("\n" + musician)


# функція, що повертає словник
def get_build_person(first_name, last_name, age=None):
    """Повернути словник з інформацією про людину."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = get_build_person("jimi", "hendrix", age=27)
print("\n", musician)


# функції та цикл while
def get_formatted_name(first_name, last_name):
    """Повернути відформатоване повне ім'я"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")  # задаємо умову виходу з циклу
    f_name = input("First name: ")
    if f_name == 'q':  # умова пeреривання
        break  # вихід з циклу
    l_name = input("Last name: ")
    if l_name == 'q':  # умова пeреривання
        break  # вихід з циклу
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


# Мій варіант (цикл всередині функції (насправді два)):
def get_formatted_name():  # визначення функції
    """Запросити та повернути відформатоване повне ім'я"""  # docstring
    while True:  # безкінечний цикл в тілі функції
        print("\nPlease enter your name:\n(enter 'q' at any time to quit)")
        # ^ запитуємо ім'я та задаємо умову виходу з циклу
        values = [f_name := None, "First name: ", l_name := None, "Last name: "]
        # ^ створюємо список для ітерації в циклі for
        for ind in range(0, len(values), 2):  # перебираємо змінні циклом for, щоб не дублювати код
            values[ind] = input(values[ind + 1])  # запрос на введення значення змінної та присвоєння цього значення
            if values[ind] == 'q':  # умова переривання функції (а якщо був би break, то було б тільки циклу for)
                return print("The program is over.")  # вихід з функції
        print(f"\nHi, {f'{values[0]} {values[2]}'.title()}!")  # вивід результату роботи функції


get_formatted_name()  # виклик функції до роботи


# передавання списку в функцію
def greet_users(names):
    """Вивести просте повідомлення для кожного користувача у списку."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)

# Редагування списку всередині функції:
# Код без використання функцій:
unprinted_designs = ["phone case", "robot pendart", "dodecahedron"]  # перелік креслень, які треба роздрукувати
completed_models = []  # перелік опрацьованих моделей
print()
while unprinted_designs:  # цикл виконується поки список не порожній (не порожній == True)
    current_design = unprinted_designs.pop()  # метод pop() виштовхує останній елемент списку і ми передаємо його у
    # змінну current_design
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)  # додаємо значення змінної current_design в список completed_models
print("\nThe following models have been printed:")  # показуємо всі готові моделі
for completed_model in completed_models:
    print(completed_model)


# Код з використанням функцій:
def print_models(unprinted_designs, completed_models):
    """
    Симулювати друк кожного креслення,
    доки всі не закінчаться.
    Перенести кожен рисунок до
    completed_models після друку.
    """
    print()
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Показати всі надруковані моделі"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


"""Думка: кожна функція повинна робити свою окрему дію. Можно завжди викликати функцію в функції."""

unprinted_designs = ["phone case", "robot pendart", "dodecahedron"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)  # перевіряємо список
# виклик тих же функцій, але з копією списку unprinted_designs, щоб зберегти оригинал:
unprinted_designs = ["phone case", "robot pendart", "dodecahedron"]
completed_models = []
print_models(unprinted_designs[:], completed_models)  # передача копії
show_completed_models(completed_models)
print(unprinted_designs)  # перевіряємо список
print()


# передавання довільної кількості аргументів
def make_pizza(*toppings):
    # ^ зірочка на початку імені параметра *toppings каже Python, що треба створити кортеж toppings та запакувати в
    # нього всі значення, які отримає функція
    """Скласти список замовлених інгредієнтів."""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# передавання довільної кількості аргументів
def make_pizza(*toppings):
    """Описати піцу, яку ми збираємося приготувати."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("papperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")


# як комбінувати довільні та позиційні аргументи
def make_pizza(size, *toppings):
    """Описати піцу, яку ми збираємося приготувати."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "papperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")

"""Параметр для збору довільних позиційних аргументів часто називають *args"""


# довільні ключові аргументи
def build_profile(first, last, **user_info):
    """Створити словник, що міститиме всю інформацію про користувача."""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='phisics')
print("\n", user_profile)

"""Для набору не описаних ключових аргументів часто використовується ім'я параметра **kwargs"""
