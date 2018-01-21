from itertools import combinations_with_replacement
string,n = input().split()
l = list(string)
l.sort()
string = ''.join(l)
data = list(combinations_with_replacement(string,int(n)))
for _ in data:
    print(''.join(_))