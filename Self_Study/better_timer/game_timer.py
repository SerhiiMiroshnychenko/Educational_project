from tkinter import *
import time
import winsound

root = Tk()
root.title('Timer')
root.geometry('495x780')
root.config(bg='#000')
root.resizable(False, False)

heading = Label(root, text='Timer', font=('DS-Digital', 60), bg='#000', fg='red')
heading.pack(pady=10)


# clock
def clock():
    clock_time = time.strftime('%H:%M:%S')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = Label(root, font=('DS-Digital', 70), text='', bg='#000', fg='cyan3')
current_time.pack(pady=10)
clock()

# Labels for timer
labels_frame = Frame(root, bg='#000')
labels_frame.pack(pady=5)

Label(labels_frame, text='hours', font=('DS-Digital', 12), bg='#000', fg='cyan2').grid(row=0, column=0, padx=50)
Label(labels_frame, text='minutes', font=('DS-Digital', 12), bg='#000', fg='cyan2').grid(row=0, column=1, padx=50)
Label(labels_frame, text='seconds', font=('DS-Digital', 12), bg='#000', fg='cyan2').grid(row=0, column=2, padx=50)

# Timer entries
timer_frame = Frame(root, bg='#000')
timer_frame.pack(pady=5)

hrs = StringVar()
Entry(timer_frame, textvariable=hrs, width=2, font=('DS-Digital', 75), bg='#222', fg='red', bd=0,
      justify='center').grid(row=0, column=0, padx=10)
hrs.set('00')

mins = StringVar()
Entry(timer_frame, textvariable=mins, width=2, font=('DS-Digital', 75), bg='#222', fg='red', bd=0,
      justify='center').grid(row=0, column=1, padx=10)
mins.set('00')

sec = StringVar()
Entry(timer_frame, textvariable=sec, width=2, font=('DS-Digital', 75), bg='#222', fg='red', bd=0,
      justify='center').grid(row=0, column=2, padx=10)
sec.set('00')


def timer():
    try:
        times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())

        if times <= 0:
            return

        while times > -1:
            minute, second = (times // 60, times % 60)

            hour = 0
            if minute > 60:
                hour, minute = (minute // 60, minute % 60)

            sec.set(f'{second:02d}')
            mins.set(f'{minute:02d}')
            hrs.set(f'{hour:02d}')

            root.update()
            time.sleep(1)

            if times == 0:
                try:
                    filename = 'meow.wav'
                    winsound.PlaySound(filename, winsound.SND_FILENAME)
                except:
                    winsound.Beep(1000, 1000)

                sec.set('00')
                mins.set('00')
                hrs.set('00')

            times -= 1
    except ValueError:
        sec.set('00')
        mins.set('00')
        hrs.set('00')


def game():
    hrs.set('01')
    mins.set('00')
    sec.set('00')


# Buttons frame
buttons_frame = Frame(root, bg='#000')
buttons_frame.pack(pady=40)

button2 = Button(buttons_frame, text='Game', font=('DS-Digital', 40), bg='#222', bd=0, fg='#999',
                 width=6, height=1, command=game)
button2.pack(pady=10)

button = Button(buttons_frame, text='Start', font=('DS-Digital', 40), bg='#800', bd=0, fg='black',
                width=6, height=1, command=timer)
button.pack(pady=10)

root.mainloop()