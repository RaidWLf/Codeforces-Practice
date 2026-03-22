n, x = map(int, input().split())

arr = list(map(int, input().split()))

st = set()

for ele in arr:
    if x - ele in st:
        print("TRUE")
        break
    st.add(ele)
    
else:
    print("FALSE")