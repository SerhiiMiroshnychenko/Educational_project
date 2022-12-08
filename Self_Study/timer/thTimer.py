##Imports and Displays
import time
from threading import Timer


def display(msg):
    print(msg + ' ' + time.strftime('%H:%M:%S'))


##Basic timer
def run_once():
    display('run_once:')
    t = Timer(10, display, ['Timeout:'])
    t.start()  # Here run is called


run_once()
##Runs immediately and once
print('Waiting.....')


##Lets make our timer run in intervals
##Put it into a class
##Making it run until we stop it
##Just getting crazy.Notice We have multiple timers at once!
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)
            print(' ')
        ##We are now creating a thread timer and controling it


timer = RepeatTimer(1, display, ['Repeating'])
timer.start()  # recalling run
print('Threading started')
time.sleep(10)  # It gets suspended for the given number of seconds
print('Threading finishing')
timer.cancel()