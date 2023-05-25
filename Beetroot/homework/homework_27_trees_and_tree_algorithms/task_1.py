# Task 1

# Розширити структуру, яку побудували на уроці, можливістю вставки
# дерева в наявне дерево та видалення піддерева з дерева, що існує.

class BinaryTree:

    def __init__(self, root_obj, value=None):
        self.key = root_obj
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node, value=None):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node, value)  # type: ignore
        else:
            t = BinaryTree(new_node, value)
            t.left_child = self.left_child
            self.left_child = t

    def delete_left(self):
        is_left = self.left_child is not None
        is_left_left = self.left_child.left_child is not None
        is_left_right = self.left_child.right_child is not None
        if is_left_right and is_left_left:
            r = self.left_child.right_child
            l = self.left_child.left_child
            self.left_child = r
            self.left_child.left_child = l
        elif is_left_right:
            r = self.left_child.right_child
            self.left_child = r
        elif is_left_left:
            l = self.left_child.left_child
            self.left_child = l
        elif is_left:
            self.left_child = None

    def insert_right(self, new_node, value=None):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node, value)  # type: ignore
        else:
            t = BinaryTree(new_node, value)
            t.right_child = self.right_child
            self.right_child = t

    def delete_right(self):
        is_right = self.right_child is not None
        is_right_left = self.right_child.left_child is not None
        is_right_right = self.right_child.right_child is not None
        if is_right_right and is_right_left:
            r = self.right_child.right_child
            l = self.right_child.left_child
            self.right_child = r
            self.right_child.left_child = l
        elif is_right_right:
            r = self.right_child.right_child
            self.right_child = r
        elif is_right_left:
            l = self.right_child.left_child
            self.right_child = l
        elif is_right:
            self.right_child = None

    def insert_tree_left(self, new_tree):
        if self.left_child is not None:
            leaf = new_tree.left_child
            while leaf.left_child is not None:
                leaf = leaf.left_child
            leaf.left_child = self.left_child
        self.left_child = new_tree

    def insert_tree_right(self, new_tree):
        if self.right_child is not None:
            leaf = new_tree.right_child
            while leaf.right_child is not None:
                leaf = leaf.right_child
            leaf.right_child = self.right_child
        self.right_child = new_tree

    def remove_node(self, node):
        if self.left_child:
            if self.left_child.key == node:
                self.delete_left()
            else:
                self.left_child.remove_node(node)
        if self.right_child:
            if self.right_child.key == node:
                self.delete_right()
            else:
                self.right_child.remove_node(node)

    def show_value(self, key):
        current = self
        stack = []
        while True:
            if current is not None:
                if current.key == key:
                    return current.value
                stack.append(current)
                current = current.left_child
            elif stack:
                current = stack.pop()
                current = current.right_child
            else:
                break


    def remove_subtree(self, subtree):
        for node in subtree.yank_keys():
            self.remove_node(node)

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_key(self, obj):
        self.key = obj

    def get_root_key(self):
        return self.key

    def set_root_val(self, value):
        self.value = value

    def get_root_val(self):
        return self.value

    def pre_order(self):
        print(self.key)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.key)

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        print(self.key)
        if self.right_child:
            self.right_child.in_order()

    def yank_keys(self):
        current = self
        stack = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left_child
            elif stack:
                current = stack.pop()
                yield current.key
                current = current.right_child
            else:
                break


    def __contains__(self, item):
        return any(value == item for value in self.yank_keys())

    @staticmethod
    def print_tree(root, prev=None, is_left=False):
        if root is None:
            return

        prev_str = '    '
        trunk = Trunk(prev, prev_str)
        root.print_tree(root.get_right_child(), trunk, True)

        if prev is None:
            trunk.str = '———'
        elif is_left:
            trunk.str = '.———'
            prev_str = '   |'
        else:
            trunk.str = '`———'
            prev.str = prev_str

        root.show_trunks(trunk)
        print(f' {str(root.get_root_key())}')
        if prev:
            prev.str = prev_str
        trunk.str = '   |'
        root.print_tree(root.get_left_child(), trunk, False)

    def show_trunks(self, p):
        if p is None:
            return
        self.show_trunks(p.prev)
        print(p.str, end='')

    def add_right_leaf(self, item, value=None):
        if self.right_child is None:
            self.insert_right(item, value)
        else:
            child = self.right_child
            child.add_right_leaf(item, value)

    def add_left_leaf(self, item, value=None):
        if self.left_child is None:
            self.insert_left(item, value)
        else:
            child = self.left_child
            child.add_left_leaf(item, value)

    def add_leaf(self, item, path, value=None):
        if path == 'left':
            if self.left_child is None:
                self.insert_left(item, value)
            elif self.right_child is None:
                self.insert_right(item, value)
            else:
                child = self.left_child
                child.add_leaf(item, path, value)
        elif path == 'right':
            if self.right_child is None:
                self.insert_right(item, value)
            elif self.left_child is None:
                self.insert_left(item, value)
            else:
                child = self.right_child
                child.add_leaf(item, path, value)


class Trunk:
    def __init__(self, prev=None, str=None):
        self.prev = prev
        self.str = str


def show_tree(root):
    print()
    root.print_tree(root)


if __name__ == "__main__":
    tree0 = BinaryTree('r0')
    tree0.insert_left(20)
    tree0.insert_right(30)
    show_tree(tree0)

    tree0.insert_left(40)
    tree0.insert_right(50, 'Hi there!')
    show_tree(tree0)

    tree0.get_left_child().insert_right(60)
    show_tree(tree0)

    tree0.get_right_child().insert_left(70)
    show_tree(tree0)

    print(tree0.show_value(50))

    tree0.insert_left(80)
    show_tree(tree0)

    tree0.get_left_child().insert_right(90)
    show_tree(tree0)

    tree0.insert_left(100)
    show_tree(tree0)

    tree0.delete_left()
    show_tree(tree0)

    tree0.remove_node(40)
    show_tree(tree0)

    tree1= BinaryTree('1r')
    tree1.insert_left(11)
    tree1.insert_right(12)
    show_tree(tree1)
    tree1.insert_left(13)
    tree1.insert_right(14)
    show_tree(tree1)
    tree1.get_right_child().insert_left(15)
    show_tree(tree1)

    tree0.get_left_child().get_left_child().get_left_child().insert_tree_left(tree1)
    show_tree(tree0)

    tree2 = BinaryTree('2r')
    tree2.insert_left(21)
    tree2.insert_right(22)
    show_tree(tree2)
    tree2.insert_left(23)
    tree2.insert_right(24)
    show_tree(tree2)
    tree2.get_left_child().insert_right(25, 'Hi!')
    show_tree(tree2)
    tree2.get_left_child().get_right_child().insert_right(26)
    show_tree(tree2)


    show_tree(tree0)
    tree0.insert_tree_right(tree2)
    show_tree(tree0)

    tree0.remove_subtree(tree1)
    show_tree(tree0)

    print(tree0.show_value(25))
