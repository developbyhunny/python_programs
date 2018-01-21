strings = []

N = int(input())
for _ in range(N):
    strings.append(input())

Q = int(input())
for _ in range(Q):
    st = input()
    c = 0
    for i in strings:
        if st == i:
            c += 1
    print(c)