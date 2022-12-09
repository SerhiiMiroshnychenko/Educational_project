from tkinter import *
import time
import winsound

root = Tk()
root.title('Timer')
root.geometry('400x580')
root.config(bg='#000')
root.resizable(False, False)

heading = Label(root, text='Timer', font=('DS-Digital', 60), bg='#000', fg='red')
heading.pack(pady=10)

# clock
def clock():
    clock_time = time.strftime('%H:%M:%S')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = Label(root, font=('DS-Digital', 80), text='', bg='#000', fg='cyan3')
current_time.place(x=32, y=85)
clock()

# timer
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font=('DS-Digital', 75), bg='#222', fg='red', bd=0).place(x=30, y=230)
hrs.set('00')
mins = StringVar()
Entry(root, textvariable=mins, width=2, font=('DS-Digital', 75), bg='#222', fg='red', bd=0).place(x=150, y=230)
mins.set('00')
sec = StringVar()
Entry(root, textvariable=sec, width=2, font=('DS-Digital', 75), bg='#222', fg='red', bd=0).place(x=270, y=230)
sec.set('00')

Label(root, text='hours', font=('DS-Digital', 12), bg='#000', fg='cyan2').place(x=80, y=200)
Label(root, text='minutes', font=('DS-Digital', 12), bg='#000', fg='cyan2').place(x=190, y=200)
Label(root, text='seconds', font=('DS-Digital', 12), bg='#000', fg='cyan2').place(x=310, y=200)


def timer():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())

    while times > -1:
        minute, second = (times // 60, times % 60)

        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if times == 0:
            filename = 'meow.wav'
            winsound.PlaySound(filename, winsound.SND_FILENAME)
            #winsound.Beep(888, 8888)
            sec.set('00')
            mins.set('00')
            hrs.set('00')

        times -= 1


def game():
    hrs.set('01')
    mins.set('00')
    sec.set('00')


button = Button(root, text='Start', font=('DS-Digital', 40), bg='#800', bd=0, fg='black', width=6, height=1,
                command=timer)
button.pack(padx=5, pady=40, side=BOTTOM)

button2 = Button(root, text='Game', font=('DS-Digital', 40), bg='#222', bd=0, fg='#999', width=6, height=1,
                 command=game)
button2.place(x=119, y=350)

root.mainloop()
