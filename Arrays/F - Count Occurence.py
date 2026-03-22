n, q = map(int, input().split())

arr = list(map(int, input().split()))

count = 0

for i in range(n):
    if q == arr[i]:
        count += 1

print(count)