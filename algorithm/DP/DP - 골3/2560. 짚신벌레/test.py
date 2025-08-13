import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

a, b, d, N = map(int, input().split())
MOD = 1000

dp = [ [0 for _ in range(4)] for _ in range(N+1)]
dp[0] = [1, 1, 0, 0]

for n in range(1, N+1):
    dp[n] = [
        dp[n-1][2],
        dp[n-1][1],
        dp[n-1][2],
        dp[n-1][3],
    ]
    if n>=a :
        dp[n][2] += dp[n-a][0]
        dp[n][0] += dp[n-a][0]
        dp[n][1] -= dp[n-a][0]
    if n>=b :
        dp[n][3] += dp[n-b][0]
        dp[n][2] -= dp[n-b][0]
        dp[n][0] -= dp[n-b][0]
    if n >= d:
        dp[n][3] -= dp[n-d][0]
    dp[n][1] += dp[n][2]

    for i in range(4):
        dp[n][i] %= MOD
print(sum(dp[-1][1:]) % MOD)