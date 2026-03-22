n = int(input())

arr = list(map(int, input().split()))

max = float("-inf")
ind = 0

for i in range(n):
    if arr[i] > max:
        max = arr[i]
        ind = i + 1
        
print(max, ind)