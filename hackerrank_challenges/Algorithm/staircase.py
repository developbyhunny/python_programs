n = int(input())

for a in range(n):
    for s in range(n, a+1, -1):
        print(" ", end='')

    for b in range(a+1):
        print("#", end='')
    print()