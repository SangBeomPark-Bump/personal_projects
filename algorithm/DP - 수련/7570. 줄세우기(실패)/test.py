import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
arr = list(map(int, input().split()))

dp = [ 0 for _ in range(N+1)]
ans = 0
for i in arr:
    ans = max(dp[i-1] +1, ans)
    dp[i] = dp[i-1] +1
print(N - ans)