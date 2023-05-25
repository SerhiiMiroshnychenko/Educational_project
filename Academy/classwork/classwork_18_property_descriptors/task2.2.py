class Person:
    education_level = 0



class School(Person):
    def __init__(self, f_name, s_name):
        super().__init__(f_name, s_name)
        if self.check_level() == 0:
            self.education_level += 1
        else:
            print('Denied')

    @staticmethod
    def check_level():
        return super().education_level