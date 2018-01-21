from collections import Counter

x = int(input())
c = Counter(list(map(int, input().split())))
pay = 0

nCustomer = int(input())

for _ in range(nCustomer):
    size, price = map(int, input().split())
    if size in c.keys() and c.get(size) != 0:
        c.subtract((size, c.get(size)))
        pay += price
    else:
        pass

print(pay)