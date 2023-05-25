class Account:
    # def __new__(self):
    #     print("__new__ called A new account is Created.")

    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance
        print("(__init__) Account Created with {} balance".format(self._balance))

    def getBalance(self):
        return self._balance

    def __add__(self, other):
        return self.name + other.name

    def __repr__(self):
        return "(__repr__) Account({0}, {1})".format(self.name, self._balance)

    def __str__(self):
        return "(__str__) Account Name = {0}, Account Balance = {1}".format(self.name, self._balance)

    def __lt__(self, otherObj):
        try:
            return self._balance < otherObj.getBalance()
        except:
            return "Cannot Be compared."

    def __del__(self):
        self._balance = 0
        print("(__del__) Account Deleted")

#
# digvijay_ac = Account("Digvijay Singh", 500)
# saket_ac = Account("Digvijay Singh", 700)
# print(digvijay_ac + saket_ac)
# # digvijay_ac.__add__(saket_ac)
#
# print(str(digvijay_ac))
# print(repr(digvijay_ac))
# print(digvijay_ac < saket_ac)


class Students(object):
    def __init__(self, idNo, grade):
        self._idNo = idNo
        self._grade = grade

    def __new__(cls, idNo, grade):
        print("Creating Instance")
        instance = super(Students, cls).__new__(cls)
        if 5 <= grade <= 10:
            return instance
        else:
            return None

    def __str__(self):
        return '{0}({1})'.format(self.__class__.__name__, self.__dict__)


stud1 = Students(1, 7)
print(stud1)

stud2 = Students(2, 12)
print(stud2)