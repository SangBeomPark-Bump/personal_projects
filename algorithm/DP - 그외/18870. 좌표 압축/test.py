import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())

arr = list(map(int, input().split()))

arr2 = [(index, value) for index, value in enumerate(arr)]
arr3 = sorted(arr2, key= lambda x: x[1])
arr3 = [(-1,float('inf') * -1)] + arr3

dp = [-1] + [0] * N

temp = 0
for i in range(1,N+1):
    dp [arr3[i][0] +1] = dp[arr3[i-1][0] +1] + (1 if arr3[i-1][1] != arr3[i][1] else 0)
print(' '.join(map(str, dp[1:])))
# for i in arr:
#     print(i)