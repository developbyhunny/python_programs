t = int(input())

student = []
grade = []

for i in range(t):
	student.append(str(input()))
	grade.append(float(input()))

low = min(grade)
s_low = grade[0]

for i in range(1,t):
	if s_low > grade[i] and s_low != low:
		s_low = grade[i]

pos = []

for i in range(t):
	if grade[i] == s_low:
		pos.append(i)

for i in pos:
	print(student[i])

