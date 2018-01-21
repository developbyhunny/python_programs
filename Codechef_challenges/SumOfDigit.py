t = int(input())
for _ in range(t):
    sum = 0
    temp = int(input())
    while temp > 0:
        sum += (temp % 10)
        temp //= 10
    print(sum)