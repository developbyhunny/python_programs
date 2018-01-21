class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def print_list(head):
    if head == None:
        print()
    else:
        temp = head
        while temp != None:
            print(temp.data)
            temp = temp.next

def insert(head, data):
    if head == None:
        head = Node(data, None)
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data, None)
    return head

def insertAtHead(head, data):
    if head == None:
        head = Node(data, None)
    else:
        newNode = Node(data, head)
        head = newNode
    return head

def insertNth(head, data, position):
    if position == 0:
        newnode = Node(data, None)
        newnode.next = head
        head = newnode
    else:
        temp = head
        for i in range(position-1):
            temp = temp.next
        newnode = Node(data, temp.next)
        temp.next = newnode
    return head

def delete(head, position):
    if position == 0:
        head = head.next
    else:
        temp = head
        for i in range(position-1):
            temp = temp.next
        temp.next = temp.next.next
    return head

def reversePrint(head):
    if head != None:
        h = None
        temp = head
        while temp != None:
            newnode = Node(temp.data)
            newnode.next = h
            h = newnode
            temp = temp.next


# 1 2 3 4 5
def reverse(head):
    if head != None:
        h = None
        temp = head
        while temp != None:
            newnode = Node(temp.data)
            newnode.next = h
            h = newnode
            temp = temp.next
    return h

def compareLists(headA, headB):
    if headA == None or headB == None:
        return 0

    s2 = s1 = 0
    t = headA
    while t != None:
        s1 += 1
        t = t.next
    t = headB
    while t != None:
        s2 += 1
        t = t.next

    if s1 != s2:
        return 0
    else:
        t1, t2 = headA, headB
        while t1 != None and t2 != None:
            if t1.data != t2.data:
                return 0
            t1 = t1.next
            t2 = t2.next
    return 1

# 1 3 5 7           2 4 6 8
def mergeLists(headA, headB):
    headC = None
    t1, t2, t3 = headA, headB, headC

    while t1 != None and t2 != None:
        if t1.data <= t2.data:
            if t3 == None:
                headC = t1
                t3 = headC
            else:
                t3.next = t1
                t3 = t3.next
            t1 = t1.next
        else:
            if t3 == None:
                headC = t2
                t3 = headC
            else:
                t3.next = t2
                t3 = t3.next
            t2 = t2.next

    while t1 != None:
        if t3 == None:
            headC = t1
            t3 = headC
        else:
            t3.next = t1
            t3 = t3.next
        t1 = t1.next

    while t2 != None:
        if t3 == None:
            headC = t2
            t3 = headC
        else:
            t3.next = t2
            t3 = t3.next
        t2 = t2.next

    return headC

def getNodeFromTail(head, position):
    if head != None:
        h = None
        temp = head
        while temp != None:
            newnode = Node(temp.data)
            newnode.next = h
            h = newnode
            temp = temp.next
        t = h
        for i in range(position):
            t = t.next
        return t
    return None

# 1 2 2 3 4 4 5
def removeDuplicate(head):
    t1, t2, par = head, None, None
    while t1 != None:
        t2 = t1.next
        par = t1
        while t2 != None:
            if t1.data == t2.data:
                t2 = t2.next
                par.next = t2
            else:
                par = par.next
                t2 = t2.next
        t1 = t1.next
    return head

def has_cycle(head):
    fp = head
    sp = head
    while fp and sp and fp.next:
        sp = sp.next
        fp = fp.next.next

        if fp == sp:
            return 1
    return 0

def findMergeNode(headA, headB):
    t1 = headA
    while t1:
        t2 = headB
        while t2:
            if t1 == t2:
                return t1.data
            t2 = t2.next
        t1 = t1.next



if __name__ == '__main__':
    headA, headB, headC = [None]*3
    node = None

    headA = insert(headA, 1)
    headA = insert(headA, 1)
    headA = insert(headA, 1)

    headA = removeDuplicate(headA)

    print_list(headA)


