n = int(input())

for _ in range(n):
    k = int(input())
    arr = list(input().split())
    
    arr2 = []
    
    for i in range(k):
        if arr[i] in arr2:
            arr2.remove(arr[i])
            continue
        
        arr2.append(arr[i])
        
    print(arr2[0])