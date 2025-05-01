import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
div = int(1e9)

dp = [ 0 for _  in range(N+1)]
dp[0] = 1
dp[1] = 0

for n in range(2, N+1):
    dp[n] = ((n-1) * (dp[n-2] + dp[n-1]))%div

print(dp[N])