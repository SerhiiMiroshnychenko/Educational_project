class Node:
    # constructor
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    # get value from node
    def getData(self):
        return self.data

    # get next node reference
    def getNext(self):
        return self.next

    # set value to node
    def setData(self, newdata):
        self.data = newdata

    # set next node reference
    def setNext(self, newnext):
        self.next = newnext

class OrderedList:
    def __init__(self):
        self.head = None

    # check if the list is empty
    def isEmpty(self):
        return self.head is None

    # insert item to be the first item of the list
    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    # size of the list
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    # find if item is in the list
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()

        return found

    # remove item from the list
    def remove(self, item):
        current = self.head
        previous = None
        found =False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    # insert the item to be last element of list
    def append(self, item):
        current = self.head
        temp = Node(item)
        while current != None:
            current = current.getNext()

        current.setNext(temp)

    # get index of item in the list
    def index(self, item):
        current = self.head
        found = False
        index = 0

        while current != None and not found:
            if current.getData() != item:
                index +=1
                current = current.getNext()
            else:
                found = True

        return index if found else "Not Found"

        # remove last item of the list
    def pop(self):
        current = self.head
        previous = None

        if current is None:
            return "No item in list"

        while current.getNext() != None:
            previous = current
            current = current.getNext()

        previous.setNext(None)
        return current.getData()

      # remove item from the pos-th of the list
    def delete(self, pos):
        current = self.head
        previous = None
        index = 0

        if current is None:
            return "No item in list"

        while index < pos and current != None:
            previous = current
            current = current.getNext()
            index += 1

        if current is None:
            return "No item in list"
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return current.getData()



def main():
    orderedlist = OrderedList()
    orderedlist.add(3)
    orderedlist.add(1)
    print(orderedlist.pop())

if __name__ == "__main__":
    main()