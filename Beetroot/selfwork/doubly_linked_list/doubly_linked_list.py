from doubly_node import DoublyNode  # type: ignore


class UnorderedDoubleList:

    def __init__(self):
        self._head = None
        self._tail = None

    def __repr__(self):
        base_string = ''
        current = self._head
        while current is not None:
            base_string += f'{current.get_value()} -> '
            current = current.get_data()
        base_string += 'None'
        return base_string

    def is_empty(self):
        return self._head is None

    def size(self):
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def add(self, value):
        node = DoublyNode(value)
        if self.size() == 0:
            self._head = node
            self._tail = node
        else:
            node.set_next(self._head)
            self._head.set_prev(node)
            self._head = node
            self._head.set_prev(self._tail)

    def delete(self, value):
        if self.is_empty():
            print("Linked List is empty. Cannot delete elements.")
        elif self._head.next is None:
            if self._head.data == value:
                self._head = None
        else:
            node = self._head
            while node is not None and node.data != value:
                node = node.next
            if node is None:
                print("Element not present in linked list. Cannot delete element.")
            elif node.next is None:
                node = self._head
                while node.next is not None:
                    node = node.next
                node.prev.next = None
                node.prev = None
            else:
                node.next = node.prev.next
                node.next.prev = node.prev
                node.next = None
                node.prev = None

    def search(self, item):
        current = self._head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            elif current is self._tail:
                stop = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
                next_ = current.get_next()

        if previous is None:
            self._head = current.get_next()
            self._head.set_prev(None)
        elif next_ is None:
            self._tail = previous
            self._tail.set_next(self._head)
        else:
            previous.set_next(current.get_next())
            current.get_next().set_prev(previous)

    def insert(self, position, value):
        current = self._head
        previous = None
        if position != 0:
            for _ in range(position):
                previous = current
                current = current.get_next()
            node = DoublyNode(value)
            node.set_next(current)
            previous.set_next(node)
        else:
            self.add(value)


if __name__ == '__main__':
    list_ = UnorderedDoubleList()
    list_.add(5)
    list_.add(4)
    list_.add(3)
    list_.add(2)
    list_.add(1)
    print(list_)
    print(list_.search(6))
    list_.remove(3)
    print(list_)
    list_.insert(2, 3)
    print(list_)
    list_.insert(0, 0)
    print(list_)
