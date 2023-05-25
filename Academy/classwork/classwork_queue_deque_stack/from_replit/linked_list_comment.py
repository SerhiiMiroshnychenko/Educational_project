"""I FOUND OUT THAT IN PYTHON DATA STRUCTURES COURSE LINKED LIST MODULE WAS NOT
 PROPERLY EXPLAINED,AND THERE WERE NO COMMENTS PROVIDED IN THE GIVEN CODE.THEREFORE I
 COMMENTED THIS CODE WITH BEST OF MY KNOWLEDGE.


PLEASE UPVOTE THIS CODE SO THAT IT CAN REACH OUT TO MANY PEOPLE WHO ARE FINDING
DIFFICULTY IN LINKED LIST MODULE .

ALL SUGGESTIONS ARE WELCOMED POSITIVELY .

"""


# Node class with data and next(LINK) attributes
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


# linkedlist class
class LinkedList:

    # empty linked list
    def __init__(self):
        self.head = None

    # Node is added with data but next attribute(LINK PART OF THE NODE) is passed as None
    def add_at_front(self, data):
        self.head = Node(data, self.head)

    def add_at_end(self, data):
        # if self.head==None :
        if not self.head:
            # Node is added with data but next attribute(node link) is passed as None
            self.head = Node(data, None)
            # gets out from the function with return statement
            return
        # this part is only relevant if linkedlist is not empty(self.head!=None)
        curr = self.head
        # infinite loop begins

        while curr.next:
            curr = curr.next
            # when curr.next==None ,loop breaks
            # loop breaks by passing the last element of the linkedlist

        # next element of the present last element is replaced  with Node of data from add_at_end function
        # link of the last node is passed as None
        curr.next = Node(data, None)

    def get_last_node(self):
        n = self.head
        # loop runs only if linkedlist contains more than one element
        while (n.next != None):
            # n is replaced with its next node
            n = n.next
            # loop breaks at last value of the node
        # returns data contained in the last node
        return n.data

    # if linkedlist is empty then returnS True else False
    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        # loop runs only if linked list is not empty
        while n != None:
            # data of each node is printed with the given string (one by one) on the same line
            print(n.data, end=" => ")
            n = n.next
        print()


s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()
print(s.get_last_node())