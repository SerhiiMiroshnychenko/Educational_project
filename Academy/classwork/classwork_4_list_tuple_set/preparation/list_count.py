import random

nums = list()
for x in range(1, 25):
    num = random.randint(1, 6)
    nums.append(num)
    print(nums)
k = 1
for y in range(1, 7):
    print(f"Цифра {k} зустрічається {nums.count(k)} разів")
    k += 1
