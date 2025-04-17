import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]
sys.setrecursionlimit(10000)

M, N = map(int, input().split())
arr = [list(map(int, input().split() ) ) for _ in range(M)]

cnt = 0
visited = [[False] * N for _ in range(M)]

def dfs(y, x):
    global cnt
    if x == N-1 and y == M-1:
        cnt +=1
        return

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx = x +dx
        ny = y +dy
        if 0 <= nx < N and 0 <= ny <M and arr[ny][nx] < arr[y][x] and not visited[y][x]:
            visited[y][x] = True
            dfs(ny, nx)
            visited[y][x] = False

dfs(0,0)
print(cnt)