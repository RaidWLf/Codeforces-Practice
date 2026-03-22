n = int(input())

for i in range(n):
    l = int(input())
    arr = list( input().split())
    
    left = 0
    right = l-1
    
    while left < right:
        while left < right and arr[left] == "0":
            left += 1
        
        while left < right and arr[right] == "1":
            right -= 1
        
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    print(" ".join(arr))