n = int(input())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

sum_d1 = 0
for _ in range(n):
    sum_d1 += mat[_][_]

mat.reverse()
sum_d2 = 0
for _ in range(n):
    sum_d2 += mat[_][_]

print(abs(sum_d1 - sum_d2))