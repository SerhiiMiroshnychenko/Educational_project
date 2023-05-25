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
        input_field.delete(0, END)
        input_field.insert(0, ' No Division by Zero!')
    except SyntaxError:
        input_field.delete(0, END)
        input_field.insert(0, ' Error...')


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
root.geometry("800x605")
root.config(bg='#000')
root.resizable(FALSE, FALSE)
root.title("CALCULATOR by Serhii Miroshnychenko")

frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")
input_field = Entry(frame_input, font=('DS-Digital', 50), width=24, fg='#000', state="readonly")

input_field.pack(fill=BOTH)

buttons = (('~', '<<', '>>', '(', '6'),
           ('^', '|', '&', ')', '6'),
           ('7', '8', '9', '/', '6'),
           ('4', '5', '6', '*', '6'),
           ('1', '2', '3', '-', '6'),
           ('0', '.', '=', '+', '6'))

expression = ''

button_c = Button(root, text='C',width=1, height=1, font=('DS-Digital', 32), bg='#400', fg='red', command=lambda: bt_clear())
button_c.grid(row=1, column=3, sticky='nsew')
button_hi = Button(root, text='Hi',width=1, height=1, font=('DS-Digital', 32), bg='#000', fg='#999', command=lambda: bt_hi())
button_hi.grid(row=1, column=2, sticky='nsew')
b_color = 'black'
for row, col in itertools.product(range(6), range(4)):
    if buttons[row][col] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        f_color = 'white'
    elif buttons[row][col] in ('~', '<<', '>>', '^', '|', '&'):
        f_color = '#900'
    else:
        f_color = '#999'
    Button(root, width=1, height=1, text=buttons[row][col], font=('DS-Digital', 32), bg=b_color, fg=f_color,
           command=lambda row=row, col=col: btn_click(buttons[row][col])).grid(row=row+2,
           column=col, sticky='nsew', padx=1, pady=1)

root.mainloop()

# auto-py-to-exe
