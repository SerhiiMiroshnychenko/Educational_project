class SomeClass:
    def __init__(self, code:str, atr):
        self.__code = code
        self.__atr = atr

    @property
    def atr(self):
        if self.__check_code():
            return self.__atr

    @atr.setter
    def atr(self, atr):
        if self.__check_code():
            self.__atr = atr


    @atr.deleter
    def atr(self):
        if self.__check_code():
            del self.__atr

    def __check_code(self):
        return input('Enter the code: ') == self.__code


test = SomeClass('01', 22)
print(test)
print(test.atr)
test.set_atr = 22
print(test.atr)
del test.atr
