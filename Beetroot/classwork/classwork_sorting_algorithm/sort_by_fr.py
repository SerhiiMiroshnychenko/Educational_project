def frequency_sorting(numbers):
    dict_ = {}
    for number in numbers:
        if number in dict_:
            dict_[number] += 1
        else:
            dict_[number] = 1
    numbers = quick_sort(numbers, dict_)
    return numbers

def quick_sort(numbers, dict_):
    import random
    if len(numbers) > 1:
        x = numbers[random.randint(0, len(numbers)-1)]
        low = [u for u in numbers if dict_[u] < dict_[x]]
        eq = [u for u in numbers if dict_[u] == dict_[x]]
        hi = [u for u in numbers if dict_[u] > dict_[x]]
        numbers = quick_sort(low, dict_) + eq + quick_sort(hi, dict_)
    return numbers


numbers = [1,5,3,1,3,1,2,5,1,6,7,8,8,7,7,6,0,5]
print(frequency_sorting(numbers))
