n, q = map(int, input().split())

arr = list(map(int, input().split()))


prefix = [0] * (n+1)

for i in range(1, n+1):
    sign = -1 if i%2 == 0 else 1
    prefix[i] = prefix[i-1] + sign * arr[i-1]

for i in range(q):
    l, r = map(int, input().split())
    
    segment = prefix[r] - prefix[l - 1]
    if l % 2 == 0:
        segment = -segment
    
    print(segment)