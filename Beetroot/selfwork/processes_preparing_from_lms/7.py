import multiprocessing

result = multiprocessing.Array('i', range(4))
temp = [1, 2, 3, 4]
def square_list(mylist, res):
    global result
    for ind, num in enumerate(mylist):
        res[ind]= num * num
    print(f"Result(in process p1): {result[:]}")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_list, args=(temp, result))
    p1.start()
    p1.join()
    print(result[:])
