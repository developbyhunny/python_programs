# 1 1 2 2
# 1 2 1 2
# 2 1 1 2



t = int(input())
d = list(map(int, input().split()))
if d[0] == d[1] or d[2] == d[3]:
	if d[0] != d[2] and d[0] != d[3] and d[1] != d[2] and d[1] != d[3]:
		print("YES")
	else:
		print("NO")
elif d[0] = d[2] or d[1] == d[3]:
	if d[0] != d[1] and d[0] != d[3] and d[2] != d[1] and d[2] != d[3]:
		print("YES")
	else:
		print("NO")
elif d[0] == d[3] or d[1] == d[2]:
	if d[0] != d[1] and d[0] != d[2] and d[3] != d[1] and d[3] != d[2]:
		print("YES")
	else:
		print("NO")
