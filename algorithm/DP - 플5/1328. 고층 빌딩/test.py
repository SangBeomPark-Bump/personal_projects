import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")

N, L, R =  map(int, input().split())
MOD = 1000000007

combination_table = [ [1 for _ in range(n+1)] for n in range(N+1)]

for i in range(N+1):
    for j in range(1, i):
        combination_table[i][j] = combination_table[i-1][j-1] + combination_table[i-1][j]
        combination_table[i][j] %= MOD


factorial_table = [1]

for i in range(1, N+1):
    factorial_table.append( (factorial_table[-1] * i) % MOD )

dp = [ [ 0 for _ in range(N+1)]  for _ in range(N+1)]

dp[0][0] = 1

for n in range(1, N+1):
    for c in range(1, n+1):
        for k in range(n):
            dp[n][c] += combination_table[n-1][k] * dp[k][c-1] * factorial_table[n-1-k]
        dp[n][c] %= MOD

ans = 0

for a in range(N):
    b = N - 1 - a
    ans += combination_table[n-1][a] * dp[a][R-1] * dp[b][L-1]

ans %= MOD
print(ans)
# for i in arr:
#     print(i)