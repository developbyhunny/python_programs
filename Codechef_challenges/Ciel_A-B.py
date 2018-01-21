a, b = map(int, input().split())

a = a - b

print(a)

if a % 10 == 0:
    a += 1
else:
    a -= 1

if a == 0:
    a += 2

print(a)

