import multiprocessing


result = []

def square_list(mylist):
    global result
    for num in mylist:
        result.append(num * num)
    print(f"Result(in process p1): {result}")


if __name__ == "__main__":

    temp = [1, 2, 3, 4]

    p1 = multiprocessing.Process(target=square_list, args=(temp,))
    p1.start()
    p1.join()

    print(result)
