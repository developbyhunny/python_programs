from collections import Counter

n = int(input())
data = list(map(int, input().strip().split(" ")))
mean = sum(data)/n
print("%.1f" % mean)

if n % 2 == 0:
    data.sort()
    median = (data[n//2] + data[(n//2)-1])/2
else:
    median = data[(n//2)+1]
print("%.1f" % median)

cnt = list(Counter(data).items())
t = cnt[0][1]
check = True
for i in range(len(cnt)):
    if t != cnt[i][1]:
        check = False
        break

if check is True:
    print(data[0])
else:
    max_cnt = 0
    for i in range(len(cnt)):
        if max_cnt < cnt[i][1]:
            max_cnt = cnt[i][1]
            pos = i

    print(cnt[pos][0])

