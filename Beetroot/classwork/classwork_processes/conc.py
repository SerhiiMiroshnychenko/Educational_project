from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def func(started=0, finished=0):
    my_list = [i ** 2 for i in range(started, finished)]
    result = sum(my_list)
    return str(result)


def run_1(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()

    future_1 = executor.submit(func, started=0, finished=2 ** 10)
    future_2 = executor.submit(func, started=2 ** 10, finished=2 ** 20)

    result = float(future_2.result()) + float(future_1.result())

    print('Result: {result}. Time for {executor}: {spent_time}'.format(
        result=result,
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


def run_2(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()

    future_1 = executor.submit(func, started=0, finished=2 ** 14)
    future_2 = executor.submit(func, started=2 ** 14, finished=2 ** 28)

    result = float(future_2.result()) + float(future_1.result())

    print('Result: {result}. Time for {executor}: {spent_time}'.format(
        result=result,
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


if __name__ == "__main__":
    print('RUN 1 Execute using submit...')
    run_1(ThreadPoolExecutor)
    run_1(ProcessPoolExecutor)

    print('RUN 2 Execute using submit...')
    run_2(ThreadPoolExecutor)
    run_2(ProcessPoolExecutor)
