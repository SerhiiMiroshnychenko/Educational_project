# Task 3.2
#
# Extend the Queue to include a method called get_from_stack that searches
# and returns an element e from a queue. Any other element must remain
# in the queue respecting their order. Consider the case in which the element
# is not found - raise ValueError with proper info Message

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

    def is_full(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def get(self, element):
        is_element = False
        hash_queue = Queue()
        for _ in range(self.size()):
            item = self.dequeue()
            if item == element:
                is_element = True
            else:
                hash_queue.enqueue(item)

        while not hash_queue.is_empty():
            self.enqueue(hash_queue.dequeue())

        if is_element:
            return element
        else:
            raise ValueError(f'There is not the element {element} in the queue.')

    def front(self):
        if self._items:
            value = self._items.pop(0)
            self._items.insert(0, value)
            return value
        else:
            return None
    def tail(self):
        if self._items:
            value = self._items.pop()
            self._items.append(value)
            return value
        else:
            return None

    def size(self):
        return len(self._items)
    def display(self):
        print('\n->enter')
        for index in range(self.size() - 1, -1, -1):
            print(f"|{f'{self._items[index]}': ^5}|\n", end='')
        print('exit->\n')

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
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.display())
    q.dequeue()
    q.display()
    print(f'Front: {q.front()}')
    print(f'Tail: {q.tail()}')
    q.display()
    print(q.get(4))
    q.display()

    try:
        q.get(3000)
    except ValueError as e:
        print(e)

    q.display()
