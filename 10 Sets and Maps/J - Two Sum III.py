from collections import Counter

n, x = map(int, input().split())

arr = list(map(int, input().split()))

freq = Counter(arr)

count = 0

for ele in freq:
    target = x - ele

    if target < ele:
        continue
    
    if target == ele:
        cnt = freq[ele]
        count += cnt * (cnt - 1) // 2
    
    else:
        if target in freq:
            count += freq[ele] * freq[target]

print(count)