import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
M = 500

arr = [list(map(int, input().split() ) ) for _ in range(N)]
arr.sort(key=lambda x : x[0])


dp = [0 for _ in range(M+1)]

for n in range(N):
    start, end = arr[n]
    dp[end] = max(dp[:end]) +1
print(N - max(dp))