n = int(input())

for i in range(n):
    k = int(input())
    arr = list(input().split())
    
    for j in range(0, k -1, 2):
        if j == k - 1:
            break
        arr[j], arr[j+1] = arr[j+1], arr[j]
        
    print(" ".join(arr))