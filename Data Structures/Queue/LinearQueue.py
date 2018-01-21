from os import system
clear = lambda: system("cls")

def isEmpty(Q):
    if len(Q) == 0:
        return True
    return False

def enQueue(Q, dt):
    if isEmpty(Q) == True:
        Q.append(dt)
    else:
        Q.append(dt)

def deQueue(Q):
    if isEmpty(Q) == True:
        print("MSG: You have no item to delete.")
    else:
        print("MSG: %d is deleted from the queue." %(Q[0]))
        Q.remove(Q[0])

Q = []
front = rear = -1

while 1:
    clear()
    print(">>> Linear Queue Demonstration,")
    print()
    print("Select the following operation your want to perform,")
    print("Press 1 to enQueue data.")
    print("Press 2 to deQueue data.")
    print("Press 3 to Exit Program.")
    print("Press 4 to view Queue.")
    choice = input("Enter your choice: ")
    print()
    if choice == '1':
        enQueue(Q, int(input("Enter data: ")))
    elif choice == '2':
        deQueue(Q)
    elif choice == '3':
        break
    elif choice == '4':
        if isEmpty(Q) == False:
            print("List: ", end="")
            for e in Q:
                print(e, end=", ")
        else:
            print("MSG: You have no item to view.")
    else:
        print("MSG: You have choose a wrong choice.")
    input()

print("Thanks for using our software.")