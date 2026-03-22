'''You are given an array A of N distinct integers and Q queries. In each query, an integer x is given.

For every query, output the 1-based index of x in the array. If x does not occur in A, output -1'''

n,q = map(int, input().split())

arr = list(map(int, input().split()))

mp = dict()

for i in range(n):
    mp[arr[i]] = i + 1

for j in range(q):
    target = int(input())
    
    print(mp.get(target, -1))