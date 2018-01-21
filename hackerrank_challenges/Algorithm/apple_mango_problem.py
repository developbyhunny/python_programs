s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())

dis_apple = list(map(int, input().split()))
dis_mango = list(map(int, input().split()))

ta = 0
tm = 0

for x in dis_apple:
    if (a + x) in range(s, t+1):
        ta += 1


for x in dis_mango:
    if (b + x) in range(s, t+1):
        tm += 1

print(ta)
print(tm)