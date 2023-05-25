class DoublyNode:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._prev = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next

    def get_prev(self):
        return self._prev

    def set_prev(self, new_prev):
        self._prev = new_prev

class UnorderedCircularDoubleList:

    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        """Перевірка чи пустий"""
        return self._head is None

    def add(self, value):
        """Додаємо новий вузол"""
        new_node = DoublyNode(value)
        if self.is_empty():
            self._tail = new_node
            self._head = new_node
            new_node.set_next(new_node)
            new_node.set_prev(new_node)
        else:
            self.__add_new_node(new_node)

    def __add_new_node(self, new_node):
        current_head_node = self._head
        current_tail_node = self._tail
        new_node.set_next(current_head_node)
        new_node.set_prev(current_tail_node)
        current_head_node.set_prev(new_node)
        current_tail_node.set_next(new_node)
        self._head = new_node

    def size(self):
        """Визначаємо розмір списку"""
        size_counter = 0
        if self.is_empty():
            return size_counter
        start_node = self._head
        current_node = self._head
        is_finished = False
        while not is_finished:
            size_counter += 1
            current_node = current_node.get_next()
            if current_node == start_node:
                is_finished = True
        return size_counter

    def delete(self, item):
        """Видаляємо всі вузли за заданим значенням"""
        is_find = False

        if self.is_empty():
            print('The list is empty.')
            return is_find
        else:
            current_node = self._head
            previous_node = current_node.get_prev()
            next_node = current_node.get_next()

            if self.size() == 1:
                if current_node.get_data() != item:
                    return is_find
                print(f'We find and delete "{item}"!')
                self._head = self._tail = None

            iteration_number = self.size()
            for _ in range(iteration_number):
                if current_node.get_data() == item:
                    print(f'We find and delete "{item}"!')
                    if current_node == self._head:
                        self._head = current_node.get_next()
                    if current_node == self._tail:
                        self._tail = current_node.get_prev()
                    is_find = True
                    previous_node.set_next(next_node)
                    next_node.set_prev(previous_node)
                    current_node = previous_node
                current_node = current_node.get_next()
                previous_node = current_node.get_prev()
                next_node = current_node.get_next()
        return is_find

    def remove(self, position):
        """Видаляємо вузол за позицією"""
        if self.is_empty():
            print('The list is empty.')
            return False
        elif self.size() < position:
            print(f'The <{position}> position is out of the list.')
            return False
        else:
            current_node = self._head
            previous_node = current_node.get_prev()
            next_node = current_node.get_next()
            iteration_number = self.size()
            for current_position, _ in enumerate(range(iteration_number)):
                if position == current_position:
                    print(f'We find and remove "{current_node.get_data()}".')
                    previous_node.set_next(next_node)
                    next_node.set_prev(previous_node)
                    return True
                current_node = current_node.get_next()
                previous_node = current_node.get_prev()
                next_node = current_node.get_next()
        return False

    def search(self, item):
        """Шукаємо кількість вузлів та їх індекси за заданим значенням"""
        if self.is_empty():
            print('The list is empty.')
            return False
        else:
            item_counter = 0
            item_indexes = []
            current_node = self._head
            iteration_number = self.size()
            for index in range(iteration_number):
                if current_node.get_data() == item:
                    item_counter += 1
                    item_indexes.append(index)
                current_node = current_node.get_next()
        if item_counter > 0:
            print(f'We find the "{item}" in the list <{item_counter}> times with {item_indexes} indexes.')
            return item_counter
        print(f'There is not the <{item}> in the list.')
        return False

    def __repr__(self):
        """Репрезентація"""
        representation = ''
        if self.is_empty():
            representation += 'The list is empty.'
        else:
            current_node = self._head
            representation += 'Head > '
            for _ in range(self.size()):
                representation += f'{current_node.get_data()} > '
                current_node = current_node.get_next()
            representation += 'Tail'
        return representation

    def __str__(self):
        """Стрічковий вигляд"""
        return self.__repr__()


if __name__ == '__main__':
    new_list = UnorderedCircularDoubleList()
    print(new_list.size())
    new_list.add('First element')
    print(new_list.size())
    new_list.add(1)
    print(new_list.size())
    print(new_list)
    for elem in range(10):
        new_list.add(elem)
    print(new_list.size())
    print(new_list)
    new_list.delete(1)
    new_list.delete(9)
    new_list.delete('First element')
    new_list.delete(100)
    print(new_list.size())
    print(new_list)
    new_list.remove(3)
    new_list.remove(100)
    print(new_list.size())
    print(new_list)

    new_list.add(0)
    new_list.add(3)

    new_list.search(0)
    new_list.search(3)

    print(new_list)

    for i in range(10):
        new_list.delete(i)
