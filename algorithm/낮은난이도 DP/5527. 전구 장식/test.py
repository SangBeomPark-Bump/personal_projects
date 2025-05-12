import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
arr = [-1] + list(map(int, input().split()))

dp = [0 for _ in range(N+1)]

for n in range(1, N+1):
    if arr[n] != arr[n-1]:
        dp[n] = dp[n-1] +1
    else:
        dp[n] = 1

value = 0
for n in range(1, N+1):
    value = max(value, dp[n] + dp[n - dp[n]] + dp[n-dp[n] - dp[n - dp[n]]])
print(value)

# for i in arr:
#     print(i)