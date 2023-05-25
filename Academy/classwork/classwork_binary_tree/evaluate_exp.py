from operator import add, sub, mul, truediv
from oop_tree import BinaryTree  # type: ignore
from classwork.classwork_queue_deque_stack.stack import Stack



def parse_exp(expression: str):
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for symbol in expression:
        if symbol == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif symbol in ['+', '-', '*', '/']:
            current_tree.set_root_val(symbol)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif symbol == ')':
            current_tree = stack.pop()
        else:
            try:
                current_tree.set_root_val(int(symbol))
                current_tree = stack.pop()
            except ValueError:
                print('We cant effort character, so we add one')
                current_tree.set_root_val(1)
                current_tree = stack.pop()

    return tree


def evaluate(tree: BinaryTree):
    operators = {'+': add, '-': sub, '*': mul, '/': truediv}

    left = tree.get_left_child()
    right = tree.get_right_child()

    if left and right:
        operation = operators[tree.get_root_val()]
        return operation(evaluate(left), evaluate(right))
    else:
        return tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree:
        s_val = f'({print_exp(tree.get_left_child())}'
        s_val += str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child()) + ')'
    return s_val


if __name__ == '__main__':
    binary_tree = parse_exp('((3/5)-(7*8))')
    print(evaluate(binary_tree))
    print(print_exp(binary_tree))
    binary_tree = parse_exp('((3/5)-(5+7))')
    print(evaluate(binary_tree))
    print(print_exp(binary_tree))
