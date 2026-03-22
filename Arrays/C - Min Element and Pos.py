n = int(input())

arr = list(map(int, input().split()))

min = float("inf")
ind = 0
for i in range(n):
    if arr[i] < min:
        min = arr[i]
        ind = i + 1
        
print(min, ind)