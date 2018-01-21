import sys

def getTotalX(a, b):
    ma = max(a)
    mb = max(b)
    c = 0
    for x in range(ma, mb+1):
        check1 = True
        check2 = True
        for i in set(a):
            if x % i != 0:
                check1 = False
                break
        for i in set(b):
            if i % x != 0:
                check2 = False
                break
        if check1 == True and check2 == True:
            c += 1

    return c


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
