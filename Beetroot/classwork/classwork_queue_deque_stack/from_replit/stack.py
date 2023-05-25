class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def print_stack(self):
        print(self.items)


names = Stack()
print("Adding an item to the stack!!!")
names.push("Sanija")
names.push("Sam")
names.push("Andre")

names.print_stack()
names.pop()
print("\n")
print("Removing an item from the stack!!!")
names.print_stack()
print("\n")
print("Checking if the stack is empty or not!!!")
print(names.is_empty())
print("\n")
print(type(names))