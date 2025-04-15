import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, K = map(int, input().split())


arr = [int(input()) for _ in range(N)]
arr =  [0] + arr

dp = [0 for _ in range(K+1)]
dp[0] = 1

for n in range(1, N+1):
    for k in range(1, K+1):
        prev = k - arr[n]
        if prev>=0:
            dp[k] = dp[prev] + dp[k]

print(dp[-1])