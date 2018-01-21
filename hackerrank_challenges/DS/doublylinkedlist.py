class Node(object):
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node

# 1 2 3 5 6
# 1
def sortedInsert(head, data):
    newnode = Node(data)
    if head is None:
        head = newnode
    elif head.next is None:
        newnode.prev = head
        head.next = newnode
    else:
        current = head
        while newnode.data > current.data and current.next:
            current = current.next
        if current.data >= newnode.data:
            newnode.prev = current.prev
            newnode.next = current
            current.prev.next = newnode
            current.prev = newnode
        else:
            current.next = newnode
            newnode.prev = current
    return head

# 1 2 3 4 5
def reverse(head):
    if head is None:
        return head
    else:
        current = head
        while current.next:
            current = current.next
        result = current
        t = result
        while current.prev:
            current = current.prev
            newnode = Node(current.data, t)
            t.next = newnode
            t = t.next
    return result

        

def printList(head):
    t = head
    while t:
        print(t.data)
        t = t.next

if __name__ == "__main__":
    head = None
    head = sortedInsert(head, 1)
    head = sortedInsert(head, 2)
    head = sortedInsert(head, 3)
    head = sortedInsert(head, 5)
    head = sortedInsert(head, 6)
    head = sortedInsert(head, 4)
    head = sortedInsert(head, 7)


    printList(head)

    head = reverse(head)

    printList(head)