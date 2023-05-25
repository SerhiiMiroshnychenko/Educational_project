class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def get_data(self):
        return self._value

    def get_next(self):
        return self._next

    def set_data(self, value):
        self._value = value

    def set_next(self, next):
        self._next = next



class OrderedList:

    def __init__(self):
        self._head = None

    def search(self, item):
        current = self._head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                current = current.get_next()

        return found

    def add(self, item):
        current = self._head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self._head)
            self._head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def is_empty(self):
        return self._head is None

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()

        return count

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

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<OrderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return f"{representation}>"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = OrderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list.search(93))
    print(my_list.search(100))
    print(my_list)
    my_list.remove(54)
    print(my_list)
