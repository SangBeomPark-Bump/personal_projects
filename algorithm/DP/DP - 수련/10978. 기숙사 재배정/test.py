import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

T = int(input())

dp = [ 0 for _ in range(21)]
dp[2] = 1

for n in range(3,21):
    dp[n] = (n-1)*(dp[n-1] + dp[n-2])
dp

for _ in range(T):
    N = int(input())
    print(dp[N])
# for i in arr:
#     print(i)