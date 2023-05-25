import multiprocessing
import time


def f(x):
    print(multiprocessing.current_process())
    return x * x



if __name__ == "__main__":

    with multiprocessing.Pool(processes=4) as pool:
        result = pool.apply_async(f, (10,)) # evaluate "f(10)" asynchronously in a single process
        print(result.get(timeout=1))        # prints "100" unless your computer is *very* slow

        print(pool.map(f, range(10)))       # prints "[0, 1, 4,..., 81]"

        it = pool.imap(f, range(10))
        print(next(it))                     # prints "0"
        print(next(it))                     # prints "1"
        print(it.next(timeout=1))           # prints "4" unless your computer is *very* slow

        result = pool.apply_async(time.sleep, (10,))
        try:
            print(result.get(timeout=1))
        except multiprocessing.context.TimeoutError as e:
            print(e.__class__, e)
        # result1 = pool.apply_async(f, (10,))
        # result2 = pool.apply_async(f, (20,))
        # result3 = pool.apply_async(f, (30,))
        # result4 = pool.apply_async(f, (40,))
