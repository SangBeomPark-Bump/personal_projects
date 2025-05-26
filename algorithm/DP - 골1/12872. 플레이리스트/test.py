import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")
MOD = int(1e9) + 7

N, M, P = map(int, input().split())


dp = [ [0 for _ in range(P+1)] for _ in range(N+1)]

dp[N][0] = 1


for x in range(N, -1, -1):
    for p in range(N-x, P):
        if x >=1:
            dp[x-1][p+1] += x * dp[x][p]
            dp[x-1][p+1] %= MOD
        if N-M-x >0:
            dp[x][p+1] += (N-M-x) * dp[x][p]
            dp[x][p+1] %= MOD

print(dp[0][P])