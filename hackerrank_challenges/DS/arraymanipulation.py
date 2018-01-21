n, m = map(int, input().strip().split(" "))
arr = [0]*n
for _ in range(m):
    a, b, k = map(int, input().strip().split(" "))
    for i in range(a-1, b):
        arr[i] += k

print(max(arr))
