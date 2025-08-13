import sys
input = sys.stdin.readline
INF = float("inf")
FIRST = "First"
SECOND = "Second"
sys.setrecursionlimit(int(1e7))

N, M, K = map(int, input().split())
arr = [list(input().strip('\n')) for _ in range(N)]
moves = [ (1, 0), (0, 1)] + [ (k, k) for k in range(1, K+1)]

def dfs(y, x, depth):
    if y == N - 1 and x == M - 1:
        dp[y][x] = -1
        return False

    win = False    
    for dy, dx in moves:
        ny = y + dy
        nx = x + dx

        if ny >= N or nx >= M:
            continue

        if arr[ny][nx] == "#":
            continue

        if dp[ny][nx]:
            appo_win = dp[ny][nx] == 1
            win |= not appo_win
            continue

        appo_win = dfs(ny, nx, depth + 1)
        win |= not appo_win

    dp[y][x] = 1 if win else -1
    return win


dp = [ [0 for _ in range(M)] for _ in range(N)]
for y in range(N):
    for x in range(M):
        if dp[y][x]:
            continue
        if arr[y][x] == "#":
            continue
        dfs(y, x, 0)

Q = int(input())

for _ in range(Q):
    y, x = map(int, input().split())
    print( FIRST if dp[y-1][x-1] > 0 else SECOND)
