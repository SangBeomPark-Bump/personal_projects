import sys
input = sys.stdin.readline
INF = float("inf")
FIRST = "First"
SECOND = "Second"
sys.setrecursionlimit(int(1e7))

N, M, K = map(int, input().split())
arr = [list(input().strip('\n')) for _ in range(N)]
moves = [ (1, 0), (0, 1)] + [ (k, k) for k in range(1, K+1)]
dp = [ [-1 for _ in range(M)] for _ in range(N)]

def dfs(y, x):
    if dp[y][x] >=0:
        return dp[y][x], True
    if y == N-1 and x == M-1 :
        dp[y][x] = 0
        return 0, True
    ans = 1
    moved = False
    for dy, dx in moves:
        ny = y + dy
        nx = x + dx
        if ny >= N or nx >= M:
            continue

        if arr[ny][nx] == "#":
            continue
        temp1, temp2 = dfs(ny, nx)
        ans *= temp1
        moved = temp2 or moved
    
    if not moved:
        arr[y][x] = "#"
        return 1, moved

    dp[y][x] = 0 if ans else 1
    return dp[y][x], moved

for x in range(N):
    for y in range(M):
        if arr[y][x] == "#":
            continue
        if dp[y][x] >= 0:
            continue
        dfs(y, x)


for x in range(N):
    for y in range(M):
        if arr[y][x] == "#":
            continue
        if dp[y][x] >= 0:
            continue
        dfs(y, x)


Q = int(input())

for _ in range(Q):
    y, x = map(int, input().split())
    # print(FIRST if (N+M - ( sum((x, y)))) %2 else SECOND )
    print(FIRST if dp[y-1][x-1] else SECOND)

# for i in arr:
#     print(i)