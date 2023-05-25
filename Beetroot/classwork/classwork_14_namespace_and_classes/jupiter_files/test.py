class Test:
    x = 3
    def __init__(self, temp):
        self.temp = temp

y = Test(100)
y.x = 2
s = Test(200)
s.x = 5
d = Test(1)
print(s.x, y.x, Test.x, d.x) # 5 2 3 3
Test.x = 22
print(s.x, y.x, Test.x, d.x) # 5 2 22 22