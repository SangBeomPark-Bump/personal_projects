import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))


dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

def dfs(y, x):
    if dp[y][x]:
        return dp[y][x]

    dp[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not(0 <= ny < N and 0 <= nx < N):
            continue

        if A[ny][nx] > A[y][x]:
            dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
    return dp[y][x]



N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

MAX = 0
for y in range(N):
    for x in range(N):
        if not dp[y][x]:
            MAX = max(MAX, dfs(y, x))
print(MAX)