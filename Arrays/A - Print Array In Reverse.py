n = int(input())

arr = list(input().split())

arr2 = []

for i in range(n):
    arr2.append(arr.pop())
    
print(" ".join(arr2))