def solve(numbers):
   numbers_map = {}
   for i in set(numbers):
      x=numbers.count(i)
      try:
         numbers_map[x].append(i)
      except KeyError:
         numbers_map[x]=[i]
   result=[]

   for i in sorted(numbers_map):
      for j in sorted(numbers_map[i], reverse=True):
         result.extend([j]*i)
   return result

def frequency_sort(a):
   import collections
   f = collections.Counter(a)
   a.sort(key = lambda x:(-f[x], x))
   return a

def frequency_sort_(items):
    return sorted(items, key = lambda x: (-items.count(x), items.index(x)))

def frequency_sorting(numbers):
    dict_ = {}
    for number in numbers:
        if number in dict_:
            dict_[number] += 1
        else:
            dict_[number] = 1
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1-i):
            if dict_[numbers[j]] > dict_[numbers[j+1]]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__ == "__main__":
    numbers = [1,5,3,1,3,1,2,5,1,6,7,8,8,7,7,6,0,5]
    print(solve(numbers))
    numbers = [1,5,3,1,3,1,2,5,1,6,7,8,8,7,7,6,0,5]
    print(frequency_sort(numbers))
    numbers = [1,5,3,1,3,1,2,5,1,6,7,8,8,7,7,6,0,5]
    print(frequency_sort_(numbers))
    numbers = [1,5,3,1,3,1,2,5,1,6,7,8,8,7,7,6,0,5]
    print(frequency_sorting(numbers))
