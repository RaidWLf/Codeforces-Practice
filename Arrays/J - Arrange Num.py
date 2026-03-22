n = int(input())

for i in range(n):
    k = int(input())
    
    arr = [0] * k
    l = 0
    r = k - 1
    c = 1
    while l <= r and c <= k:
        if l == r:
            arr[l] = str(c)
            break
            
        arr[l] = str(c)
        arr[r] = str(c + 1)
        
        l += 1
        r -= 1
        c += 2
    
    print(" ".join(arr))