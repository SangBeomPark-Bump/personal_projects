import sys
input = sys.stdin.readline
verbose = False
verboses = [False for _ in range(10)]

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split() ) ) for _ in range(H)]


from collections import deque
def bfs(y, x):
    visited = [ [[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    horse_dx = [1, 1, -1, -1, 2, 2, -2, -2]
    horse_dy = [2, -2, 2, -2, 1, -1, 1, -1]

    visited[y][x][K] = 0
    que = deque()
    que.append((y, x, K))
    
    while que:
        y, x, horse = que.popleft()
        if y == (H-1) and x == (W-1):
            return(visited[y][x][horse])
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < H and 0 <= nx < W):
                continue
            if arr[ny][nx] == 1:
                continue
            if not visited[ny][nx][horse]:
                visited[ny][nx][horse] = visited[y][x][horse] + 1
                que.append((ny, nx, horse))
        if horse:
            for i in range(8):
                ny = y + horse_dy[i]
                nx = x + horse_dx[i]
                if not(0 <= ny < H and 0 <= nx < W):
                    continue
                if arr[ny][nx] == 1:
                    continue
                if not visited[ny][nx][horse-1]:
                    visited[ny][nx][horse-1] = visited[y][x][horse] + 1
                    que.append((ny, nx, horse-1))

    return -1

print(bfs(0,0))