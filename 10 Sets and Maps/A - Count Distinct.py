'''You are given an array A of N integers.
Your task is to determine how many distinct values appear in the array.'''

n = int(input())
arr = list(map(int, input().split()))

st = set()

for a in arr:
    st.add(a)
    
print(len(st))