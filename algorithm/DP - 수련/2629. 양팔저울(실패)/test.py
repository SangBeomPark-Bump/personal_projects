import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

N = int(input())
ns = [0] + list(map(int, input().split()))
M = int(input())
ms = list(map(int, input().split()))

x = 40001

dp = [[False for _ in range(x)] for _ in range(N+1)]
dp[0][0] = True

for n in range(1, N+1):
    for d in range(15001):
        if dp[n-1][d]:
            dp[n][d] = True 
            dp[n][d+ns[n]] = True
            dp[n][abs(d-ns[n])] = True

print(*["Y" if dp[-1][m] else "N"  for m in ms])