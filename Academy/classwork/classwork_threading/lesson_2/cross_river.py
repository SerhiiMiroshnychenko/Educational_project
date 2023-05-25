import time
from threading import *


class Boat:
    def __init__(self):
        self.boatlocation = True  # T for left bank, F for right
        self.boatcount = 0
        self.mutex = Lock()
        self.leftbank = Condition(self.mutex)
        self.rightbank = Condition(self.mutex)

    def ArriveAtBoat(self, location):
        with self.mutex:
            mybank = self.leftbank if location else self.rightbank
            while self.boatlocation != location or self.boatcount == 3:
                mybank.wait()

    def GetOffOfBoat(self, location):
        with self.mutex:
            self.boatcount -= 1
            if self.boatcount == 0:
                # we arrived on the other side, update boat direction
                self.boatlocation = not self.boatlocation
                newbank = self.leftbank if location else self.rightbank
                newbank.notifyAll()

    def BoardBoatAndCrossRiver(self):
        print('crossing river')
        time.sleep(2)


def person(location):
    print(current_thread().getName())
    boat.ArriveAtBoat(location)
    boat.BoardBoatAndCrossRiver()
    boat.GetOffOfBoat(location)


global boat

boat = Boat()

for i in [0, 1, 0, 1]:
    t1 = Thread(target=person, args=(i,))
    t2 = Thread(target=person, args=(i,))
    t3 = Thread(target=person, args=(i,))

    t1.start()
    t2.start()
    t3.start()

