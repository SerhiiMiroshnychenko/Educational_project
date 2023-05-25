numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)
print(a + b + c)

x, y = [1, 2]
x, y = y, x
print(x)
print(y)

i, j, *k, l = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(i)
print(j)
print(k)
print(l)

n, *m, u = "Python"
print(n)
print(m)
print(u)

_, *tail = "Python"
print(_, tail)

*head, _ = "Python"
print(_, head)
