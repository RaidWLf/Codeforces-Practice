n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

st = set(arr1 + arr2)

arr3 = sorted(list(st))

print(len(arr3))
print(" ".join(map(str, arr3)))