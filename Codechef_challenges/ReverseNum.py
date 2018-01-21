for _ in range(int(input())):
    rev = 0
    n = int(input())
    l = len(str(n))
    while l > 0:
        rev = rev + (n % 10)*(10**(l-1))
        n //= 10
        l -= 1
    print(rev)