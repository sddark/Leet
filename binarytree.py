class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def visit(Node):
    print(Node.val)

def preorder(current):
    visit(current)
    if current.left != None:
        preorder(current.left)
    elif current.right != None:
        preorder(current.right)

    

root = Node(2)
n2 = Node(1)
n3 = Node(3)
root.left  = n2
root.right = n3

preorder(root)
