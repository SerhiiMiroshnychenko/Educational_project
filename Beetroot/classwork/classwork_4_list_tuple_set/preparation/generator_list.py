def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


res = list(numbers(11))
print(res)

res2 = [i for i in range(20) if i % 2 == 0]
print(res2)
