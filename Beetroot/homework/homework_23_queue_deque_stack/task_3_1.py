# Task 3.1
#
# Extend the Stack to include a method called get_from_stack that searches
# and returns an element e from a stack. Any other element must remain
# on the stack respecting their order. Consider the case in which the element
# is not found - raise ValueError with proper info Message

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
        print('\n')
        for index in range(self.size() - 1, -1, -1):
            print(f"|{f'{self._items[index]}': ^5}|\n", end='')
        print('<Stack>\n')

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

    def change(self, position, item):
        hash_stack = Stack()
        for i in range(position):
            if i == position - 1:
                self.pop()
                hash_stack.push(item)
            else:
                hash_stack.push(self.pop())
        while not hash_stack.is_empty():
            self.push(hash_stack.pop())

    def get(self, element):
        is_element = False
        hash_stack = Stack()
        for _ in range(self.size()):
            item = self.pop()
            if item == element:
                is_element = True
                break
            hash_stack.push(item)

        while not hash_stack.is_empty():
            self.push(hash_stack.pop())

        if is_element:
            return element
        else:
            raise ValueError(f'There is not the element {element} in the stack.')

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

    for i in range(10, 60, 10):
        s.push(i)
    s.display()

    s.change(3, 300)
    s.display()

    s.change(1, 500)
    s.display()

    s.change(5, 1000)
    s.display()

    print(s.get(300))
    s.display()

    try:
        s.get(3000)
    except ValueError as e:
        print(e)

    s.display()
