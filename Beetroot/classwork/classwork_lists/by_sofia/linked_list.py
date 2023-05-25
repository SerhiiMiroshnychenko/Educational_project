class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_value(self, value):
        self._value = value

    def set_next(self, next):
        self._next = next


# LinkedList - not ordered
# Вставка – додає елемент на початку списку.
# Видалення – видаляє елемент на початку списку.
# Відображення – відображає повний список.
# Пошук – шукає елемент за допомогою вказаного ключа.
# Видалити – видаляє елемент за допомогою вказаного ключа.
class LinkedList:
    def __init__(self):
        self._head = None

    def __repr__(self):
        base_string = ''
        current = self._head
        while current is not None:
            base_string += f'{current.get_value()} -> '
            current = current.get_next()
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
        node = Node(value)
        node.set_next(self._head)
        self._head = node

    def delete(self):
        self._head = self._head.get_next()

    def search(self, item):
        current = self._head
        while current is not None:
            if current.get_value() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        current = self._head
        previous = None
        while current is not None:
            if current.get_value() == item:
                if previous is None:
                    self.delete()
                else:
                    previous.set_next(current.get_next())
            previous = current
            current = current.get_next()

    def insert(self, position, value):
        current = self._head
        previous = None
        if position != 0:
            for _ in range(position):
                previous = current
                current = current.get_next()
            node = Node(value)
            node.set_next(current)
            previous.set_next(node)
        else:
            self.add(value)


if __name__ == '__main__':
    list_ = LinkedList()
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
