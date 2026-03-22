n = int(input())

for _ in range(n):
    k = int(input())
    arr = list(input().split())
    
    unique = []
    
    for i in range(k):
        if arr[i] in unique:
            print(arr[i])
            break
        
        unique.append(arr[i])