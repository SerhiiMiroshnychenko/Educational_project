class Car:
    def __init__(self, brand:str, year:int, color:str):
        self.brand = brand
        self.year = year
        self.color = color
        self.tank_full = False
        self.status = 'is standing'

    def refuel(self):
        if self.tank_full:
            print("Tank already full")
        else:
            self.tank_full = True
            print("Tank full")

    def go(self):
        if self.tank_full:
            print("The car goes!")
            self.status = 'is going'
        else:
            print('Fuel the car')


    def stop(self):
        if self.status == 'is going':
            print("The car stops")
            self.status = 'is standing'
        else:
            print("The car is already standing")


if __name__ == '__main__':
    bmv = Car('BMV', 2020, 'black')
    bmv.stop()
    bmv.go()
    bmv.refuel()
    bmv.go()
    bmv.stop()


