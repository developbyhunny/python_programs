n = int(input())

for i in range(1,n+1):
	print('%2s %2s %2s %5s' %(i,oct(i)[2:],hex(i).upper()[2:],bin(i)[2:]))