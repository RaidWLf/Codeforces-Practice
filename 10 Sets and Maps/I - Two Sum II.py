n, x = map(int, input().split())

arr = list(map(int, input().split()))

dic = dict()

for i in range(n):
    to_find = x - arr[i]
    ind = dic.get(to_find, -1)
    
    if ind > 0:
        print(ind, i + 1)
        break
    
    dic[arr[i]] = i + 1

else:
    print(-1)