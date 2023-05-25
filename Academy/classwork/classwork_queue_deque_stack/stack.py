"""СТЕК"""
# LIFO, «останній прийшов – перший вийшов»
class Stack:
    def __init__(self, max_length=None):
        self._items = []
        self._max_length = max_length

    def is_empty(self):
        return not bool(self._items)

    def is_full(self):
        return len(self._items) == self._max_length

    def push(self, item):
        if self._max_length:
            if len(self._items) < self._max_length:
                self._items.append(item)
            else:
                print('<Stack overflow>')
        else:
            self._items.append(item)

    def top(self):
        return self._items[-1]

    def display(self):
        for index in range(self.size() - 1, -1, -1):
            print(f'|{self._items[index]}|')
        print('__')

    def peek(self, position):
        hash_stack = Stack()
        for i in range(position):
            if i == position - 1:
                value = self.pop()
            else:
                hash_stack.push(self.pop())
        while not hash_stack.is_empty():
            self.push(hash_stack.pop())
        return value

    def pop(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    s = Stack()

    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek(2))
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s)

    for i in range(6):
        s.push(i)
    def pop(self):
        return self._items.pop()
    s.display()
    s.peek(3)
    s.display()
