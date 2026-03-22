n = int(input())

arr = list(input().split())


l = 0 
r = n -1

while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
    
print(" ".join(arr))