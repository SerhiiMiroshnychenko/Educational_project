"""ЧЕРГА"""
# FIFO, перший прийшов – перший вийшов

"""Enqueue() – Adds (or stores) an element to the end of the queue..
Dequeue() – Removal of elements from the queue.
Peek() or front()- Acquires the data element available at the front node of the queue without deleting it.
rear() – This operation returns the element at the rear end without removing it.
isFull() – Validates if the queue is full.
isNull() – Checks if the queue is empty."""
class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def front(self):
        print(self._items[0])

    def tail(self):
        print(self._items[-1])

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def __contains__(self, item):
        return item in self._items


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
