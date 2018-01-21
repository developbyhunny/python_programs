import re

result = re.split(r'[,.]', input())

index = []
final = []

for i in range(len(result)):
    if result[i] == '':
        index.append(i)

for i in range(len(result)):
    if i in index:
        continue
    else:
        final.append(result[i])

print(final)