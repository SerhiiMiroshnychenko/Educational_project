#Task 2
#Implement a stack using a singly linked list.

from homework.homework_24_lists.task_1.task_1 import LinkedList

class Stack:
    """
    Implement a stack using a singly linked list.
    """

    def __init__(self):
        self._items = LinkedList()

    def is_empty(self):
        """Перевіряємо чи порожній"""
        return self._items.is_empty()

    def push(self, item):
        """Додаємо елемент"""
        self._items.add(item)

    def show(self):
        """Показати верхній без видалення"""
        return self._items.get_head()

    def pop(self):
        """Повертає верхній елемент з видаленням"""
        value = self.show()
        self._items.delete()
        return value

    def peek(self):
        """Показати нижній елемент без видалення"""
        return self._items.get(self._items.size() - 1)

    def size(self):
        """Обчислити розмір"""
        return self._items.size()

    def copy(self):
        """Створити копію"""
        stack_slice = self._items.slice(0, self._items.size())
        copy_stack = Stack()
        for _ in range(self._items.size()):
            copy_stack.push(stack_slice.pop())
        return copy_stack

    def clear(self):
        """Очистити"""
        self._items.clear()

    def __repr__(self):
        """Репрезентація"""
        if self.size() == 0:
            return 'None'
        repr_stack = self._items.slice(0, self._items.size())
        repr_string = '\n'
        for _ in range(self._items.size()):
            repr_string += f"|{f'{repr_stack.get_head()}': ^5}|\n"
            repr_stack.delete()
        repr_string += '<Stack>\n'
        return repr_string

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    my_stack = Stack()
    print('My stack is empty: ', my_stack.is_empty())

    for elem in range(11):
        my_stack.push(elem)
    print('My stack:', my_stack)
    print('My stack is empty: ', my_stack.is_empty())
    print('My stack size:', my_stack.size())

    print('My stack show: ', my_stack.show())
    print('My stack pop: ', my_stack.pop())
    print('My stack peek: ',my_stack.peek())
    print('My stack:', my_stack)

    new_stack = my_stack.copy()
    print('New stack:', new_stack)

    my_stack.clear()
    print('My stack:', my_stack)
    print('New stack:', new_stack)
