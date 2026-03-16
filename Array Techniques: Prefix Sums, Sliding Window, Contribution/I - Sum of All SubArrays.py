n = int(input())

arr = list(map(int, input().split()))

# for i in range(n):
#     sum = 0
#     for j in range(i, n):
#         sum += arr[j]
#         print(str(sum))

# prefixSum = [0] * (n + 1)

# for i in range(1, n + 1):
#     prefixSum[i] = prefixSum[i - 1] + arr[i - 1]
    
# for i in range(1, n + 1):
#     for j in range(i , n + 1):
#         print(str(prefixSum[j] - prefixSum[i - 1]))


# getting tle issue