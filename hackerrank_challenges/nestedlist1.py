t = int(input())
record = []

for i in range(t):
	name = str(input())
	grade = input()
	record.append([name,grade])

lowest = record[0][1]
slowest = record[1][1]

for i in range(2,t):
	if record[i][1] < lowest:
		slowest = lowest
		lowest = record[i][1]
	else:
		if record[i][1] < slowest:
			slowest = record[i][1]

result = []

for i in range(t):
	if record[i][1] == slowest:
		result.append(record[i][0])

result.sort()

for name in result:
	print(name)



