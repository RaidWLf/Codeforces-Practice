n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))


dic1 = {}
dic2 = {}
dic3 = {}

for ele in arr1:
    dic1[ele] = dic1.get(ele, 0) + 1

for ele in arr2:
    dic2[ele] = dic2.get(ele, 0) + 1

for key in dic1:
    dic3[key] = min(dic1.get(key), dic2.get(key, 0))
    

arr = []
for key in dic3:
    arr.extend([key] * dic3[key])

arr = sorted(arr)

print(len(arr))
print(' '.join(map(str, arr)))