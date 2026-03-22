n , q = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(n):
    if q == arr[i]:
        print("YES")
        break

else:
    print("NO")