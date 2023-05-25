import time
from threading import *


class Boat:
    def __init__(self, max_members=5):
        self.location = True  # True - left side, False - right side
        self.passengers_amount = 0
        self.max_members = max_members
        self.mutex = Lock()
        self.right_bank = Condition(self.mutex)
        self.left_bank = Condition(self.mutex)

    def take_place(self, location):
        with self.mutex:
            current_bank = self.left_bank if location else self.right_bank
            self.passengers_amount += 1
            while self.location != location and self.passengers_amount != self.max_members:
                current_bank.wait()
                print('Passengers', self.passengers_amount)

    def get_to_another_side(self):
        print('Cross the river')
        time.sleep(2)

    def get_off_boat(self):
        with self.mutex:
            while self.passengers_amount != 0:
                print('Boat unpacking')
                self.passengers_amount -= 1
                time.sleep(0.5)
            else:
                self.location = not self.location
                current_bank = self.left_bank if self.location else self.right_bank
                current_bank.notify_all()


boat = Boat()


def person(location):
    boat.take_place(location)
    boat.get_to_another_side()
    boat.get_off_boat()


for i in [True, False, True, False]:
    t1 = Thread(target=person, args=(i,))
    t2 = Thread(target=person, args=(i,))
    t3 = Thread(target=person, args=(i,))
    t4 = Thread(target=person, args=(i,))
    t5 = Thread(target=person, args=(i,))
    t6 = Thread(target=person, args=(i,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    time.sleep(10)
