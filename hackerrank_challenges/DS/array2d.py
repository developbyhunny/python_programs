
arr = []


for arr_i in range(6):
	arr_t = [int(temp) for temp in input().split(' ')]
	arr.append(arr_t)

pos = 0
rt = []
hour_glass = []

for n in range(4):

	temp = []
	
	for i_row in range(pos,pos+3):
		for j_col in range(pos,pos+3):
			temp.append(arr[i_row][j_col])

	pos += 1
	temp.remove(hour_glass[3])
	temp.remove(hour_glass[4])

	print(hour_glass)
	rt.append(sum(hour_glass))

print()
print()
print(rt)



