# Task 2
# Create your own implementation of a built-in function range, named in_range(),
# which takes three parameters: `start`, `end`, and optional step.
# Tips: See the documentation for `range` function

def in_range(start: int, end: int, step: int=0):
    ind = start

    while ind < end:
        yield ind
        ind += step


c = in_range(2, 20, 2)

print(c)
print(*c)
print(type(c))
for i in in_range(2, 20, 2):
    print(i * 1.0, end='...')
for i in c:
    print(i * 1.0, end='---')
