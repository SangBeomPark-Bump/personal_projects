import sys
input = sys.stdin.readline
INF = float("inf")

W, H = map(int, input().split())
MOD = 100000

dp = [ [[0 for _ in range(4)] for _ in range(W)] for _ in range(H)]

dp[1][0] = [0, 0, 0, 1]

dp[0][1] = [0, 1, 0, 0]
sad = [ [] for _ in range(W + H -1) ]
sad[0].append([0,0])
for i in range(1, W + H -1):
    for x in range( min(i+1, W)):
        y = i - x
        if y >= H:
            continue
        sad[i].append([y, x])

for i in range(2, W + H -1):
    for y, x in sad[i]:
        if x>0:
            dp[y][x][0] = (dp[y][x-1][3]) % MOD
            dp[y][x][1] = (dp[y][x-1][0] + dp[y][x-1][1]) % MOD
        if y>0:
            dp[y][x][2] = (dp[y-1][x][1]) % MOD
            dp[y][x][3] = (dp[y-1][x][2] + dp[y-1][x][3]) % MOD

print(sum(dp[-1][-1]) % MOD)