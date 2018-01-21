from itertools import combinations
string,n = input().split()
data = list(string)
data.sort()
string = ''.join(data)
for i in range(1,int(n)+1):
    data = list(combinations(string,i))
    for _ in data:
        print(''.join(_))
    