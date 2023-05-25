class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def print_queue(self):
        print(self.items)


q = Queue()
q.enqueue(99)
q.enqueue(15)
q.enqueue(82)
q.enqueue(50)
q.enqueue(47)
q.print_queue()

q.dequeue()
q.print_queue()