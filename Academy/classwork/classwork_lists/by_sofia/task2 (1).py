# extend the doubly linked list to be circular
# https://www.geeksforgeeks.org/circular-linked-list-set-2-traversal/

from node_double import Node


class UnorderedDoubleList:

    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        if self.size() == 0:
            self._head = temp
            self._tail = temp
        else:
            temp.set_next(self._head)
            self._head.set_previous(temp)
            self._head = temp
            self._head.set_previous(self._tail)

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

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
            self._head.set_previous(None)
        elif next_ is None:
            self._tail = previous
            self._tail.set_next(self._head)
        else:
            previous.set_next(current.get_next())
            current.get_next().set_previous(previous)

    def __repr__(self):
        representation = "<UnorderedDoubleList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedDoubleList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))
    print(my_list)
