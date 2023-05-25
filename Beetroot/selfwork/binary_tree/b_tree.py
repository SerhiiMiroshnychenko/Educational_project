from turtle import left, right


class Node:
    def __init__(self,data):
        self.left= None
        self.right=None
        self.data=data

    def degree(self):
        n=0
        if left:
            n=n+1
        if right:
            n=n+1
        return n
    def find(self,data):
        if self.data:
            if data ==self.data:
                return True
            elif data>self.data:
                if self.right:
                    return self.right.find(data)
                else:
                    return False
            elif data<self.data:
                if self.left:
                    return self.left.find(data)
                else:
                    return False
        else:
            return False

    def insert(self,data):
        if self.data:

            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def printTree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()
    def depth_first(self,root):
        res=[]
        if root:
            res.append(root.data)
            res=res+self.depth_first(root.left)
            res=res+self.depth_first(root.right)



a=Node(1)
a.insert(2)
a.insert(3)
a.insert(0)
a.printTree()