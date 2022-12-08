from tkinter import *
from playsound import playsound
import time

root = Tk()
root.title('Timer')
root.geometry('400x600')
root.config(bg='#000')
root.resizable(False, False)

heading = Label(root, text='Timer', font=('DS-Digital', 40), bg='#000', fg='red')
heading.pack(pady=10)

# clock
Label(root, font=('DS-Digital', 15), text='current time:', bg='#000', fg='cyan3').place(x=100, y=80)

def clock():
    clock_time = time.strftime('%H:%M:%S')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)

current_time = Label(root, font=('DS-Digital', 18), text='', bg='#000', fg='cyan3')
current_time.place(x=220, y=76)
clock()

# timer
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font=('DS-Digital', 75), bg='#222', fg='red', bd=0).place(x=30, y=155)
hrs.set('00')
mins = StringVar()
Entry(root, textvariable=mins, width=2, font=('DS-Digital', 75), bg='#222', fg='red', bd=0).place(x=150, y=155)
mins.set('00')
sec = StringVar()
Entry(root, textvariable=sec, width=2, font=('DS-Digital', 75), bg='#222', fg='red', bd=0).place(x=270, y=155)
sec.set('00')

Label(root, text='hours', font=('DS-Digital', 12), bg='#000', fg='cyan2').place(x=80, y=130)
Label(root, text='minutes', font=('DS-Digital', 12), bg='#000', fg='cyan2').place(x=190, y=130)
Label(root, text='seconds', font=('DS-Digital', 12), bg='#000', fg='cyan2').place(x=310, y=130)

button = Button(root, text='Start', font=('DS-Digital', 40), bg='#800', bd=0, fg='black', width=6, height=1)
button.pack(padx=5, pady=40, side=BOTTOM)





root.mainloop()

