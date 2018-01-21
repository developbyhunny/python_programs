class Node(object):
    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left = left_node
        self.right = right_node

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = root

            while True:
                if data < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                elif data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break
                else:
                    break




    def create

if __name__ == "__main__":
    root = None