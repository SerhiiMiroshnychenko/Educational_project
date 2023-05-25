# Зв'язаний список
class MyLinkedList:
    # Each element in MyList is a Node
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.size = 0

    # Add an element tothe head of the list
    def add(self, data):

        if self.head:
            new = self.Node(data)
            new.next = self.head.next
            self.head.next = new
        else:
            self.head = self.Node(data)

        self.size += 1

    # Remove the first element
    def pop(self):
        removed = self.head.data
        self.head = self.head.next
        return removed

    def is_empty(self):
        if self.size:
            return False
        else:
            return True

    def list_size(self):
        return self.size

    # Gets a Node and prints it's data
    def recursive_show(self, current):
        # If current is None, go home
        if not current:
            print("None")
            return

        print(current.data, end=' -> ')
        self.recursive_show(current.next)


#
# Test the Linked List functionality
#
link = MyLinkedList()
print("list is empty:", link.is_empty())

link.add("Not a language")
link.add("Python")
link.add("Java")
link.add("Bash")
link.add("C")

print(link.list_size(),
      "elements added to the list.")

print("\nList looks like:")
link.recursive_show(link.head)

print("Take out first element:", link.pop())

print("\nList looks like:")
link.recursive_show(link.head)

print("list is empty:", link.is_empty())

# The END :-)