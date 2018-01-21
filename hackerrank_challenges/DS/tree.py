class Node:
    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left = left_node
        self.right = right_node

def preOrder(root):
    if root != None:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root != None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)