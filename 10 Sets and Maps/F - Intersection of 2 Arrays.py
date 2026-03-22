n = int(input())
arr1 = set(map(int, input().split()))

m = int(input())
arr2 = set(map(int, input().split()))

st = set()

for ele in arr1:
    if ele in arr2:
        st.add(ele)

arr3 = list(st)
arr3 = sorted(arr3)

print(len(arr3))
print(" ".join(map(str, arr3)))