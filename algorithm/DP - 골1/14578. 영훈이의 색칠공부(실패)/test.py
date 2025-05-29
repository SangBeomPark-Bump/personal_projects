import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")
MOD = int(1e9) + 7

N = int(input())
if N < 2:
    print(0)
else:
    dp = [ 0 for _ in range(N+1)]
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = (i * (i-1) * (dp[i-1] + dp[i-2])) % MOD
    print(dp[-1])

# for i in arr:
#     print(i)