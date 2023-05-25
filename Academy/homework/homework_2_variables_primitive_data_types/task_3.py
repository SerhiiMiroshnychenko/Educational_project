"""Using python as a calculator."""

a, b = 10, 7

# Children's calculator
print(f'a = {a}\nb = {b}')
print(f'Addition: {a} + {b} = {a + b}')
print(f'Subtraction: {a} - {b} = {a - b}')
print(f'Division: {a} / {b} = {a / b}')
print(f'Multiplication: {a} * {b} = {a * b}')
print(f'Exponent (Power): {a} ** {b} = {a ** b}')
print(f'Modulus: {a} % {b} = {a % b}')
print(f'Floor division: {a} // {b} = {a // b}')


# Simple calculator
def calculator():
    """Simple calculator --- Простий калькулятор."""
    print("\n\nSIMPLE CALCULATOR --- ПРОСТИЙ КАЛЬКУЛЯТОР")
    print('Quit --- Вихід: "q"')
    while True:
        calculation = input("Enter your calculation --- Введіть обчислення: ")
        if calculation == "q":
            print("END...")
            break
        try:
            result = eval(calculation)
            print(f"Result --- Результат: {result}")
        except:  # Знаю, що погано, але ж це Simple :)
            print("Something is wrong --- Щось не так...")


calculator()
