class Node(object):
    def __init__(self, key, left_node=None, right_node=None):
        self.key = key
        self.left = left_node
        self.right = right_node

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root

            while True:
                if current.key > data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                elif current.key < data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break
                else:
                    break

    def search(self, data):
        if self.root is None:
            return self.root
        else:
            current = self.root
            while True:
                if data == current.key:
                    return current
                elif data < current.key:
                    current = current.left
                elif data > current.key:
                    current = current.right




if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.create(10)
    tree.create(20)
    tree.create(30)
    tree.create(40)
    tree.create(50)
    tree.create(60)
    tree.create(70)
    tree.create(80)

    node = tree.search(70)





