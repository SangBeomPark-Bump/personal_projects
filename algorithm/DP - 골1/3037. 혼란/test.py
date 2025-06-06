import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N, C = map(int, input().split())
MOD = int(1e9) + 7


dp = [ [0 for _ in range(C+1)] for _ in range(N+1)]
dp[0][0] = 1

for n in range(1, N+1): ## N번
    window = 0
    for c in range(C+1): ## C번
        window += dp[n-1][c]
        if c >= n:
            window -= dp[n-1][c-n]
        window %= MOD
        dp[n][c] = window

print(dp[-1][-1])
