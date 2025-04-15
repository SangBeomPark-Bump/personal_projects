import sys
input = sys.stdin.readline
verbose = False
verboses = [True for _ in range(10)]

N = int(input())
dp = [[0,0] for _ in range(N+1)]
dp[0][0] = 1
dp[0][1] = 0


for i in range(1,N+1):
    dp[i][0] = dp[i-1][1]
    dp[i][1] = dp[i-1][1] + dp[i-1][0]

print(dp[N][0], dp[N][1])