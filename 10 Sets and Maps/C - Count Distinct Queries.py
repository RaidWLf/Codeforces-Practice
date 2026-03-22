q = int(input())

st = set()

for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 3:
        print(len(st))
    
    elif query[0] == 1:
        st.add(query[1])
    
    elif query[0] == 2:
        st.discard(query[1])
    
    elif query[0] == 4:
        if query[1] in st:
            print("YES")
        else:
            print("NO")