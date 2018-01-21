for _ in range(int(input())):
    n = int(input())
    skills = list(map(int, input().split()))
    m = 1000000000
    for a in skills:
        for b in range(a+1, len(skills)):
            tmp = a - skills[b]
            if tmp < 0:
                tmp = tmp*(-1)
            elif tmp < m:
                m = tmp

    print(m)