from classwork.classwork_4_list_tuple_set.preparation.generator_list import res


class ExecutionCounter:

  def __init__(self, func):
    self.func = func
    self.call_count = 0
    self.limit = 5
  def __call__(self, *args, **kwargs):
    while True:
      if self.call_count == self.limit:
        break
      self.call_count += 1
      print(f"Called {self.func.__name__} for the {self.call_count}th time")
    return self.func(*args, **kwargs)

@ExecutionCounter
def multiply(number_a:int, number_b:int):
  """ multiplies two provided numbers """
  return number_a * number_b

res1 = multiply(7, 8)
res2 = multiply(6, 7)
res3 = multiply(5, 6)
res4 = multiply(4, 5)
res5 = multiply(3, 4)
res6 = multiply(2, 3)
res7 = multiply (1,2)
print(res1, res2, res3, res4, res5, res6, res7, sep='\n')