import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
MOD = 987654321

dp = [0 for _ in range(N+1)]

dp[0] = 1

for n in range(2, N+1, 2):
    for m in range(0,n-1, 2):
        dp[n] += (dp[m] * dp[n-2-m]) % MOD
print(dp[N] % MOD)