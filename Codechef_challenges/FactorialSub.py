def z(n):
    zeros = 0
    i = 1
    while n//5**i > 0:
        zeros = zeros + n//5**i
        i += 1
    return zeros

times = int(input())
for _ in range(times):
    print(z(int(input())))
