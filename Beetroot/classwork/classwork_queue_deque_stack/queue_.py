# from pythonds.basic import Queue

class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        return self._items.pop(0)

    def front(self):
        if self._items:
            return self._items[0]
        else:
            return None

    def rear(self):
        try:
            return self._items[-1]
        except IndexError:
            return None

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(self._items, 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
