import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
div = int(1e9) + 7
dp = [1, 0, 0]

for n in range(1, N):
    temp = sum(dp)
    dp = [ (temp - dp[i])%div for i in range(3)]

print(dp[1] % div)