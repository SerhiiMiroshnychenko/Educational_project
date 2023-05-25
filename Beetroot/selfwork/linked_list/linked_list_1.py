# From: https://stackabuse.com/python-linked-lists/

class ListNode:
    """ВУЗОЛ ОДНОЗВ’ЯЗАНОГО СПИСКУ"""
    def __init__(self, data):
        """constructor to initiate this object"""

        # store data
        self.data = data

        # store reference (next item)
        self.next = None
        return

    def has_value(self, value):
        """method to compare the value with the node data"""
        return self.data == value

class SingleLinkedList:
    """ОДНОЗВ'ЯЗАНИЙ СПИСОК"""
    def __init__(self):
        """constructor to initiate this object"""

        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        """add an item at the end of the list"""

        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return

    def list_length(self):
        """returns the number of list items"""

        count = 0
        current_node = self.head

        while current_node is not None:
            # increase counter by one
            count = count + 1

            # jump to the linked node
            current_node = current_node.next

        return count

    def output_list(self):
        """outputs the list (the value of the node, actually)"""

        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            # jump to the linked node
            current_node = current_node.next

        return

    def unordered_search (self, value):
        """search the linked list for the node that has this value"""

        # define current_node
        current_node = self.head

        # define position
        node_id = 1

        # define list of results
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)

            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1

            return results

    def remove_list_item_by_id(self, item_id):
        """remove the list item with the item id"""

        current_id = 1
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                if previous_node is None:
                    self.head = current_node.next
                    # we don't have to look any further
                    return

                else:
                    previous_node.next = current_node.next
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1

        return


if __name__ == '__main__':
    # create four single nodes
    node1 = ListNode(15)
    node2 = ListNode(8.2)
    item3 = "Berlin"
    node4 = ListNode(15)

    track = SingleLinkedList()
    print("track length: %i" % track.list_length())

    for current_item in [node1, node2, item3, node4]:
        track.add_list_item(current_item)
        print("track length: %i" % track.list_length())
        track.output_list()