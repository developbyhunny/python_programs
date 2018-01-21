N, Q = map(int, input().split())
S = []
for _ in range(N):
    S.append([])
lastAnswer = 0

for _ in range(Q):
    q, x, y = map(int, input().split())
    if q == 1:
        S[(x ^ lastAnswer) % N].append(y)
    elif q == 2:
        index = (x ^ lastAnswer) % N
        size = len(S[index])
        lastAnswer = S[index][y % size]
        print(lastAnswer)

