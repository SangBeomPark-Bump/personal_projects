import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
dp =[[0] * 10 for _ in range(N+1)]
dp[1] = [0] + [1] * 9
for n in range(2, N+1):
    for i in range(10):
        minus =  i-1
        plus = i+1
        factor = int(dp[n-1][i] % 1e9)
        if plus <10:
            dp[n][plus] += factor
            # print(i * 10 + plus)
        if minus >=0:
            dp[n][minus] += factor

print(int(sum(dp[-1]) % 1e9))