K = int(input())
List = input().split()
for i in List:
	if List.count(i) == 1:
		print(i)
		break