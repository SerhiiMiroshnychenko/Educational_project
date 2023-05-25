class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node._v:
            if node.l is None:
                node.l = Node(val)
            else:
                self._add(val, node.l)
        elif node.r is not None:
            self._add(val, node.r)
        else:
            node.r = Node(val)

    def find(self, val):
        return self._find(val, self.root) if self.root is not None else None

    def _find(self, val, node):
        if val == node._v:
            return node
        elif (val < node._v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node._v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us.
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(f'{str(node._v)} ')
            self._printTree(node.r)

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print(tree.find(3).v)
print(tree.find(10))
tree.deleteTree()
tree.printTree()
