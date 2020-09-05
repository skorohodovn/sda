class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __left_value(self):
        if self.left is None:
            return None
        else:
            return self.left.value

    def __right_value(self):
        if self.right is None:
            return None
        else:
            return self.right.value

    def __str__(self):
        return f"[{self.value}] L: [{self.left.value}], R: [{self.right.value}]"

class BinaryTree:
    def __init__(self):
        self.__root = None

    def add(self, value):
        return self.__add(self.__root, value)

    def __add(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                add(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                add(node.right, value)


root = Node(7)
n2 = Node(5)
n3 = Node(9)

root.left = n2
root.right = n3

print(root)
print(n2)

def add(root, value):
    if value < node.value:
        if node.left is None:
            node.left = Node(value)
        else:
            add(node.left,value)
    else:
        if node.right is None:
            node.right = Node(value)
        else:
            add(node.right, value)

add(root, 4)

print(n2)

