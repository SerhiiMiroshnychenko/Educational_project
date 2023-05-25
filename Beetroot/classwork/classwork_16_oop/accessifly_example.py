from accessify import private

class Point:
    def __init__(self, x, y):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)
    