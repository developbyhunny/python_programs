nA = int(input())
A = set(map(int,input().split()))
n = int(input())
for i in range(n):
	operate,nB = input().split()
	B = set(map(int,input().split()))
	operate = 'A.'+operate+'(B)'
	eval(operate)

print(sum(A))	