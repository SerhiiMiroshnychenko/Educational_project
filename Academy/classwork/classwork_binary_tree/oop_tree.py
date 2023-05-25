from typing import Optional


class BinaryTree:

    def __init__(self, root_obj) -> None:
        self.key: str = str(root_obj)
        self.left_child: Optional[BinaryTree] = None
        self.right_child: Optional[BinaryTree] = None

    def insert_left(self, new_node) -> None:
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node) -> None:
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t: BinaryTree = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self) -> "Optional[BinaryTree]":
        return self.right_child

    def get_left_child(self) -> "Optional[BinaryTree]":
        return self.left_child

    def set_root_val(self, obj) -> None:
        self.key = obj

    def get_root_val(self) -> str:
        return self.key

    def __repr__(self) -> str:
        return f"BinaryTree: {self.key}"
        # return f"""   {self.key}   \n  /  \\  \n{self.left_child}  {self.left_child}"""

    def pre_order(self) -> None:
        print(self.key)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def post_order(self) -> None:
        if self.left_child:
            self.left_child.post_order()
        if self.right_child:
            self.right_child.post_order()
        print(self.key)

    def in_order(self) -> None:
        if self.left_child:
            self.left_child.in_order()
        print(self.key)
        if self.right_child:
            self.right_child.in_order()


if __name__ == "__main__":
    tr = BinaryTree('a')
    print(tr.get_root_val())
    print(tr.get_left_child())
    tr.insert_left('b')
    print(tr.get_left_child())
    print(tr.get_left_child().get_root_val())
    tr.insert_right('c')
    print(tr.get_right_child())
    print(tr.get_right_child().get_root_val())
    tr.get_right_child().set_root_val('hello')
    print(tr.get_right_child().get_root_val())
    # print(tr, tr.get_left_child(), tr.get_right_child())
    print(tr)
