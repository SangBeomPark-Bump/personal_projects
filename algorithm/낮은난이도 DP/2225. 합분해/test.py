import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]


N, K = map(int, input().split())
div = int(1e9)
dp = [[0 for _ in range(K+1)] for _ in range(N+1) ]
dp[0][0] = 1
for n in range(N+1):
    for k in range(1,K+1):
        for i in range(n+1):
            dp[n][k] += dp[i][k-1]
    dp[n][k] %= div

print(dp[N][K])

# for i in arr:
#     print(i)