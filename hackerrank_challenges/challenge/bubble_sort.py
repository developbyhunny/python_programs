n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numSwaps = 0

for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numSwaps += 1

print("Array is sorted in %d swaps." % numSwaps)
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[len(a)-1]))