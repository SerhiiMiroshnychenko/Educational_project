#Task 3
#Implement a queue using a singly linked list.

from homework.homework_24_lists.task_1.task_1 import LinkedList

class Queue:
    """
    Implement a queue using a singly linked list.
    """

    def __init__(self):
        self._items = LinkedList()

    def is_empty(self):
        """Перевіряємо чи порожня"""
        return self._items.is_empty()

    def front(self):
        """Показуємо початок черги"""
        print(self._items.get(self._items.size() - 1))

    def tail(self):
        """Показуємо хвіст черги"""
        print(self._items.get_head())

    def enqueue(self, item):
        """Додаємо елемент в чергу"""
        self._items.add(item)

    def dequeue(self):
        """Видаляємо елемент з черги"""
        return self._items.pop()

    def size(self):
        """Обчислити розмір"""
        return self._items.size()

    def __repr__(self):
        """Репрезентація"""
        if self.size() == 0:
            return 'None'
        repr_stack = self._items.slice(0, self._items.size())
        repr_string = '\n->Enter\n'
        for _ in range(self._items.size()):
            repr_string += f"|{f'{repr_stack.get_head()}': ^5}|\n"
            repr_stack.delete()
        repr_string += '->Exit\n'
        return repr_string

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    my_queue = Queue()

    print(my_queue.is_empty())
    print(my_queue.size())

    for char in 'abcdefgh':
        my_queue.enqueue(char)

    print(my_queue.is_empty())
    print(my_queue.size())
    print(my_queue)

    my_queue.dequeue()
    print(my_queue)

    my_queue.front()
    my_queue.tail()
