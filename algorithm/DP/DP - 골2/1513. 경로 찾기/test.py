import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
INF = float("inf")


MOD = int(1e6)+7

N, M, C = map(int, input().split())

degree = [ [0 for _ in range(M)] for _ in range(N)]

for c in range(C):
    cy, cx = map(int, input().split())
    degree[cy-1][cx-1] = c+1

dp = [ [[[0 for _ in range(C+1)] for _ in range(C+1)] for _ in range(M)] for _ in range(N)]
dp[0][0][ 1 if degree[0][0] else 0 ][degree[0][0]] = 1

move = ([1, 0], [0, 1])
for y in range(N):
    for x in range(M):
        for manyc in range(C+1):
            for maxc in range(C+1):
                for i in range(2):
                    dy, dx = move[i]
                    ny = y + dy
                    nx = x + dx
                    if ny <= N-1 and nx <= M-1:
                        if degree[ny][nx] and degree[ny][nx] < maxc:
                            continue
                        cur_maxc = 0
                        cur_maxc = max(degree[ny][nx], maxc)
                        cur_manyc = manyc
                        if degree[ny][nx]:
                            cur_manyc = manyc + 1
                        if cur_manyc <= C:
                            dp[ny][nx][cur_manyc][cur_maxc] += dp[y][x][manyc][maxc]
                            dp[ny][nx][cur_manyc][cur_maxc] %= MOD

print(*map(lambda x: sum(x) % MOD, dp[-1][-1]))