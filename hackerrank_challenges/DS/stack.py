stack = []

n = int(input())
for _ in range(n):
    x = list(map(int, input().split()))
    if x[0] == 1:
        stack.append(x[1])
    else:
        if x[0] == 2:
            stack.pop()
        else:
            if x[0] == 3:
                print(max(stack))