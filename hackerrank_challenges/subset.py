t = int(input())
for i in range(t):
	nA = int(input())
	A = set(map(int,input().split()))
	nB = int(input())
	B = set(map(int,input().split()))
	print(A.issubset(B))