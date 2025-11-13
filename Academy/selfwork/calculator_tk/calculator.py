import itertools
from tkinter import *


def btn_click(item):
    global expression
    try:
        input_field['state'] = 'normal'
        expression += item
        input_field.insert(END, item)
        if item == '=':
            result = str(eval(expression[:-1]))
            input_field.insert(END, result)
            expression = ''
        input_field['state'] = 'readonly'
    except ZeroDivisionError:
        input_field['state'] = 'normal'
        input_field.delete(0, END)
        input_field.insert(0, ' No Division by Zero!')
        input_field['state'] = 'readonly'
    except SyntaxError:
        input_field['state'] = 'normal'
        input_field.delete(0, END)
        input_field.insert(0, ' Error...')
        input_field['state'] = 'readonly'


def bt_clear():
    global expression
    expression = ''
    input_field['state'] = 'normal'
    input_field.delete(0, END)
    input_field['state'] = 'readonly'


def bt_hi():
    global expression
    expression = ''
    input_field['state'] = 'normal'
    input_field.delete(0, END)
    input_field.insert(0, ' Hi, Academy Python Group!')
    input_field['state'] = 'readonly'


root = Tk()
root.geometry("800x640")  # Збільшено висоту
root.config(bg='#000')
root.resizable(FALSE, FALSE)
root.title("CALCULATOR by Serhii Miroshnychenko")

# Налаштування grid для root
for i in range(8):  # 8 рядків (0-вхід, 1-Hi/C, 2-7 кнопки)
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # 4 колонки
    root.grid_columnconfigure(i, weight=1)

# Поле введення
frame_input = Frame(root, bg='#000')
frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

input_field = Entry(frame_input, font=('DS-Digital', 40), justify='right',
                    fg='#000', bg='white', state="readonly", bd=0)
input_field.pack(fill=BOTH, expand=True, padx=5, pady=5)

buttons = (('~', '<<', '>>', '('),
           ('^', '|', '&', ')'),
           ('7', '8', '9', '/'),
           ('4', '5', '6', '*'),
           ('1', '2', '3', '-'),
           ('0', '.', '=', '+'))

expression = ''

# Кнопка C
button_c = Button(root, text='C', font=('DS-Digital', 32), bg='#400', fg='red',
                  command=lambda: bt_clear(), bd=0)
button_c.grid(row=1, column=3, sticky='nsew', padx=1, pady=1)

# Кнопка Hi
button_hi = Button(root, text='Hi', font=('DS-Digital', 32), bg='#000', fg='#999',
                   command=lambda: bt_hi(), bd=0)
button_hi.grid(row=1, column=2, sticky='nsew', padx=1, pady=1)

# Генерація кнопок
b_color = 'black'
for row, col in itertools.product(range(6), range(4)):
    if buttons[row][col] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        f_color = 'white'
    elif buttons[row][col] in ('~', '<<', '>>', '^', '|', '&'):
        f_color = '#900'
    else:
        f_color = '#999'

    Button(root, text=buttons[row][col], font=('DS-Digital', 32),
           bg=b_color, fg=f_color, bd=0,
           command=lambda row=row, col=col: btn_click(buttons[row][col])
           ).grid(row=row + 2, column=col, sticky='nsew', padx=1, pady=1)

root.mainloop()