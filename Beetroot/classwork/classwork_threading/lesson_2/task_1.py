"""
Задача. Змоделювати переміщення людей човном через річку.
"""

from threading import *
import time

class Boat:
    def __init__(self, max_members=5):
        self.location = True # True is left side, False is right side
        self.passengers_amount = 0
        self.max_members = max_members
        self.mutex = Lock()
        self.right_bank = Condition(self.mutex)
        self.left_bank = Condition(self.mutex)

    def take_place(self, location):
        with self.mutex:
            current_bank = self.left_bank if location else self.right_bank
            self.passengers_amount += 1
            print(f"Passengers Amount: {self.passengers_amount}")
            while self.location != location and self.passengers_amount != self.max_members:
                current_bank.wait()
                print("Passengers", self.passengers_amount)

    def get_to_another_side(self):
        print('Cross the river')
        time.sleep(2)

    def get_off_boat(self):
        with self.mutex:
            while self.passengers_amount:
                print('Bouat unpacking')
                self.passengers_amount -=1
                time.sleep(.5)
            self.location = not self.location
            current_bank = self.left_bank if self.location else self.right_bank
            current_bank.notify_all()


boat = Boat()
def person(location):
    boat.take_place(location)
    boat.get_to_another_side()
    boat.get_off_boat()

for i in [True, False, True, False, True]:
    p1 = Thread(target=person, args =(1,))
    p2 = Thread(target=person, args =(2,))
    p3 = Thread(target=person, args =(3,))
    p4 = Thread(target=person, args =(4,))
    p5 = Thread(target=person, args =(5,))
    p6 = Thread(target=person, args =(6,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()

    time.sleep(5)









