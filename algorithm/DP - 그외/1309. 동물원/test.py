import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
dp = [1, 3]
for n in range(2,N+1):
    dp.append( (dp[n-2] + 2 * dp[n-1]) % 9901)
print(dp[-1])