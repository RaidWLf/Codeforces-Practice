q = int(input())

dic = dict()

for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 3:
        print(len(dic))
    
    elif query[0] == 1:
        dic[query[1]] = dic.get(query[1], 0) + 1
    
    elif query[0] == 2:
        freq = dic.get(query[1], 0)
        freq = freq -1
        if freq > 0:
            dic[query[1]] = freq
        else:
            dic.pop(query[1], None)
        
    
    elif query[0] == 4:
        if query[1] in dic:
            print("YES")
        else:
            print("NO")