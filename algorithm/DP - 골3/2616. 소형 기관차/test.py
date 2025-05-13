import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
arr = [0] + list(map(int, input().split()))
M = int(input())

dp = [ [0,0,0] for _ in range(N+1)]

cur_sum = 0
for n in range(1, N+1):
    cur_sum += arr[n]
    if n >= M:
        cur_sum -= arr[n - M]
    dp[n][0] = max(dp[n-1][0] , cur_sum)
    dp[n][1] = max(dp[n-1][1], cur_sum + dp[n-M][0])
    dp[n][2] = max(dp[n-1][2], cur_sum + dp[n-M][1])

print(dp[-1][-1])