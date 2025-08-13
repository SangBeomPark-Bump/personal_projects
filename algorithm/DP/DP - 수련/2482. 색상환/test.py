import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
K = int(input())

div = 10**9 + 3

dp = [ [ 0 for _ in range(K+1)  ] for _ in range(N)]
for num, row in enumerate (dp):
    row[0] = 1
    row[1] = num

for k in range(2, K+1):
    for n in range(k, N):
        dp[n][k] = (dp[n-2][k-1] + dp[n-1][k])%div

print((dp[N-3][K-1] + dp[N-1][K])%div)
