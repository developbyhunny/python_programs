t, k = map(int, input().split())
count = 0
for _ in range(t):
    temp = int(input())
    if temp % k == 0:
        count += 1
print(count)