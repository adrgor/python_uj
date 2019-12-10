class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if self.data < node.data:
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        elif self.data > node.data:
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            pass

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None


def bst_max(top):
    while top.right != None:
        top = top.right
    return top

def bst_min(top):
    while top.left != None:
        top = top.left
    return top

korzen = Node(15)
korzen.left = Node(8)
korzen.right = Node(40)
korzen.left.left = Node(3)
korzen.left.right = Node(9)
korzen.right.left = Node(30)
korzen.right.right = Node(60)
korzen.left.left.left = Node(1)
korzen.left.left.right = Node(4)
korzen.left.right.left = Node(7)
korzen.left.right.right = Node(10)
korzen.right.left.left = Node(25)
korzen.right.left.right = Node(35)
korzen.right.right.left = Node(50)
korzen.right.right.right = Node(70)

print(bst_max(korzen))
print(bst_min(korzen))