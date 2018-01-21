
class Node:
    def __init__(self, value):
        self.key = value
        self.next = None

def insertAtBeg(head):
    data = int(input("Enter data: "))
    if head == None:
        head = Node(data)
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)

def insertAtEnd(head):
    pass

def insertAt(head, pos):
    pass

def traverse(head):
    if head == None:
        print("Empty list.")
    else:
        temp = head
        print("List: ", end='')
        while temp.next != None:
            print(temp.key, end=", ")
            temp = temp.next

if __name__ == '__main__':
    from os import system
    clear = lambda: system("cls")

    head = None
    while True:
        clear()
        print("Main Menu,")
        print("Press 1 to add an element.")
        print("Press 2 to delete an element.")
        print("Press 3 to search an element.")
        print("Press 4 to traverse the list.")
        print("Press 5 to exit the program.")
        choice = int(input("Enter your choice: "))
        clear()

        if choice == 1:
            print("Select the option,")
            print("Press 1 to insert at beginning.")
            print("Press 2 to insert at end.")
            print("Press 3 to insert at specified Position.")
            choice1 = int(input("Enter your choice: "))
            print()

            if choice1 == 1:
                insertAtBeg(head)
            elif choice1 == 2:
                pass
            elif choice1 == 3:
                pass
            else:
                print()
                print("You have wrong choice.")

        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            break
        input()

clear()
print("Thanks for using our software.")

