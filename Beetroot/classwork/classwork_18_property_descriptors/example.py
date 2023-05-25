# We want to extend the usability of the Celsius class defined above. We know that the
# temperature of any object cannot reach below -273.15 degrees Celsius (Absolute Zero in Thermodynamics)


class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return f'{self._temperature} C*'

    @temperature.setter
    def temperature(self, value):
        if value >= -273.15:
            self._temperature = value
        else:
            print('Too low temperature')

    @temperature.deleter
    def temperature(self):
        self._temperature = 0

    def to_fahrenheit(self):
        return self._temperature * 1.8 + 32


c = Celsius(10)
c.temperature = - 10000
print(c.temperature)
print(c.to_fahrenheit())
del c.temperature
print(c.temperature)
