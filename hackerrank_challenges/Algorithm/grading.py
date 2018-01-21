n = int(input()) # number of student
for _ in range(n):
    m = int(input())
    if m < 38:
        print(m)
    else:
        t = m
        while t % 5 != 0:
            t += 1
        if (t - m) < 3:
            print(t)
        else:
            print(m)

