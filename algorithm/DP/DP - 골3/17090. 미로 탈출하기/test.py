import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
sys.setrecursionlimit(int(1e7))

N, M = map(int, input().split())

arr = [list(input().strip('\n')) for _ in range(N)]
dp = [ [0 for _ in range(M)] for _ in range(N)]
def dfs(y, x):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    if dp[y][x]:
        return dp[y][x]
    direction = ["R", "L", "D", "U"]
    value = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny<0 or ny>=N or nx <0 or nx >= M:
            continue

        if dp[y][x]:
            continue
        
        if arr[ny][nx] == direction[i] :
            value += dfs(ny, nx)

    dp[y][x] = value
    return dp[y][x]

value = 0

for m in range(M):
    for n, direction in zip( [0, N-1], ['U', "D"] ):
        if arr[n][m] == direction:
            value += dfs(n, m)

for n in range(N):
    for m , direction in zip([0, M-1], ['L', "R"]):
        if arr[n][m] == direction:
            value += dfs(n, m)
print(value)