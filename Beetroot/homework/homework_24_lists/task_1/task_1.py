# Task 1

# Extend UnorderedList
# Implement append, index, pop, insert methods for UnorderedList.
# Also implement a slice method, which will take two parameters `start`
# and `stop`, and return a copy of the list starting at the position and
# going up to but not including the stop position.

class Node:
    """Вузол"""
    def __init__(self, value):
        self._value = value
        self._next = None

    def get_value(self):
        """Повертаємо значення"""
        return self._value

    def get_next(self):
        """Повертаємо наступний вузол"""
        return self._next

    def set_value(self, value):
        """Встановлюємо значення"""
        self._value = value

    def set_next(self, next):
        """Встановлюємо наступний вузол"""
        self._next = next

class LinkedList:
    """
    Unordered Linked List
    """

    def __init__(self):
        self._head = None

    def is_empty(self):
        """Визначаємо, чи є пустий"""
        return self._head is None

    def size(self):
        """Визначаємо кількість вузлів"""
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def add(self, value):
        """Додаємо новий вузол до голови"""
        node = Node(value)
        node.set_next(self._head)
        self._head = node

    def append(self, value):
        """Додаємо новий вузол до хвоста"""
        node = Node(value)

        if self.size() == 0:
            node.set_next(self._head)
            self._head = node
            return None
        current = self._head
        while current is not None:
            if current.get_next() is None:
                current.set_next(node)
                return None
            current = current.get_next()

    def delete(self):
        """Видаляємо вузол-голову"""
        self._head = self._head.get_next()

    def get_head(self):
        """Повертає значення вузла-голови"""
        return self._head.get_value()

    def get(self, index):
        """Повертає значення вузла за індексом"""
        current = self._head
        if index != 0:
            index_counter = 0
            while index_counter < index:
                current = current.get_next()
                index_counter += 1
            return current.get_value()
        else:
            self.get_head()

    def pop(self):
        """Видаляємо вузол-хвіст та повертаємо значення"""
        if self.size() == 1:
            value = self.get_head()
            self.delete()
            return value
        current = self._head
        while current.get_next() is not None:
            if current.get_next().get_next() is None:
                value = current.get_next().get_value()
                current.set_next(None)
                return value
            current = current.get_next()

    def search(self, item):
        """Шукаємо вузол за значенням"""
        current = self._head
        while current is not None:
            if current.get_value() == item:
                return True
            current = current.get_next()
        return False

    def remove(self, item):
        """Видаляємо вузол за значенням"""
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
        """Вставка вузла в відповідну позицію"""
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

    def index(self, item):
        """Визначаємо індекси вузлів, що відповідають значенню"""
        index_counter = 0
        indexes = []
        current = self._head
        while current is not None:
            index_counter += 1
            if current.get_value() == item:
               indexes.append(index_counter)
            current = current.get_next()
        if len(indexes):
            print(f'We find "{item}" in the list with index: {indexes}.')
            return indexes
        print(f'We do not find "{item}" in the list.')
        return None

    def slice(self, start, end):
        """Повертаємо зріз списку"""
        slice_node = LinkedList()
        index_counter = 0
        current = self._head
        while current is not None:
            if start <= index_counter < end:
                slice_node.append(current.get_value())
            index_counter += 1
            current = current.get_next()
        return slice_node

    def clear(self):
        self._head = None

    def __repr__(self):
        """Репрезентація"""
        base_string = ''
        current = self._head
        while current is not None:
            base_string += f'{current.get_value()} -> '
            current = current.get_next()
        base_string += 'None'
        return base_string


if __name__ == '__main__':
    list_ = LinkedList()

    for elem in range(11):
        list_.add(elem)

    print(list_)

    list_.append(-1)
    list_.append(-2)
    print(list_)

    print(list_.pop())
    list_.pop()
    print(list_)

    for elem in range(11):
        list_.append(elem)
    print(list_)

    list_.index(5)

    new_list = list_.slice(1, 6)

    print(new_list)
    new_list.insert(2, 77)
    print(new_list)
    new_list.remove(7)
    new_list.delete()
    print(new_list)

    print(new_list.get(1))
    print(list_.get(3))

    list_.clear()
    print(list_.size())
