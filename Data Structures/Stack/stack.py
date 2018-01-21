## import statement
from os import system


## Function definition
def push(stack,max_index,top,value):
	if top < max_index-1:
		stack.append(value)
		return stack,top+1
	print('Stack Overflow')
	return stack,top	

def pop(stack,top):
	if top != -1:
		data = stack[top]
		return stack,data,top-1
	print('Stack is empty')
	return stack,-1,top

def view(stack,top):
	for i in range(top+1):
		print(stack[i],end=' ')

## Main Program
stack = []


system('cls')
max_index = int(input('Enter the size for stack: '))
top = -1

while(True):
	system('cls')
	print('Main Menu')
	print('Select the operation you want to perform')
	print('1) PUSH')
	print('2) POP')
	print('3) VIEW')
	print('4) EXIT')

	choice = int(input('Enter your choice: '))

	if choice == 1:
		value = int(input('Enter the value to be put on stack: '))
		stack,top = push(stack,max_index,top,value)
	elif choice == 2:
		stack,value,top = pop(stack,top)
		if value != -1:
			print(value,'is removed')
	elif choice == 3:
		view(stack,top)
	elif choice == 4:
		exit()

	input()
