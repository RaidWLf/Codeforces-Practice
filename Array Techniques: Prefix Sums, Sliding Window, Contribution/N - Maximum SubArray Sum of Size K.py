n, k = map(int, input().split())

arr = list(map(int, input().split()))


prefix = [0] * (n+1)

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]

max = prefix[k]


for i in range(k+1,n+1):
    sum = prefix[i] - prefix[i-k]
    if sum > max:
        max = sum
        
print(max)