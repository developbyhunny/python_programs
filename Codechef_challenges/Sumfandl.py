for _ in range(int(input())):
    n = int(input())
    l = len(str(n))
    print((n//(10**(l-1))) + (n%10))