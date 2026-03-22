n = int(input())

for _ in range(n):
    k = int(input())
    arr1 = list(map(int,input().split()))
    
    m = int(input())
    arr2 = list(map(int,input().split()))
    
    ans = []
    
    for i in range(k):
        if arr1[i] in arr2:
            ans.append(arr1[i])
            arr2.remove(arr1[i])
        
    print(" ".join(map(str,ans)))