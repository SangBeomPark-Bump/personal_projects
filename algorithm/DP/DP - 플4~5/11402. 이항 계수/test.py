import sys
input = sys.stdin.readline
INF = float("inf")


N, K, M = map(int, input().split())
dp = [[0 for _ in range(M)] for _ in range(M)]

dp[0][0] = 1

dp[1][0] = 1
dp[1][1] = 1

for m in range(1, M):
    dp[m][0] = 1
    dp[m][m] = 1

    for k in range(1, m):
        dp[m][k] = dp[m-1][k-1] + dp[m-1][k]
        dp[m][k] %= M

def dfs(n, k, verbose = False):
    if verbose:
        print(n, k)
    if k < M:
        return dp[n%M][k]
    return (dfs(n//M, k//M, verbose=verbose) * dfs(n - M * (k//M), k%M, verbose=verbose)) % M

print(dfs(N, K))