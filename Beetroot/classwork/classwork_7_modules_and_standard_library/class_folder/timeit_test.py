import timeit

# код, що виконується тільки один раз
mysetup = "from itertools import count"

# код, час виконання якого треба виміряти
mycode = '''
def count_down(n):
  for i in count(n,-1):
    if i == 0:
      print(f'Count від number до 0')
      break  
'''

# timeit statement
print(timeit.timeit(setup=mysetup,
                    stmt=mycode,
                    number=20000))

times = timeit.repeat(setup=mysetup,
                      stmt=mycode,
                      repeat=3,
                      number=10000)
print(times)

print(timeit.default_timer())


