"""INFINITY"""

x = 1.79e308
k = 0

print(f'We have number "{x}. "')
print("Let's see how many times we can multiply it by 1.001:\n")

while x != 1.8e308:
    k += 1
    print(f'Iteration N°: {k}')
    print(f'"{x}" * 1.001 = {x * 1.001}\n')
    x *= 1.001

print(f'We were able to do this {k} times and got INFINITY ♾️!')
