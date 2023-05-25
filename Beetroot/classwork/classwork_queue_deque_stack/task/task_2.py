from pythonds.basic import Queue  # type: ignore


def hot_potato(names, number):
    queue_ = Queue()
    for name in names:
        queue_.enqueue(name)

    while queue_.size() > 1:
        for _ in range(number):
            queue_.enqueue(queue_.dequeue())

        queue_.dequeue()

    return queue_.dequeue()


if __name__ == '__main__':
    for number in range(1, 20):
        print(hot_potato(['Adam', 'Brand', 'Ceo', 'David', 'Eva'], number))
