import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
dp = [ [0,0] for _ in range(N+1)]
dp[0][0] = 1

for n in range(1,N+1):
    if n%2 ==1:
        continue
    dp[n][0] = dp[n-2][0] * 3 + dp[n-2][1]
    dp[n][1] = dp[n-2][0] * 2 + dp[n-2][1]

print(dp[N][0])



# for i in arr:
#     print(i)