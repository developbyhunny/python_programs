import copy

arr = list(map(int, input().split()))
arr1 = copy.copy((arr))
min_num = min(arr)
max_num = max(arr)

arr1.remove(max_num)
arr.remove(min_num)

print(sum(arr1), end=" ") #Min Sum

print(sum(arr)) #Max Sum

