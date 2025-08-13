import sys
input = sys.stdin.readline
INF = float("inf")

string = input().strip('\n')
N = len(string)

pel = [ [False for _ in range(N+1)] for _ in range(N+1)]
for n in range(N+1):
    pel[n][n] = True
    if n+1 <=N:
        pel[n][n+1] = True

for factor in range(2, N+1):
    for start in range(N+1-factor):
        end = start + factor
        if pel[start+1][end-1] and string[start] == string[end-1]:
            pel[start][end] = True

dp = [INF for _ in range(N+1)]
dp[0] = 0
for start in range(N):
    for end in range(start+1, N+1):
        if pel[start][end]:
            dp[end] = min(dp[end], dp[start] + 1)
print(dp[-1])