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


text_1 = "(a(b)c ())"
text_2 = "((as)))"
text_3 = ")((gfd))"
text_4 = ")()("


def balanced(text):
    brackets = Stack()
    for char in text:
        if char == "(":
            brackets.push(char)
            print(brackets.print_stack())
        elif char == ")":
            if brackets.is_empty():
                brackets.push(char)
            else:
                brackets.pop()
            print(brackets.print_stack())
    print(brackets.print_stack())
    if brackets.is_empty():
        return True
    else:
        return False


print(balanced(text_1))
print()
print(balanced(text_2))
print()
print(balanced(text_3))
print()
print(balanced(text_4))