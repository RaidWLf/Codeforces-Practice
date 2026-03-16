n = int(input())
arr = list(map(int, input().split()))


# prefix = [0] * (n + 1)

# for i in range(1, n + 1):
#     prefix[i] = prefix[i - 1] + arr[i - 1]

# sum = 0

# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         sum += prefix[j] - prefix[i - 1]
        

# print(str(sum))

# Using direct mathematical formula

total = 0
for i in range(n):
    total += a[i] * (i + 1) * (n - i)

print(total)